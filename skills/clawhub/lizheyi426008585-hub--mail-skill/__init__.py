"""
Exchange 2010 EWS integration for OpenClaw.
Provides email, calendar, contacts, tasks, and out-of-office management.
"""

import json
import os
import subprocess
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from exchangelib import Credentials, Account, DELEGATE, Configuration, EWSDateTime, EWSTimeZone
from exchangelib.folders import Folder
from exchangelib.items import Message, CalendarItem, Task, Contact
from exchangelib.version import Build, Version


def mask_password(text: str) -> str:
    """Replace password value with *** in any string output."""
    password = os.getenv('EXCHANGE_PASSWORD')
    if password and password in text:
        return text.replace(password, '***')
    return text


_builtin_print = print


def _masked_print(*args, **kwargs):
    args = tuple(mask_password(str(a)) for a in args)
    _builtin_print(*args, **kwargs)


print = _masked_print


def _find_credential_paths():
    """Build priority list of .env.credentials file paths."""
    paths = []

    # 1. Explicit env var (set by Electron skillManager)
    env_path = os.getenv('EXCHANGE_CREDENTIAL_PATH')
    if env_path:
        paths.append(env_path)

    # 2. User data directory (where the settings UI saves credentials)
    # macOS: ~/Library/Application Support/ennewClaw/exchange2010-skill/.env.credentials
    if os.name == 'posix' and os.uname().sysname == 'Darwin':
        user_data = os.path.expanduser('~/Library/Application Support/ennewClaw')
    elif os.name == 'posix':
        user_data = os.path.expanduser('~/.config/ennewClaw')
    elif os.name == 'nt':
        user_data = os.path.join(os.getenv('APPDATA', ''), 'ennewClaw')
    else:
        user_data = ''
    if user_data:
        paths.append(os.path.join(user_data, 'exchange2010-skill', '.env.credentials'))

    # 3. Skill directory (bundled defaults / manual editing)
    paths.append(os.path.join(os.path.dirname(__file__), '.env.credentials'))

    return paths


def _find_credential_file():
    """Find the first existing .env.credentials file."""
    for p in _find_credential_paths():
        if os.path.exists(p):
            return p
    return None


def _fetch_email_from_dws():
    """Call dws contact user get-self to get the user's email."""
    try:
        result = subprocess.run(
            ['dws', 'contact', 'user', 'get-self', '--format', 'json'],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode == 0:
            user_info = json.loads(result.stdout)
            email = user_info.get('orgAuthEmail') or user_info.get('email', '')
            if email and '@' in email:
                return email
    except Exception as e:
        print(f'[Exchange] DWS email lookup failed: {e}')
    return None


def _patch_credential_password(password):
    """Update EXCHANGE_PASSWORD in the credential file."""
    cred_path = _find_credential_file()
    if not cred_path:
        return
    lines = []
    found = False
    with open(cred_path, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith('EXCHANGE_PASSWORD='):
                lines.append(f'EXCHANGE_PASSWORD={password}')
                found = True
            else:
                lines.append(line.rstrip('\n'))
    if not found:
        lines.append(f'EXCHANGE_PASSWORD={password}')
    with open(cred_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')


def _patch_credential_email(email):
    """Add or update EXCHANGE_EMAIL in the credential file."""
    cred_path = _find_credential_file()
    if not cred_path:
        return
    lines = []
    found = False
    with open(cred_path, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith('EXCHANGE_EMAIL='):
                lines.append(f'EXCHANGE_EMAIL={email}')
                found = True
            else:
                lines.append(line.rstrip('\n'))
    if not found:
        lines.append(f'EXCHANGE_EMAIL={email}')
    with open(cred_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')


def _test_credentials(email, password, server):
    """Try connecting to Exchange to verify credentials. Returns True on success."""
    try:
        creds = Credentials(username=email, password=password)
        config = Configuration(
            server=server,
            credentials=creds,
            version=Version(build=Build(15, 0, 0, 0))
        )
        account = Account(
            primary_smtp_address=email,
            config=config,
            autodiscover=False,
            access_type=DELEGATE
        )
        # Access inbox to trigger authentication
        _ = account.inbox.children
        return True
    except Exception as e:
        err_msg = str(e).lower()
        if 'unauthorized' in err_msg or '401' in err_msg or 'invalid credential' in err_msg or 'auth' in err_msg:
            return False
        # Network/other errors — don't treat as wrong password
        raise


def get_credentials():
    """Load Exchange credentials from environment or .env.credentials file."""
    default_server = 'mail.enn.cn'

    for env_file in _find_credential_paths():
        if os.path.exists(env_file):
            with open(env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        value = value.strip()
                        if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                            value = value[1:-1]
                        os.environ[key.strip()] = value
            break

    server = os.getenv('EXCHANGE_SERVER') or default_server
    email = os.getenv('EXCHANGE_EMAIL')
    password = os.getenv('EXCHANGE_PASSWORD') or os.getenv('PICARD_PASSWORD')

    # Auto-discover email via DWS if missing
    if not email:
        email = _fetch_email_from_dws()
        if email:
            os.environ['EXCHANGE_EMAIL'] = email
            _patch_credential_email(email)
            print(f'[Exchange] Auto-configured email: {email}')

    if not email:
        raise ValueError(
            "Exchange 邮箱地址未获取到。\n\n"
            "请确认已登录钉钉工作台（DWS），然后重新尝试。"
        )

    if not password:
        raise ValueError(
            "Exchange 邮箱密码未配置。\n\n"
            "请使用密码方式登录 EnnewClaw，密码会自动同步到 Exchange。"
        )

    os.environ['EXCHANGE_SERVER'] = server

    # Verify credentials by attempting connection
    try:
        if _test_credentials(email, password, server):
            print(f'[Exchange] Connected as {email} (password: ***)')
            return Credentials(username=email, password=password)
    except Exception:
        # Network or server error — proceed anyway, let the actual operation fail later
        print(f'[Exchange] Could not verify credentials (network error), proceeding as {email}')
        return Credentials(username=email, password=password)

    # Credentials are wrong — prompt user for correct password
    raise ValueError(
        f"Exchange 邮箱密码验证失败（邮箱: {email}）。\n\n"
        "当前保存的密码可能不是邮箱的登录密码。请在对话中提供正确的邮箱密码，"
        "我会更新配置后重新尝试连接。"
    )


def update_exchange_password(new_password: str) -> str:
    """
    Update the Exchange password and retry connection.

    Use this when the saved password is incorrect and the user provides
    the correct one. The credential file is updated so future operations
    work without re-prompting.

    Args:
        new_password: The correct Exchange/email password from the user

    Returns:
        Confirmation message
    """
    email = os.getenv('EXCHANGE_EMAIL')
    server = os.getenv('EXCHANGE_SERVER') or 'mail.enn.cn'

    if not email:
        email = _fetch_email_from_dws()
        if email:
            os.environ['EXCHANGE_EMAIL'] = email
            _patch_credential_email(email)

    if not email:
        return "错误：无法获取邮箱地址，请先确认已登录钉钉工作台（DWS）。"

    # Verify the new password works
    try:
        if not _test_credentials(email, new_password, server):
            return f"密码验证失败（邮箱: {email}），请确认密码是否正确。"
    except Exception as e:
        # Network error — save password anyway, will verify on next use
        print(f'[Exchange] Network error during password verification: {e}')

    # Save the new password
    os.environ['EXCHANGE_PASSWORD'] = new_password
    _patch_credential_password(new_password)
    print(f'[Exchange] Password updated for {email}')
    return f"邮箱密码已更新，可以继续进行邮箱操作。"


def get_account(email_address: Optional[str] = None) -> Account:
    """
    Connect to Exchange server.
    
    Args:
        email_address: Optional email address for shared mailbox access
        
    Returns:
        Account object connected to Exchange
    """
    credentials = get_credentials()
    server = os.getenv('EXCHANGE_SERVER')
    primary_email = os.getenv('EXCHANGE_EMAIL')
    
    config = Configuration(
        server=server,
        credentials=credentials,
        version=Version(build=Build(15, 0, 0, 0))  # Exchange 2013
    )
    
    target_email = email_address or primary_email
    
    account = Account(
        primary_smtp_address=target_email,
        config=config,
        autodiscover=False,
        access_type=DELEGATE
    )
    
    return account


def get_unread_emails(account: Account, limit: int = 50) -> List[Dict[str, Any]]:
    """
    Get unread emails from inbox.
    
    Args:
        account: Exchange account
        limit: Maximum number of emails to return
        
    Returns:
        List of email dictionaries
    """
    emails = []
    for item in account.inbox.filter(is_read=False).order_by('-datetime_received')[:limit]:
        emails.append({
            'id': item.id,
            'subject': item.subject,
            'sender': str(item.sender),
            'datetime_received': item.datetime_received.isoformat() if item.datetime_received else None,
            'body': item.text_body[:500] if item.text_body else '',
            'has_attachments': item.has_attachments
        })
    return emails


def search_emails(
    search_term: Optional[str] = None,
    sender: Optional[str] = None,
    subject: Optional[str] = None,
    is_unread: Optional[bool] = None,
    folder: str = 'inbox',
    limit: int = 50
) -> List[Dict[str, Any]]:
    """
    Search emails with various filters.
    
    Args:
        search_term: General search term
        sender: Filter by sender
        subject: Filter by subject
        is_unread: Filter by read status
        folder: Folder to search (inbox, sent, drafts, etc.)
        limit: Maximum results
        
    Returns:
        List of email dictionaries
    """
    account = get_account()
    
    # Get target folder
    if folder.lower() == 'inbox':
        target_folder = account.inbox
    elif folder.lower() == 'sent':
        target_folder = account.sent
    elif folder.lower() == 'drafts':
        target_folder = account.drafts
    elif folder.lower() == 'trash':
        target_folder = account.trash
    elif folder.lower() == 'junk':
        target_folder = account.junk
    else:
        target_folder = account.inbox
    
    # Build filter
    filters = {}
    if is_unread is not None:
        filters['is_read'] = not is_unread
    if sender:
        filters['sender__contains'] = sender
    if subject:
        filters['subject__contains'] = subject
    if search_term:
        filters['text_body__contains'] = search_term
    
    if filters:
        items = target_folder.filter(**filters).order_by('-datetime_received')[:limit]
    else:
        items = target_folder.all().order_by('-datetime_received')[:limit]
    
    emails = []
    for item in items:
        if isinstance(item, Message):
            emails.append({
                'id': item.id,
                'subject': item.subject,
                'sender': str(item.sender),
                'datetime_received': item.datetime_received.isoformat() if item.datetime_received else None,
                'body': item.text_body[:500] if item.text_body else '',
                'has_attachments': item.has_attachments
            })
    
    return emails


def send_email(
    to: List[str],
    subject: str,
    body: str,
    cc: Optional[List[str]] = None,
    bcc: Optional[List[str]] = None
) -> str:
    """
    Send an email.
    
    Args:
        to: List of recipient email addresses
        subject: Email subject
        body: Email body text
        cc: Optional CC recipients
        bcc: Optional BCC recipients
        
    Returns:
        Message ID of sent email
    """
    account = get_account()
    
    message = Message(
        account=account,
        subject=subject,
        body=body,
        to_recipients=to,
        cc_recipients=cc or [],
        bcc_recipients=bcc or []
    )
    
    message.send_and_save()
    return message.id


def mark_email_as_read(email_id: str) -> bool:
    """
    Mark an email as read.
    
    Args:
        email_id: Email item ID
        
    Returns:
        True if successful
    """
    account = get_account()
    
    item = account.inbox.get(id=email_id)
    item.is_read = True
    item.save()
    return True


def get_email_attachments(
    email_id: str,
    download_path: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Get attachments from an email.
    
    Args:
        email_id: Email item ID
        download_path: Optional path to download attachments
        
    Returns:
        List of attachment info dictionaries
    """
    account = get_account()
    
    item = account.inbox.get(id=email_id)
    attachments = []
    
    for attachment in item.attachments:
        att_info = {
            'name': attachment.name,
            'size': attachment.size if hasattr(attachment, 'size') else len(attachment.content) if hasattr(attachment, 'content') else 0,
            'content_type': attachment.content_type if hasattr(attachment, 'content_type') else None
        }
        
        if download_path and hasattr(attachment, 'content'):
            os.makedirs(download_path, exist_ok=True)
            file_path = os.path.join(download_path, attachment.name)
            with open(file_path, 'wb') as f:
                f.write(attachment.content)
            att_info['downloaded_path'] = file_path
        
        attachments.append(att_info)
    
    return attachments


def process_attachment_content(
    email_id: str,
    attachment_name: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Extract text content from attachments (PDF, TXT).
    
    Args:
        email_id: Email item ID
        attachment_name: Optional specific attachment name
        
    Returns:
        List of attachment content dictionaries
    """
    account = get_account()
    item = account.inbox.get(id=email_id)
    
    results = []
    
    for attachment in item.attachments:
        if attachment_name and attachment.name != attachment_name:
            continue
        
        result = {
            'name': attachment.name,
            'extracted_text': None
        }
        
        if hasattr(attachment, 'content') and attachment.content:
            # Try to extract text based on file type
            if attachment.name.lower().endswith('.txt'):
                try:
                    result['extracted_text'] = attachment.content.decode('utf-8')
                except:
                    result['extracted_text'] = attachment.content.decode('latin-1')
            elif attachment.name.lower().endswith('.pdf'):
                try:
                    import PyPDF2
                    import io
                    pdf_reader = PyPDF2.PdfReader(io.BytesIO(attachment.content))
                    text = ''
                    for page in pdf_reader.pages:
                        text += page.extract_text()
                    result['extracted_text'] = text
                except ImportError:
                    result['error'] = 'PyPDF2 not installed. Run: pip install PyPDF2'
                except Exception as e:
                    result['error'] = str(e)
        
        results.append(result)
    
    return results


def get_folder_emails(
    folder_name: str,
    limit: int = 50,
    is_unread: Optional[bool] = None
) -> List[Dict[str, Any]]:
    """
    Get emails from a specific folder.
    
    Args:
        folder_name: Folder name (inbox, sent, drafts, trash, junk)
        limit: Maximum number of emails
        is_unread: Filter by read status
        
    Returns:
        List of email dictionaries
    """
    account = get_account()
    
    folder_map = {
        'inbox': account.inbox,
        'sent': account.sent,
        'drafts': account.drafts,
        'trash': account.trash,
        'junk': account.junk
    }
    
    target_folder = folder_map.get(folder_name.lower(), account.inbox)
    
    filters = {}
    if is_unread is not None:
        filters['is_read'] = not is_unread
    
    if filters:
        items = target_folder.filter(**filters).order_by('-datetime_received')[:limit]
    else:
        items = target_folder.all().order_by('-datetime_received')[:limit]
    
    emails = []
    for item in items:
        if isinstance(item, Message):
            emails.append({
                'id': item.id,
                'subject': item.subject,
                'sender': str(item.sender),
                'datetime_received': item.datetime_received.isoformat() if item.datetime_received else None,
                'body': item.text_body[:500] if item.text_body else '',
                'has_attachments': item.has_attachments
            })
    
    return emails


def list_email_folders(account: Account) -> List[Dict[str, Any]]:
    """
    List all email folders.
    
    Args:
        account: Exchange account
        
    Returns:
        List of folder info dictionaries
    """
    folders = []
    for folder in account.root.walk():
        if hasattr(folder, 'total_count'):
            folders.append({
                'name': folder.name,
                'total_count': folder.total_count,
                'unread_count': folder.unread_count
            })
    return folders


def get_today_events(email_address: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Get today's calendar events.
    
    Args:
        email_address: Optional email for shared calendar
        
    Returns:
        List of event dictionaries
    """
    account = get_account(email_address)
    
    tz = EWSTimeZone('Asia/Shanghai')
    start = EWSDateTime.now(tz).replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=1)
    
    events = []
    for item in account.calendar.filter(start__gte=start, start__lte=end).order_by('start'):
        if isinstance(item, CalendarItem):
            events.append({
                'id': item.id,
                'subject': item.subject,
                'start': item.start.isoformat() if item.start else None,
                'end': item.end.isoformat() if item.end else None,
                'location': str(item.location) if item.location else None,
                'body': item.text_body[:200] if item.text_body else '',
                'is_recurring': item.is_recurring if hasattr(item, 'is_recurring') else False
            })
    
    return events


def get_upcoming_events(
    email_address: Optional[str] = None,
    days: int = 7
) -> List[Dict[str, Any]]:
    """
    Get upcoming calendar events for next N days.
    
    Args:
        email_address: Optional email for shared calendar
        days: Number of days to look ahead
        
    Returns:
        List of event dictionaries
    """
    account = get_account(email_address)
    
    tz = EWSTimeZone('Asia/Shanghai')
    start = EWSDateTime.now(tz)
    end = start + timedelta(days=days)
    
    events = []
    for item in account.calendar.filter(start__gte=start, start__lte=end).order_by('start'):
        if isinstance(item, CalendarItem):
            events.append({
                'id': item.id,
                'subject': item.subject,
                'start': item.start.isoformat() if item.start else None,
                'end': item.end.isoformat() if item.end else None,
                'location': str(item.location) if item.location else None,
                'body': item.text_body[:200] if item.text_body else '',
                'is_recurring': item.is_recurring if hasattr(item, 'is_recurring') else False
            })
    
    return events


def get_calendar_events(
    account: Account,
    start: datetime,
    end: datetime
) -> List[Dict[str, Any]]:
    """
    Get calendar events in a date range.
    
    Args:
        account: Exchange account
        start: Start datetime
        end: End datetime
        
    Returns:
        List of event dictionaries
    """
    tz = EWSTimeZone('Asia/Shanghai')
    ews_start = EWSDateTime.from_datetime(start).astimezone(tz)
    ews_end = EWSDateTime.from_datetime(end).astimezone(tz)
    
    events = []
    for item in account.calendar.filter(start__gte=ews_start, start__lte=ews_end).order_by('start'):
        if isinstance(item, CalendarItem):
            events.append({
                'id': item.id,
                'subject': item.subject,
                'start': item.start.isoformat() if item.start else None,
                'end': item.end.isoformat() if item.end else None,
                'location': str(item.location) if item.location else None,
                'body': item.text_body[:200] if item.text_body else '',
                'is_recurring': item.is_recurring if hasattr(item, 'is_recurring') else False
            })
    
    return events


def get_shared_calendar_events(
    email: str,
    start: datetime,
    end: datetime
) -> List[Dict[str, Any]]:
    """
    Get events from a shared calendar.
    
    Args:
        email: Email address of shared calendar owner
        start: Start datetime
        end: End datetime
        
    Returns:
        List of event dictionaries
    """
    account = get_account(email)
    return get_calendar_events(account, start, end)


def search_calendar_by_subject(
    email_address: str,
    search_term: str,
    start_date: datetime,
    end_date: datetime
) -> List[Dict[str, Any]]:
    """
    Search calendar events by subject.
    
    Args:
        email_address: Email address
        search_term: Subject search term
        start_date: Start date
        end_date: End date
        
    Returns:
        List of matching events
    """
    account = get_account(email_address)
    
    tz = EWSTimeZone('Asia/Shanghai')
    ews_start = EWSDateTime.from_datetime(start_date).astimezone(tz)
    ews_end = EWSDateTime.from_datetime(end_date).astimezone(tz)
    
    events = []
    for item in account.calendar.filter(
        start__gte=ews_start,
        start__lte=ews_end,
        subject__contains=search_term
    ).order_by('start'):
        if isinstance(item, CalendarItem):
            events.append({
                'id': item.id,
                'subject': item.subject,
                'start': item.start.isoformat() if item.start else None,
                'end': item.end.isoformat() if item.end else None,
                'location': str(item.location) if item.location else None
            })
    
    return events


def create_calendar_event(
    subject: str,
    start: datetime,
    end: datetime,
    body: str = '',
    location: str = ''
) -> str:
    """
    Create a calendar event.
    
    Args:
        subject: Event subject
        start: Start datetime
        end: End datetime
        body: Event body/description
        location: Event location
        
    Returns:
        Event ID
    """
    account = get_account()
    tz = EWSTimeZone('Asia/Shanghai')
    
    event = CalendarItem(
        account=account,
        subject=subject,
        start=EWSDateTime.from_datetime(start).astimezone(tz),
        end=EWSDateTime.from_datetime(end).astimezone(tz),
        body=body,
        location=location
    )
    
    event.save()
    return event.id


def update_calendar_event(
    event_id: str,
    subject: Optional[str] = None,
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
    body: Optional[str] = None,
    location: Optional[str] = None
) -> bool:
    """
    Update a calendar event.
    
    Args:
        event_id: Event ID to update
        subject: New subject (optional)
        start: New start time (optional)
        end: New end time (optional)
        body: New body (optional)
        location: New location (optional)
        
    Returns:
        True if successful
    """
    account = get_account()
    tz = EWSTimeZone('Asia/Shanghai')
    
    event = account.calendar.get(id=event_id)
    
    if subject:
        event.subject = subject
    if start:
        event.start = EWSDateTime.from_datetime(start).astimezone(tz)
    if end:
        event.end = EWSDateTime.from_datetime(end).astimezone(tz)
    if body:
        event.body = body
    if location:
        event.location = location
    
    event.save()
    return True


def get_event_details(event_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a calendar event.
    
    Args:
        event_id: Event ID
        
    Returns:
        Event details dictionary
    """
    account = get_account()
    event = account.calendar.get(id=event_id)
    
    return {
        'id': event.id,
        'subject': event.subject,
        'start': event.start.isoformat() if event.start else None,
        'end': event.end.isoformat() if event.end else None,
        'location': str(event.location) if event.location else None,
        'body': event.text_body,
        'organizer': str(event.organizer) if event.organizer else None,
        'required_attendees': [str(a) for a in event.required_attendees] if event.required_attendees else [],
        'optional_attendees': [str(a) for a in event.optional_attendees] if event.optional_attendees else [],
        'is_recurring': event.is_recurring if hasattr(event, 'is_recurring') else False
    }


def delete_calendar_event(event_id: str) -> bool:
    """
    Delete a calendar event.
    
    Args:
        event_id: Event ID to delete
        
    Returns:
        True if successful
    """
    account = get_account()
    event = account.calendar.get(id=event_id)
    event.delete()
    return True


def get_recurring_events(
    email_address: Optional[str] = None,
    days: int = 30
) -> List[Dict[str, Any]]:
    """
    Get recurring calendar events.
    
    Args:
        email_address: Optional email for shared calendar
        days: Number of days to look ahead
        
    Returns:
        List of recurring events
    """
    account = get_account(email_address)
    
    tz = EWSTimeZone('Asia/Shanghai')
    start = EWSDateTime.now(tz)
    end = start + timedelta(days=days)
    
    events = []
    for item in account.calendar.filter(start__gte=start, start__lte=end).order_by('start'):
        if isinstance(item, CalendarItem) and hasattr(item, 'is_recurring') and item.is_recurring:
            events.append({
                'id': item.id,
                'subject': item.subject,
                'start': item.start.isoformat() if item.start else None,
                'end': item.end.isoformat() if item.end else None,
                'recurrence': str(item.recurrence) if hasattr(item, 'recurrence') and item.recurrence else None
            })
    
    return events


def list_available_calendars(account: Account) -> List[Dict[str, Any]]:
    """
    List all available calendar folders.
    
    Args:
        account: Exchange account
        
    Returns:
        List of calendar info dictionaries
    """
    calendars = []
    for folder in account.root.walk():
        if folder.folder_class == 'IPF.Appointment':
            calendars.append({
                'name': folder.name,
                'folder_id': folder.id
            })
    return calendars


def search_contacts(search_term: str, limit: int = 50) -> List[Dict[str, Any]]:
    """
    Search contacts.
    
    Args:
        search_term: Search term (name or email)
        limit: Maximum results
        
    Returns:
        List of contact dictionaries
    """
    account = get_account()
    
    contacts = []
    for item in account.contacts.filter(display_name__contains=search_term).order_by('display_name')[:limit]:
        if isinstance(item, Contact):
            contacts.append({
                'id': item.id,
                'name': item.display_name,
                'email': item.email_addresses[0].email if item.email_addresses else None,
                'phone': item.phone_numbers[0].phone_number if item.phone_numbers else None
            })
    
    return contacts


def resolve_name(name: str) -> Optional[Dict[str, Any]]:
    """
    Resolve a name using Global Address List (GAL).
    
    Args:
        name: Name or email to resolve
        
    Returns:
        Contact info dictionary or None
    """
    account = get_account()
    
    try:
        results = account.protocol.resolve_names(name)
        if results:
            return {
                'name': results[0][0],
                'email': results[0][1]
            }
    except:
        pass
    
    return None


def get_tasks(status: Optional[str] = None, folder: str = 'tasks') -> List[Dict[str, Any]]:
    """
    Get tasks.
    
    Args:
        status: Filter by status (optional)
        folder: Task folder (default: tasks)
        
    Returns:
        List of task dictionaries
    """
    account = get_account()
    
    tasks = []
    
    # Get tasks folder
    if folder == 'tasks':
        target_folder = account.tasks
    else:
        target_folder = account.tasks
    
    for item in target_folder.all().order_by('-due_date'):
        if isinstance(item, Task):
            task_info = {
                'id': item.id,
                'subject': item.subject,
                'is_complete': item.is_complete if hasattr(item, 'is_complete') else False,
                'due_date': item.due_date.isoformat() if item.due_date else None,
                'status': item.status if hasattr(item, 'status') else None,
                'importance': item.importance if hasattr(item, 'importance') else None
            }
            
            if status is None or (status == 'complete' and task_info['is_complete']) or (status == 'open' and not task_info['is_complete']):
                tasks.append(task_info)
    
    return tasks


def create_task(
    subject: str,
    body: str = '',
    due_date: Optional[datetime] = None,
    importance: str = 'Normal',
    categories: Optional[List[str]] = None
) -> str:
    """
    Create a new task.
    
    Args:
        subject: Task subject
        body: Task body/description
        due_date: Due date
        importance: Importance level (Low, Normal, High)
        categories: List of categories
        
    Returns:
        Task ID
    """
    account = get_account()
    
    task = Task(
        account=account,
        subject=subject,
        body=body,
        importance=importance
    )
    
    if due_date:
        tz = EWSTimeZone('Asia/Shanghai')
        task.due_date = EWSDateTime.from_datetime(due_date).astimezone(tz)
    
    if categories:
        task.categories = categories
    
    task.save()
    return task.id


def complete_task(task_id: str) -> bool:
    """
    Mark a task as complete.
    
    Args:
        task_id: Task ID
        
    Returns:
        True if successful
    """
    account = get_account()
    task = account.tasks.get(id=task_id)
    task.is_complete = True
    task.save()
    return True


def delete_task(task_id: str) -> bool:
    """
    Delete a task.
    
    Args:
        task_id: Task ID
        
    Returns:
        True if successful
    """
    account = get_account()
    task = account.tasks.get(id=task_id)
    task.delete()
    return True


def get_out_of_office(email_address: Optional[str] = None) -> Dict[str, Any]:
    """
    Get out-of-office status.
    
    Args:
        email_address: Optional email address
        
    Returns:
        Out-of-office status dictionary
    """
    account = get_account(email_address)
    
    oof_settings = account.protocol.get_user_oof_settings(account.primary_smtp_address)
    
    return {
        'enabled': oof_settings.oof_state == 'Scheduled' or oof_settings.oof_state == 'Enabled',
        'internal_reply': oof_settings.internal_reply.message if hasattr(oof_settings.internal_reply, 'message') else str(oof_settings.internal_reply),
        'external_reply': oof_settings.external_reply.message if hasattr(oof_settings.external_reply, 'message') else str(oof_settings.external_reply),
        'start': oof_settings.scheduled_start.isoformat() if hasattr(oof_settings, 'scheduled_start') and oof_settings.scheduled_start else None,
        'end': oof_settings.scheduled_end.isoformat() if hasattr(oof_settings, 'scheduled_end') and oof_settings.scheduled_end else None
    }


def set_out_of_office(
    enabled: bool,
    internal_reply: str = '',
    external_reply: str = '',
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
    external_audience: str = 'All'
) -> bool:
    """
    Set out-of-office status.
    
    Args:
        enabled: Enable or disable OOF
        internal_reply: Internal reply message
        external_reply: External reply message
        start: Scheduled start time
        end: Scheduled end time
        external_audience: External audience (All, Known, None)
        
    Returns:
        True if successful
    """
    account = get_account()
    
    from exchangelib.settings import OofSettings
    
    oof_state = 'Enabled' if enabled else 'Disabled'
    if start and end:
        oof_state = 'Scheduled'
        tz = EWSTimeZone('Asia/Shanghai')
        oof_start = EWSDateTime.from_datetime(start).astimezone(tz)
        oof_end = EWSDateTime.from_datetime(end).astimezone(tz)
    
    oof_settings = OofSettings(
        state=oof_state,
        internal_reply=internal_reply,
        external_reply=external_reply,
        scheduled_start=oof_start if start and end else None,
        scheduled_end=oof_end if start and end else None,
        external_audience=external_audience
    )
    
    account.protocol.set_user_oof_settings(account.primary_smtp_address, oof_settings)
    return True


def count_ekadashi_events(email: str, start_year: int) -> int:
    """
    Count Ekadashi events in calendar.
    
    Args:
        email: Email address
        start_year: Year to start counting from
        
    Returns:
        Number of Ekadashi events found
    """
    from datetime import date
    
    events = search_calendar_by_subject(
        email_address=email,
        search_term='Ekadashi',
        start_date=date(start_year, 1, 1),
        end_date=date(start_year + 1, 12, 31)
    )
    
    return len(events)
