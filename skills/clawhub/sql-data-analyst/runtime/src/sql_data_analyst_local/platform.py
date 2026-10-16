from __future__ import annotations

import asyncio
import json
import re
from typing import Literal
from uuid import UUID

import httpx
from pydantic import ValidationError

from sql_data_analyst_local.contracts import (
    AuthorizationReceipt,
    StrictContract,
    TicketEnvelope,
)
from sql_data_analyst_local.settings import (
    AUTHORIZE_PATH,
    MAX_PLATFORM_RESPONSE_BYTES,
    MAX_PLATFORM_TIMEOUT_SECONDS,
    PLATFORM_API_ORIGIN,
    RUNNER_VERSION,
)


_FINGERPRINT = re.compile(r"^[a-f0-9]{64}$")
_MONEY = re.compile(r"^-?(?:0|[1-9]\d*)\.\d{6}$")
_CHARGE = re.compile(r"^(?:0|[1-9]\d*)\.\d{6}$")
_OPERATIONS = frozenset(
    {
        "dataset.ingest",
        "dataset.inspect",
        "analysis.run",
        "query.execute",
        "report.create",
        "dataset.delete",
    }
)


class PlatformError(RuntimeError):
    """A sanitized platform-boundary error with no response or credential text."""

    def __init__(self, code: str = "license_unavailable") -> None:
        self.code = code
        super().__init__(code)


class _AuthorizationResponse(StrictContract):
    execution_id: UUID
    status: Literal["succeeded"]
    operation: str
    ticket: TicketEnvelope


class PlatformClient:
    def __init__(
        self,
        api_key: str,
        *,
        timeout_seconds: float = MAX_PLATFORM_TIMEOUT_SECONDS,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        if not isinstance(api_key, str) or not api_key.strip():
            raise PlatformError()
        if not 0 < timeout_seconds <= MAX_PLATFORM_TIMEOUT_SECONDS:
            raise PlatformError()
        if transport is not None and not isinstance(
            transport, httpx.AsyncBaseTransport
        ):
            raise PlatformError()
        self._api_key = api_key
        self._timeout_seconds = timeout_seconds
        self._transport = transport
        self._closed = False

    def authorize(
        self,
        operation: str,
        installation_id: UUID,
        input_fingerprint: str,
        idempotency_key: str,
    ) -> AuthorizationReceipt:
        if (
            operation not in _OPERATIONS
            or not isinstance(installation_id, UUID)
            or not isinstance(input_fingerprint, str)
            or _FINGERPRINT.fullmatch(input_fingerprint) is None
            or not isinstance(idempotency_key, str)
            or not 0 < len(idempotency_key.strip()) <= 191
        ):
            raise PlatformError("authorization_invalid")
        if self._closed:
            raise PlatformError()
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            pass
        else:
            raise PlatformError()
        return asyncio.run(
            self._authorize_async(
                operation,
                installation_id,
                input_fingerprint,
                idempotency_key,
            )
        )

    async def _authorize_async(
        self,
        operation: str,
        installation_id: UUID,
        input_fingerprint: str,
        idempotency_key: str,
    ) -> AuthorizationReceipt:
        payload = {
            "operation": operation,
            "runner_version": RUNNER_VERSION,
            "installation_id": str(installation_id),
            "input_fingerprint": input_fingerprint,
        }
        try:
            async with asyncio.timeout(self._timeout_seconds):
                async with httpx.AsyncClient(
                    base_url=PLATFORM_API_ORIGIN,
                    follow_redirects=False,
                    timeout=httpx.Timeout(self._timeout_seconds),
                    transport=self._transport,
                ) as client:
                    async with client.stream(
                        "POST",
                        AUTHORIZE_PATH,
                        json=payload,
                        headers={
                            "Authorization": f"Bearer {self._api_key}",
                            "Idempotency-Key": idempotency_key,
                            "Accept": "application/json",
                        },
                    ) as response:
                        if response.status_code != 200:
                            raise PlatformError()
                        raw = await self._bounded_body(response)
                        parsed = json.loads(raw)
                        result = _AuthorizationResponse.model_validate(parsed)
                        if result.operation != operation:
                            raise PlatformError()
                        currency = response.headers.get(
                            "X-AI-Skills-Billing-Currency"
                        )
                        charged_amount = response.headers.get(
                            "X-AI-Skills-Billing-Charged"
                        )
                        balance_after = response.headers.get(
                            "X-AI-Skills-Billing-Balance"
                        )
                        if (
                            currency != "CNY"
                            or charged_amount is None
                            or _CHARGE.fullmatch(charged_amount) is None
                            or balance_after is None
                            or _MONEY.fullmatch(balance_after) is None
                        ):
                            raise PlatformError()
                        return AuthorizationReceipt(
                            execution_id=result.execution_id,
                            operation=result.operation,
                            ticket=result.ticket,
                            currency=currency,
                            charged_amount=charged_amount,
                            balance_after=balance_after,
                        )
        except PlatformError:
            raise
        except (
            TimeoutError,
            httpx.HTTPError,
            json.JSONDecodeError,
            ValidationError,
            UnicodeError,
        ):
            raise PlatformError() from None

    def close(self) -> None:
        self._closed = True

    def __enter__(self) -> PlatformClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    @staticmethod
    async def _bounded_body(response: httpx.Response) -> bytes:
        content_length = response.headers.get("Content-Length")
        if content_length is not None:
            try:
                if int(content_length) > MAX_PLATFORM_RESPONSE_BYTES:
                    raise PlatformError()
            except ValueError:
                raise PlatformError() from None
        body = bytearray()
        async for chunk in response.aiter_bytes():
            body.extend(chunk)
            if len(body) > MAX_PLATFORM_RESPONSE_BYTES:
                raise PlatformError()
        return bytes(body)
