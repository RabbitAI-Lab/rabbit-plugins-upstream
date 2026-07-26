#!/usr/bin/env python3
"""
Tests for seedance.py.

Two kinds of tests:

1. Offline tests (default): mock the HTTP layer so they run anywhere without an
   API key or network. They assert the *shape* of the request sent to Ark and
   the synchronous polling behavior.

2. Live tests: real calls against the openai-video endpoint (api_type forced
   to "openai-video", model doubao-seedance-2.0-mini). Skipped automatically
   unless ARK_API_KEY is set in the environment. They become useful once you
   have a key. Run them with:

       ARK_API_KEY=... python3 -m unittest test_seedance.LiveTests -v

   (from within scripts/, or: python3 scripts/test_seedance.py LiveTests)
   They cost real tokens / quota, so they are opt-in.
"""

from __future__ import annotations

import os
import sys
import unittest
from unittest import mock

# Allow running the test file in place (no package install).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import seedance  # noqa: E402
from seedance import ArkVideoClient, ArkVideoError

TEXT = "a daisy field under a blue sky, camera slowly pushing in"
IMG = "https://example.com/first.png"
IMG2 = "https://example.com/last.png"

DEFAULTS = {
    "generate_audio": True,
    "watermark": False,
    "ratio": "16:9",
    "duration": 5,
    "resolution": "720p",
}


def make_client(**kw) -> ArkVideoClient:
    """Build a client with a dummy key (no network in these tests).

    Defaults to the Ark API shape so the existing body/polling tests (which
    assert the Ark request body) still hold. OpenAI-shape tests pass
    api_type="openai-video" explicitly or use make_openai_video_client().
    """
    kw.setdefault("api_key", "test-key")
    kw.setdefault("api_type", "ark")
    kw.setdefault("poll_interval", 0)  # no sleeping in tests
    kw.setdefault("timeout", 60)
    return ArkVideoClient(**kw)


def make_openai_video_client(**kw) -> ArkVideoClient:
    """Build an openai-video (doubao-seedance-2.0-mini) client with a dummy key."""
    kw.setdefault("api_key", "test-key")
    kw.setdefault("api_type", "openai-video")
    kw.setdefault("poll_interval", 0)
    kw.setdefault("timeout", 60)
    return ArkVideoClient(**kw)


def make_openai_client(**kw) -> ArkVideoClient:
    """Build an openai (Ark-shaped, doubao-seedance-2.0 full) client with a dummy key."""
    kw.setdefault("api_key", "test-key")
    kw.setdefault("api_type", "openai")
    kw.setdefault("poll_interval", 0)
    kw.setdefault("timeout", 60)
    return ArkVideoClient(**kw)


class FakeHttp:
    """Records calls and returns scripted responses.

    `responses` maps (method, path) -> list of dicts (queued FIFO). A callable
    is also accepted per entry for full control.
    """

    def __init__(self, responses=None):
        self.responses = responses or {}
        self.calls = []  # list of (method, path, body)

    def __call__(self, method, path, body=None):
        self.calls.append((method, path, body))
        key = (method, path)
        if key not in self.responses:
            raise AssertionError(f"unexpected HTTP call {method} {path}")
        queue = self.responses[key]
        if callable(queue):
            return queue(method, path, body)
        if not queue:
            raise AssertionError(f"no more responses queued for {method} {path}")
        return queue.pop(0)


class BuildContentTests(unittest.TestCase):
    """Pure construction — no HTTP, no key needed."""

    def test_text_only(self):
        content = ArkVideoClient.build_content(TEXT)
        self.assertEqual(content, [{"type": "text", "text": TEXT}])

    def test_image_url_acts_as_plain_first_frame(self):
        content = ArkVideoClient.build_content(TEXT, image_url=IMG)
        self.assertEqual(len(content), 2)
        self.assertEqual(content[0], {"type": "text", "text": TEXT})
        # No role => implicit first frame (image-to-video).
        self.assertEqual(content[1], {"type": "image_url", "image_url": {"url": IMG}})

    def test_first_and_last_frame_get_roles(self):
        content = ArkVideoClient.build_content(
            TEXT, first_frame=IMG, last_frame=IMG2
        )
        self.assertEqual(len(content), 3)
        self.assertEqual(content[0]["type"], "text")
        self.assertEqual(content[1]["role"], "first_frame")
        self.assertEqual(content[1]["image_url"]["url"], IMG)
        self.assertEqual(content[2]["role"], "last_frame")
        self.assertEqual(content[2]["image_url"]["url"], IMG2)

    def test_empty_text_raises(self):
        with self.assertRaises(ArkVideoError):
            ArkVideoClient.build_content("")


class ConflictTests(unittest.TestCase):
    """Parameter conflict / dependency validation."""

    def _body(self, **kw):
        kw.setdefault("text", TEXT)
        return make_client().build_request_body(**kw)

    # --- allowed combos (sanity, must not raise) ----------------------- #
    def test_text_only_ok(self):
        self._body()

    def test_image_url_only_ok(self):
        self._body(image_url=IMG)

    def test_first_frame_only_ok(self):
        self._body(first_frame=IMG)

    def test_first_and_last_frame_ok(self):
        self._body(first_frame=IMG, last_frame=IMG2)

    def test_adaptive_with_image_ok(self):
        self._body(image_url=IMG, ratio="adaptive")
        self._body(first_frame=IMG, last_frame=IMG2, ratio="adaptive")

    # --- conflicts ----------------------------------------------------- #
    def test_image_url_with_first_frame_conflict(self):
        with self.assertRaises(ArkVideoError):
            self._body(image_url=IMG, first_frame=IMG)

    def test_image_url_with_last_frame_conflict(self):
        with self.assertRaises(ArkVideoError):
            self._body(image_url=IMG, last_frame=IMG2)

    def test_image_url_with_both_frames_conflict(self):
        with self.assertRaises(ArkVideoError):
            self._body(image_url=IMG, first_frame=IMG, last_frame=IMG2)

    # --- dependencies --------------------------------------------------- #
    def test_last_frame_without_first_frame_rejected(self):
        with self.assertRaises(ArkVideoError):
            self._body(last_frame=IMG2)

    def test_adaptive_without_image_rejected(self):
        with self.assertRaises(ArkVideoError):
            self._body(ratio="adaptive")

    def test_missing_text_rejected(self):
        with self.assertRaises(ArkVideoError):
            make_client().build_request_body(text="")

    def test_non_positive_duration_rejected(self):
        with self.assertRaises(ArkVideoError):
            self._body(duration=0)
        with self.assertRaises(ArkVideoError):
            self._body(duration=-3)


class BuildRequestTests(unittest.TestCase):
    def test_text_to_video_defaults(self):
        client = make_client()
        body = client.build_request_body(text=TEXT)
        self.assertEqual(body["model"], client.model)  # ark → DEFAULT_MODEL_ARK
        self.assertEqual(body["content"], [{"type": "text", "text": TEXT}])
        self.assertEqual(body["generate_audio"], True)
        self.assertEqual(body["watermark"], False)
        self.assertEqual(body["ratio"], "16:9")
        self.assertEqual(body["duration"], 5)
        self.assertEqual(body["resolution"], "720p")
        self.assertNotIn("seed", body)

    def test_image_to_video_body(self):
        client = make_client()
        body = client.build_request_body(text=TEXT, image_url=IMG)
        self.assertEqual(body["content"], [
            {"type": "text", "text": TEXT},
            {"type": "image_url", "image_url": {"url": IMG}},
        ])

    def test_first_last_frame_body(self):
        client = make_client()
        body = client.build_request_body(
            text=TEXT, first_frame=IMG, last_frame=IMG2
        )
        self.assertEqual(body["content"], [
            {"type": "text", "text": TEXT},
            {"type": "image_url", "image_url": {"url": IMG}, "role": "first_frame"},
            {"type": "image_url", "image_url": {"url": IMG2}, "role": "last_frame"},
        ])

    def test_overrides_and_seed(self):
        client = make_client()
        body = client.build_request_body(
            text=TEXT, duration=10, ratio="9:16", resolution="1080p", seed=42
        )
        self.assertEqual(body["duration"], 10)
        self.assertEqual(body["ratio"], "9:16")
        self.assertEqual(body["resolution"], "1080p")
        self.assertEqual(body["seed"], 42)

    def test_fixed_params_cannot_be_overridden_via_convenience_kwargs(self):
        """generate_audio and watermark are fixed per spec."""
        client = make_client()
        body = client.build_request_body(text=TEXT)
        # They are not part of the build_request_body signature at all.
        self.assertNotIn("generate_audio", inspect_signature_extras())  # sanity on the test itself
        self.assertEqual(body["generate_audio"], True)
        self.assertEqual(body["watermark"], False)


def inspect_signature_extras():
    """Helper kept tiny to avoid importing inspect at module top."""
    import inspect

    params = inspect.signature(ArkVideoClient.build_request_body).parameters
    return set(params)


class ClientConstructionTests(unittest.TestCase):
    def test_missing_api_key_raises(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ArkVideoError):
                ArkVideoClient()

    def test_uses_env_endpoint(self):
        with mock.patch.dict(
            os.environ,
            {"ARK_API_KEY": "k", "ARK_ENDPOINT": "https://example.test/api/v3/"},
            clear=True,
        ):
            c = ArkVideoClient()
        self.assertEqual(c.endpoint, "https://example.test/api/v3")  # trailing slash stripped

    def test_ark_api_type_env_picks_openai_video(self):
        with mock.patch.dict(
            os.environ,
            {"ARK_API_KEY": "k", "ARK_API_TYPE": "openai-video"},
            clear=True,
        ):
            c = ArkVideoClient()
        self.assertEqual(c.api_type, "openai-video")
        self.assertEqual(c.model, seedance.DEFAULT_MODEL_OPENAI_VIDEO)

    def test_ark_api_type_env_invalid_rejected(self):
        with mock.patch.dict(
            os.environ,
            {"ARK_API_KEY": "k", "ARK_API_TYPE": "bogus"},
            clear=True,
        ):
            with self.assertRaises(ArkVideoError):
                ArkVideoClient()

    def test_explicit_api_type_beats_env(self):
        # CLI/arg priority > ARK_API_TYPE env
        with mock.patch.dict(
            os.environ,
            {"ARK_API_KEY": "k", "ARK_API_TYPE": "ark"},
            clear=True,
        ):
            c = ArkVideoClient(api_type="openai-video")
        self.assertEqual(c.api_type, "openai-video")

    def test_ark_model_env_overrides_per_type_default(self):
        with mock.patch.dict(
            os.environ,
            {"ARK_API_KEY": "k", "ARK_MODEL": "my-custom-model"},
            clear=True,
        ):
            c = ArkVideoClient()  # default api_type ark
        self.assertEqual(c.model, "my-custom-model")

    def test_explicit_model_beats_env(self):
        with mock.patch.dict(
            os.environ,
            {"ARK_API_KEY": "k", "ARK_MODEL": "env-model"},
            clear=True,
        ):
            c = ArkVideoClient(model="cli-model")
        self.assertEqual(c.model, "cli-model")


class DotenvTests(unittest.TestCase):
    """Tests for the dependency-free .env loader."""

    def _write_env(self, tmpdir, content):
        path = os.path.join(tmpdir, ".env")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    def test_loads_key_and_endpoint(self):
        import tempfile

        with tempfile.TemporaryDirectory() as d:
            path = self._write_env(d, "ARK_API_KEY=fromfile\nARK_ENDPOINT=https://env.test/api/v3\n")
            with mock.patch.dict(os.environ, {}, clear=True):
                loaded = seedance.load_dotenv(path)
                self.assertTrue(loaded)
                self.assertEqual(os.environ.get("ARK_API_KEY"), "fromfile")
                self.assertEqual(os.environ.get("ARK_ENDPOINT"), "https://env.test/api/v3")

    def test_real_env_takes_precedence(self):
        import tempfile

        with tempfile.TemporaryDirectory() as d:
            path = self._write_env(d, "ARK_API_KEY=fromfile\n")
            with mock.patch.dict(os.environ, {"ARK_API_KEY": "real"}, clear=True):
                seedance.load_dotenv(path)
                self.assertEqual(os.environ.get("ARK_API_KEY"), "real")

    def test_override_flag_overwrites(self):
        import tempfile

        with tempfile.TemporaryDirectory() as d:
            path = self._write_env(d, "ARK_API_KEY=fromfile\n")
            with mock.patch.dict(os.environ, {"ARK_API_KEY": "real"}, clear=True):
                seedance.load_dotenv(path, override=True)
                self.assertEqual(os.environ.get("ARK_API_KEY"), "fromfile")

    def test_quotes_export_and_comments(self):
        import tempfile

        content = (
            "# a comment\n"
            "export ARK_API_KEY='quoted value'\n"
            'ARK_ENDPOINT="https://q.test/api/v3" # trailing comment\n'
            "BARE_KEY=plain\n"
            "NOT_AN_ENV_LINE\n"
        )
        with tempfile.TemporaryDirectory() as d:
            path = self._write_env(d, content)
            with mock.patch.dict(os.environ, {}, clear=True):
                seedance.load_dotenv(path)
                self.assertEqual(os.environ.get("ARK_API_KEY"), "quoted value")
                self.assertEqual(os.environ.get("ARK_ENDPOINT"), "https://q.test/api/v3")
                self.assertEqual(os.environ.get("BARE_KEY"), "plain")
                self.assertNotIn("NOT_AN_ENV_LINE", os.environ)

    def test_missing_file_returns_false(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertFalse(seedance.load_dotenv("/no/such/.env"))


class GenerateVideoSyncTests(unittest.TestCase):
    """End-to-end sync flow with a mocked HTTP transport."""

    def _run(self, fake):
        client = make_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            result = client.generate_video(text=TEXT)
        return client, result

    def test_text_to_video_polls_until_succeeded(self):
        create = {"id": "cgt-123"}

        def get_resp(method, path, body):
            # path is /contents/generations/tasks/cgt-123
            return {
                "id": "cgt-123",
                "status": "queued",
            }

        # First queued, then running, then succeeded with a video_url.
        get_states = [
            {"id": "cgt-123", "status": "queued"},
            {"id": "cgt-123", "status": "running"},
            {
                "id": "cgt-123",
                "model": seedance.DEFAULT_MODEL_OPENAI_VIDEO,
                "status": "succeeded",
                "content": {"video_url": "https://cdn/video.mp4"},
                "usage": {"completion_tokens": 1, "total_tokens": 1},
            },
        ]
        fake = FakeHttp(
            {
                ("POST", "/contents/generations/tasks"): [create],
                ("GET", "/contents/generations/tasks/cgt-123"): get_states,
            }
        )
        client, result = self._run(fake)

        self.assertEqual(result["status"], "succeeded")
        url = ArkVideoClient.video_url(result)
        self.assertEqual(url, "https://cdn/video.mp4")

        # Exactly one create call, three polls.
        posts = [c for c in fake.calls if c[0] == "POST"]
        gets = [c for c in fake.calls if c[0] == "GET"]
        self.assertEqual(len(posts), 1)
        self.assertEqual(len(gets), 3)

        # The create body is the text-to-video body.
        method, path, body = posts[0]
        self.assertEqual(path, "/contents/generations/tasks")
        self.assertEqual(body["model"], client.model)  # ark → DEFAULT_MODEL_ARK
        self.assertEqual(body["content"], [{"type": "text", "text": TEXT}])
        for k, v in DEFAULTS.items():
            self.assertEqual(body[k], v)

    def test_image_to_video_sends_plain_image_block(self):
        fake = FakeHttp(
            {
                ("POST", "/contents/generations/tasks"): [{"id": "cgt-img"}],
                ("GET", "/contents/generations/tasks/cgt-img"): [
                    {
                        "id": "cgt-img",
                        "status": "succeeded",
                        "content": {"video_url": "https://cdn/img.mp4"},
                    },
                ],
            }
        )
        client, result = self._run(fake)
        # Re-run through the mocked transport to inspect the body actually sent.
        # (The first run already consumed the queue; reconstruct with a fresh fake.)
        fake2 = FakeHttp(
            {
                ("POST", "/contents/generations/tasks"): [{"id": "cgt-img"}],
                ("GET", "/contents/generations/tasks/cgt-img"): [
                    {"id": "cgt-img", "status": "succeeded", "content": {"video_url": "https://cdn/img.mp4"}}
                ],
            }
        )
        client2 = make_client()
        with mock.patch.object(client2, "_http_request", side_effect=fake2):
            client2.generate_video(text=TEXT, image_url=IMG)

        post_body = fake2.calls[0][2]
        self.assertEqual(
            post_body["content"],
            [
                {"type": "text", "text": TEXT},
                {"type": "image_url", "image_url": {"url": IMG}},
            ],
        )
        self.assertEqual(result["status"], "succeeded")

    def test_first_last_frame_sends_roles(self):
        fake = FakeHttp(
            {
                ("POST", "/contents/generations/tasks"): [{"id": "cgt-fl"}],
                ("GET", "/contents/generations/tasks/cgt-fl"): [
                    {
                        "id": "cgt-fl",
                        "status": "succeeded",
                        "content": {"video_url": "https://cdn/fl.mp4"},
                    }
                ],
            }
        )
        client = make_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            client.generate_video(text=TEXT, first_frame=IMG, last_frame=IMG2)

        post_body = fake.calls[0][2]
        self.assertEqual(
            post_body["content"],
            [
                {"type": "text", "text": TEXT},
                {"type": "image_url", "image_url": {"url": IMG}, "role": "first_frame"},
                {"type": "image_url", "image_url": {"url": IMG2}, "role": "last_frame"},
            ],
        )

    def test_task_failed_raises(self):
        fake = FakeHttp(
            {
                ("POST", "/contents/generations/tasks"): [{"id": "cgt-fail"}],
                ("GET", "/contents/generations/tasks/cgt-fail"): [
                    {
                        "id": "cgt-fail",
                        "status": "failed",
                        "error": {"code": "X", "message": "bad prompt"},
                    }
                ],
            }
        )
        client = make_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            with self.assertRaises(ArkVideoError) as ctx:
                client.generate_video(text=TEXT)
        self.assertIn("failed", str(ctx.exception))

    def test_timeout_raises(self):
        client = make_client(timeout=0)  # deadline already in the past

        def fake_http(method, path, body=None):
            if method == "POST":
                return {"id": "cgt-slow"}
            return {"id": "cgt-slow", "status": "running"}

        with mock.patch.object(client, "_http_request", side_effect=fake_http):
            with self.assertRaises(ArkVideoError):
                client.generate_video(text=TEXT)


class OpenaiVideoTransportTests(unittest.TestCase):
    """Tests for the openai-video transport (api_type=openai).

    Targets the openai-video endpoint (POST /video/generations,
    GET /video/generations/{id}) which speaks an OpenAI-video-style request
    body (seconds/size/input_reference) over the tokenhub response shape
    ({code, data:{status, result_url, fail_reason}}).
    """

    # --- request body -------------------------------------------------- #
    def test_body_text_only(self):
        body = make_openai_video_client().build_request_body(text=TEXT)
        self.assertEqual(body["model"], seedance.DEFAULT_MODEL_OPENAI_VIDEO)  # doubao-seedance-2.0-mini
        self.assertEqual(body["prompt"], TEXT)
        self.assertEqual(body["seconds"], "4")     # duration 5 -> snapped, as STRING
        self.assertEqual(body["size"], "1280x720")  # 16:9 @ 720p
        # The openai-video body has none of these Ark-only params.
        for absent in ("generate_audio", "watermark", "ratio", "duration",
                       "resolution", "content", "image", "first_frame",
                       "last_frame", "seed", "input_reference"):
            self.assertNotIn(absent, body)

    def test_body_seconds_snaps_to_allowed_as_string(self):
        c = make_openai_video_client()
        self.assertEqual(c.build_request_body(text=TEXT, duration=4)["seconds"], "4")
        self.assertEqual(c.build_request_body(text=TEXT, duration=5)["seconds"], "4")
        self.assertEqual(c.build_request_body(text=TEXT, duration=8)["seconds"], "8")
        self.assertEqual(c.build_request_body(text=TEXT, duration=10)["seconds"], "8")
        self.assertEqual(c.build_request_body(text=TEXT, duration=12)["seconds"], "12")
        self.assertEqual(c.build_request_body(text=TEXT, duration=99)["seconds"], "12")
        # always a string, never a number (the endpoint rejects numbers)
        for d in (4, 5, 8, 12):
            self.assertIsInstance(c.build_request_body(text=TEXT, duration=d)["seconds"], str)

    def test_body_size_maps_ratio_and_resolution(self):
        c = make_openai_video_client()
        self.assertEqual(c.build_request_body(text=TEXT, ratio="16:9", resolution="720p")["size"], "1280x720")
        self.assertEqual(c.build_request_body(text=TEXT, ratio="9:16", resolution="720p")["size"], "720x1280")
        self.assertEqual(c.build_request_body(text=TEXT, ratio="1:1", resolution="720p")["size"], "720x720")
        self.assertEqual(c.build_request_body(text=TEXT, ratio="16:9", resolution="1080p")["size"], "1920x1080")
        # adaptive has no openai-video equivalent; _size_for falls back to landscape.
        self.assertEqual(ArkVideoClient._size_for("adaptive", "720p"), "1280x720")

    def test_body_image_uses_input_reference(self):
        body = make_openai_video_client().build_request_body(text=TEXT, image_url=IMG)
        self.assertEqual(body["input_reference"], IMG)  # single URL string

    def test_body_first_and_last_frame(self):
        body = make_openai_video_client().build_request_body(
            text=TEXT, first_frame=IMG, last_frame=IMG2
        )
        # first+last frame -> comma-joined URL string
        self.assertEqual(body["input_reference"], f"{IMG},{IMG2}")

    def test_body_seed_dropped(self):
        # seed is not part of the openai-video body.
        body = make_openai_video_client().build_request_body(text=TEXT, seed=7)
        self.assertNotIn("seed", body)

    # --- create + poll paths ------------------------------------------- #
    def test_create_posts_video_generations_and_parses_id(self):
        fake = FakeHttp({
            ("POST", "/video/generations"): [{"id": "task_123", "task_id": "task_123", "status": "queued"}],
        })
        client = make_openai_video_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            tid = client.create_task({"model": "doubao-seedance-2.0-mini", "prompt": "x"})
        self.assertEqual(tid, "task_123")
        self.assertEqual(fake.calls[0][:2], ("POST", "/video/generations"))

    def test_create_parses_task_id_when_no_id(self):
        fake = FakeHttp({("POST", "/video/generations"): [{"task_id": "task_456"}]})
        client = make_openai_video_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            tid = client.create_task({"model": "x", "prompt": "x"})
        self.assertEqual(tid, "task_456")

    def test_poll_gets_video_generations_id(self):
        fake = FakeHttp({("GET", "/video/generations/task_123"): [
            {"code": "success", "data": {"task_id": "task_123", "status": "IN_PROGRESS"}},
        ]})
        client = make_openai_video_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            res = client.get_task("task_123")
        self.assertEqual(res["status"], "in_progress")  # non-terminal, lowercased
        self.assertIsNone(res["video_url"])

    # --- status normalization ------------------------------------------ #
    def test_normalize_success(self):
        client = make_openai_video_client()
        res = client._normalize_task({"code": "success", "data": {"status": "SUCCESS", "result_url": "https://x/v.mp4"}})
        self.assertEqual(res["status"], "succeeded")
        self.assertEqual(res["video_url"], "https://x/v.mp4")

    def test_normalize_fail_reason(self):
        client = make_openai_video_client()
        res = client._normalize_task({"code": "success", "data": {"status": "FAIL", "fail_reason": "boom"}})
        self.assertEqual(res["status"], "failed")
        self.assertEqual(res["error"], "boom")

    def test_normalize_error_code(self):
        client = make_openai_video_client()
        res = client._normalize_task({"code": "invalid_request", "message": "bad", "data": None})
        self.assertEqual(res["status"], "failed")
        self.assertIn("bad", res["error"])

    # --- end-to-end sync (mocked) -------------------------------------- #
    def test_generate_video_polls_to_success(self):
        fake = FakeHttp({
            ("POST", "/video/generations"): [{"id": "task_1", "status": "queued"}],
            ("GET", "/video/generations/task_1"): [
                {"code": "success", "data": {"status": "IN_PROGRESS"}},
                {"code": "success", "data": {"status": "SUCCESS", "result_url": "https://cdn/v.mp4"}},
            ],
        })
        client = make_openai_video_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            result = client.generate_video(text=TEXT)
        self.assertEqual(result["status"], "succeeded")
        self.assertEqual(ArkVideoClient.video_url(result), "https://cdn/v.mp4")
        # posted body is the openai-video shape
        post_body = fake.calls[0][2]
        self.assertEqual(post_body["prompt"], TEXT)
        self.assertEqual(post_body["model"], seedance.DEFAULT_MODEL_OPENAI_VIDEO)
        self.assertEqual(post_body["seconds"], "4")
        self.assertIn("size", post_body)
        self.assertNotIn("content", post_body)

    def test_generate_video_failed_raises(self):
        fake = FakeHttp({
            ("POST", "/video/generations"): [{"id": "task_9"}],
            ("GET", "/video/generations/task_9"): [
                {"code": "success", "data": {"status": "FAIL", "fail_reason": "nope"}},
            ],
        })
        client = make_openai_video_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            with self.assertRaises(ArkVideoError):
                client.generate_video(text=TEXT)

    def test_unknown_api_type_rejected(self):
        with self.assertRaises(ArkVideoError):
            ArkVideoClient(api_key="k", api_type="bogus")


class OpenaiTransportTests(unittest.TestCase):
    """Tests for the openai (Ark-shaped) transport (api_type=openai).

    Targets POST /video/generations with an Ark-shaped body
    (image/first_frame/last_frame/generate_audio/ratio/duration/watermark/
    resolution/seed) for doubao-seedance-2.0 (full).
    """

    # --- request body -------------------------------------------------- #
    def test_body_text_only(self):
        body = make_openai_client().build_request_body(text=TEXT)
        self.assertEqual(body["model"], seedance.DEFAULT_MODEL_OPENAI)
        self.assertEqual(body["prompt"], TEXT)
        self.assertEqual(body["generate_audio"], True)
        self.assertEqual(body["watermark"], False)
        self.assertEqual(body["ratio"], "16:9")
        self.assertEqual(body["duration"], 5)
        self.assertEqual(body["resolution"], "720p")
        self.assertNotIn("image", body)
        self.assertNotIn("first_frame", body)
        self.assertNotIn("content", body)  # no Ark content[] in openai mode

    def test_body_image_uses_image_field(self):
        body = make_openai_client().build_request_body(text=TEXT, image_url=IMG)
        self.assertEqual(body[seedance.OPENAI_FIELD_IMAGE], IMG)
        self.assertNotIn("first_frame", body)

    def test_body_first_and_last_frame(self):
        body = make_openai_client().build_request_body(
            text=TEXT, first_frame=IMG, last_frame=IMG2
        )
        self.assertEqual(body[seedance.OPENAI_FIELD_FIRST_FRAME], IMG)
        self.assertEqual(body[seedance.OPENAI_FIELD_LAST_FRAME], IMG2)

    def test_body_seed(self):
        # openai (Ark-shaped) supports seed (unlike openai-video).
        body = make_openai_client().build_request_body(text=TEXT, seed=7)
        self.assertEqual(body["seed"], 7)

    # --- create + poll paths ------------------------------------------- #
    def test_create_posts_video_generations_and_parses_id(self):
        fake = FakeHttp({
            ("POST", "/video/generations"): [{"id": "task_123", "task_id": "task_123", "status": "queued"}],
        })
        client = make_openai_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            tid = client.create_task({"model": "doubao-seedance-2.0", "prompt": "x"})
        self.assertEqual(tid, "task_123")

    def test_poll_gets_video_generations_id(self):
        fake = FakeHttp({("GET", "/video/generations/task_123"): [
            {"code": "success", "data": {"task_id": "task_123", "status": "IN_PROGRESS"}},
        ]})
        client = make_openai_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            res = client.get_task("task_123")
        self.assertEqual(res["status"], "in_progress")  # non-terminal, lowercased
        self.assertIsNone(res["video_url"])

    # --- status normalization ------------------------------------------ #
    def test_normalize_success(self):
        client = make_openai_client()
        res = client._normalize_task({"code": "success", "data": {"status": "SUCCESS", "result_url": "https://x/v.mp4"}})
        self.assertEqual(res["status"], "succeeded")
        self.assertEqual(res["video_url"], "https://x/v.mp4")

    def test_normalize_fail_reason(self):
        client = make_openai_client()
        res = client._normalize_task({"code": "success", "data": {"status": "FAIL", "fail_reason": "boom"}})
        self.assertEqual(res["status"], "failed")
        self.assertEqual(res["error"], "boom")

    # --- end-to-end sync (mocked) -------------------------------------- #
    def test_generate_video_polls_to_success(self):
        fake = FakeHttp({
            ("POST", "/video/generations"): [{"id": "task_1", "status": "queued"}],
            ("GET", "/video/generations/task_1"): [
                {"code": "success", "data": {"status": "IN_PROGRESS"}},
                {"code": "success", "data": {"status": "SUCCESS", "result_url": "https://cdn/v.mp4"}},
            ],
        })
        client = make_openai_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            result = client.generate_video(text=TEXT)
        self.assertEqual(result["status"], "succeeded")
        self.assertEqual(ArkVideoClient.video_url(result), "https://cdn/v.mp4")
        # posted body is the Ark-shaped openai body
        post_body = fake.calls[0][2]
        self.assertEqual(post_body["prompt"], TEXT)
        self.assertEqual(post_body["model"], seedance.DEFAULT_MODEL_OPENAI)
        self.assertEqual(post_body["generate_audio"], True)
        self.assertNotIn("content", post_body)

    def test_generate_video_failed_raises(self):
        fake = FakeHttp({
            ("POST", "/video/generations"): [{"id": "task_9"}],
            ("GET", "/video/generations/task_9"): [
                {"code": "success", "data": {"status": "FAIL", "fail_reason": "nope"}},
            ],
        })
        client = make_openai_client()
        with mock.patch.object(client, "_http_request", side_effect=fake):
            with self.assertRaises(ArkVideoError):
                client.generate_video(text=TEXT)


class HttpErrorTests(unittest.TestCase):
    def test_http_error_is_wrapped(self):
        # Exercise the REAL _http_request error path by faking urlopen.
        import io
        import urllib.error

        client = make_client()
        err = urllib.error.HTTPError(
            "https://ark.test/api/v3/contents/generations/tasks",
            400,
            "Bad Request",
            {},
            io.BytesIO(b'{"error":{"code":"bad","message":"nope"}}'),
        )
        with mock.patch("urllib.request.urlopen", side_effect=err):
            with self.assertRaises(ArkVideoError) as ctx:
                client.create_task({"model": "x"})
        self.assertIn("400", str(ctx.exception))
        self.assertIn("nope", str(ctx.exception))

    def test_create_without_id_raises(self):
        client = make_client()
        with mock.patch.object(
            client, "_http_request", side_effect=lambda *a, **k: {"nope": 1}
        ):
            with self.assertRaises(ArkVideoError):
                client.create_task({"model": "x"})


def io_bytes(b: bytes):
    import io

    return io.BytesIO(b)


class OSSUploaderTests(unittest.TestCase):
    """Tests for the Alibaba OSS uploader (no real OSS / no SDK install needed)."""

    def _fake_oss_module(self):
        """A stand-in for `alibabacloud_oss_v2` capturing request objects."""
        import sys
        import types

        mod = types.ModuleType("alibabacloud_oss_v2")

        class PutObjectRequest:
            def __init__(self, bucket=None, key=None, body=None):
                self.bucket, self.key, self.body = bucket, key, body

        class GetObjectRequest:
            def __init__(self, bucket=None, key=None):
                self.bucket, self.key = bucket, key

        mod.PutObjectRequest = PutObjectRequest
        mod.GetObjectRequest = GetObjectRequest
        # Remember so the test can read back the request classes.
        self._PutObjectRequest = PutObjectRequest
        self._GetObjectRequest = GetObjectRequest
        return mod

    def setUp(self):
        import sys

        self._real_oss = sys.modules.get("alibabacloud_oss_v2")
        sys.modules["alibabacloud_oss_v2"] = self._fake_oss_module()
        self.addCleanup(self._restore_oss)

    def _restore_oss(self):
        import sys

        if self._real_oss is None:
            sys.modules.pop("alibabacloud_oss_v2", None)
        else:
            sys.modules["alibabacloud_oss_v2"] = self._real_oss

    def _fake_client(self, url="https://oss/signed/foo.png"):
        class _Result:
            def __init__(self, url):
                self.url = url

        class FakeClient:
            def __init__(self):
                self.put_calls = []
                self.presign_calls = []

            def put_object(self, req):
                self.put_calls.append(req)
                # drain the body so the file handle can be closed cleanly
                if req.body is not None:
                    getattr(req.body, "read", lambda: b"")()
                return mock.Mock(status_code=200, request_id="r")

            def presign(self, req, expires=None):
                self.presign_calls.append((req, expires))
                return _Result(url)

        return FakeClient()

    # --- key construction ---------------------------------------------- #
    def test_key_with_default_prefix(self):
        u = seedance.OSSUploader("ak", "sk", key_prefix="dev/")
        self.assertEqual(u._key_for("/tmp/foo.png"), "dev/foo.png")

    def test_key_normalizes_prefix_without_trailing_slash(self):
        u = seedance.OSSUploader("ak", "sk", key_prefix="dev")
        self.assertEqual(u._key_for("/tmp/foo.png"), "dev/foo.png")

    def test_key_strips_leading_slash_in_prefix(self):
        u = seedance.OSSUploader("ak", "sk", key_prefix="/dev/")
        self.assertEqual(u._key_for("foo.png"), "dev/foo.png")

    def test_key_empty_prefix(self):
        u = seedance.OSSUploader("ak", "sk", key_prefix="")
        self.assertEqual(u._key_for("/tmp/foo.png"), "foo.png")

    # --- credentials --------------------------------------------------- #
    def test_missing_credentials_raises(self):
        with self.assertRaises(ArkVideoError):
            seedance.OSSUploader("", "sk")

    def test_from_env_defaults(self):
        with mock.patch.dict(
            os.environ,
            {"OSS_ACCESS_KEY_ID": "ak", "OSS_ACCESS_KEY_SECRET": "sk"},
            clear=True,
        ):
            u = seedance.OSSUploader.from_env()
        self.assertEqual(u.ak, "ak")
        self.assertEqual(u.sk, "sk")
        self.assertEqual(u.region, "cn-beijing")
        self.assertEqual(u.bucket, "jiangsier")
        self.assertEqual(u.key_prefix, "dev/")
        self.assertEqual(u.signed_url_minutes, 10)

    def test_from_env_overrides(self):
        with mock.patch.dict(
            os.environ,
            {
                "OSS_ACCESS_KEY_ID": "ak",
                "OSS_ACCESS_KEY_SECRET": "sk",
                "OSS_ENDPOINT": "us-west-1",
                "OSS_BUCKET": "mybucket",
                "OSS_KEY_PREFIX": "prod/v2/",
            },
            clear=True,
        ):
            u = seedance.OSSUploader.from_env()
        self.assertEqual(u.region, "us-west-1")
        self.assertEqual(u.bucket, "mybucket")
        self.assertEqual(u.key_prefix, "prod/v2/")

    # --- upload + sign ------------------------------------------------- #
    def test_upload_and_sign_uses_key_and_10min_url(self):
        import os
        import tempfile

        fake = self._fake_client(url="https://oss/signed/x.png")
        u = seedance.OSSUploader(
            "ak", "sk", bucket="bkt", key_prefix="dev/", oss_client=fake
        )
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "frame.png")
            with open(path, "wb") as f:
                f.write(b"\x89PNG fake")

            url = u.upload_and_sign(path)

        self.assertEqual(url, "https://oss/signed/x.png")
        # put_object got the right bucket / key / a readable body
        self.assertEqual(len(fake.put_calls), 1)
        put = fake.put_calls[0]
        self.assertEqual(put.bucket, "bkt")
        self.assertEqual(put.key, "dev/frame.png")
        # presign got the same key and a 10-minute expiry
        self.assertEqual(len(fake.presign_calls), 1)
        req, expires = fake.presign_calls[0]
        self.assertEqual(req.bucket, "bkt")
        self.assertEqual(req.key, "dev/frame.png")
        import datetime

        self.assertEqual(expires, datetime.timedelta(minutes=10))

    def test_upload_missing_file_raises(self):
        u = seedance.OSSUploader("ak", "sk", oss_client=self._fake_client())
        with self.assertRaises(ArkVideoError):
            u.upload_and_sign("/no/such/file.png")


class ResolveInputsTests(unittest.TestCase):
    """Tests for the CLI _resolve_image_inputs helper."""

    def _args(self, *a):
        return seedance.build_arg_parser().parse_args(list(a))

    def test_url_only_passes_through(self):
        args = self._args("-t", "hi", "--image-url", "https://x/i.png")
        resolved = seedance._resolve_image_inputs(args)
        self.assertEqual(resolved, {
            "image_url": "https://x/i.png",
            "first_frame": None,
            "last_frame": None,
        })

    def test_text_only_all_none(self):
        args = self._args("-t", "hi")
        resolved = seedance._resolve_image_inputs(args)
        self.assertEqual(resolved, {"image_url": None, "first_frame": None, "last_frame": None})

    def test_image_and_image_url_conflict(self):
        args = self._args("-t", "hi", "--image", "local.png", "--image-url", "https://x/i.png")
        with self.assertRaises(ArkVideoError):
            seedance._resolve_image_inputs(args)

    def test_first_frame_and_first_frame_url_conflict(self):
        args = self._args("-t", "hi", "--first-frame", "f.png", "--first-frame-url", "https://x/f.png")
        with self.assertRaises(ArkVideoError):
            seedance._resolve_image_inputs(args)

    def test_last_frame_and_last_frame_url_conflict(self):
        args = self._args("-t", "hi", "--last-frame", "l.png", "--last-frame-url", "https://x/l.png")
        with self.assertRaises(ArkVideoError):
            seedance._resolve_image_inputs(args)

    def test_cross_conflict_fails_before_upload(self):
        # --image-url + --first-frame-url is a conflict; no OSS upload should happen.
        args = self._args(
            "-t", "hi", "--image-url", "https://x/i.png", "--first-frame-url", "https://x/f.png"
        )
        with mock.patch.object(seedance.OSSUploader, "from_env") as m:
            with self.assertRaises(ArkVideoError):
                seedance._resolve_image_inputs(args)
        m.assert_not_called()  # failed fast, no uploader built

    def test_local_image_uploaded_to_url(self):
        args = self._args("-t", "hi", "--image", "local.png")
        fake_uploader = mock.Mock()
        fake_uploader.upload_and_sign.return_value = "https://oss/signed/local.png"
        with mock.patch.object(seedance.OSSUploader, "from_env", return_value=fake_uploader):
            resolved = seedance._resolve_image_inputs(args)
        self.assertEqual(resolved["image_url"], "https://oss/signed/local.png")
        fake_uploader.upload_and_sign.assert_called_once_with("local.png")

    def test_local_first_and_last_uploaded(self):
        args = self._args("-t", "hi", "--first-frame", "f.png", "--last-frame", "l.png")
        fake_uploader = mock.Mock()
        fake_uploader.upload_and_sign.side_effect = [
            "https://oss/signed/f.png",
            "https://oss/signed/l.png",
        ]
        with mock.patch.object(seedance.OSSUploader, "from_env", return_value=fake_uploader):
            resolved = seedance._resolve_image_inputs(args)
        self.assertEqual(resolved["first_frame"], "https://oss/signed/f.png")
        self.assertEqual(resolved["last_frame"], "https://oss/signed/l.png")
        self.assertEqual(fake_uploader.upload_and_sign.call_count, 2)


# ---------------------------------------------------------------------- #
# Live tests — opt-in. Skipped unless ARK_API_KEY is set.
# ---------------------------------------------------------------------- #
@unittest.skipUnless(os.environ.get("ARK_API_KEY"), "set ARK_API_KEY to run live tests")
class LiveTests(unittest.TestCase):
    """Real API calls against the openai-video endpoint (openai-video api-type).

    NB: these target the openai-video endpoint (POST /video/generations,
    doubao-seedance-2.0-mini), NOT the raw Ark API, so _client() forces
    api_type="openai-video" even though the module default is ark. ARK_ENDPOINT
    must point at the openai-video base (set in .env).

    They use the public sample images from the Volcengine docs so you do not
    need to host your own. Run with:

        ARK_API_KEY=... python3 -m unittest test_seedance.LiveTests -v
    """

    FIRST_FRAME = "https://ark-project.tos-cn-beijing.volces.com/doc_image/i2v_foxrgirl.png"
    LAST_FRAME = "https://ark-project.tos-cn-beijing.volces.com/doc_image/seepro_last_frame.jpeg"

    def _client(self):
        return ArkVideoClient(api_type="openai-video", timeout=900, poll_interval=10)

    def test_text_to_video(self):
        result = self._client().generate_video(
            text="写实风格，晴朗的蓝天之下，一大片白色的雏菊花田，镜头逐渐拉近，最终定格在一朵雏菊花的特写上",
            duration=5,
            ratio="16:9",
            resolution="720p",
        )
        self.assertEqual(result["status"], "succeeded")
        self.assertTrue(ArkVideoClient.video_url(result))

    def test_image_to_video(self):
        result = self._client().generate_video(
            text="女孩抱着狐狸，镜头缓缓拉出，女孩的头发被风吹动",
            image_url=self.FIRST_FRAME,
            ratio="adaptive",
            duration=5,
            resolution="720p",
        )
        self.assertEqual(result["status"], "succeeded")
        self.assertTrue(ArkVideoClient.video_url(result))

    def test_first_last_frame_to_video(self):
        result = self._client().generate_video(
            text="图中女孩对着镜头微笑，360度环绕运镜",
            first_frame=self.FIRST_FRAME,
            last_frame=self.LAST_FRAME,
            ratio="adaptive",
            duration=5,
            resolution="720p",
        )
        self.assertEqual(result["status"], "succeeded")
        self.assertTrue(ArkVideoClient.video_url(result))


@unittest.skipUnless(os.environ.get("ARK_API_KEY"), "set ARK_API_KEY to run live tests")
class OpenaiLiveTests(unittest.TestCase):
    """Real API calls against the openai (Ark-shaped) endpoint (openai api-type).

    NB: these target POST /video/generations with the Ark-shaped body for
    doubao-seedance-2.0 (full) — the proxy's OpenAI chat-mirror entry (the
    /v1/chat/completions entry returns unsupported_model_endpoint on this
    account, so the full model is reached via /video/generations). Audio is not
    produced.
    """

    FIRST_FRAME = "https://ark-project.tos-cn-beijing.volces.com/doc_image/i2v_foxrgirl.png"
    LAST_FRAME = "https://ark-project.tos-cn-beijing.volces.com/doc_image/seepro_last_frame.jpeg"

    def _client(self):
        return ArkVideoClient(api_type="openai", timeout=900, poll_interval=10)

    def test_text_to_video(self):
        result = self._client().generate_video(
            text="写实风格，晴朗的蓝天之下，一大片白色的雏菊花田，镜头逐渐拉近，最终定格在一朵雏菊花的特写上",
            duration=5,
            ratio="16:9",
            resolution="720p",
        )
        self.assertEqual(result["status"], "succeeded")
        self.assertTrue(ArkVideoClient.video_url(result))

    def test_image_to_video(self):
        result = self._client().generate_video(
            text="女孩抱着狐狸，镜头缓缓拉出，女孩的头发被风吹动",
            image_url=self.FIRST_FRAME,
            ratio="adaptive",
            duration=5,
            resolution="720p",
        )
        self.assertEqual(result["status"], "succeeded")
        self.assertTrue(ArkVideoClient.video_url(result))


if __name__ == "__main__":
    unittest.main(verbosity=2)
