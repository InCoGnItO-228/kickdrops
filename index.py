import asyncio
import traceback
import os
import sys
import subprocess

from core import tl
from core import kick
from core import view_controller
from core import formatter

from functools import partial

# Файл для сохранения выбранного режима
MODE_FILE = "selected_mode.txt"


async def create_file_tasks():
    listcamp = kick.get_all_campaigns()
    formatter.convert_drops_json(listcamp)


async def start_general_drops():
    while True:
        print(f"\n{tl.c['search_streamers']}")

        try:
            rndstreamercategory = kick.get_random_stream_from_category(13)
            if not rndstreamercategory:
                print(f"\n{tl.c['unablefindstreamer']}")
                print(f"\n{tl.c['waitcd300seconds']}")
                await asyncio.sleep(300)
                continue

            username = rndstreamercategory['username']
            remaining = await formatter.get_remaining_time(username)
            print(tl.c["streamer_found"].format(username=username))
            stream_info = await kick.get_stream_info(username)

            if not stream_info['is_live']:
                print(tl.c["streamer_offline_looking_another"].format(username=username))
                await asyncio.sleep(30)
                continue

            if stream_info['game_id'] != 13:
                print(tl.c["streamer_play_another_game"].format(username=username))
                await asyncio.sleep(30)
                continue

            print(tl.c["streamer_online"].format(username=username))
            print(tl.c["starting_view_streamer"].format(remaining=remaining))

            stream_ended = await view_controller.run_with_timer(
                partial(view_controller.view_stream, username, 13),
                remaining + 120
            )

            if stream_ended:
                print(tl.c["streamer_play_another_game"].format(username=username))
                print(f"\n{tl.c['wait_for_new_streamer']}")
                await view_controller.check_campaigns_claim_status()
                await asyncio.sleep(60)
            else:
                print(tl.c["finish_view"].format(username=username))
                print(f"\n{tl.c['waitcd300seconds']}")
                await view_controller.check_campaigns_claim_status()
                await asyncio.sleep(300)

        except Exception as e:
            print(tl.c["error_viewing"].format(e=e))
            print(f"\n{tl.c['waitcd120seconds']}")
            await asyncio.sleep(120)


async def start_streamer_drops():
    while True:
        streamers_data = formatter.collect_usernames()
        found_online = False
        print(f"\n{tl.c['search_streamers']}")

        for streamer in streamers_data:
            username = streamer['username']
            required_seconds = streamer['required_seconds']
            claim_status = streamer['claim']

            if claim_status == 1:
                print(tl.c["streamer_time_skip"].format(username=username))
                continue

            remaining = await formatter.get_remaining_time(username)
            if remaining <= 0:
                print(tl.c["streamer_time_skip"].format(username=username))
                continue

            stream_info = await kick.get_stream_info(username)

            if stream_info['is_live'] and stream_info['game_id'] == 13:
                print(tl.c["streamer_found"].format(username=username))
                print(tl.c["starting_view_streamer"].format(remaining=remaining))
                found_online = True

                stream_ended = await view_controller.run_with_timer(
                    partial(view_controller.view_stream, username, 13),
                    required_seconds + 120
                )

                if stream_ended:
                    print(tl.c["streamer_play_another_game"].format(username=username))
                    print(f"\n{tl.c['waitcd120seconds']}")
                    await asyncio.sleep(120)
                    break
                else:
                    remaining_after = await formatter.get_remaining_time(username)
                    if remaining_after > 0:
                        print(f"\n{tl.c['waitcd120seconds']}")
                        await asyncio.sleep(120)
                    else:
                        print(tl.c['finish_view'].format(username=username))
                        await asyncio.sleep(60)
                    break
            else:
                print(tl.c["streamer_offline"].format(username=username))

        if not found_online:
            print(f"\n{tl.c['all_streamers_offline']}")
            print(f"\n{tl.c['wait_streamers_online']}")
            await view_controller.check_campaigns_claim_status()
            rnd = kick.get_random_stream_from_category(13)
            if rnd:
                await view_controller.run_with_timer(
                    partial(view_controller.view_stream, rnd['username'], 13),
                    3600
                )
            await asyncio.sleep(600)


async def show_menu():
    print("Thanks Mixanicys")
    if not os.path.exists("current_views.json"):
        await create_file_tasks()
    else:
        print(tl.c['file_view_found'])

    await asyncio.sleep(3)
    await view_controller.check_campaigns_claim_status()

    menu_items = {
        "1": (tl.c['start_streamers_drops'], "streamers"),
        "2": (tl.c['start_general_drops'], "general"),
        "0": (tl.c['exit'], None)
    }

    while True:
        for key, (label, _) in menu_items.items():
            print(f"{key}. {label}")
        choice = input(tl.c['select_menu']).strip()

        if choice == "0":
            print(f"\n{tl.c['exit_script']}")
            sys.exit(0)

        if choice not in menu_items or menu_items[choice][1] is None:
            print(f"\n{tl.c['wrong_choice']}")
            input(tl.c['press_enter'])
            continue

        mode = menu_items[choice][1]
        with open(MODE_FILE, "w") as f:
            f.write(mode)
        print(f"\n✅ Selected mode: {mode}")

        # Спрашиваем, запускать ли в фоне
        while True:
            bg_choice = input("Run in background (close terminal safely)? (Y/n): ").strip().lower()
            if bg_choice in ("", "y", "yes"):
                # Запуск в фоне
                print("✨ Starting in background...")
                python = sys.executable
                script = os.path.abspath(__file__)
                subprocess.Popen(
                    ["nohup", python, script, "--background"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    preexec_fn=os.setpgrp
                )
                print("✅ Running in background. You can close this terminal.")
                sys.exit(0)
            elif bg_choice in ("n", "no"):
                # Запуск в текущем терминале
                print("\n🚀 Starting in foreground (keep terminal open)...")
                if mode == "streamers":
                    await start_streamer_drops()
                elif mode == "general":
                    await start_general_drops()
                break
            else:
                print("⚠️ Please enter 'y' or 'n'.")


async def run_background_mode():
    """Фоновый запуск без интерактивного меню"""
    if not os.path.exists(MODE_FILE):
        print("❌ No mode selected. Please run script normally first.")
        return

    with open(MODE_FILE) as f:
        mode = f.read().strip()

    if mode == "streamers":
        await start_streamer_drops()
    elif mode == "general":
        await start_general_drops()
    else:
        print(f"⚠️ Unknown mode: {mode}")


if __name__ == "__main__":
    if "--background" in sys.argv:
        try:
            asyncio.run(run_background_mode())
        except KeyboardInterrupt:
            pass
        except Exception:
            # Тихо выходим в фоне — ошибки можно логировать позже
            pass
    else:
        try:
            asyncio.run(show_menu())
        except KeyboardInterrupt:
            print(f"\n\n{tl.c['exit_script']}")
        except Exception as e:
            print(f"\n{tl.c['critical_error'].format(e=e)}")
            traceback.print_exc()
