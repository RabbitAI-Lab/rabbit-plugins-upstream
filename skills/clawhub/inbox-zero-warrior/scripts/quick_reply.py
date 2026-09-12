#!/usr/bin/env python3
"""
Quick Reply Generator

Generates suggested email replies for common email patterns.

Usage:
  python quick_reply.py templates
  python quick_reply.py generate --input triaged.json
  python quick_reply.py generate --type meeting_confirm --sender "John" --context "Friday 3pm"
"""

import json
import re
import sys
import argparse
from datetime import datetime


REPLY_TEMPLATES = {
    'meeting_confirm': {
        'name': 'Meeting Confirmation',
        'triggers': ['meeting', 'meet', 'schedule', 'call', 'sync', 'catch up'],
        'subject_pattern': r'(meeting|call|sync|catch up|schedule)',
        'template': [
            "Hi {sender},",
            "",
            "Confirmed — I'll see you {context}. I've added it to my calendar.",
            "",
            "Looking forward to it.",
            "",
            "Best,",
            "{your_name}",
        ],
    },
    'meeting_reschedule': {
        'name': 'Meeting Reschedule',
        'triggers': ['reschedule', 'move', 'different time', 'can\'t make'],
        'subject_pattern': r'(reschedule|move|postpone|different time)',
        'template': [
            "Hi {sender},",
            "",
            "No problem at all. {context} works better for me too.",
            "I've updated my calendar.",
            "",
            "Thanks for flagging it.",
            "",
            "Best,",
            "{your_name}",
        ],
    },
    'meeting_decline': {
        'name': 'Meeting Decline',
        'triggers': ['decline', 'cannot attend', 'can\'t attend', 'unable'],
        'subject_pattern': r'(invited|invitation|meeting request)',
        'template': [
            "Hi {sender},",
            "",
            "Thanks for the invitation. Unfortunately, I won't be able to attend {context}.",
            "",
            "Could you share notes or a recording afterward? I'd like to stay in the loop.",
            "",
            "Best,",
            "{your_name}",
        ],
    },
    'acknowledgment': {
        'name': 'Quick Acknowledgment',
        'triggers': ['got it', 'thanks', 'noted', 'received'],
        'subject_pattern': r'.*',  # matches anything
        'template': [
            "Hi {sender},",
            "",
            "Got it — thanks for sending this over. I'll review and get back to you {context}.",
            "",
            "Best,",
            "{your_name}",
        ],
    },
    'will_follow_up': {
        'name': 'Will Follow Up',
        'triggers': ['follow up', 'get back', 'review and respond', 'need time'],
        'subject_pattern': r'.*',
        'template': [
            "Hi {sender},",
            "",
            "Thanks for this. I need to {context} before I can give you a proper response.",
            "I'll follow up by {deadline}.",
            "",
            "Best,",
            "{your_name}",
        ],
    },
    'document_received': {
        'name': 'Document/ File Received',
        'triggers': ['attached', 'document', 'file', 'report', 'draft'],
        'subject_pattern': r'(attached|document|report|file|draft|proposal)',
        'template': [
            "Hi {sender},",
            "",
            "Got the {context} — thanks. I'll review it and share feedback by {deadline}.",
            "",
            "Best,",
            "{your_name}",
        ],
    },
    'out_of_office': {
        'name': 'Out of Office (Auto-Reply)',
        'triggers': ['ooo', 'out of office', 'vacation', 'away'],
        'subject_pattern': r'.*',
        'template': [
            "Hi {sender},",
            "",
            "Thanks for your email. I'm currently out of the office {context}",
            "and will have limited access to email.",
            "",
            "For urgent matters, please contact {backup_contact}.",
            "Otherwise, I'll respond when I return.",
            "",
            "Best,",
            "{your_name}",
        ],
    },
    'intro_request': {
        'name': 'Introduction Request Response',
        'triggers': ['introduce', 'connect', 'intro', 'referral'],
        'subject_pattern': r'(introduc|connect|referral)',
        'template': [
            "Hi {sender},",
            "",
            "Happy to connect you. I've CC'd {context} here — {context}, meet {sender}.",
            "",
            "I'll let you two take it from here.",
            "",
            "Best,",
            "{your_name}",
        ],
    },
}


def match_template(email: dict) -> str:
    """Find the best matching template type for an email."""
    subject = email.get('subject', '').lower()
    body = email.get('body', '').lower()
    text = f"{subject} {body}"
    
    best_match = None
    best_score = 0
    
    for template_key, template in REPLY_TEMPLATES.items():
        score = 0
        
        # Check trigger words
        for trigger in template['triggers']:
            if trigger in text:
                score += 2
        
        # Check subject pattern
        if re.search(template['subject_pattern'], subject, re.IGNORECASE):
            score += 1
        
        if score > best_score:
            best_score = score
            best_match = template_key
    
    return best_match or 'acknowledgment'


def generate_reply(template_key: str, sender: str = 'there',
                   context: str = 'soon', deadline: str = 'end of week',
                   your_name: str = '[Your Name]',
                   backup_contact: str = '[colleague]') -> str:
    """Generate a reply from a template."""
    template = REPLY_TEMPLATES.get(template_key)
    if not template:
        return f"Unknown template: {template_key}"
    
    body = '\n'.join(template['template'])
    
    # Fill in variables
    body = body.replace('{sender}', sender)
    body = body.replace('{context}', context)
    body = body.replace('{deadline}', deadline)
    body = body.replace('{your_name}', your_name)
    body = body.replace('{backup_contact}', backup_contact)
    
    return body


def generate_replies_for_emails(triaged: list, your_name: str = '[Your Name]') -> list:
    """Generate suggested replies for all emails needing a response."""
    results = []
    
    for email in triaged:
        if email.get('action') in ('reply_now', 'reply_later'):
            template_key = match_template(email)
            sender_raw = email.get('from', '')
            # Extract name from email
            sender_name = sender_raw.split('<')[0].strip().split('@')[0]
            if not sender_name:
                sender_name = 'there'
            
            reply = generate_reply(template_key, sender=sender_name, your_name=your_name)
            
            results.append({
                'original_subject': email.get('subject', ''),
                'from': sender_raw,
                'urgency': email.get('urgency', ''),
                'template_used': template_key,
                'template_name': REPLY_TEMPLATES[template_key]['name'],
                'suggested_reply': reply,
            })
    
    return results


def list_templates():
    """List all available reply templates."""
    print("\n📋 AVAILABLE REPLY TEMPLATES:")
    print("=" * 55)
    for key, template in REPLY_TEMPLATES.items():
        print(f"\n  📝 {key}")
        print(f"     Name: {template['name']}")
        print(f"     Triggers: {', '.join(template['triggers'][:5])}")


def main():
    parser = argparse.ArgumentParser(description='Quick reply generator')
    sub = parser.add_subparsers(dest='command')
    
    p_gen = sub.add_parser('generate', help='Generate replies')
    p_gen.add_argument('--input', help='Triaged emails JSON')
    p_gen.add_argument('--type', help='Specific template type')
    p_gen.add_argument('--sender', default='there')
    p_gen.add_argument('--context', default='soon')
    p_gen.add_argument('--name', default='[Your Name]')
    
    sub.add_parser('templates', help='List all templates')
    
    args = parser.parse_args()
    
    if args.command == 'templates':
        list_templates()
        return
    
    if args.command == 'generate':
        if args.type:
            # Generate single reply from template
            reply = generate_reply(args.type, sender=args.sender,
                                   context=args.context, your_name=args.name)
            print(reply)
        elif args.input:
            # Generate replies for all actionable emails
            with open(args.input) as f:
                triaged = json.load(f)
            
            replies = generate_replies_for_emails(triaged, args.name)
            
            print(f"\n💬 GENERATED {len(replies)} SUGGESTED REPLIES:")
            print("=" * 55)
            
            for i, r in enumerate(replies, 1):
                print(f"\n--- Reply {i} ---")
                print(f"Re: {r['original_subject']}")
                print(f"From: {r['from']}")
                print(f"Urgency: {r['urgency']}")
                print(f"Template: {r['template_name']}")
                print()
                print(r['suggested_reply'])
                print("\n" + "-" * 55)
        else:
            parser.print_help()
        return
    
    parser.print_help()


if __name__ == '__main__':
    main()
