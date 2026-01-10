import requests
import json
from datetime import datetime
import os
import sys

def get_ip():
    """Get only IP address"""
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        return data.get('ip', 'N/A')
    except Exception as e:
        print(f"Error getting IP: {str(e)}")
        return None

def load_ip_history():
    """Load IP history from file"""
    try:
        if os.path.exists('ip_history.json'):
            with open('ip_history.json', 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading history: {str(e)}")
    return {}

def save_ip_history(history):
    """Save IP history to file"""
    try:
        with open('ip_history.json', 'w') as f:
            json.dump(history, f, indent=4)
    except Exception as e:
        print(f"Error saving history: {str(e)}")

def main():
    # Get current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Load existing history
    ip_history = load_ip_history()
    
    # Check if we need to reset for new day
    if current_date not in ip_history:
        ip_history = {current_date: []}
    
    # Get current IP
    current_ip = get_ip()
    if current_ip:
        # Check if this IP matches any previous IP from today
        is_ip_new = True
        if ip_history[current_date]:
            # Get all previous IPs from today
            previous_ips = [check['ip'] for check in ip_history[current_date]]
            # Check if current IP matches any previous IP
            is_ip_new = current_ip not in previous_ips
        
        # Only save if IP is new
        if is_ip_new:
            # Add timestamp to IP check
            timestamp = datetime.now().strftime("%H:%M:%S")
            ip_check = {
                "time": timestamp,
                "ip": current_ip
            }
            
            # Add to today's history
            ip_history[current_date].append(ip_check)
            
            # Save updated history
            save_ip_history(ip_history)
        
        # Display only current status
        print(f"Current IP: {current_ip}")
        print(f"IP is new: {'Yes' if is_ip_new else 'No'}")
        
        sys.exit(0 if is_ip_new else 1)
    else:
        print("Failed to get IP")
        sys.exit(2)

if __name__ == "__main__":
    main() 
