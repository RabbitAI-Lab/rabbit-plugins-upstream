#!/usr/bin/env python3
import requests
import hashlib
import json
import sys
import os
import argparse


def check_site(url, state_file):
    """检查网站状态和内容变化"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; SiteMonitor/1.0)',
        'Accept': 'text/html'
    }

    try:
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()

        content_hash = hashlib.md5(r.text.encode()).hexdigest()

        old_state = {}
        if os.path.exists(state_file):
            with open(state_file, 'r') as f:
                old_state = json.load(f)

        status_code = r.status_code
        is_changed = old_state.get('hash') != content_hash

        with open(state_file, 'w') as f:
            json.dump({
                'hash': content_hash,
                'status': status_code,
                'last_check': str(__import__('datetime').datetime.now())
            }, f)

        return {
            'status': status_code,
            'changed': is_changed,
            'online': True,
            'message': f"✅ {url} 状态正常 (HTTP {status_code})"
        }

    except requests.exceptions.RequestException as e:
        return {
            'status': getattr(e.response, 'status_code', 0),
            'changed': False,
            'online': False,
            'message': f"❌ {url} 无法访问: {str(e)}"
        }


def cmd_check(args):
    all_msg = check_site(args.url, args.state_file)
    status = all_msg['status']
    changed = all_msg['changed']
    online = all_msg['online']
    message = all_msg['message']
    # print(status, changed, online, message)
    print(message)
    return 0 if not changed else 1


def main():
    parser = argparse.ArgumentParser(description="Website Monitor")
    subparsers = parser.add_subparsers(dest='command')
    p_check = subparsers.add_parser('check', help='Check site status')
    p_check.add_argument('url')
    p_check.add_argument('--state-file', default='/tmp/monitor-state.json')
    p_check.set_defaults(func=cmd_check)
    args = parser.parse_args()
    sys.exit(args.func(args))


if __name__ == '__main__':
    main()

