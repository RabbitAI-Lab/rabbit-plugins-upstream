#!/usr/bin/env python3
"""Build and reserve risk-based team-task reminders.

This is deliberately a policy and storage adapter, not a scheduler or a
notification client.  A trusted integration invokes it at the configured
time, supplies the local holiday calendar, sends the returned messages, and
uses the returned ``scheduledFor`` value for its randomized delivery time.
"""

import argparse
import datetime as dt
import json
import random
import sys
from pathlib import Path

from task_store import MAIN, StoreError, TaskStore


SLOTS = ('09:00', '10:00', '14:00', '18:00')
LEVELS = ('low', 'medium', 'high', 'critical')
LEVEL_NUMBER = {level: number for number, level in enumerate(LEVELS)}
URGENCY_NUMBER = {'overdue': 4, 'today': 3, 'soon': 2, 'normal': 1, 'none': 0}
PRIORITY_NUMBER = {'critical': 4, 'high': 3, 'medium': 2, 'low': 1}


def parse_now(value=None):
    if value is None:
        return dt.datetime.now().astimezone()
    parsed = dt.datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise ValueError('--now must include a UTC offset')
    return parsed


def due_at(task, tzinfo):
    """Return the effective deadline; a date-only deadline ends that day."""
    due_date = task.get('dueDate')
    if due_date in (None, '', 'none'):
        return None
    day = dt.date.fromisoformat(due_date)
    due_time = task.get('dueTime')
    clock = dt.time.fromisoformat(due_time) if due_time not in (None, '', 'none') else dt.time.max
    return dt.datetime.combine(day, clock, tzinfo=tzinfo)


def urgency_for(task, now):
    deadline = due_at(task, now.tzinfo)
    if deadline is None:
        return 'none', None
    if now > deadline:
        return 'overdue', deadline
    if deadline.date() == now.date() or deadline - now <= dt.timedelta(hours=24):
        return 'today', deadline
    if deadline - now <= dt.timedelta(hours=72):
        return 'soon', deadline
    return 'normal', deadline


def raise_level(level):
    return LEVELS[min(LEVEL_NUMBER[level] + 1, len(LEVELS) - 1)]


def attention_for(task, urgency):
    """Combine business priority, time risk, and blocking without mutating a task."""
    priority = task.get('priority', 'medium')
    if priority not in PRIORITY_NUMBER:
        priority = 'medium'
    attention = priority
    if urgency == 'overdue':
        attention = max((attention, 'high'), key=LEVEL_NUMBER.get)
    elif urgency == 'today':
        attention = max((attention, 'high'), key=LEVEL_NUMBER.get)
        if priority in ('high', 'critical'):
            attention = 'critical'
    elif urgency == 'soon':
        attention = max((attention, 'medium'), key=LEVEL_NUMBER.get)
    if task.get('isBlocking'):
        attention = raise_level(attention)
    return attention


def classified(task, now):
    urgency, deadline = urgency_for(task, now)
    priority = task.get('priority', 'medium')
    if priority not in PRIORITY_NUMBER:
        priority = 'medium'
    return {**task, 'priority': priority, 'urgency': urgency, 'deadline': deadline,
            'attentionLevel': attention_for(task, urgency)}


def action_sort_key(task):
    deadline = task['deadline'] or dt.datetime.max.replace(tzinfo=dt.timezone.utc)
    # Earlier deadline wins within identical risk, followed by stable task ID.
    return (-LEVEL_NUMBER[task['attentionLevel']], -URGENCY_NUMBER[task['urgency']],
            -PRIORITY_NUMBER[task['priority']], not task.get('isBlocking', False), deadline, task['id'])


def is_summary_candidate(task):
    return (task['urgency'] in ('overdue', 'today', 'soon') or
            (task.get('isBlocking') and task['priority'] in ('critical', 'high')))


def selected_for_slot(tasks, slot):
    if slot == '09:00':
        return sorted((task for task in tasks if is_summary_candidate(task)), key=action_sort_key)[:5]
    # An unscheduled task does not become a daytime interruption merely because
    # it has a high business priority; a blocking item is the explicit exception.
    high_frequency = [task for task in tasks
                      if task['urgency'] != 'none' or task.get('isBlocking')]
    selected = [task for task in high_frequency if task['attentionLevel'] == 'critical']
    if slot in ('10:00', '18:00'):
        selected.extend(task for task in high_frequency
                        if task['attentionLevel'] != 'critical' and task['priority'] == 'high')
    return sorted(selected, key=action_sort_key)


def due_label(task):
    if task['deadline'] is None:
        return '未排期'
    return task['deadline'].isoformat(timespec='minutes')


def snoozed(task, now):
    value = task.get('snoozedUntil')
    if value in (None, '', 'none'):
        return False
    try:
        until = dt.datetime.fromisoformat(value)
    except (TypeError, ValueError):
        return False
    if until.tzinfo is None:
        return False
    return until > now


def render_summary(tasks, pending_total):
    lines = ['[团队任务晨间摘要]']
    for task in tasks:
        lines.append('[{id}] {title}｜负责人：{assignee}｜截止：{due}｜紧急度：{urgency}'.format(
            id=task['id'], title=task['title'], assignee=task.get('assignee') or '未分配',
            due=due_label(task), urgency=task['urgency']))
    lines.append('另有 {} 项待处理任务。'.format(pending_total - len(tasks)))
    return '\n'.join(lines)


def render_focus(tasks, slot):
    lines = ['[团队任务重点提醒 {}]'.format(slot)]
    for task in tasks:
        lines.append('[{id}] {title}｜负责人：{assignee}｜截止：{due}｜重要性：{priority}｜紧急度：{urgency}｜关注度：{attention}'.format(
            id=task['id'], title=task['title'], assignee=task.get('assignee') or '未分配',
            due=due_label(task), priority=task['priority'], urgency=task['urgency'],
            attention=task['attentionLevel']))
    return '\n'.join(lines)


def slot_key(now, slot):
    offset = now.strftime('%z')
    offset = offset[:3] + ':' + offset[3:] if offset else ''
    return '{}T{}{}'.format(now.date().isoformat(), slot, offset)


def load_holidays(path):
    if path is None:
        return set()
    values = json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
        raise ValueError('holiday file must be a JSON array of YYYY-MM-DD strings')
    return {dt.date.fromisoformat(value) for value in values}


def build_plan(doc, now, slot, holidays):
    if now.weekday() >= 5 or now.date() in holidays:
        return {'silent': True, 'reason': 'non_working_day', 'pendingTotal': 0, 'tasks': []}
    pending = [classified(task, now) for task in doc['tasks']
               if task.get('status') == 'pending' and not snoozed(task, now)]
    receipt_key = slot_key(now, slot)
    receipts = doc.get('_reminderReceipts', {})
    candidates = [task for task in selected_for_slot(pending, slot)
                  if receipt_key not in receipts.get(task['id'], []) and task.get('lastRemindedSlot') != receipt_key]
    if not candidates:
        return {'silent': True, 'reason': 'no_eligible_tasks', 'pendingTotal': len(pending), 'tasks': []}
    text = render_summary(candidates, len(pending)) if slot == '09:00' else render_focus(candidates, slot)
    return {'silent': False, 'reason': None, 'pendingTotal': len(pending), 'tasks': candidates, 'text': text,
            'receiptSlot': receipt_key}


def execute(data_dir, now, slot, holidays, reserve=False, delay_minutes=None):
    store = TaskStore(data_dir)
    doc = store.execute({'op': 'read'})['ledgers'][MAIN]
    plan = build_plan(doc, now, slot, holidays)
    delay = random.SystemRandom().randint(0, 15) if delay_minutes is None else delay_minutes
    result = {key: value for key, value in plan.items() if key != 'tasks'}
    result.update(slot=slot, scheduledFor=(now + dt.timedelta(minutes=delay)).isoformat(timespec='minutes'),
                  delayMinutes=delay, selected=[task['id'] for task in plan['tasks']], reserved=[])
    if reserve:
        for task in plan['tasks']:
            try:
                receipt = store.execute({'op': 'remind', 'id': task['id'], 'slot': plan['receiptSlot']})
            except StoreError as exc:
                if exc.code not in ('conflict', 'not_found'):
                    raise
                continue
            if not receipt.get('duplicate'):
                result['reserved'].append(task['id'])
        if not result['reserved']:
            result.update(silent=True, reason='already_reserved', text=None)
        elif len(result['reserved']) != len(plan['tasks']):
            sent = set(result['reserved'])
            kept = [task for task in plan['tasks'] if task['id'] in sent]
            result['selected'] = result['reserved']
            result['text'] = render_summary(kept, plan['pendingTotal']) if slot == '09:00' else render_focus(kept, slot)
    return result


def find_task(doc, task_id):
    for task in doc.get('tasks', []):
        if task.get('id') == task_id:
            return task
    return None


def render_task_reminder(task):
    latest_comment = task.get('comments', [])[-1].get('content') if task.get('comments') else '暂无'
    return ('[任务提醒]\n'
            '[{id}] {title}\n'
            '负责人：{assignee}\n'
            '截止：{due}\n'
            '重要性：{priority}\n'
            '紧急度：{urgency}\n'
            '关注度：{attention}\n'
            '最新进展：{comment}').format(
                id=task['id'], title=task['title'], assignee=task.get('assignee') or '未分配',
                due=due_label(task), priority=task['priority'], urgency=task['urgency'],
                attention=task['attentionLevel'], comment=latest_comment)


def resolve_task_reminder(data_dir, task_id, slot, now, reserve=False, delivery_reference=None):
    """Resolve one dynamic reminder from the current task snapshot.

    ``slot`` is an opaque, adapter-supplied idempotency key and must include a
    date and timezone.  It is deliberately not a scheduler expression.
    """
    if not isinstance(task_id, str) or not task_id:
        raise ValueError('task ID is required')
    if not isinstance(slot, str) or not slot.strip() or 'T' not in slot:
        raise ValueError('slot must include date and timezone')
    store = TaskStore(data_dir)
    doc = store.execute({'op': 'read'})['ledgers'][MAIN]
    task = find_task(doc, task_id)
    base = {'taskId': task_id, 'slot': slot, 'deliveryReference': delivery_reference}
    if task is None:
        return {**base, 'action': 'silent', 'reason': 'task_not_found'}
    if task.get('status') != 'pending':
        return {**base, 'action': 'silent', 'reason': 'inactive_task', 'status': task.get('status')}
    if snoozed(task, now):
        return {**base, 'action': 'silent', 'reason': 'snoozed', 'status': 'pending'}
    current = classified(task, now)
    if reserve:
        try:
            receipt = store.execute({'op': 'remind', 'id': task_id, 'slot': slot})
        except StoreError as exc:
            if exc.code in ('conflict', 'not_found'):
                return {**base, 'action': 'silent', 'reason': 'state_changed'}
            raise
        if receipt.get('duplicate'):
            return {**base, 'action': 'silent', 'reason': 'already_reserved'}
    return {**base, 'action': 'deliver', 'status': 'pending', 'text': render_task_reminder(current),
            'task': {key: current.get(key) for key in ('id', 'title', 'assignee', 'dueDate', 'dueTime',
                                                       'priority', 'urgency', 'attentionLevel')}}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', required=True, help='local team-tasks data directory')
    parser.add_argument('--slot', required=True, help='planned reminder time slot or specialized reminder key')
    parser.add_argument('--task-id', help='resolve one task-backed specialized reminder')
    parser.add_argument('--delivery-reference', help='opaque adapter delivery reference, echoed in output')
    parser.add_argument('--holiday-file', help='JSON array of local non-working dates')
    parser.add_argument('--now', help='ISO-8601 timestamp with UTC offset; for deterministic runs')
    parser.add_argument('--reserve', action='store_true', help='record task ID + date + slot through task_store before sending')
    parser.add_argument('--delay-minutes', type=int, choices=range(16), metavar='0..15',
                        help='override the 0–15 minute random delivery delay')
    args = parser.parse_args(argv)
    try:
        current = parse_now(args.now)
        if args.task_id:
            output = resolve_task_reminder(Path(args.data_dir), args.task_id, args.slot, current,
                                            reserve=args.reserve,
                                            delivery_reference=args.delivery_reference)
        else:
            if args.slot not in SLOTS:
                raise ValueError('--slot must be one of {} for team reminders'.format(', '.join(SLOTS)))
            if args.delivery_reference is not None:
                raise ValueError('--delivery-reference requires --task-id')
            output = execute(Path(args.data_dir), current, args.slot, load_holidays(args.holiday_file),
                             reserve=args.reserve, delay_minutes=args.delay_minutes)
    except (StoreError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({'ok': False, 'message': str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps({'ok': True, **output}, ensure_ascii=False, default=str))
    return 0


if __name__ == '__main__':
    sys.exit(main())
