import secrets
import stat
import unittest
from pathlib import Path

from fetch_health_data import (
    DROP_VALUE,
    MAX_HEART_RATE_SAMPLES_PER_WORKOUT,
    merge_scope_payloads,
    sanitize_decrypted_payload,
    sanitize_workout_heart_rate_samples,
    write_ndjson,
    write_sqlite,
)


class FetchHealthDataTests(unittest.TestCase):
    def setUp(self) -> None:
        self.runtime_dir = Path("/tmp") / f"ahs-fetch-test-{secrets.token_hex(8)}"
        self.runtime_dir.mkdir(mode=0o700)

    def tearDown(self) -> None:
        for path in self.runtime_dir.iterdir():
            path.unlink(missing_ok=True)
        self.runtime_dir.rmdir()

    def test_sanitizer_keeps_more_than_512_workout_heart_rate_samples(self) -> None:
        samples = [
            {
                "start_offset_ms": index * 5_000,
                "end_offset_ms": (index + 1) * 5_000,
                "bpm": 120.5,
            }
            for index in range(600)
        ]
        payload = {
            "2026-07-20": {
                "workouts": [
                    {
                        "heart_rate": {"avg_bpm": 120.5, "samples": len(samples)},
                        "heart_rate_samples": samples,
                    }
                ]
            }
        }

        sanitized, metrics = sanitize_decrypted_payload(payload)

        stored_samples = sanitized["2026-07-20"]["workouts"][0]["heart_rate_samples"]
        self.assertEqual(len(stored_samples), 600)
        self.assertEqual(metrics["stored_days"], 1)
        self.assertEqual(metrics["dropped_days"], 0)

    def test_sanitizer_rejects_entire_malformed_heart_rate_series(self) -> None:
        payload = {
            "2026-07-20": {
                "workouts": [
                    {
                        "duration_seconds": 60,
                        "heart_rate_samples": [
                            {"start_offset_ms": 0, "end_offset_ms": 5_000, "bpm": 110},
                            {"start_offset_ms": 5_000, "end_offset_ms": 4_000, "bpm": 115},
                        ],
                    }
                ]
            }
        }

        sanitized, _ = sanitize_decrypted_payload(payload)

        workout = sanitized["2026-07-20"]["workouts"][0]
        self.assertNotIn("heart_rate_samples", workout)
        self.assertEqual(workout["duration_seconds"], 60)

    def test_sanitizer_rejects_entire_oversized_heart_rate_series(self) -> None:
        valid_sample = {"start_offset_ms": 0, "end_offset_ms": 5_000, "bpm": 110}
        samples = [valid_sample] * (MAX_HEART_RATE_SAMPLES_PER_WORKOUT + 1)

        sanitized = sanitize_workout_heart_rate_samples(samples)

        self.assertIs(sanitized, DROP_VALUE)

    def test_recent_scope_overlays_history_per_day_category(self) -> None:
        history = {
            "2026-07-20": {
                "sleep": {"total_hours": 8},
                "workouts": [{"heart_rate": {"avg_bpm": 100}}],
            }
        }
        recent_workouts = [
            {
                "heart_rate": {"avg_bpm": 120},
                "heart_rate_samples": [
                    {"start_offset_ms": 0, "end_offset_ms": 5_000, "bpm": 120}
                ],
            }
        ]
        recent = {
            "2026-07-20": {
                "activity": {"steps": 1000},
                "workouts": recent_workouts,
            }
        }

        merged = merge_scope_payloads({}, history, recent)

        self.assertEqual(merged["2026-07-20"]["sleep"], {"total_hours": 8})
        self.assertEqual(merged["2026-07-20"]["activity"], {"steps": 1000})
        self.assertEqual(merged["2026-07-20"]["workouts"], recent_workouts)

    def test_sqlite_storage_is_private(self) -> None:
        sqlite_path = self.runtime_dir / "health.db"

        write_sqlite(
            sqlite_path,
            "ahs_private",
            "2026-07-20T00:00:00+00:00",
            {"2026-07-20": {"activity": {"steps": 1000}}},
        )

        self.assertEqual(stat.S_IMODE(sqlite_path.stat().st_mode), 0o600)

    def test_ndjson_storage_is_private(self) -> None:
        json_path = self.runtime_dir / "health.ndjson"

        write_ndjson(json_path, {"user_id": "ahs_private", "payload": {}})

        self.assertEqual(stat.S_IMODE(json_path.stat().st_mode), 0o600)


if __name__ == "__main__":
    unittest.main()
