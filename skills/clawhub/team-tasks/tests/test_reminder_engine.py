import datetime as dt
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import reminder_engine as engine
import task_store


NOW = dt.datetime.fromisoformat('2026-09-18T09:00:00+08:00')  # Friday


def task(identifier, **changes):
    value = {
        'id': identifier, 'title': identifier, 'priority': 'medium', 'isBlocking': False,
        'status': 'pending', 'assignee': 'Ada', 'dueDate': None, 'dueTime': None,
        'lastRemindedSlot': None,
    }
    value.update(changes)
    return value


class ReminderEngineTests(unittest.TestCase):
    def document(self, tasks, receipts=None):
        return {'version': '1.0', 'updatedAt': NOW.isoformat(), 'tasks': tasks,
                '_reminderReceipts': receipts or {}}

    def test_classification_and_attention_rules(self):
        overdue = engine.classified(task('overdue', dueDate='2026-09-17', dueTime='18:00'), NOW)
        today_high = engine.classified(task('today-high', priority='high', dueDate='2026-09-18', dueTime='18:00'), NOW)
        soon = engine.classified(task('soon', dueDate='2026-09-20', dueTime='08:00'), NOW)
        normal = engine.classified(task('normal', dueDate='2026-10-01'), NOW)
        unscheduled = engine.classified(task('none'), NOW)
        blocking = engine.classified(task('blocking', priority='high', isBlocking=True), NOW)
        self.assertEqual((overdue['urgency'], overdue['attentionLevel']), ('overdue', 'high'))
        self.assertEqual((today_high['urgency'], today_high['attentionLevel']), ('today', 'critical'))
        self.assertEqual(soon['urgency'], 'soon')
        self.assertEqual(normal['urgency'], 'normal')
        self.assertEqual(unscheduled['urgency'], 'none')
        self.assertEqual(blocking['attentionLevel'], 'critical')

    def test_summary_is_limited_and_includes_pending_total(self):
        tasks = [task('T-{:03}'.format(index), dueDate='2026-09-18', dueTime='18:00') for index in range(6)]
        plan = engine.build_plan(self.document(tasks), NOW, '09:00', set())
        self.assertFalse(plan['silent'])
        self.assertEqual(len(plan['tasks']), 5)
        self.assertIn('另有 1 项待处理任务。', plan['text'])
        self.assertIn('负责人：Ada', plan['text'])
        self.assertIn('紧急度：today', plan['text'])

    def test_focus_slots_only_include_critical_or_permitted_high_priority(self):
        tasks = [
            task('critical', priority='critical', dueDate='2026-09-18', dueTime='18:00'),
            task('high', priority='high', dueDate='2026-09-20', dueTime='08:00'),
            task('medium', priority='medium', dueDate='2026-09-18', dueTime='18:00'),
            task('unscheduled', priority='critical'),
        ]
        afternoon = engine.build_plan(self.document(tasks), NOW, '14:00', set())
        morning = engine.build_plan(self.document(tasks), NOW, '10:00', set())
        self.assertEqual([value['id'] for value in afternoon['tasks']], ['critical'])
        self.assertEqual({value['id'] for value in morning['tasks']}, {'critical', 'high'})
        self.assertIn('重要性：critical', afternoon['text'])
        self.assertIn('关注度：critical', afternoon['text'])

    def test_existing_slot_receipt_is_excluded(self):
        values = [task('once', priority='critical')]
        key = engine.slot_key(NOW, '10:00')
        plan = engine.build_plan(self.document(values, {'once': [key]}), NOW, '10:00', set())
        self.assertTrue(plan['silent'])
        self.assertEqual(plan['reason'], 'no_eligible_tasks')

    def test_weekend_and_holiday_are_silent(self):
        values = self.document([task('critical', priority='critical')])
        weekend = NOW + dt.timedelta(days=1)
        self.assertEqual(engine.build_plan(values, weekend, '09:00', set())['reason'], 'non_working_day')
        self.assertEqual(engine.build_plan(values, NOW, '09:00', {NOW.date()})['reason'], 'non_working_day')

    def test_reservation_uses_safe_store_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            store = task_store.TaskStore(directory)
            store.execute({'op': 'init'})
            identifier = store.execute({'op': 'create', 'actor': 'test', 'fields': {
                'title': 'critical', 'priority': 'critical', 'dueDate': '2026-09-18', 'dueTime': '18:00'}})['id']
            first = engine.execute(Path(directory), NOW, '10:00', set(), reserve=True, delay_minutes=0)
            second = engine.execute(Path(directory), NOW, '10:00', set(), reserve=True, delay_minutes=0)
            saved = store.execute({'op': 'read'})['ledgers'][task_store.MAIN]
            saved_task = saved['tasks'][0]
            self.assertEqual(first['reserved'], [identifier])
            self.assertFalse(first['silent'])
            self.assertEqual(second['reserved'], [])
            self.assertTrue(second['silent'])
            self.assertEqual(saved_task['reminderCount'], 1)
            self.assertEqual(saved_task['lastRemindedSlot'], engine.slot_key(NOW, '10:00'))

    def test_cli_emits_a_message_and_random_delay_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            store = task_store.TaskStore(directory)
            store.execute({'op': 'init'})
            store.execute({'op': 'create', 'actor': 'test', 'fields': {
                'title': 'critical', 'priority': 'critical', 'dueDate': '2026-09-18', 'dueTime': '18:00'}})
            command = [sys.executable, str(SCRIPTS / 'reminder_engine.py'), '--data-dir', directory,
                       '--slot', '10:00', '--now', NOW.isoformat(), '--delay-minutes', '7']
            completed = subprocess.run(command, check=True, capture_output=True, text=True)
            result = json.loads(completed.stdout)
            self.assertTrue(result['ok'])
            self.assertFalse(result['silent'])
            self.assertEqual(result['delayMinutes'], 7)
            self.assertEqual(result['scheduledFor'], '2026-09-18T09:07+08:00')
            self.assertIn('重点提醒 10:00', result['text'])

    def test_specialized_reminder_uses_live_task_state_and_reserves(self):
        with tempfile.TemporaryDirectory() as directory:
            store = task_store.TaskStore(directory)
            store.execute({'op': 'init'})
            identifier = store.execute({'op': 'create', 'actor': 'test', 'fields': {
                'title': 'old title', 'assignee': 'Ada', 'dueDate': '2026-09-18'}})['id']
            store.execute({'op': 'update', 'actor': 'test', 'id': identifier,
                           'changes': {'title': 'latest title', 'assignee': 'Lin'},
                           'expected': {'title': 'old title', 'assignee': 'Ada'}})
            result = engine.resolve_task_reminder(directory, identifier, '2026-09-18T14:00+08:00', NOW,
                                                   reserve=True, delivery_reference='job-1')
            self.assertEqual(result['action'], 'deliver')
            self.assertEqual(result['deliveryReference'], 'job-1')
            self.assertIn('latest title', result['text'])
            self.assertIn('负责人：Lin', result['text'])
            duplicate = engine.resolve_task_reminder(directory, identifier, '2026-09-18T14:00+08:00', NOW,
                                                      reserve=True)
            self.assertEqual(duplicate['reason'], 'already_reserved')

    def test_specialized_reminder_silences_inactive_and_snoozed_tasks(self):
        with tempfile.TemporaryDirectory() as directory:
            store = task_store.TaskStore(directory)
            store.execute({'op': 'init'})
            identifier = store.execute({'op': 'create', 'actor': 'test', 'fields': {'title': 'task'}})['id']
            store.execute({'op': 'status', 'actor': 'test', 'id': identifier, 'status': 'done',
                           'expected': {'status': 'pending'}})
            inactive = engine.resolve_task_reminder(directory, identifier, '2026-09-18T14:00+08:00', NOW)
            self.assertEqual((inactive['action'], inactive['reason']), ('silent', 'inactive_task'))
            reopened = store.execute({'op': 'reopen', 'actor': 'test', 'id': identifier,
                                      'expected': {'status': 'done'}})
            self.assertTrue(reopened['ok'])
            store.execute({'op': 'update', 'actor': 'test', 'id': identifier,
                           'changes': {'snoozedUntil': '2026-09-18T10:00:00+08:00'},
                           'expected': {'snoozedUntil': None}})
            paused = engine.resolve_task_reminder(directory, identifier, '2026-09-18T14:00+08:00', NOW)
            self.assertEqual((paused['action'], paused['reason']), ('silent', 'snoozed'))


if __name__ == '__main__':
    unittest.main()
