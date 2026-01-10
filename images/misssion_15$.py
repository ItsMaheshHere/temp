import subprocess
import time
import os
import pyautogui
import asyncio,json,random,pyperclip
import local_module

def random_coordinates_from_found_img(img,margin=5):
    left,top,width,height=img
    left+=margin
    top+=margin
    right=left+width-margin
    bottom=top+height-margin
    x=random.randint(left,right)
    y=random.randint(top,bottom)
    pyautogui.moveTo(x,y,duration=random.uniform(0.1,0.3))
    pyautogui.mouseDown(x,y)
    time.sleep(random.uniform(0.01,0.2))
    pyautogui.mouseUp()

def change_ip():
    pyautogui.click(797, 752)
    time.sleep(0.3)
    pyautogui.hotkey('winleft', '7')
    time.sleep(0.5)

    max_attempts = 10
    attempts = 0

    connect_btn_found = False

    while attempts < max_attempts:
        if attempts == max_attempts:
            print("Max attempts reached, restarting program...")
            python_exe = sys.executable
            os.execl(python_exe, python_exe, *sys.argv)
        attempts += 1
        print("Looking for toggle btn")
        
        try:
            connect_btn_location = pyautogui.locateOnScreen('connect_btn.png', confidence=0.7)
            if connect_btn_location:
                connect_x, connect_y = pyautogui.center(connect_btn_location)
                pyautogui.click(connect_x, connect_y)
                connect_btn_found = True
            else:
                print("Connect btn image not found")
        except Exception as e:
            print("Error finding connect btn.")

        try:
            connect_btn_location = pyautogui.locateOnScreen('error1.png', confidence=0.7)
            if connect_btn_location:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                handler_path = os.path.join(current_dir, 'vpn_toggle.py')
                python_exe = sys.executable
                subprocess.run([python_exe, handler_path], check=True)
                print("restarting program...")
                os.execl(python_exe, python_exe, *sys.argv)
                return
        except subprocess.TimeoutExpired:
            print("VPN toggle process timed out after 30 seconds, restarting program...")
            time.sleep(0.5)
            os.execl(python_exe, python_exe, *sys.argv)
            return
        except Exception as e:
            print("Error finding connect btn.")

        if not connect_btn_found:
            print("Failed to find connect btn")
            continue

        for attempt in range(40):

            try:
                connect_confirm_location = pyautogui.locateOnScreen('confirmation_image.png', confidence=0.7)
                if connect_confirm_location:
                    try:
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        print("Checking if we got new ip")
                        main0_path = os.path.join(current_dir, 'main0.py')
                        python_exe = sys.executable
                        result = subprocess.run([python_exe, main0_path], capture_output=True, text=True, check=True, timeout=20)
                        if result.returncode == 1:
                            print("Successfully got a new IP!")
                            return True
                        else:
                            print("IP is not new, retrying")
                            break
                    except subprocess.CalledProcessError as e:
                        print("Error running main0.py")
                        print("Output:", e.output)
                        print("Stderr:", e.stderr)
                        break
                    except Exception as e:
                        print("Unexpected error running main0.py")
                        break
            except Exception as e:
                print("Error finding confirmation image")

            try:
                ip_not_changed_location = pyautogui.locateOnScreen('IP_not_changed.png', confidence=0.7)
                if ip_not_changed_location:
                    print("IP not changed detected, running handler.")
                    try:
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        handler_path = os.path.join(current_dir, 'vpn_toggle.py')
                        python_exe = sys.executable
                        subprocess.run([python_exe, handler_path], check=True)
                        print("IP not changed handler completed, restarting program...")
                        os.execl(python_exe, python_exe, *sys.argv)
                        return
                    except subprocess.TimeoutExpired:
                        print("restarting program...")
                        os.execl(python_exe, python_exe, *sys.argv)
                        return
                    except subprocess.CalledProcessError as e:
                        print("Error running ip_not_change_handle.py")
                        break
                    except Exception as e:
                        print("Unexpected error running ip_not_change_handle.py")
                        break
            except Exception as e:
                print("Error finding IP not changed image")

            try:
                ip_not_changed_location = pyautogui.locateOnScreen('IP_not_changed2.png', confidence=0.7)
                if ip_not_changed_location:
                    print("IP not changed detected, running handler.")
                    try:
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        handler_path = os.path.join(current_dir, 'vpn_toggle.py')
                        python_exe = sys.executable
                        subprocess.run([python_exe, handler_path], check=True)
                        print("restarting program...")
                        os.execl(python_exe, python_exe, *sys.argv)
                        return
                    except subprocess.TimeoutExpired:
                        print("VPN toggle process timed out after 30 seconds, restarting program...")
                        time.sleep(0.5)
                        os.execl(python_exe, python_exe, *sys.argv)
                        return
                    except subprocess.CalledProcessError as e:
                        print("Error running ip_not_change_handle.py")
                        break
                    except Exception as e:
                        print("Unexpected error running ip_not_change_handle.py")
                        break
            except Exception as e:
                print("Error finding IP not changed image")
            time.sleep(0.5)

def handle_starting():
    x=random.uniform(50,440)
    y=random.uniform(200,600)
    pyautogui.moveTo(x,y,duration=0.1)
    pyautogui.moveTo(x+50,y+20,duration=0.1)
    ch=random.randint(1,2)
    if ch==1:
        local_module.simple_scroll()
    else:
        local_module.scroll_down_up()
    
    for i in range(150):
        try:
            verification_success_location = pyautogui.locateOnScreen('success.png', confidence=0.7)
            if verification_success_location is not None:
                verification_success_found = True
                break
        except:
            pass
            
        try:
            verify_human_location =pyautogui.locateOnScreen('verify you are human.png', confidence=0.7)
            if verify_human_location is not None:
                x,y = pyautogui.center(verify_human_location)
                pyautogui.click(x,y)
                time.sleep(6)
                break
        except:
            pass
        time.sleep(1)
    
    for i in range(50):
        try:
            continue0=pyautogui.locateOnScreen('continue_img.png',confidence=0.8)
            if continue0:
                print("continue img found")
                redirected=True
                random_coordinates_from_found_img(continue0)
                time.sleep(0.7)
                pyautogui.moveRel(random.randint(-100,-80),random.randint(25,70))
                try:
                    img=pyautogui.locateOnScreen('link_img.png',confidence=0.8)
                    if img:
                        img=None
                except:
                    time.sleep(1)
                    pyautogui.click(475,20)
                    time.sleep(0.5)
        except Exception as e:
            print(f"{e}continue img not found")
            if redirected:
                consecutive_failures+=1
            if consecutive_failures>=1:
                break
        time.sleep(1)

def open_firefox_n_navigate_to_sort_link():
    pyautogui.click(797, 752)
    time.sleep(0.2)
    pyautogui.hotkey('winleft', '8')
    time.sleep(0.4)
    pyautogui.hotkey('ctrl', 'l')
    yt_url="https://youtu.be/oihOMTtUWPQ"
    pyperclip.copy(yt_url)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pyautogui.press('enter')
    for i in range(50):
        try:
            more_logo=pyautogui.locateOnScreen('more.png',confidence=0.9)
            if more_logo:
                x,y=pyautogui.center(more_logo)
                pyautogui.click(x,y)
                time.sleep(0.3)
                break
        except Exception as e:
            print(e)
        time.sleep(0.5)
    else:
        restart_program()

    for i in range(50):
        try:
            link_logo=pyautogui.locateOnScreen('yt_url_img.png',confidence=0.8)
            if link_logo:
                x,y=pyautogui.center(link_logo)
                pyautogui.click(x,y)
                time.sleep(0.3)
                break
        except Exception as e:
            print(e)
    
    for i in range(80):
        try:
            health_shield=pyautogui.locateOnScreen('loan_buzz.png',confidence=0.8)
            if health_shield:
                pyautogui.click(250,20)
                break
        except:
            pass
        time.sleep(1)
    else:
        restart_program()

def clear_cookies():
    pyautogui.hotkey('ctrl','shift','del')
    for i in range(10):
        try:
            clear=pyautogui.locateOnScreen('clear_img.png',confidence=0.8)
            if clear:
                x,y=pyautogui.center(clear)
                time.sleep(0.3)
                break
        except:
            pass
        time.sleep(1)
    
def for_end():
    pyautogui.click(285,15)
    time.sleep(0.4)
    pyautogui.click(250,20)

def main():
    change_ip()
    open_firefox_n_navigate_to_sort_link()
    while True:
        try:
            drive=pyautogui.locateOnScreen('drive.png',confidence=0.8)
            if drive:
                break
        except:
            pass
        time.sleep(1)
    for_end()
    clear_cookies()

main()