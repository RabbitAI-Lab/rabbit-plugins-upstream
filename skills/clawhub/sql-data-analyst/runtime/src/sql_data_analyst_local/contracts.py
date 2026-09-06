from __future__ import annotations

from typing import Annotated, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, StrictInt


FINGERPRINT_PATTERN = r"^[a-f0-9]{64}$"
KEY_ID_PATTERN = r"^[a-z0-9][a-z0-9._-]{0,63}$"


class StrictContract(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class TicketEnvelope(StrictContract):
    key_id: str = Field(min_length=1, max_length=64, pattern=KEY_ID_PATTERN)
    signed_payload: str
    signature: str


class ExpectedTicket(StrictContract):
    operation: str = Field(min_length=1, max_length=64)
    installation_id: UUID
    input_fingerprint: str = Field(pattern=FINGERPRINT_PATTERN)
    runner_version: str = Field(min_length=1, max_length=64)


class TicketClaims(StrictContract):
    schema_version: Literal[1]
    execution_id: UUID
    operation: str = Field(min_length=1, max_length=64)
    installation_id: UUID
    input_fingerprint: str = Field(pattern=FINGERPRINT_PATTERN)
    billing_units: Annotated[StrictInt, Field(ge=0, le=1)]
    charged_amount: str
    currency: str
    runner_min_version: str
    issued_at: str
    expires_at: str


class AuthorizationReceipt(StrictContract):
    execution_id: UUID
    operation: str
    ticket: TicketEnvelope
    currency: str
    charged_amount: str
    balance_after: str
