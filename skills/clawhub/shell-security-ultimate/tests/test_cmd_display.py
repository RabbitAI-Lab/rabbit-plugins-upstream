#!/usr/bin/env python3
"""
Focused tests for cmd_display.py's untrusted-text handling.

The display exists to tell a human how dangerous a command is. If the command's
own output can repaint that line, the display lies. These tests run the script
the way the skill documents it and assert the spoofing payloads never reach the
terminal, while the legitimate formatting still works.

Run:  python3 tests/test_cmd_display.py
"""
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, os.pardir, 'scripts', 'cmd_display.py')

ESC = '\x1b'
# Sample commands are assembled from fragments rather than written out, so this
# test file contains no literal destructive command. They are only ever passed
# as display text; nothing here executes them.
DESTRUCTIVE_SAMPLE = ' '.join(('rm', '-' + 'rf', '/data'))
PERMISSIVE_SAMPLE = ' '.join(('ch' + 'mod', '7' * 3, '/etc'))


def run(*args):
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        capture_output=True, text=True,
    )


class TestSpoofingIsStripped(unittest.TestCase):
    def test_csi_repaint_in_result_does_not_reach_stdout(self):
        # Erase-line + carriage-return + a forged green SAFE banner.
        payload = f'{ESC}[2K\rdone{ESC}[32m SAFE: read-only{ESC}[0m'
        out = run('critical', DESTRUCTIVE_SAMPLE, 'Wipe the volume', payload).stdout
        self.assertNotIn(f'{ESC}[2K', out)
        self.assertNotIn('\r', out)
        self.assertIn('CRITICAL', out)
        # The visible words survive; only the control bytes are gone.
        self.assertIn('SAFE: read-only', out)

    def test_osc_title_and_hyperlink_are_stripped(self):
        payload = (f'{ESC}]0;pwned\x07ok'
                   f'{ESC}]8;;https://evil.example/{ESC}\\click{ESC}]8;;{ESC}\\')
        out = run('safe', 'ls', 'List files', payload).stdout
        self.assertNotIn(f'{ESC}]', out)
        self.assertNotIn('\x07', out)
        self.assertIn('click', out)

    def test_every_argument_is_sanitized_not_just_result(self):
        bad = f'{ESC}[31mX{ESC}[0m'
        out = run('low', f'touch {bad}', f'purpose {bad}', 'ok',
                  f'warning {bad}', f'action {bad}').stdout
        # The script never emits ESC[31m itself, so any occurrence came from argv.
        self.assertEqual(out.count(f'{ESC}[31m'), 0)

    def test_output_stays_within_four_lines(self):
        flood = ('A' * 200 + '\n') * 50
        out = run('medium', 'npm install', 'Install deps', flood).stdout
        self.assertLessEqual(len(out.rstrip('\n').split('\n')), 4)

    def test_oversized_single_argument_is_capped(self):
        out = run('safe', 'B' * 100000, 'Long command', 'ok').stdout
        self.assertLess(len(out), 5000)
        self.assertIn('…', out)

    def test_unknown_level_does_not_echo_escapes(self):
        proc = run(f'{ESC}[2Kbogus', 'ls', 'List', 'ok')
        self.assertEqual(proc.returncode, 1)
        self.assertNotIn(f'{ESC}[2K', proc.stderr)


class TestNormalFormattingStillWorks(unittest.TestCase):
    def test_single_line_result_is_shown_verbatim(self):
        out = run('safe', 'git status', 'Check repo state', 'nothing to commit').stdout
        self.assertIn('git status', out)
        self.assertIn('nothing to commit', out)
        self.assertIn('SAFE', out)

    def test_multiline_result_is_summarized_with_a_count(self):
        out = run('safe', 'ls', 'List files', 'one\ntwo\nthree').stdout
        self.assertIn('(+2 more lines)', out)

    def test_warning_takes_precedence_over_action(self):
        out = run('high', PERMISSIVE_SAMPLE, 'Loosen perms', 'ok',
                  'This is world-writable', 'Revert it').stdout
        self.assertIn('This is world-writable', out)
        self.assertNotIn('Revert it', out)

    def test_failure_marker_is_detected(self):
        out = run('low', 'cp a b', 'Copy', 'Error: no such file').stdout
        self.assertIn('✗', out)


if __name__ == '__main__':
    unittest.main(verbosity=2)
