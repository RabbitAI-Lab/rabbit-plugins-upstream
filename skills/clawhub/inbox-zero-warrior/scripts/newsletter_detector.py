#!/usr/bin/env python3
"""
Newsletter Detector & Unsubscribe Manager

Identifies newsletters and promotional emails, generates unsubscribe action lists.

Usage:
  python newsletter_detector.py detect --input emails.json
  python newsletter_detector.py unsubscribe --input emails.json
  python newsletter_detector.py demo
"""

import json
import re
import sys
import argparse
from collections import Counter
from typing import List, Dict
from email.utils import parseaddr


# Known ESP (Email Service Provider) domains
ESP_DOMAINS = {
    'mailchimp.com': 'Mailchimp',
    'campaign-archive.com': 'Mailchimp',
    'sendgrid.net': 'SendGrid',
    'sendgrid.info': 'SendGrid',
    'sendgrid.com': 'SendGrid',
    'hubspot.com': 'HubSpot',
    'hs-email.com': 'HubSpot',
    'constantcontact.com': 'Constant Contact',
    'ccsend.com': 'Constant Contact',
    'mailgun.net': 'Mailgun',
    'amazonses.com': 'Amazon SES',
    'postmarkapp.com': 'Postmark',
    'mandrillapp.com': 'Mandrill',
    'bluehornet.com': 'Bluehornet',
    'exacttarget.com': 'ExactTarget',
    'marketo.com': 'Marketo',
    'mktomail.com': 'Marketo',
    'pardot.com': 'Pardot',
    'activecampaign.com': 'ActiveCampaign',
    'mailerlite.com': 'MailerLite',
    'convertkit.com': 'ConvertKit',
    'klaviyo.com': 'Klaviyo',
    'brevo.com': 'Brevo',
    'sendinblue.com': 'Brevo',
    'moosend.com': 'Moosend',
    'dianomi.com': 'Dianomi',
    'rsvpify.com': 'RSVPify',
    'emarsys.net': 'Emarsys',
}

# Known retailer/promo sender patterns
PROMO_KEYWORDS_IN_SENDER = ['promo', 'deals', 'offers', 'sale', 'marketing',
                            'newsletter', 'updates', 'noreply', 'no-reply',
                            'news', 'digest', 'weekly', 'monthly']


def extract_domain(email_addr: str) -> str:
    """Extract domain from email address."""
    _, addr = parseaddr(email_addr)
    if '@' in addr:
        return addr.split('@')[1].lower()
    return ''


def extract_sender_name(email_addr: str) -> str:
    """Extract sender display name or email."""
    name, addr = parseaddr(email_addr)
    return name if name else addr


def is_newsletter(email: dict) -> bool:
    """Detect if an email is a newsletter or promotional email."""
    headers = email.get('headers', {})
    sender = email.get('from', '').lower()
    body = email.get('body', '').lower()
    subject = email.get('subject', '').lower()
    domain = extract_domain(sender)
    
    # Strong signal: List-Unsubscribe header
    if headers.get('List-Unsubscribe'):
        return True
    
    # Strong signal: ESP domain
    for esp_domain in ESP_DOMAINS:
        if esp_domain in domain or esp_domain in sender:
            return True
    
    # Content signals
    newsletter_phrases = [
        'unsubscribe', 'manage preferences', 'view in browser',
        'update your email preferences', 'this email was sent to',
        'you are receiving this because', 'click here to unsubscribe',
        'to unsubscribe', 'privacy policy', 'terms of service',
    ]
    
    matches = sum(1 for phrase in newsletter_phrases if phrase in body)
    if matches >= 2:
        return True
    
    # Subject line patterns
    promo_subjects = ['sale', '% off', 'deal', 'offer', 'coupon', 'discount',
                      'limited time', 'expires', 'last chance', 'final hours']
    if any(p in subject for p in promo_subjects):
        return True
    
    return False


def extract_unsubscribe_info(email: dict) -> dict:
    """Extract unsubscribe method from a newsletter email."""
    headers = email.get('headers', {})
    body = email.get('body', '')
    
    unsub_info = {
        'method': None,
        'link': None,
        'email': None,
    }
    
    # Check List-Unsubscribe header
    list_unsub = headers.get('List-Unsubscribe', '')
    if list_unsub:
        # Could be mailto: or http(s)://
        mailto_match = re.search(r'<mailto:([^>]+)>', list_unsub)
        http_match = re.search(r'<(https?://[^>]+)>', list_unsub)
        
        if http_match:
            unsub_info['method'] = 'link'
            unsub_info['link'] = http_match.group(1)
        elif mailto_match:
            unsub_info['method'] = 'email'
            unsub_info['email'] = mailto_match.group(1)
    
    # Try to find unsubscribe link in body
    if not unsub_info['link']:
        link_patterns = [
            r'(?:unsubscribe|opt.?out|manage\s+preferences)[\s\S]*?(https?://[^\s<>"\']+)',
            r'(https?://[^\s<>"\']*(?:unsubscribe|optout|opt-out|preferences)[^\s<>"\']*)',
        ]
        for pattern in link_patterns:
            match = re.search(pattern, body, re.IGNORECASE)
            if match:
                unsub_info['method'] = 'link'
                unsub_info['link'] = match.group(1)
                break
    
    return unsub_info


def detect_newsletters(emails: List[dict]) -> List[dict]:
    """Detect all newsletters in a list of emails."""
    newsletters = []
    
    for email in emails:
        if is_newsletter(email):
            domain = extract_domain(email.get('from', ''))
            esp = ESP_DOMAINS.get(domain, '')
            if not esp:
                for esp_domain, esp_name in ESP_DOMAINS.items():
                    if esp_domain in domain:
                        esp = esp_name
                        break
            
            unsub = extract_unsubscribe_info(email)
            
            newsletters.append({
                'sender': email.get('from', ''),
                'domain': domain,
                'esp': esp,
                'subject': email.get('subject', ''),
                'date': email.get('date', ''),
                'unsubscribe': unsub,
                'has_easy_unsub': bool(unsub['method']),
            })
    
    return newsletters


def group_by_sender(newsletters: List[dict]) -> Dict[str, dict]:
    """Group newsletters by sender domain for bulk actions."""
    grouped = {}
    
    for nl in newsletters:
        domain = nl['domain']
        if domain not in grouped:
            grouped[domain] = {
                'domain': domain,
                'sender': nl['sender'],
                'esp': nl['esp'],
                'count': 0,
                'subjects': [],
                'has_easy_unsub': nl['has_easy_unsub'],
                'unsubscribe': nl['unsubscribe'],
            }
        grouped[domain]['count'] += 1
        grouped[domain]['subjects'].append(nl['subject'])
    
    return grouped


def generate_unsubscribe_list(emails: List[dict]) -> str:
    """Generate a prioritized unsubscribe action list."""
    newsletters = detect_newsletters(emails)
    grouped = group_by_sender(newsletters)
    
    # Sort by frequency (most emails = highest priority to unsubscribe)
    sorted_senders = sorted(grouped.values(), key=lambda x: x['count'], reverse=True)
    
    lines = []
    lines.append("")
    lines.append("📧 NEWSLETTER UNSUBSCRIBE LIST")
    lines.append("═" * 55)
    lines.append(f"Total newsletters detected: {len(newsletters)}")
    lines.append(f"Unique senders: {len(grouped)}")
    lines.append("")
    lines.append("PRIORITIZED BY FREQUENCY (unsubscribe highest-volume first):")
    lines.append("")
    
    for i, sender_info in enumerate(sorted_senders, 1):
        domain = sender_info['domain']
        count = sender_info['count']
        esp = sender_info['esp']
        easy = sender_info['has_easy_unsub']
        
        icon = "✅" if easy else "⚠️"
        
        lines.append(f"  {i}. {domain}")
        lines.append(f"     Emails received: {count}")
        if esp:
            lines.append(f"     ESP: {esp}")
        lines.append(f"     One-click unsub: {icon}")
        
        if easy:
            unsub = sender_info['unsubscribe']
            if unsub['method'] == 'link':
                lines.append(f"     Link: {unsub['link']}")
            elif unsub['method'] == 'email':
                lines.append(f"     Email: {unsub['email']}")
        else:
            lines.append(f"     → Manual: open email and find unsubscribe link")
        
        # Show sample subjects
        sample = sender_info['subjects'][:2]
        for s in sample:
            lines.append(f"     Example: \"{s}\"")
        lines.append("")
    
    # Summary
    easy_count = sum(1 for s in sorted_senders if s['has_easy_unsub'])
    total_time = len(sorted_senders) * 0.5  # 30 sec each
    
    lines.append("─" * 55)
    lines.append(f"📊 SUMMARY:")
    lines.append(f"  Easy unsubscribe (1-click): {easy_count}/{len(sorted_senders)}")
    lines.append(f"  Estimated time: {total_time:.0f} minutes")
    lines.append(f"  Emails eliminated: {sum(s['count'] for s in sorted_senders)}")
    lines.append("")
    
    return '\n'.join(lines)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Newsletter detector & unsubscribe manager')
    sub = parser.add_subparsers(dest='command')
    
    p_detect = sub.add_parser('detect', help='Detect newsletters in email export')
    p_detect.add_argument('--input', required=True)
    
    p_unsub = sub.add_parser('unsubscribe', help='Generate unsubscribe action list')
    p_unsub.add_argument('--input', required=True)
    
    sub.add_parser('demo', help='Run with sample data')
    
    args = parser.parse_args()
    
    if args.command == 'demo':
        from email_triage import generate_demo_emails
        emails = generate_demo_emails()
        print(generate_unsubscribe_list(emails))
        return
    
    if args.command == 'detect':
        with open(args.input) as f:
            emails = json.load(f)
        newsletters = detect_newsletters(emails)
        print(f"\n📧 Detected {len(newsletters)} newsletters out of {len(emails)} emails:")
        for nl in newsletters:
            print(f"  • {nl['domain']} — {nl['subject'][:50]}")
        return
    
    if args.command == 'unsubscribe':
        with open(args.input) as f:
            emails = json.load(f)
        print(generate_unsubscribe_list(emails))
        return
    
    parser.print_help()


if __name__ == '__main__':
    main()
