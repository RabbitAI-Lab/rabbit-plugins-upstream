import sys
import io
import json
import os
from contextlib import redirect_stderr
from pathlib import Path
from types import SimpleNamespace
import unittest
import tempfile
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).parents[1] / 'scripts'))
import analyze_video as video


class AgenticTests(unittest.TestCase):
    def client(self):
        client = Mock()
        client.interactions.create.return_value = SimpleNamespace(
            status='completed', output_text='{"answer":"red"}', usage=None)
        return client

    def test_youtube_uses_agentic_and_no_retention(self):
        client = self.client()
        result = video.analyze_youtube(client, 'https://youtu.be/example', 'question', video.AGENTIC_MODELS[0], None)
        request = client.interactions.create.call_args.kwargs
        self.assertEqual(request['input'][0]['processing'], 'agentic')
        self.assertEqual(request['input'][0]['uri'], 'https://youtu.be/example')
        self.assertFalse(request['store'])
        self.assertIn('answer', result)
        client.models.generate_content.assert_not_called()

    def test_uploaded_file_uses_agentic(self):
        client = self.client()
        source = SimpleNamespace(uri='https://generativelanguage.googleapis.com/v1beta/files/test', mime_type='video/mp4')
        video.analyze_with_file(client, source, 'question', video.AGENTIC_MODELS[0], None)
        request = client.interactions.create.call_args.kwargs
        self.assertEqual(request['input'][0]['uri'], source.uri)
        self.assertEqual(request['input'][0]['processing'], 'agentic')

    def test_unsupported_model_fails_before_request(self):
        client = self.client()
        with self.assertRaises(ValueError):
            video.analyze_youtube(client, 'https://youtu.be/example', 'q', 'gemini-2.5-flash', None)
        client.interactions.create.assert_not_called()

    def test_nontransient_failure_does_not_fallback(self):
        client = self.client()
        client.interactions.create.side_effect = ValueError('invalid request')
        with self.assertRaises(ValueError):
            video.analyze_youtube(client, 'https://youtu.be/example', 'q', *video.AGENTIC_MODELS[:2])
        self.assertEqual(client.interactions.create.call_count, 1)

    @patch.object(video.time, 'sleep')
    def test_transient_fallback_stays_agentic(self, sleep):
        client = self.client()
        success = client.interactions.create.return_value
        client.interactions.create.side_effect = [RuntimeError('503')] * 3 + [success]
        video.analyze_youtube(client, 'https://youtu.be/example', 'q', *video.AGENTIC_MODELS[:2])
        self.assertEqual(client.interactions.create.call_count, 4)
        for call in client.interactions.create.call_args_list:
            self.assertEqual(call.kwargs['input'][0]['processing'], 'agentic')

    def test_incomplete_output_is_not_success(self):
        client = self.client()
        client.interactions.create.return_value.status = 'incomplete'
        with self.assertRaises(RuntimeError):
            video.analyze_youtube(client, 'https://youtu.be/example', 'q', video.AGENTIC_MODELS[0], None)

    def test_question_does_not_request_verbatim_transcript(self):
        self.assertNotIn('Full verbatim transcript', video.build_prompt('What color?'))
        self.assertIn('Full verbatim transcript', video.build_prompt(mode='full'))
        self.assertIn('start_seconds', video.build_prompt('What color?'))

    def test_expired_upload_is_not_reused(self):
        client = self.client()
        self.assertIsNone(video.validate_cached_file(client, {'gemini_file': {
            'name': 'files/test', 'expiration_time': '2020-01-01T00:00:00Z'}}))
        client.files.get.assert_not_called()

    def test_cached_content_rejected(self):
        with self.assertRaises(ValueError):
            video.generate_content_with_retry(self.client(), [], video.AGENTIC_MODELS[0], cached_content='cache/test')

    def test_failed_purge_retains_record(self):
        client = self.client()
        client.files.delete.side_effect = RuntimeError('503')
        with self.assertRaises(RuntimeError):
            video.delete_remote_handles(client, {'gemini_file': {'name': 'files/test'}})

    def test_local_default_and_cleanup(self):
        client = self.client()
        source = SimpleNamespace(name='files/test', uri='https://example.org/test', mime_type='video/mp4')
        with tempfile.TemporaryDirectory() as folder:
            asset = Path(folder) / 'test.mp4'
            asset.write_bytes(b'test fixture')
            with patch.object(video.sys, 'argv', ['analyze_video.py', str(asset), '--allow-cloud', '--cache-dir', folder]), \
                 patch.object(video, 'load_gemini_api_key', return_value='unit-test-only'), \
                 patch.object(video.genai, 'Client', return_value=client), \
                 patch.object(video, 'upload_to_gemini', return_value=source):
                video.main()
            client.files.delete.assert_called_once_with(name='files/test')
            request = client.interactions.create.call_args.kwargs
            self.assertEqual(request['model'], 'gemini-3.7-flash')
            self.assertEqual(request['input'][0]['processing'], 'agentic')
            self.assertTrue(asset.exists())

    def test_cli_rejects_context_cache_before_auth(self):
        with patch.object(video.sys, 'argv', ['analyze_video.py', 'test.mp4', '--use-context-cache']), \
             patch.object(video, 'load_gemini_api_key') as auth:
            with self.assertRaises(SystemExit) as result:
                video.main()
            self.assertEqual(result.exception.code, 2)
            auth.assert_not_called()

    def test_cloud_requires_authorization_before_auth(self):
        with patch.object(video.sys, 'argv', ['video', 'https://youtu.be/example']), \
             patch.object(video, 'load_gemini_api_key') as auth, redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                video.main()
            auth.assert_not_called()

    def test_source_rejects_credentials_queries_and_spoofed_youtube(self):
        for source in ('https://example.org/v?token=test-canary', 'https://user:pass@example.org/v'):
            with self.assertRaises(ValueError):
                video.validate_source(source)
        self.assertFalse(video.is_youtube_url('https://evil.example/youtube.com/watch?v=x'))
        video.validate_source('https://www.youtube.com/watch?v=example')
        video.validate_source('https://vimeo.com/12345?quality=hd')
        video.validate_source('https://www.loom.com/share/example')
        video.validate_source('http://example.org/video.mp4?format=mp4')

    def test_cache_has_private_permissions_and_no_source_identity(self):
        with tempfile.TemporaryDirectory() as folder:
            path = str(Path(folder) / 'record.json')
            video.save_cache_record(path, {'source': 'private-canary', 'asset_id': 'private-canary', 'session_key': 'private-canary'})
            self.assertNotIn('private-canary', Path(path).read_text())
            self.assertEqual(os.stat(path).st_mode & 0o777, 0o600)

    def test_history_requires_explicit_save(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(video, 'write_output'):
            path = str(Path(folder) / 'record.json')
            video.handle_result('private-canary', 'private-canary', None, {}, path, 'private-question')
            self.assertNotIn('private-canary', Path(path).read_text())
            video.handle_result('answer', 'answer', None, {'save_history': True}, path, 'question')
            self.assertEqual(json.loads(Path(path).read_text())['turns'][0]['output'], 'answer')

    def test_downloader_error_does_not_log_source_or_body(self):
        err = io.StringIO()
        with patch.object(video.subprocess, 'run', return_value=SimpleNamespace(returncode=1, stderr='private-canary')), redirect_stderr(err):
            with self.assertRaises(RuntimeError) as result:
                video.download_video('https://example.org/private-canary', '/tmp/video-test.mp4')
            self.assertNotIn('private-canary', str(result.exception) + err.getvalue())

    def test_cli_suppresses_raw_exception(self):
        err = io.StringIO()
        with patch.object(video, 'main', side_effect=RuntimeError('private-canary')), redirect_stderr(err):
            self.assertEqual(video.cli(), 1)
        self.assertNotIn('private-canary', err.getvalue())

    def test_output_is_private(self):
        with tempfile.TemporaryDirectory() as folder:
            path = str(Path(folder) / 'answer.json')
            video.write_output('answer', path)
            self.assertEqual(os.stat(path).st_mode & 0o777, 0o600)

    def test_failed_cleanup_persists_minimal_handle_and_fails(self):
        client = self.client()
        client.files.delete.side_effect = RuntimeError('private-canary')
        source = SimpleNamespace(name='files/test', uri='https://example.org/test', mime_type='video/mp4')
        with tempfile.TemporaryDirectory() as folder, redirect_stderr(io.StringIO()) as err:
            asset = Path(folder) / 'test.mp4'
            asset.write_bytes(b'test fixture')
            with patch.object(video.sys, 'argv', ['video', str(asset), '--allow-cloud', '--cache-dir', folder]), \
                 patch.object(video, 'load_gemini_api_key', return_value='unit-test-only'), \
                 patch.object(video.genai, 'Client', return_value=client), \
                 patch.object(video, 'upload_to_gemini', return_value=source):
                self.assertEqual(video.cli(), 1)
            record = json.loads(next(Path(folder).glob('*.json')).read_text())
            self.assertEqual(record['gemini_file']['name'], 'files/test')
            self.assertNotIn('source', record)
            self.assertNotIn('turns', record)
            self.assertNotIn('private-canary', err.getvalue())


if __name__ == '__main__':
    unittest.main()
