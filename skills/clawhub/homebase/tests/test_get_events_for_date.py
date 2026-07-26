"""
test_get_events_for_date.py — the "what's on <day>" tool.

The agent needs a friendly-formatted list of events on any given date,
so "and tomorrow" / "what's on Friday" queries don't fall back to
`add_calendar_event` as a hallucinated workaround. This module covers
the date parsing, formatting, and empty-state paths.
"""
from __future__ import annotations

import sys
import types
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent.parent))

for _mod in (
    "google", "google.oauth2", "google.oauth2.credentials",
    "google.auth", "google.auth.transport", "google.auth.transport.requests",
    "googleapiclient", "googleapiclient.discovery",
):
    sys.modules.setdefault(_mod, types.ModuleType(_mod))

import tools  # noqa: E402


def _mocked_aggregator(events_by_date):
    """Return a MagicMock FamilyCalendarAggregator that answers get_events_by_date."""
    agg = MagicMock()
    agg.sync_with_google_calendar.return_value = None
    agg.get_events_by_date.side_effect = lambda d: events_by_date.get(d, [])
    return agg


class TestGetEventsForDate:
    def test_returns_formatted_events_for_requested_date(self):
        agg = _mocked_aggregator({
            "2026-07-06": [
                {"title": "Pay Woodbridge HOA Fees", "time": "All day"},
                {"title": "Amit Birthday Pizza Class", "time": "10:00"},
                {"title": "Ride class at Club Studio", "time": "18:30"},
            ]
        })
        with patch("features.calendar.calendar_aggregator.FamilyCalendarAggregator",
                   return_value=agg):
            out = tools.get_events_for_date("2026-07-06")

        assert "Monday, July 06" in out
        assert "Pay Woodbridge HOA Fees" in out
        assert "10:00 AM" in out
        assert "6:30 PM" in out
        assert "All day" in out
        # Ensure the aggregator was queried for the correct date
        agg.get_events_by_date.assert_called_once_with("2026-07-06")
        # Sync must run first — otherwise stale data
        agg.sync_with_google_calendar.assert_called_once()

    def test_empty_day_returns_friendly_message(self):
        agg = _mocked_aggregator({})
        with patch("features.calendar.calendar_aggregator.FamilyCalendarAggregator",
                   return_value=agg):
            out = tools.get_events_for_date("2026-07-06")
        assert "No events on Monday, July 06" in out

    def test_invalid_date_string_returns_error_without_syncing(self):
        agg = _mocked_aggregator({})
        with patch("features.calendar.calendar_aggregator.FamilyCalendarAggregator",
                   return_value=agg):
            out = tools.get_events_for_date("tomorrow")
        assert out.startswith("❌")
        assert "YYYY-MM-DD" in out
        # Must NOT sync on a validation failure — cheap fast-fail
        agg.sync_with_google_calendar.assert_not_called()

    def test_dispatch_wires_the_tool(self):
        """The tool must be reachable via execute_tool, or the agent can't call it."""
        agg = _mocked_aggregator({"2026-07-06": []})
        with patch("features.calendar.calendar_aggregator.FamilyCalendarAggregator",
                   return_value=agg):
            out = tools.execute_tool("get_events_for_date", {"date": "2026-07-06"})
        assert "No events on Monday, July 06" in out
