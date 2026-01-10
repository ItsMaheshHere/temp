import pyautogui
import time
import os
import sys
import random
import subprocess
import asyncio
import pyperclip 
import cv2

PNG_PATH='./images/'
running1=False
running2=False

def random_coordinates_from_found_img(img,margin=2):
    left,top,width,height=img
    left+=margin
    top+=margin
    right=left+width-margin
    bottom=top+height-margin
    x=random.randint(left,right)
    y=random.randint(top,bottom)
    pyautogui.click(x,y)

def run_batch_file(batch_file):
    try:
        subprocess.run([batch_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {batch_file}: {e}")

def wait_and_click_image():
    max_attempts = 70
    attempt = 0
    india_flag_found = False
    time.sleep(5)
    while attempt < max_attempts and not india_flag_found:
        try:
            india_location = pyautogui.locateOnScreen(PNG_PATH+'india_flag.png', confidence=0.8)
            if india_location:
                print("Found India flag!")
                india_flag_found = True
                break
        except Exception as e:
            print(e)
        
        print("India flag not found")
        time.sleep(1)
        attempt += 1

    print("Looking for toggle button...")
    try:
        toggle_location = pyautogui.locateOnScreen(PNG_PATH+'toggle_btn_image.png', confidence=0.8)
        if toggle_location:
            print("Found toggle button! Clicking...")
            toggle_center = pyautogui.center(toggle_location)
            pyautogui.click(toggle_center)
            time.sleep(3)
            return True
        else:
            print("Toggle button not found")
            return False
    except Exception as e:
        print(f"Error while looking for toggle button: {e}")

def vpn_connect_btn_click():
    try:
        connect_btn_location=pyautogui.locateOnScreen(PNG_PATH + 'connect_btn.png', confidence=0.7)
        if connect_btn_location:
            x,y = pyautogui.center(connect_btn_location)
            pyautogui.click(x, y)
    except Exception as e:
        print(f"{e}Error finding connect btn.")
    
    for i in range(40):
        try:
            connect_confirmed=pyautogui.locateOnScreen(PNG_PATH + 'confirmation_image.png', confidence=0.7)
            if connect_confirmed:
                try:
                    current_dir = os.path.dirname(os.path.abspath(__file__))
                    print("Checking if we got new ip")
                    main0_path = os.path.join(current_dir, 'main0.py')
                    python_exe = sys.executable
                    result = subprocess.run([python_exe, main0_path], capture_output=True, text=True, check=True, timeout=20)
                    if result.returncode == 0:
                        print("Successfully got a new IP!")
                        return True
                except Exception as e:
                    print(f"Unexpected error running main0.py{e}")
                    vpn_connect_btn_click()
                    return
                except subprocess.CalledProcessError as e:
                    print(f"Error running main0.py: {e}")
                    print("stdout:", e.stdout)
                    print("stderr:", e.stderr)
                    vpn_connect_btn_click()
                    return
        except Exception as e:
            print("Error finding confirmation image")
        time.sleep(1)


def gplinks_co_pc_handle():
    for i in range(30):
        try:
            gplinks_co=pyautogui.locateOnScreen(PNG_PATH+'gplink_co_pc.png',confidence=0.8)
            if gplinks_co:
                break
        except Exception as e:
            print(e)
        time.sleep(1)
    else:
        return False
    
    x=random.uniform(290,1100)
    y=random.uniform(200,600)
    pyautogui.moveTo(x,y)
    
    ch=random.randint(1,2)
    if ch==1:
        time.sleep(random.randint(2,4))
        pyautogui.scroll(random.randint(-10,10))

    x=random.uniform(290,1100)
    y=random.uniform(200,600)
    pyautogui.moveTo(x,y)
    
    ch=random.randint(1,2)
    if ch==1:
        time.sleep(random.randint(1,3))
        pyautogui.scroll(random.randint(-10,10))

    for i in range(30):
        try:
            human_verfi=pyautogui.locateOnScreen(PNG_PATH+'human_verification_pc.png',confidence=0.8)
            if human_verfi:
                random_coordinates_from_found_img(human_verfi)
        except Exception as e:
            print(e)
        
        try:
            human_verfi_success=pyautogui.locateOnScreen(PNG_PATH+'human_verification_success_pc.png',confidence=0.8)
            if human_verfi_success:
                break
        except Exception as e:
            print(e)
        time.sleep(1)
    else:
        return False
    
    return True
    
def middle_link_pc_handle():
    x=random.uniform(290,1100)
    y=random.uniform(200,600)
    pyautogui.moveTo(x,y)
    for i in range(30):
        try:
            thr=pyautogui.locateOnScreen(PNG_PATH+'home_img.png',confidence=0.7)
            if thr:
                break
        except:
            pass
        time.sleep(1)
    else:
        return False
    
    time.sleep(random.randint(3,6))
    ch=random.randint(1,2)
    if ch==1:
        pyautogui.scroll(random.randint(-20,20))

    x=random.uniform(290,1100)
    y=random.uniform(200,600)
    pyautogui.moveTo(x,y)
    time.sleep(random.randint(4,7))
    ch=random.randint(1,2)
    if ch==1:
        pyautogui.scroll(random.randint(-10,10))

    x=random.uniform(290,1100)
    y=random.uniform(200,600)
    pyautogui.moveTo(x,y)
    time.sleep(random.randint(4,7))
    ch=random.randint(1,2)
    if ch==1:
        pyautogui.scroll(random.randint(-10,10))

    x=random.uniform(290,1100)
    y=random.uniform(200,600)
    pyautogui.moveTo(x,y)
    time.sleep(random.randint(4,7))
    ch=random.randint(1,2)
    if ch==1:
        pyautogui.scroll(random.randint(-10,10))
    
    x=random.uniform(290,1100)
    y=random.uniform(200,600)
    pyautogui.moveTo(x,y)
    time.sleep(random.randint(4,7))
    ch=random.randint(1,2)
    if ch==1:
        pyautogui.scroll(random.randint(-10,10))
    
    verify_found=False
    consecutive_failures=0
    attempt=0
    for i in range(20):
        attempt+=1
        try:
            verify_image=pyautogui.locateOnScreen(PNG_PATH+'verify_img_pc.png',confidence=0.8)
            if verify_image:
                time.sleep(random.randint(1,3))
                random_coordinates_from_found_img(verify_image)
                time.sleep(4)
                pyautogui.scroll(475,20)
                verify_found=True
        except:
            if verify_found:
                consecutive_failures+=1
            if consecutive_failures>=1:
                break
            if attempt>=13:
                x=random.uniform(290,1100)
                y=random.uniform(200,600)
                pyautogui.moveTo(x,y)
                pyautogui.scroll(-50)
        time.sleep(1)
    else:
        return False
    
    time.sleep(random.randint(1,3))
    pyautogui.moveTo(1355,700)
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    consecutive_failures=0
    continue_found=False
    attempt=0
    for i in range(20):
        attempt+=1
        try:
            continue_img=pyautogui.locateOnScreen(PNG_PATH+'continue_img_pc.png',confidence=0.8)
            if continue_img:
                continue_found=True
                time.sleep(random.randint(1,3))
                random_coordinates_from_found_img(continue_img)
                time.sleep(2)
                pyautogui.scroll(475,20)
        except:
            if continue_found:
                consecutive_failures+=1
            if consecutive_failures>=1:
                break
            if attempt>5 and attempt<13:
                x=random.uniform(290,1100)
                y=random.uniform(200,600)
                pyautogui.moveTo(x,y)
                pyautogui.scroll(-50)
            if attempt>13:
                x=random.uniform(290,1100)
                y=random.uniform(200,600)
                pyautogui.moveTo(x,y)
                pyautogui.scroll(50)
        time.sleep(1)
    else:
        return False
    
    return True

def last_link_pc():
    for i in range(30):
        try:
            gp_logo=pyautogui.locateOnScreen(PNG_PATH+'Gp_logo_pc.png',confidence=0.8)
            if gp_logo:
                break
        except:
            pass
        time.sleep(1)
    else:
        return False
    
    time.sleep(random.randint(7,10))
    x=random.uniform(290,1100)
    y=random.uniform(200,600)
    pyautogui.moveTo(x,y)
    ch=random.randint(1,2)
    if ch==1:
        pyautogui.scroll(random.randint(-20,20))
    
    for i in range(30):
        try:
            human_verfi=pyautogui.locateOnScreen(PNG_PATH+'human_verification_pc.png',confidence=0.8)
            if human_verfi:
                random_coordinates_from_found_img(human_verfi)
        except Exception as e:
            print(e)
        
        try:
            human_verfi_success=pyautogui.locateOnScreen(PNG_PATH+'cloudflare_verification_success_pc.png',confidence=0.8)
            if human_verfi_success:
                break
        except Exception as e:
            print(e)
        time.sleep(1)
    else:
        return False
    
    time.sleep(random.randint(1,3))
    x=random.uniform(290,1100)
    y=random.uniform(200,600)
    pyautogui.moveTo(x,y)
    ch=random.randint(1,2)
    if ch==1:
        pyautogui.scroll(random.randint(-20,20))
    
    pyautogui.scroll(random.randint(-100,-60))

    for i in range(10):
        try:
            get_link=pyautogui.locateOnScreen(PNG_PATH+'get_link_pc.png',confidence=0.8)
            if get_link:
                random_coordinates_from_found_img(get_link)
        except Exception as e:
            print(e)
        time.sleep(1)
    else:
        return False
    
    time.sleep(3)
    return True
    

def user_agent_change():
    pyautogui.click(1300,60)
    time.sleep(0.6)
    pyautogui.click(1150,185)
    time.sleep(0.6)

def clear_cookies():
    pyautogui.click(1340,60)
    time.sleep(0.8)
    pyautogui.click(1150,575)
    time.sleep(1)
    pyautogui.click(150,320)
    time.sleep(0.6)
    pyautogui.moveTo(600,300,duration=0.2)
    time.sleep(0.3)
    pyautogui.scroll(-500)
    time.sleep(0.6)
    try:
        result=pyautogui.locateOnScreen(PNG_PATH+'clear_cookies_img_pc.png',confidence=0.8)
        if result:
            x,y=pyautogui.center(result)
            pyautogui.click(x,y)
    except:
        pass
    time.sleep(0.8)
    pyautogui.click(800,640)
    time.sleep(0.5)
    for_end()
    return True

def for_end():
    pyautogui.click(285,15)
    time.sleep(0.7)
    pyautogui.click(250,20)
    time.sleep(0.6)

def open_firefox_n_navigate_to_sort_link():
    pyautogui.click(797, 752)
    time.sleep(0.2)
    pyautogui.hotkey('win', '2')
    time.sleep(0.4)
    user_agent_change()
    time.sleep(0.4)
    pyautogui.hotkey('ctrl', 'l')
    yt_url="https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqblB3X0tIclZyaElXa2tpbkM0TjF2ejNFUUQtZ3xBQ3Jtc0trUzZLSWU0TUFiSGZtNm9SeWVMWnhJTXhra2k1cnhDVHBMMFZxbEFoY3FRcURrdXUxWm44QndLd1o1TU54TzJmVW13MTd0bXVfQjFLb1JrZnBuOWdiaWFQalBxWmlBMV9abk50ZEdmTnZRRTdkTmItNA&q=https%3A%2F%2Fgplinks.co%2Fj80N&v=zI91oaUZbFE"
    pyperclip.copy(yt_url)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pyautogui.press('enter')

    for i in range(40):
        try:
            go_to_site=pyautogui.locateOnScreen(PNG_PATH + 'go_to_site_pc.png',confidence=0.7)
            if go_to_site:
                x,y=pyautogui.center(go_to_site)
                pyautogui.click(x,y)
                break
        except Exception as e:
            print(f"go to site img not found{e}")
        time.sleep(1)
    else:
        return False
    
    return True




def change_ip_mobile():
    subprocess.run(['adb', 'shell' , 'cmd' , 'connectivity' , 'airplane-mode' , 'enable'])
    time.sleep(2)
    subprocess.run(['adb', 'shell' , 'cmd' , 'connectivity' , 'airplane-mode' , 'disable'])
    return True

def touch_on_mobile(x,y):
    subprocess.run(['adb', 'shell' , 'input', 'tap' , str(x), str(y)])

def mobile_scroll(x, y, x2, y2, duration):
    subprocess.run(['adb', 'shell', 'input', 'swipe', str(x), str(y), str(x2), str(y2), str(duration)])

def find_image_on_mobile(template_path, confidence=0.8, temp_screenshot="temp_screen.png", margin=3):
    subprocess.run(['adb', 'shell', 'screencap', '-p', '/sdcard/temp.png'])
    subprocess.run(['adb', 'pull', '/sdcard/temp.png', temp_screenshot])
    # subprocess.run(['adb', 'shell', 'rm', '/sdcard/temp.png'])
    
    screenshot = cv2.imread(temp_screenshot, cv2.IMREAD_COLOR)
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    if max_val >= confidence:
        h, w = template.shape[:2]
        x = max_loc[0]
        y = max_loc[1]
        
        left = x + margin
        top = y + margin
        right = x + w - margin
        bottom = y + h - margin
        
        random_x = random.randint(left, right)
        random_y = random.randint(top, bottom)
        print("Img found at mobile")
        return {
            'found': True,
            'bbox': (x, y, w, h),
            'center': (x + w // 2, y + h // 2),
            'random': (random_x, random_y),
            'confidence': float(max_val)
        }
    
    return {'found': False, 'confidence': float(max_val)}

def nav_to_mobile_ua_change():
    time.sleep(0.5)
    touch_on_mobile(676,111)
    time.sleep(1)
    touch_on_mobile(450,751)
    time.sleep(1)
    touch_on_mobile(440,417)
    time.sleep(0.7)
    touch_on_mobile(365,420)
    time.sleep(0.5)
    touch_on_mobile(85,97)
    time.sleep(0.5)

def random_scroll():
    ch=random.randint(1,4)
    if ch==1:
        x=random.randint(175,625)
        y=random.randint(700,900)
        x2=x+random.randint(-70,120)
        y2=random.randint(270,550)
        duration=random.randint(210,280)
        mobile_scroll(x,y,x2,y2,duration)
    elif ch==2:
        x=random.randint(175,625)
        y=random.randint(700,900)
        x2=x+random.randint(-70,120)
        y2=random.randint(270,550)
        duration=random.randint(210,280)
        mobile_scroll(x,y,x2,y2,duration)
        time.sleep(random.uniform(0.1,0.5))
        x=random.randint(175,625)
        y=random.randint(270,550)
        x2=x+random.randint(-70,120)
        y2=random.randint(700,900)
        duration=random.randint(210,280)
        mobile_scroll(x,y,x2,y2,duration)
    elif ch==3:
        x=random.randint(175,625)
        y=random.randint(700,900)
        x2=x+random.randint(-70,120)
        y2=random.randint(270,550)
        duration=random.randint(210,280)
        mobile_scroll(x,y,x2,y2,duration)
        time.sleep(random.uniform(0.1,0.5))
        x=random.randint(175,625)
        y=random.randint(270,550)
        x2=x+random.randint(-70,120)
        y2=random.randint(700,900)
        duration=random.randint(210,280)
        mobile_scroll(x,y,x2,y2,duration)

        #fhfyudtdtdttdtdtdtdtdtdtdtdtdtdt
        x=random.randint(175,625)
        y=random.randint(700,900)
        x2=x+random.randint(-70,120)
        y2=random.randint(270,550)
        duration=random.randint(210,280)
        mobile_scroll(x,y,x2,y2,duration)
        time.sleep(random.uniform(0.1,0.5))
        x=random.randint(175,625)
        y=random.randint(270,550)
        x2=x+random.randint(-70,120)
        y2=random.randint(700,900)
        duration=random.randint(210,280)
        mobile_scroll(x,y,x2,y2,duration)
    else:
        x=random.randint(175,625)
        y=random.randint(700,900)
        x2=x+random.randint(-70,120)
        y2=random.randint(270,550)
        duration=random.randint(210,280)
        mobile_scroll(x,y,x2,y2,duration)

        #ghghghghghghghhghghghghghghhghghgh
        x=random.randint(175,625)
        y=random.randint(700,900)
        x2=x+random.randint(-70,120)
        y2=random.randint(270,550)
        duration=random.randint(210,280)
        mobile_scroll(x,y,x2,y2,duration)

def mobile_opening_link_handle():
    touch_on_mobile(670,115)
    time.sleep(0.5)
    touch_on_mobile(320,245)
    time.sleep(1)
    touch_on_mobile(45,985)
    time.sleep(1)
    touch_on_mobile(630,1135)
    time.sleep(0.7)
    touch_on_mobile(235,1255)
    time.sleep(0.7)
    touch_on_mobile(653,985)
    time.sleep(0.7)
    touch_on_mobile(675,1535)
    time.sleep(0.7)

def mobile_closing_link_handle():
    touch_on_mobile(560,115)
    time.sleep(1.2)
    touch_on_mobile(673, 932)
    time.sleep(0.8)
    touch_on_mobile(131, 742)
    time.sleep(0.8)
    touch_on_mobile(680,95)
    time.sleep(0.8)
    mobile_scroll(436, 1296,389, 602,50)
    time.sleep(0.8)
    touch_on_mobile(376, 1517)
    time.sleep(0.8)
    mobile_scroll(436, 796,389, 402,100)
    time.sleep(1.4)
    try:
        result=find_image_on_mobile(PNG_PATH+"clear_data_img.png",confidence=0.8)
        x,y=result['center']
        touch_on_mobile(x,y)
    except Exception as e:
        print(e)
    time.sleep(0.8)
    touch_on_mobile(386, 1025)
    time.sleep(0.8)
    touch_on_mobile(597, 889)
    time.sleep(0.8)
    touch_on_mobile(61, 93)
    time.sleep(0.8)
    touch_on_mobile(61, 93)
    time.sleep(0.8)


def mobile_reach_to_first_link():
    time.sleep(random.randint(15,30))
    for i in range(30):
        try:
            result = find_image_on_mobile(PNG_PATH+"go_to_site_mobile.png", confidence=0.8)
            if result and result['found']:
                x,y=result['center']
                touch_on_mobile(x,y)
                break
            else:
                print("go_to_site img not found")
        except:
            pass
        time.sleep(1)
    else:
        return False
    


def main1():
    global running1,running2
    while not running2:
        time.sleep(1)
    if not running1:
        run_batch_file("start_tuxler.bat")
        wait_and_click_image()
        running1=True
    vpn_connect_btn_click()
    if open_firefox_n_navigate_to_sort_link():
        if gplinks_co_pc_handle():
            if middle_link_pc_handle():
                if middle_link_pc_handle():
                    if middle_link_pc_handle():
                        if last_link_pc():
                            for_end()
                            clear_cookies()
                            run_batch_file("stop_tuxler.bat")
                            running1=False
                            return True
                        else:
                            for_end()
                            clear_cookies()
                            pyautogui.hotkey('win', '3')
                            main1()
                            return
                    else:
                        for_end()
                        clear_cookies()
                        pyautogui.hotkey('win', '3')
                        main1()
                        return
                else:
                    for_end()
                    clear_cookies()
                    pyautogui.hotkey('win', '3')
                    main1()
                    return
            else:
                for_end()
                clear_cookies()
                pyautogui.hotkey('win', '3')
                main1()
                return
        else:
            for_end()
            clear_cookies()
            pyautogui.hotkey('win', '3')
            main1()
            return
    else:
        for_end()
        clear_cookies()
        pyautogui.hotkey('win', '3')
        main1()
        return

def main2():
    global running1,running2
    change_ip_mobile()
    time.sleep(0.3)
    running2=True
    nav_to_mobile_ua_change()
    if mobile_reach_to_first_link():
        if mobile_handle_second_link():
            if handle_last_link():
                mobile_closing_link_handle()
            else:
                mobile_closing_link_handle()
                return
        else:
            mobile_closing_link_handle()
            return
    else:
        mobile_closing_link_handle()
        return
    
    