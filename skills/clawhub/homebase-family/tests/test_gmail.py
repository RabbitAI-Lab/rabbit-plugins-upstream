"""
Tests for core/gmail.py search — the command line it builds.

`--all` is asserted deliberately: both mail fetchers filter search results
against a processed ledger, and a fixed first page of newest ids fills up with
mail already handled. Anything older than that page was never returned, and
aged out of the lookback unseen.
"""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent.parent))

from core import gmail


def _run(payload):
    result = MagicMock(stdout=json.dumps(payload), stderr="", returncode=0)
    return patch("subprocess.run", return_value=result)


def _argv(mock):
    return mock.call_args.args[0]


class TestSearch:
    def test_all_pages_passes_all_flag(self):
        with _run({"messages": [{"id": "a"}, {"id": "b"}]}) as run:
            ids = gmail.search("from:x newer_than:4d", all_pages=True)
        assert "--all" in _argv(run)
        assert ids == ["a", "b"]

    def test_first_page_only_by_default(self):
        with _run({"messages": []}) as run:
            gmail.search("from:x", max_results=5)
        argv = _argv(run)
        assert "--all" not in argv
        assert argv[argv.index("--max") + 1] == "5"


# The shape of the 2026-10-28 08:07 failure: Go's url.Error quotes the whole
# search URL before the reason. The domains are placeholders; the length is
# what matters, and it is asserted so the fixture cannot quietly stop
# reproducing the cut.
SEARCH_URL = ('https://gmail.googleapis.com/gmail/v1/users/me/messages?alt=json'
              '&fields=messages%28id%2CthreadId%29%2CnextPageToken&maxResults=20'
              '&prettyPrint=false&q=%28from%3Aschool-one.example.com+OR+from%3A'
              'school-messaging.example.com+OR+from%3Aschool-software.example'
              '.com%29+newer_than%3A4d')
REFRESH_DIAL_FAILURE = (
    f'Get "{SEARCH_URL}": round trip: base token source: oauth2: cannot fetch '
    'token: Post "https://oauth2.googleapis.com/token": dial tcp: lookup '
    'oauth2.googleapis.com: no such host'
)


class TestFailureReason:
    def test_the_reason_survives_a_long_request_url(self):
        """Regression: the cap kept the URL and cut the reason, so the 08:07
        log ended at `base token ` and the school monitor's network check
        never saw the text it keys on."""
        assert len(SEARCH_URL) > 250
        failed = MagicMock(stdout="", stderr=REFRESH_DIAL_FAILURE, returncode=1)
        with patch("subprocess.run", return_value=failed):
            try:
                gmail.search("q")
            except gmail.GogError as e:
                reason = str(e)
            else:
                raise AssertionError("a failed search must raise")
        assert "no such host" in reason
        assert SEARCH_URL not in reason
