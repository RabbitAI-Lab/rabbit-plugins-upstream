from __future__ import annotations

import asyncio
import json
import time
from uuid import UUID

import httpx
import pytest

from sql_data_analyst_local.platform import PlatformClient, PlatformError
from sql_data_analyst_local.settings import PLATFORM_API_ORIGIN


API_KEY = "sk-secret-must-never-appear"
INSTALLATION_ID = UUID("018f47a2-7b2b-7e47-8794-c11316f5023c")
EXECUTION_ID = UUID("018f47a2-7b2b-7e47-8794-c11316f5023b")


class BlockingAsyncStream(httpx.AsyncByteStream):
    def __init__(self, body: bytes, chunk_delay: float) -> None:
        self.body = body
        self.chunk_delay = chunk_delay
        self.chunk_at: float | None = None
        self.cancelled_at: float | None = None
        self.closed = False

    async def __aiter__(self):
        await asyncio.sleep(self.chunk_delay)
        self.chunk_at = asyncio.get_running_loop().time()
        yield self.body[: len(self.body) // 2]
        try:
            await asyncio.Event().wait()
        except asyncio.CancelledError:
            self.cancelled_at = asyncio.get_running_loop().time()
            raise

    async def aclose(self) -> None:
        self.closed = True


class CumulativeDelayTransport(httpx.BaseTransport, httpx.AsyncBaseTransport):
    def __init__(self, response: httpx.Response, header_delay: float) -> None:
        self.response = response
        self.header_delay = header_delay
        self.sync_calls = 0
        self.async_calls = 0

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.sync_calls += 1
        return success_response()

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        self.async_calls += 1
        await asyncio.sleep(self.header_delay)
        return self.response


class SyncOnlySecretTransport(httpx.BaseTransport):
    def handle_request(self, request: httpx.Request) -> httpx.Response:
        raise AssertionError("transport-secret-must-never-appear")


def success_response(**changes: object) -> httpx.Response:
    body: dict[str, object] = {
        "execution_id": str(EXECUTION_ID),
        "status": "succeeded",
        "operation": "query.execute",
        "ticket": {
            "key_id": "local-2026-01",
            "signed_payload": "{}",
            "signature": "eA==",
        },
    }
    body.update(changes)
    return httpx.Response(
        200,
        json=body,
        headers={
            "X-AI-Skills-Billing-Currency": "CNY",
            "X-AI-Skills-Billing-Charged": "0.080000",
            "X-AI-Skills-Billing-Balance": "99.920000",
        },
    )


def authorize(transport: httpx.AsyncBaseTransport):
    return PlatformClient(
        api_key=API_KEY,
        transport=transport,
    ).authorize(
        "query.execute",
        INSTALLATION_ID,
        "a" * 64,
        "018f47a2-7b2b-7e47-8794-c11316f5023e",
    )


def test_authorize_sends_only_four_metadata_fields_and_returns_billing_receipt():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "POST"
        assert str(request.url) == (
            "https://sql-data-analyst.invalid/api/v1/sql-data-analyst/executions/authorize"
        )
        assert json.loads(request.content) == {
            "operation": "query.execute",
            "runner_version": "1.0.0",
            "installation_id": str(INSTALLATION_ID),
            "input_fingerprint": "a" * 64,
        }
        assert request.headers["Authorization"] == f"Bearer {API_KEY}"
        assert request.headers["Idempotency-Key"] == (
            "018f47a2-7b2b-7e47-8794-c11316f5023e"
        )
        assert request.extensions["timeout"]["read"] == 15.0
        return success_response()

    receipt = authorize(httpx.MockTransport(handler))

    assert receipt.execution_id == EXECUTION_ID
    assert receipt.ticket.key_id == "local-2026-01"
    assert receipt.currency == "CNY"
    assert receipt.charged_amount == "0.080000"
    assert receipt.balance_after == "99.920000"


def test_client_uses_non_routable_build_origin_and_has_no_origin_override():
    assert PLATFORM_API_ORIGIN == "https://sql-data-analyst.invalid"

    with pytest.raises(TypeError):
        PlatformClient(api_key=API_KEY, api_origin="https://evil.example")


def test_client_rejects_sync_only_transport_with_sanitized_error():
    with pytest.raises(PlatformError, match="^license_unavailable$") as caught:
        PlatformClient(api_key=API_KEY, transport=SyncOnlySecretTransport())

    assert "SyncOnlySecretTransport" not in str(caught.value)
    assert "transport-secret-must-never-appear" not in str(caught.value)
    assert caught.value.__cause__ is None


@pytest.mark.parametrize("status", [301, 302, 307, 308])
def test_authorize_never_follows_redirects_or_leaks_key(status):
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        return httpx.Response(
            status,
            headers={"Location": f"https://evil.example/collect?key={API_KEY}"},
        )

    with pytest.raises(PlatformError, match="^license_unavailable$") as caught:
        authorize(httpx.MockTransport(handler))

    assert seen == [
        "https://sql-data-analyst.invalid/api/v1/sql-data-analyst/executions/authorize"
    ]
    assert API_KEY not in str(caught.value)


def test_authorize_rejects_response_over_64_kib_before_json_parsing():
    transport = httpx.MockTransport(
        lambda request: httpx.Response(
            200,
            content=b"{" + (b"x" * (64 * 1024)),
            headers={"Content-Type": "application/json"},
        )
    )

    with pytest.raises(PlatformError, match="^license_unavailable$"):
        authorize(transport)


def test_authorize_cancels_blocked_body_at_remaining_total_deadline():
    template = success_response()
    stream = BlockingAsyncStream(template.content, chunk_delay=0.02)
    transport = CumulativeDelayTransport(
        httpx.Response(200, headers=template.headers, stream=stream),
        header_delay=0.04,
    )

    started_at = time.monotonic()
    with pytest.raises(PlatformError, match="^license_unavailable$") as caught:
        PlatformClient(
            api_key=API_KEY,
            timeout_seconds=0.1,
            transport=transport,
        ).authorize(
            "query.execute",
            INSTALLATION_ID,
            "a" * 64,
            "018f47a2-7b2b-7e47-8794-c11316f5023e",
        )
    elapsed = time.monotonic() - started_at

    assert transport.sync_calls == 0
    assert transport.async_calls == 1
    assert elapsed < 0.25
    assert stream.chunk_at is not None
    assert stream.cancelled_at is not None
    assert stream.cancelled_at - stream.chunk_at < 0.08
    assert stream.closed
    assert API_KEY not in str(caught.value)
    assert caught.value.__cause__ is None


def test_authorize_rejects_unknown_success_response_fields():
    transport = httpx.MockTransport(
        lambda request: success_response(unexpected=API_KEY)
    )

    with pytest.raises(PlatformError, match="^license_unavailable$") as caught:
        authorize(transport)

    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__ is True


@pytest.mark.parametrize(
    "response",
    [
        httpx.Response(401, json={"error": {"message": API_KEY}}),
        success_response(operation="analysis.run"),
        success_response(status="processing"),
        success_response(),
    ],
)
def test_authorize_maps_remote_or_invalid_billing_failures_without_echoing_key(response):
    if response.status_code == 200 and response.json().get("operation") == "query.execute" and response.json().get("status") == "succeeded":
        response.headers["X-AI-Skills-Billing-Currency"] = "USD"

    with pytest.raises(PlatformError, match="^license_unavailable$") as caught:
        authorize(httpx.MockTransport(lambda request: response))

    assert API_KEY not in str(caught.value)
    assert response.text not in str(caught.value)
