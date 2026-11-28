import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]

def load(relative, name):
    p = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, p)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

aw_status = load('scripts/status.py', 'aw_status')
asset = load('scripts/verify_asset.py', 'aw_asset')

GOOD = {
    'status': 'read_only',
    'real_original_market_data': True,
    'public_agent_registration_open': False,
    'public_agent_write_API_online': True,
    'one_original_ledger': True,
}

class FakeResponse:
    status = 200
    def __init__(self, value=GOOD, url=aw_status.URL, media_type="application/json; charset=utf-8", http_status=200):
        self.value = json.dumps(value).encode()
        self.url = url
        self.headers = {"Content-Type": media_type}
        self.status = http_status
    def geturl(self): return self.url
    def read(self, n): return self.value[:n]
    def __enter__(self): return self
    def __exit__(self, *args): pass

class FakeOpener:
    def __init__(self, response): self.response=response
    def open(self, request, timeout):
        assert request.full_url == aw_status.URL
        assert request.get_method() == 'GET'
        assert timeout == 8
        assert 'Authorization' not in request.headers
        return self.response

class AgentWorldDiscoveryTests(unittest.TestCase):
    def test_preview_is_not_open_to_public(self):
        r = aw_status.validate_status(json.dumps(GOOD).encode())
        self.assertFalse(r['registration_advertised_open'])
        self.assertFalse(r['public_trading_authorized_by_this_check'])
        self.assertIn('closed',r['next_step'])

    def test_even_open_registration_is_not_unconditional_go(self):
        copy = dict(GOOD, public_agent_registration_open=True, status='active')
        r = aw_status.validate_status(json.dumps(copy).encode())
        self.assertTrue(r['registration_advertised_open'])
        self.assertFalse(r['public_trading_authorized_by_this_check'])
        self.assertIn('advertised open',r['next_step'])
        self.assertIn('signed onboarding',r['next_step'])

    def test_read_only_health_can_truthfully_advertise_open_registration(self):
        live_shape = dict(GOOD, status='read_only', public_agent_registration_open=True)
        report = aw_status.validate_status(json.dumps(live_shape).encode())
        self.assertEqual(report['health_status'], 'read_only')
        self.assertTrue(report['registration_advertised_open'])
        self.assertTrue(report['write_api_online'])
        self.assertIn('advertised open', report['next_step'])
        self.assertFalse(report['public_trading_authorized_by_this_check'])

    def test_active_health_does_not_override_explicitly_closed_enrollment(self):
        shape = dict(GOOD, status='active', public_agent_registration_open=False)
        report = aw_status.validate_status(json.dumps(shape).encode())
        self.assertFalse(report['registration_advertised_open'])
        self.assertIn('closed', report['next_step'])
        self.assertFalse(report['public_trading_authorized_by_this_check'])

    def test_advertised_open_not_proof_of_completed_agent_registration(self):
        shape=dict(GOOD,public_agent_registration_open=True,
                   public_agent_write_API_online=False)
        report=aw_status.validate_status(json.dumps(shape).encode())
        self.assertTrue(report['registration_advertised_open'])
        self.assertFalse(report['write_api_online'])
        self.assertFalse(report['public_trading_authorized_by_this_check'])
        self.assertNotIn('completed', report['next_step'])

    def test_only_fixed_origin_and_no_token(self):
        self.assertEqual(aw_status.get_public_status(FakeOpener(FakeResponse()))['health_status'], 'read_only')
        with self.assertRaises(aw_status.InvalidPublicStatus):
            aw_status.get_public_status(FakeOpener(FakeResponse(url='https://other.invalid/api/v1/health')))

    def test_bad_types_and_duplicate_members_rejected(self):
        bads = [b'', b'[]', b'{}', b'{' + b'x'*17000 + b'}',
                json.dumps(dict(GOOD,one_original_ledger=False)).encode(),
                json.dumps(dict(GOOD,public_agent_registration_open=0)).encode(),
                json.dumps(GOOD)[:-1].encode()+b',"status":"active"}',
                b'not-json']
        for blob in bads:
            with self.subTest(blob=blob[:40]):
                with self.assertRaises(aw_status.InvalidPublicStatus):
                    aw_status.validate_status(blob)

    def test_file_hash_never_executes(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'fixture.pyz'
            p.write_bytes(b'fake fixture, no executable code')
            expected=hashlib.sha256(p.read_bytes()).hexdigest()
            self.assertTrue(asset.verify(p,expected)['matches_supplied_sha256'])
            self.assertFalse(asset.verify(p,'f'*64)['matches_supplied_sha256'])
            self.assertFalse(asset.verify(p,expected)['official_expected_digest_provenance_verified'])
            self.assertEqual(asset.verify(p,expected)['network_requests'],0)
            self.assertFalse(asset.verify(p,expected)['executed'])
            with self.assertRaises(ValueError):
                asset.verify(p,'not-hash')
            (Path(t)/'link.pyz').symlink_to(p)
            with self.assertRaises(ValueError):
                asset.verify(Path(t)/'link.pyz',expected)

    def test_wrong_content_type_and_http_status_refused(self):
        for response in (
            FakeResponse(media_type="text/html"),
            FakeResponse(http_status=503),
            FakeResponse(url="https://agentworldhub.com/elsewhere"),
        ):
            with self.subTest(response=response.status):
                with self.assertRaises(aw_status.InvalidPublicStatus):
                    aw_status.get_public_status(FakeOpener(response))

    def test_health_overflow_number_and_nonfinite_data_refused(self):
        for trailing in (',"unused":NaN', ',"unused":Infinity', ',"unused":-Infinity',
                         ',"unused":1e309', ',"unused":-1e309'):
            raw=json.dumps(GOOD)[:-1].encode()+trailing.encode()+b'}'
            with self.subTest(extra=trailing):
                with self.assertRaises(aw_status.InvalidPublicStatus):
                    aw_status.validate_status(raw)

    def test_local_client_only_and_bounded_size(self):
        with tempfile.TemporaryDirectory() as t:
            temp=Path(t)
            small=temp/'client.pyz'
            small.write_bytes(b'local legitimate file example')
            digest=hashlib.sha256(small.read_bytes()).hexdigest()
            self.assertTrue(asset.verify(small,digest)['matches_supplied_sha256'])
            with self.assertRaises(ValueError):
                asset.verify(temp/'client.zip',digest)
            with self.assertRaises(ValueError):
                asset.verify(Path('client.pyz'),digest)
            too_large=temp/'too-large.pyz'
            with too_large.open('wb') as f:
                f.truncate(asset.MAX_BYTES+1)
            with self.assertRaises(ValueError):
                asset.verify(too_large,digest)
            link=temp/'hardlink.pyz'
            link.hardlink_to(small)
            with self.assertRaises(ValueError):
                asset.verify(small,digest)
            link.unlink()

    def test_bogus_open_label_remains_unapproved(self):
        expected=dict(GOOD,status='active',public_agent_registration_open=True)
        report=aw_status.validate_status(json.dumps(expected).encode())
        self.assertTrue(report['registration_advertised_open'])
        self.assertFalse(report['public_trading_authorized_by_this_check'])

    def test_public_skill_is_discovery_only_without_publisher_workflow(self):
        expected = {
            'SKILL.md', 'agents/openai.yaml', 'references/connection.md',
            'scripts/status.py', 'scripts/verify_asset.py', 'tests/test_skill.py',
        }
        observed = {
            str(p.relative_to(ROOT)) for p in ROOT.rglob('*')
            if p.is_file() and '__pycache__' not in p.parts
            and p.suffix != '.pyc'
        }
        self.assertEqual(observed, expected)
        contents = [
            (ROOT / p).read_text()
            for p in ('SKILL.md', 'references/connection.md')
        ]
        self.assertFalse((ROOT / 'README_RELEASE.md').exists())
        for content in contents:
            self.assertNotIn(' '.join(('clawhub', 'login')), content)
            self.assertNotIn(' '.join(('clawhub', 'skill', 'publish')), content)
        skill = contents[0]
        self.assertIn('Strict tool boundaries', skill)
        self.assertIn('fixed Agent World health endpoint', skill)
        self.assertIn('not marketplace operations or package publication', skill)
        self.assertIn('`status=read_only`', skill)
        self.assertIn('`public_agent_registration_open`', skill)
        self.assertNotIn('`status=read_only` or `public_agent_registration_open=false`', skill)
        self.assertNotIn('has reported `read_only` and `public_agent_registration_open: false` on',contents[1])

    def test_no_external_urls_or_token_parameters(self):
        self.assertTrue(aw_status.URL.startswith('https://agentworldhub.com/'))
        self.assertNotIn('secret', aw_status.URL)

if __name__ == '__main__': unittest.main()
