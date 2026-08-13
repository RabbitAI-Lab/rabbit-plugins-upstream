"""Supplier configuration — a per-service endpoint map, never a base URL.

A PromoStandards supplier does not have "an endpoint". It has a separate
URL *and* an independently-chosen version per service, and the two do not
move together: SanMar publishes Inventory at both 1.2.1 and 2.0.0, Product
Data at 1.0.0 and 2.0.0, and Purchase Order only at 1.0.0, each on its own
path. Any design with a single base URL breaks on the first real supplier,
so the config is a map keyed by service code:

    {
      "supplier": "sanmar",
      "credentials": {"id": "${PS_SANMAR_ID}",
                      "password": "${PS_SANMAR_PASSWORD}"},
      "services": {
        "INV":     {"url": "https://...", "wsVersion": "2.0.0",
                    "testUrl": "https://..."},
        "PRODUCT": {"url": "https://...", "wsVersion": "2.0.0"},
        "PO":      {"url": "https://...", "wsVersion": "1.0.0"}
      }
    }

**Credentials are not part of this object's job.** The config describes
*endpoints*; who you are when calling them comes from the environment,
resolved from `${ENV_VAR}` references at load time. Two deployments fill
that environment differently, but the config itself is identical in both:

1. **Single-tenant** — the host exports the vars at boot and every call
   uses the host's own supplier account.
2. **Multi-tenant (delegated)** — this agent acts on behalf of a calling
   agent, and the platform injects the caller's shared credentials into
   this process's environment for the duration of one turn, before the
   script runs. Nothing in this file changes; the same `${ENV_VAR}`
   reference simply resolves to the caller's value instead of the host's.

Because the process reads the environment at load time and exits when the
call is over, a delegated identity cannot outlive its turn and two callers
cannot share one.

A *literal* secret inside the `credentials` block is rejected, whether that
config came from a file or was passed inline: that block is the shape that
ends up committed.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field

from errors import ConfigError  # noqa: E402  (sibling module)

_ENV_REF = re.compile(r"^\$\{([A-Za-z_][A-Za-z0-9_]*)\}$")

# Canonical internal service codes. The registry spells Product Data as
# "Product" (mixed case) and hands back an empty string for Company Data
# and Remittance Advice, so codes are upper-cased on the way in and the
# empty ones are addressed by name instead.
SERVICE_CODES = {
    "INV": "Inventory",
    "PRODUCT": "Product Data",
    "PPC": "Product Pricing and Configuration",
    "PO": "Purchase Order",
    "OSN": "Order Shipment Notification",
    "ODRSTAT": "Order Status",
    "INVC": "Invoice",
    "MED": "Media Content",
    "PDC": "Product Compliance",
}


def normalize_service(code: str) -> str:
    """Upper-case a service code and map known aliases onto canonical ones."""
    if not code:
        raise ConfigError("empty service code")
    upper = str(code).strip().upper()
    # "PROD" is a common mis-spelling of the registry's "Product".
    return {"PROD": "PRODUCT", "PRODUCTDATA": "PRODUCT"}.get(upper, upper)


def _resolve_secret(value: object, where: str) -> str | None:
    """Resolve a `${VAR}` reference from the environment.

    A value that is not an env reference is refused outright. Accepting a
    literal here would let a working credential be committed to a config
    file, which is the failure this rule exists to prevent — so the error
    names the offending field but never echoes the value.
    """
    if value is None:
        return None
    if not isinstance(value, str):
        raise ConfigError(f"{where} must be a '${{ENV_VAR}}' reference")
    match = _ENV_REF.match(value.strip())
    if not match:
        raise ConfigError(
            f"{where} must be a '${{ENV_VAR}}' reference, not a literal value. "
            "Credentials belong in the environment, never in config files."
        )
    return os.environ.get(match.group(1))


@dataclass
class ServiceEndpoint:
    """One service's URL and version for one supplier."""

    service: str
    url: str
    ws_version: str
    test_url: str | None = None
    status: str | None = None
    #: Per-supplier namespace overrides, merged over the adapter's defaults.
    #: Needed because not every supplier honours the spec's namespace: 3M
    #: serves Inventory 1.2.1 under `http://inventoryservice.promostandards.mmm/`.
    #: Response parsing ignores namespaces anyway, so this only affects the
    #: request side — which is exactly where a non-compliant service rejects us.
    namespaces: dict[str, str] = field(default_factory=dict)

    def resolve_url(self, use_test: bool = False) -> str:
        """Pick the production or test URL.

        Falls back to production when no test URL is registered, and the
        caller is told via `has_test_endpoint` so a PO flow can refuse to
        proceed rather than silently submitting to production.
        """
        if use_test and self.test_url:
            return self.test_url
        return self.url

    @property
    def has_test_endpoint(self) -> bool:
        return bool(self.test_url)


@dataclass
class SupplierConfig:
    supplier: str
    services: dict[str, ServiceEndpoint] = field(default_factory=dict)
    credential_id: str | None = None
    credential_password: str | None = None
    # Names of the env vars the credentials came from, for diagnostics.
    credential_env: dict[str, str] = field(default_factory=dict)
    #: "environment" | "none" — reported by describe() so an operator can
    #: tell whether a call had an identity at all. It cannot distinguish a
    #: host credential from a delegated one, and deliberately does not try:
    #: both arrive as the same env var, and the process is never told which
    #: filled it.
    credential_source: str = "none"

    # -- lookup ------------------------------------------------------------

    def endpoint(self, service: str) -> ServiceEndpoint:
        """Return the endpoint for `service`, or raise NotSupportedError.

        This is the structural check that keeps an unsupported service from
        being discovered by faulting mid-call.
        """
        from errors import NotSupportedError  # local import: avoid cycle

        code = normalize_service(service)
        endpoint = self.services.get(code)
        if endpoint is None:
            raise NotSupportedError(
                f"supplier '{self.supplier}' does not publish service "
                f"'{code}'",
                supplier=self.supplier,
                service=code,
                available=sorted(self.services),
            )
        return endpoint

    def supports(self, service: str) -> bool:
        try:
            return normalize_service(service) in self.services
        except ConfigError:
            return False

    def require_credentials(self) -> tuple[str, str | None]:
        """Return (id, password), raising if the id is unset.

        `password` is `minOccurs="0"` across the specs, so an unset password
        is passed through as absent rather than as an empty string — some
        suppliers accept id-only auth and an empty element is not the same
        as an omitted one.
        """
        if not self.credential_id:
            env = self.credential_env.get("id")
            if env:
                raise ConfigError(
                    f"no credentials for supplier '{self.supplier}': "
                    f"environment variable {env} is not set. On a delegated "
                    "turn this means the calling agent's connection does not "
                    f"share a credential bound to {env}; otherwise the host "
                    "has not exported it."
                )
            raise ConfigError(
                f"no credentials for supplier '{self.supplier}': the config "
                "has no 'credentials' block, so there is no environment "
                "variable to read. Add '${ENV_VAR}' references — provision.py "
                "writes them."
            )
        return self.credential_id, self.credential_password or None

    # -- construction ------------------------------------------------------

    @classmethod
    def from_dict(cls, raw: dict) -> "SupplierConfig":
        if not isinstance(raw, dict):
            raise ConfigError("config must be a JSON object")
        supplier = raw.get("supplier") or raw.get("companyCode")
        if not supplier:
            raise ConfigError("config is missing 'supplier'")

        creds = raw.get("credentials") or {}
        if not isinstance(creds, dict):
            raise ConfigError("'credentials' must be an object")
        cred_env = {}
        for key in ("id", "password"):
            ref = creds.get(key)
            if isinstance(ref, str):
                match = _ENV_REF.match(ref.strip())
                if match:
                    cred_env[key] = match.group(1)

        services_raw = raw.get("services") or {}
        if not isinstance(services_raw, dict):
            raise ConfigError("'services' must be an object keyed by service code")
        if not services_raw:
            raise ConfigError(f"supplier '{supplier}' has no services configured")

        services: dict[str, ServiceEndpoint] = {}
        for code, entry in services_raw.items():
            if not isinstance(entry, dict):
                raise ConfigError(f"service '{code}' must be an object")
            url = entry.get("url")
            version = entry.get("wsVersion") or entry.get("version")
            if not url:
                raise ConfigError(f"service '{code}' is missing 'url'")
            if not version:
                raise ConfigError(f"service '{code}' is missing 'wsVersion'")
            key = normalize_service(code)
            overrides = entry.get("namespaces") or {}
            if not isinstance(overrides, dict):
                raise ConfigError(
                    f"service '{code}': 'namespaces' must be an object "
                    "mapping prefix to URI"
                )
            services[key] = ServiceEndpoint(
                service=key,
                url=str(url),
                ws_version=str(version),
                test_url=entry.get("testUrl") or entry.get("test_url"),
                status=entry.get("status"),
                namespaces={str(k): str(v) for k, v in overrides.items()},
            )

        return cls(
            supplier=str(supplier),
            services=services,
            credential_id=_resolve_secret(creds.get("id"), "credentials.id"),
            credential_password=_resolve_secret(
                creds.get("password"), "credentials.password"
            ),
            credential_env=cred_env,
            credential_source=("environment" if cred_env else "none"),
        )

    @classmethod
    def load(cls, path: str) -> "SupplierConfig":
        try:
            with open(path, encoding="utf-8") as handle:
                raw = json.load(handle)
        except FileNotFoundError as exc:
            raise ConfigError(f"config not found: {path}") from exc
        except json.JSONDecodeError as exc:
            raise ConfigError(f"config is not valid JSON: {path}: {exc}") from exc
        return cls.from_dict(raw)

    def describe(self) -> dict:
        """Non-secret summary, safe to log or return to a caller."""
        return {
            "supplier": self.supplier,
            "services": {
                code: {
                    "url": ep.url,
                    "wsVersion": ep.ws_version,
                    "hasTestEndpoint": ep.has_test_endpoint,
                }
                for code, ep in sorted(self.services.items())
            },
            "credentials": {
                "id": bool(self.credential_id),
                "password": bool(self.credential_password),
                "source": self.credential_source,
                "env": self.credential_env,
            },
        }
