#!/usr/bin/env python3
"""
Email Triage Classifier

Classifies emails by urgency, category, and action needed.
Processes email exports in JSON format.

Usage:
  python email_triage.py triage --input emails.json --output triaged.json
  python email_triage.py report --input triaged.json
  python email_triage.py urgent --input triaged.json
  python email_triage.py demo
"""

import json
import re
import sys
import argparse
from datetime import datetime, timezone
from typing import List, Dict, Tuple
from collections import Counter


# ─── Classification Rules ─────────────────────────────────────────────────────

URGENT_KEYWORDS = [
    r'\burgent\b', r'\basap\b', r'\bcritical\b', r'\bemergency\b',
    r'\bdeadline\b', r'\bimmediately\b', r'\bby eod\b', r'\bby end of day\b',
    r'\bwithin the hour\b', r'\baction required\b', r'\btime.?sensitive\b',
]

URGENT_SUBJECT_PATTERNS = [
    r'(?i)\bURGENT\b', r'(?i)\bASAP\b', r'(?i)\bCRITICAL\b',
    r'(?i)\bEMERGENCY\b', r'(?i)\b!\s*!\s*!', r'(?i)\bACTION REQUIRED\b',
]

NEWSLETTER_ESP_DOMAINS = [
    'mailchimp.com', 'sendgrid.net', 'sendgrid.info', 'hubspot.com',
    'constantcontact.com', 'campaign-archive.com', 'mailgun.net',
    'amazonses.com', 'postmarkapp.com', 'mandrillapp.com',
    'dianomi.com', 'bluehornet.com', 'exacttarget.com',
    'marketo.com', 'pardot.com', 'activecampaign.com',
    'mailerlite.com', 'convertkit.com', 'klaviyo.com',
    'brevo.com', 'sendinblue.com', 'moosend.com',
]

NEWSLETTER_KEYWORDS = [
    'unsubscribe', 'manage preferences', 'view in browser',
    'update your email preferences', 'privacy policy', 'terms of service',
    'this email was sent to', 'you are receiving this',
    'click here to unsubscribe',
]

NOTIFICATION_DOMAINS = [
    'noreply', 'no-reply', 'donotreply', 'do-not-reply', 'notifications',
    'alert', 'automated', 'postmaster', 'mailer-daemon',
]

RECEIPT_KEYWORDS = [
    'receipt', 'order confirmation', 'invoice', 'payment received',
    'transaction', 'your order', 'purchase confirmation', 'statement',
    'billing', 'payment processed', 'thank you for your purchase',
]

QUICK_REPLY_PATTERNS = [
    r'(?i)\bcan you\b', r'(?i)\bdo you have\b', r'(?i)\bwhen\b',
    r'(?i)\bwhat time\b', r'(?i)\bplease confirm\b', r'(?i)\blet me know\b',
    r'(?i)\bthoughts\?\b', r'(?i)\breview\b', r'(?i)\bfeedback\b',
]


# ─── Classification Functions ─────────────────────────────────────────────────

def classify_urgency(email: dict) -> str:
    """Classify email urgency level."""
    subject = email.get('subject', '').lower()
    body = email.get('body', '').lower()
    text = f"{subject} {body}"
    
    # Check for urgent patterns
    for pattern in URGENT_SUBJECT_PATTERNS:
        if re.search(pattern, email.get('subject', '')):
            return 'critical'
    
    for keyword in URGENT_KEYWORDS:
        if re.search(keyword, text):
            return 'critical'
    
    # Check if it asks a question (needs response)
    has_question = '?' in email.get('body', '')
    has_request = any(re.search(p, body) for p in QUICK_REPLY_PATTERNS)
    
    if has_question or has_request:
        # Has a question — at least medium
        # Check if it seems time-sensitive
        if any(word in text for word in ['today', 'tomorrow', 'this week', 'meeting']):
            return 'high'
        return 'medium'
    
    return 'low'


def classify_category(email: dict) -> str:
    """Classify email category."""
    sender = email.get('from', '').lower()
    subject = email.get('subject', '').lower()
    body = email.get('body', '').lower()
    headers = email.get('headers', {})
    text = f"{sender} {subject} {body}"
    
    # Check for newsletter/promo
    if headers.get('List-Unsubscribe'):
        return 'newsletter'
    
    for esp in NEWSLETTER_ESP_DOMAINS:
        if esp in sender:
            return 'newsletter'
    
    for kw in NEWSLETTER_KEYWORDS:
        if kw in text:
            return 'newsletter'
    
    # Check for notification
    for domain in NOTIFICATION_DOMAINS:
        if domain in sender:
            return 'notification'
    
    # Check for receipt/finance
    for kw in RECEIPT_KEYWORDS:
        if kw in subject or kw in body:
            return 'receipt'
    
    # Check for social
    social_domains = ['facebook.com', 'twitter.com', 'linkedin.com', 'instagram.com',
                      'pinterest.com', 'tiktok.com', 'youtube.com', 'reddit.com']
    for domain in social_domains:
        if domain in sender:
            return 'social'
    
    # Default: work or personal
    personal_indicators = ['family', 'dinner', 'weekend', 'vacation', 'birthday']
    if any(word in text for word in personal_indicators):
        return 'personal'
    
    return 'work'


def determine_action(email: dict, urgency: str, category: str) -> str:
    """Determine recommended action for an email."""
    if urgency == 'critical':
        return 'reply_now'
    
    if category == 'newsletter':
        return 'unsubscribe'
    
    if category == 'notification':
        return 'file'
    
    if category == 'receipt':
        return 'file'
    
    if urgency == 'high':
        return 'reply_now'
    
    if urgency == 'medium':
        return 'reply_later'
    
    return 'delete'


def classify_email(email: dict) -> dict:
    """Classify a single email."""
    urgency = classify_urgency(email)
    category = classify_category(email)
    action = determine_action(email, urgency, category)
    
    return {
        **email,
        'urgency': urgency,
        'category': category,
        'action': action,
    }


def triage_emails(emails: List[dict]) -> List[dict]:
    """Triage a list of emails."""
    return [classify_email(e) for e in emails]


# ─── Reporting ────────────────────────────────────────────────────────────────

URGENCY_ICONS = {
    'critical': '🔴',
    'high': '🟠',
    'medium': '🟡',
    'low': '🔵',
}

CATEGORY_ICONS = {
    'work': '💼',
    'personal': '👤',
    'newsletter': '📧',
    'notification': '📱',
    'receipt': '🧾',
    'social': '🤝',
}

ACTION_LABELS = {
    'reply_now': 'Reply Now',
    'reply_later': 'Reply Later',
    'file': 'File',
    'unsubscribe': 'Unsubscribe',
    'delete': 'Delete',
}


def generate_report(triaged: List[dict]) -> str:
    """Generate a summary report."""
    total = len(triaged)
    
    urgency_counts = Counter(e['urgency'] for e in triaged)
    category_counts = Counter(e['category'] for e in triaged)
    action_counts = Counter(e['action'] for e in triaged)
    
    lines = []
    lines.append("")
    lines.append("📊 INBOX TRIAGE REPORT")
    lines.append("═" * 55)
    lines.append(f"Total emails: {total}")
    lines.append("")
    
    # Urgency breakdown
    lines.append("BY URGENCY:")
    for level in ['critical', 'high', 'medium', 'low']:
        count = urgency_counts.get(level, 0)
        icon = URGENCY_ICONS[level]
        pct = (count / total * 100) if total else 0
        desc = {
            'critical': 'Respond today',
            'high': 'Respond within 24h',
            'medium': 'Respond within a week',
            'low': 'No response needed',
        }[level]
        lines.append(f"  {icon} {level.title():8s} ({count:3d}) — {desc}")
    lines.append("")
    
    # Category breakdown
    lines.append("BY CATEGORY:")
    for cat in ['newsletter', 'notification', 'work', 'receipt', 'personal', 'social']:
        count = category_counts.get(cat, 0)
        icon = CATEGORY_ICONS.get(cat, '📧')
        lines.append(f"  {icon} {cat.title():20s}: {count}")
    lines.append("")
    
    # Action breakdown
    lines.append("ACTION NEEDED:")
    for action in ['reply_now', 'reply_later', 'file', 'unsubscribe', 'delete']:
        count = action_counts.get(action, 0)
        label = ACTION_LABELS[action]
        lines.append(f"  {label:15s}: {count} emails")
    
    # Time estimate
    reply_count = action_counts.get('reply_now', 0) + action_counts.get('reply_later', 0)
    unsub_count = action_counts.get('unsubscribe', 0)
    file_count = action_counts.get('file', 0) + action_counts.get('delete', 0)
    
    # Estimate: 2 min per reply, 30 sec per unsubscribe, 5 sec per file
    minutes = (reply_count * 2) + (unsub_count * 0.5) + (file_count * 0.1)
    
    lines.append("")
    lines.append(f"⏱️  ESTIMATED TIME TO INBOX ZERO: {int(minutes)} minutes")
    lines.append("")
    
    return '\n'.join(lines)


def show_urgent(triaged: List[dict]):
    """Show only urgent items."""
    urgent = [e for e in triaged if e['urgency'] in ('critical', 'high')]
    
    print(f"\n{'='*55}")
    print(f"🚨 URGENT ITEMS ({len(urgent)})")
    print(f"{'='*55}\n")
    
    for email in urgent:
        icon = URGENCY_ICONS[email['urgency']]
        print(f"{icon} [{email['urgency'].upper()}] {email.get('subject', '(no subject)')}")
        print(f"   From: {email.get('from', 'unknown')}")
        print(f"   Date: {email.get('date', 'unknown')}")
        body_preview = email.get('body', '')[:100].replace('\n', ' ')
        print(f"   Preview: {body_preview}...")
        print()


# ─── Sample Data for Demo ─────────────────────────────────────────────────────

def generate_demo_emails() -> List[dict]:
    """Generate sample emails for demonstration."""
    return [
        {
            'from': 'cfo@company.com',
            'to': 'you@company.com',
            'subject': 'URGENT: Q3 Budget Approval Needed Today',
            'date': '2026-08-13T09:00:00Z',
            'body': 'I need your approval on the Q3 budget by end of day today. Can you review and respond ASAP?',
        },
        {
            'from': 'sales@client.com',
            'to': 'you@company.com',
            'subject': 'Client demo in 2 hours - can you send slides?',
            'date': '2026-08-13T10:30:00Z',
            'body': 'The demo is in 2 hours. Do you have the presentation slides ready? Please confirm.',
        },
        {
            'from': 'devops@company.com',
            'to': 'you@company.com',
            'subject': 'CRITICAL: Production server down',
            'date': '2026-08-13T08:45:00Z',
            'body': 'The production server is down. This is an emergency. Action required immediately.',
        },
        {
            'from': 'colleague@company.com',
            'to': 'you@company.com',
            'subject': 'Project update - thoughts?',
            'date': '2026-08-13T07:00:00Z',
            'body': 'I updated the project plan. Let me know your thoughts when you have time this week.',
        },
        {
            'from': 'newsletter@techblog.com',
            'to': 'you@company.com',
            'subject': 'This Week in Tech - Issue #142',
            'date': '2026-08-13T06:00:00Z',
            'body': 'View in browser | Unsubscribe | Manage preferences. Top stories this week...',
            'headers': {'List-Unsubscribe': '<mailto:unsub@techblog.com>'},
        },
        {
            'from': 'noreply@amazon.com',
            'to': 'you@company.com',
            'subject': 'Your order has shipped',
            'date': '2026-08-13T05:00:00Z',
            'body': 'Your order confirmation. Track your package. This email was sent to you@company.com.',
        },
        {
            'from': 'notifications@github.com',
            'to': 'you@company.com',
            'subject': '[repo] PR #42 merged',
            'date': '2026-08-13T04:00:00Z',
            'body': 'Pull request #42 was merged by user. View on GitHub.',
        },
        {
            'from': 'promotions@retailer.com',
            'to': 'you@company.com',
            'subject': '50% OFF Everything - Today Only!',
            'date': '2026-08-13T03:00:00Z',
            'body': 'Click here for 50% off. Update your email preferences. Privacy policy.',
            'headers': {'List-Unsubscribe': '<mailto:unsub@retailer.com>'},
        },
        {
            'from': 'hr@company.com',
            'to': 'you@company.com',
            'subject': 'Meeting tomorrow at 2pm?',
            'date': '2026-08-13T11:00:00Z',
            'body': 'Can we meet tomorrow at 2pm to discuss the hiring process? Please confirm.',
        },
        {
            'from': 'billing@service.com',
            'to': 'you@company.com',
            'subject': 'Invoice #4521 - Payment Received',
            'date': '2026-08-13T02:00:00Z',
            'body': 'Thank you for your payment. Invoice #4521 has been paid. Transaction confirmed.',
        },
        {
            'from': 'friend@personal.com',
            'to': 'you@company.com',
            'subject': 'Dinner this weekend?',
            'date': '2026-08-13T12:00:00Z',
            'body': 'Hey! Want to grab dinner this weekend? What time works for you?',
        },
        {
            'from': 'updates@linkedin.com',
            'to': 'you@company.com',
            'subject': 'You appeared in 7 searches this week',
            'date': '2026-08-13T01:00:00Z',
            'body': 'See who searched for you. Update your preferences.',
        },
    ]


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Email triage classifier')
    sub = parser.add_subparsers(dest='command')
    
    # triage
    p_triage = sub.add_parser('triage', help='Triage an email export')
    p_triage.add_argument('--input', required=True, help='Input JSON file')
    p_triage.add_argument('--output', help='Output file for triaged emails')
    
    # report
    p_report = sub.add_parser('report', help='Show triage report')
    p_report.add_argument('--input', required=True)
    
    # urgent
    p_urgent = sub.add_parser('urgent', help='Show only urgent items')
    p_urgent.add_argument('--input', required=True)
    
    # demo
    sub.add_parser('demo', help='Run with sample data')
    
    args = parser.parse_args()
    
    if args.command == 'demo':
        emails = generate_demo_emails()
        triaged = triage_emails(emails)
        print(generate_report(triaged))
        show_urgent(triaged)
        return
    
    if args.command == 'triage':
        with open(args.input) as f:
            emails = json.load(f)
        triaged = triage_emails(emails)
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(triaged, f, indent=2)
            print(f"✓ Triaged {len(triaged)} emails → {args.output}")
        print(generate_report(triaged))
        return
    
    if args.command == 'report':
        with open(args.input) as f:
            triaged = json.load(f)
        print(generate_report(triaged))
        return
    
    if args.command == 'urgent':
        with open(args.input) as f:
            triaged = json.load(f)
        show_urgent(triaged)
        return
    
    parser.print_help()


if __name__ == '__main__':
    main()
