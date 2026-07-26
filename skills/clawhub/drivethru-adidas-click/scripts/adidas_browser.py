"""Playwright-driven adidas Click B2B ordering automation (browser surface).

adidas Click exposes no public API, so placing a purchase order means driving
the portal with Playwright. This module is being reverse-engineered from real
HTML **one step at a time** — see ``references/order_flow_notes.md`` for the
captured selectors and the step map. Nothing here invents selectors: a step is
only implemented once its HTML has been captured.

Playwright is an **optional** dependency, imported lazily — the skill loads
fine without it; only :func:`create_purchase_order` needs it (plus a browser
binary, installed via ``python -m playwright install chromium``).

Scope note: each page step is gated behind a ``*_IMPLEMENTED`` flag. Until a
step lands, the driver stops early and returns a structured ``not_implemented``
result rather than guessing at selectors. With ``confirm`` false the driver
fills and validates whatever is implemented and returns a ``dry_run`` preview
without placing an order.
"""

from __future__ import annotations

import atexit
import logging
import os
import re
import secrets
import shutil
import string
import subprocess
import sys
from contextlib import contextmanager
from typing import TYPE_CHECKING

from adidas_client import (  # noqa: E402  (sibling module, scripts dir on sys.path)
    AdidasAPIError,
    AdidasClickCredentials,
    AdidasConfigError,
    AdidasTransportError,
    credentials_from_env,
)
from schemas import (  # noqa: E402  (sibling module)
    CheckLineResult,
    CheckResult,
    OrderLine,
    OrderLineResult,
    OrderRequest,
    OrderResult,
    ShipTo,
)

if TYPE_CHECKING:  # pragma: no cover — typing only
    from playwright.sync_api import Page

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _norm(value: str | None) -> str:
    return (value or "").strip().lower()


def _size_lookup_keys(value: str | None) -> list[str]:
    """Candidate size-bar keys for a requested size, most specific first.

    adidas footwear sizes on the size bar are bare integers plus an ``N-`` form
    for the half size *up* (``13-`` == 13.5). Odoo hands sizes as float-strings
    (``"13.0"``, ``"13.5"``), so map those onto the bar's labels; non-numeric
    sizes (apparel: ``XL``) pass through unchanged.
    """
    norm = _norm(value)
    keys = [norm]
    try:
        number = float(norm)
    except ValueError:
        return keys
    whole = int(number)
    frac = number - whole
    if abs(frac) < 1e-9:
        candidate = str(whole)            # 13.0 -> "13"
    elif abs(frac - 0.5) < 1e-9:
        candidate = f"{whole}-"           # 13.5 -> "13-" (half size up)
    else:
        return keys
    if candidate not in keys:
        keys.append(candidate)
    return keys


def _clean(value: str | None) -> str:
    return " ".join((value or "").split())


def _to_int(value: str | None) -> int | None:
    digits = "".join(ch for ch in (value or "") if ch.isdigit())
    return int(digits) if digits else None


def _parse_available(indicator: str | None) -> int | None:
    """Interpret a size tile's inventory indicator as an available count.

    Returns an int for an exact count (``"0"``, ``"160"``), or None when the
    availability is effectively unbounded/unknown (``"300+"``, blank) — in which
    case the line is treated as sufficiently in stock.
    """

    if not indicator:
        return None
    text = indicator.strip()
    if text.endswith("+"):  # e.g. "300+" — at least this many
        return None
    return _to_int(text)


class _InsufficientStockPause(Exception):
    """Internal signal: some line isn't fully in stock and the policy is 'pause'.

    Carries the out-of-stock summary and a snapshot of all requested lines so
    the entry point can return a ``needs_confirmation`` result without ordering.
    """

    def __init__(self, out_of_stock: list[dict], lines: list["OrderLineResult"]):
        super().__init__("insufficient stock — awaiting confirmation")
        self.out_of_stock = out_of_stock
        self.lines = lines


def _group_by_style(lines: list[OrderLine]) -> dict[str, list[OrderLine]]:
    """Group order lines by article number, preserving first-seen order."""

    grouped: dict[str, list[OrderLine]] = {}
    for line in lines:
        grouped.setdefault(line.style, []).append(line)
    return grouped


# US state / territory 2-letter abbreviation -> the full name adidas Click's
# State dropdown displays. Names must match the dropdown text exactly.
_US_STATE_ABBREV = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "DC": "District of Columbia", "FL": "Florida", "GA": "Georgia",
    "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana",
    "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
    "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan",
    "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana",
    "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
    "NM": "New Mexico", "NY": "New York", "NC": "North Carolina",
    "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
    "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming",
    # Territories / associated states present in the dropdown.
    "AS": "American Samoa", "GU": "Guam", "PR": "Puerto Rico",
    "VI": "Virgin Islands", "MP": "Northern Mariana Isl", "PW": "Palau",
    "MH": "Marshall Islands", "FM": "Fed. st. Micronesia",
}


# adidas Click Customer PO # allows only letters, numbers, space, and / _ . ? &
# (per the field's own validation message). Anything else (e.g. '-') is rejected.
_PO_ALLOWED_RE = re.compile(r"[^A-Za-z0-9 /_.?&]+")


def _sanitize_po_number(po: str) -> tuple[str, bool]:
    """Replace runs of disallowed characters with '_'. Returns (clean, changed)."""

    clean = _PO_ALLOWED_RE.sub("_", po).strip()
    return clean, clean != po


# A pricing check fills a throwaway cart just to reach the priced checkout page,
# then deletes it — but if a run dies mid-flight, the leftover cart / Customer PO
# must scream "do not buy". The Customer PO field is hard-capped at 18 chars and
# only allows letters, numbers, space, and / _ . ? & (see _PO_ALLOWED_RE), so the
# fuller "AUTOMATED CHECK - DO NOT PURCHASE - …" cannot fit; this is the clearest
# imperative that leaves room for a 5-char random suffix (cart names must be
# unique). Override by passing an explicit ``po_number`` to the check.
_CHECK_PO_PREFIX = "DO NOT BUY"
_CHECK_PO_RANDOM_LEN = 5
# Uppercase letters + digits are all inside the PO charset; drop easily-confused
# glyphs so a human reading the marker off the portal isn't misled.
_CHECK_PO_ALPHABET = "".join(
    c for c in (string.ascii_uppercase + string.digits) if c not in "O0I1L"
)


def _generate_check_po() -> str:
    """Build the "DO NOT BUY {rand5}" marker for a check's throwaway cart / PO.

    Fits the 18-char Customer PO limit and the 25-char cart-name limit, and only
    uses characters the PO field accepts, so it passes through the sanitizer
    unchanged.
    """

    rand = "".join(secrets.choice(_CHECK_PO_ALPHABET) for _ in range(_CHECK_PO_RANDOM_LEN))
    return f"{_CHECK_PO_PREFIX} {rand}"


# Map the internal availability classification (used by the order flow, relative
# to a requested quantity) onto the check's stock-facing vocabulary.
_INVENTORY_STATUS = {
    "ok": "in_stock",
    "short": "backorder",  # orderable but 0/low with a restock date
    "unavailable": "unavailable",  # the portal's "X" cell — never orderable
}


_CURRENCY_RE = re.compile(r"([£$€]?)\s*([\d,]+(?:\.\d+)?)")


def _sum_currency(values: list[str | None]) -> str | None:
    """Sum currency-like strings (e.g. '$35.08'), preserving the symbol.

    Returns None if no value parsed.
    """

    total = 0.0
    symbol = "$"
    found = False
    for value in values:
        match = _CURRENCY_RE.search(value or "")
        if match:
            symbol = match.group(1) or symbol
            total += float(match.group(2).replace(",", ""))
            found = True
    return f"{symbol}{total:,.2f}" if found else None


def _unit_price(line_total: str | None, quantity: int | None) -> str | None:
    """Derive a per-unit price from a line total and quantity, same symbol."""

    if not line_total or not quantity:
        return None
    match = _CURRENCY_RE.search(line_total)
    if not match:
        return None
    symbol = match.group(1) or "$"
    value = float(match.group(2).replace(",", ""))
    return f"{symbol}{value / quantity:,.2f}"


def _install_chromium() -> None:
    """Download Playwright's Chromium browser binary (one-time, ~150 MB)."""

    subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        check=True,
    )


def _launch_chromium(playwright, headless: bool):
    """Launch Chromium, auto-installing the browser binary if it is missing.

    The Playwright *package* is a declared dependency, but its Chromium *binary*
    is a separate ~150 MB download that pip/uv does not fetch. There is no
    OpenClaw install-time hook for it, so on the first run — if the binary is
    absent — we install it once and retry, rather than requiring a manual
    `python -m playwright install chromium`.
    """

    try:
        return playwright.chromium.launch(headless=headless, args=_STEALTH_LAUNCH_ARGS)
    except Exception as exc:  # noqa: BLE001
        message = str(exc).lower()
        looks_missing = (
            "executable doesn't exist" in message
            or "playwright install" in message
            or "browsertype.launch" in message
            and "download" in message
        )
        if not looks_missing:
            raise AdidasConfigError(
                "Could not launch a Chromium browser for Playwright "
                f"(underlying error: {exc})."
            ) from exc
        logger.info("Chromium binary missing — installing it once (~150 MB)…")
        try:
            _install_chromium()
        except Exception as install_exc:  # noqa: BLE001
            raise AdidasConfigError(
                "Chromium is not installed and the automatic install failed. Run "
                "`python -m playwright install chromium` manually. (install error: "
                f"{install_exc})"
            ) from install_exc
        try:
            return playwright.chromium.launch(headless=headless, args=_STEALTH_LAUNCH_ARGS)
        except Exception as retry_exc:  # noqa: BLE001
            raise AdidasConfigError(
                "Could not launch Chromium even after installing it. Run "
                "`python -m playwright install chromium` and check the container "
                f"has the required system libraries. (error: {retry_exc})"
            ) from retry_exc


def _stop_process(proc) -> None:
    """Terminate a spawned helper process (best effort)."""
    if not proc or proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except Exception:  # noqa: BLE001
        proc.kill()


def _headed_needs_virtual_display() -> bool:
    """True only when a headed browser must fall back to an Xvfb virtual display.

    The virtual display is an **X11 (Linux) workaround** for a host with no
    display server — e.g. a headless cloud container. Windows and macOS render a
    headed browser on their native GUI and have no ``DISPLAY`` concept at all, so
    they must **never** try to start Xvfb (doing so wrongly demanded the `xvfb`
    package on Windows). On Linux we still only need it when no display is
    already present — neither an X11 ``DISPLAY`` nor a Wayland session.
    """

    if not sys.platform.startswith("linux"):
        return False  # Windows / macOS: native display, Xvfb is irrelevant.
    return not (os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"))


def _start_virtual_display():
    """Start an Xvfb virtual display for a headed browser on a **Linux** host with
    no X server and point ``$DISPLAY`` at it; return the Xvfb process (register it
    for teardown) or raise ``AdidasConfigError`` if the Xvfb binary is missing.
    Only ever called when :func:`_headed_needs_virtual_display` is true.

    adidas Click's Akamai edge stalls headless Chromium, so the working path is
    a *headed* browser on a virtual display. We spawn ``Xvfb`` directly rather
    than via ``xvfb-run`` so we don't depend on ``xauth`` (minimal images ship
    neither ``xvfb`` nor ``xauth``). ``-displayfd`` lets Xvfb choose a free
    display and report it back once the server is ready — that doubles as a
    readiness signal and avoids display-number collisions across runs.
    """
    xvfb = shutil.which("Xvfb")
    if not xvfb:
        raise AdidasConfigError(
            "Headed mode needs a virtual display, but the Xvfb binary is not "
            "installed. Install it (`apt-get install -y xvfb`) or set "
            "ADIDAS_CLICK_HEADLESS=true to run headless (note: adidas's WAF "
            "stalls headless Chromium)."
        )
    read_fd, write_fd = os.pipe()
    try:
        proc = subprocess.Popen(
            [xvfb, "-displayfd", str(write_fd),
             "-screen", "0", "1440x900x24", "-nolisten", "tcp"],
            pass_fds=(write_fd,),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    finally:
        os.close(write_fd)
    with os.fdopen(read_fd) as handle:
        display_num = handle.readline().strip()
    if not display_num or proc.poll() is not None:
        _stop_process(proc)
        raise AdidasConfigError(
            "Could not start an Xvfb virtual display for headed Chromium."
        )
    os.environ["DISPLAY"] = f":{display_num}"
    logger.info("Started Xvfb virtual display :%s for headed Chromium", display_num)
    return proc


def _insufficient_stock_message(out_of_stock: list[dict]) -> str:
    """Human-readable summary + the choices for a needs_confirmation result."""

    parts = []
    for s in out_of_stock:
        if s.get("status") == "unavailable":
            parts.append(f"{s['style']} size {s['size']} — not available (cannot be ordered)")
        else:
            parts.append(
                f"{s['style']} size {s['size']} — requested {s['requested']}, "
                f"available {s['available'] or 0}"
            )
    has_unavailable = any(s.get("status") == "unavailable" for s in out_of_stock)
    msg = (
        f"{len(out_of_stock)} line(s) are not fully in stock, so the order was "
        f"NOT placed: {'; '.join(parts)}. Confirm how to proceed, then re-run: "
        "order the backorderable line(s) with delayed delivery "
        "(on_insufficient_stock='order'); remove the out-of-stock line(s) and "
        "order the rest (on_insufficient_stock='skip'); or substitute (edit the "
        "order's lines) and re-run."
    )
    if has_unavailable:
        msg += (
            " NOTE: 'not available' sizes will never be restocked and can only "
            "be removed or substituted — 'order' cannot place them."
        )
    return msg


def _resolve_state_name(state: str) -> str:
    """Map a 2-letter US state abbreviation to adidas's full name; pass through
    a value that is already a full name."""

    s = (state or "").strip()
    if len(s) == 2 and s.upper() in _US_STATE_ABBREV:
        return _US_STATE_ABBREV[s.upper()]
    return s


# ---------------------------------------------------------------------------
# Step gates — flip to True as each step's HTML is captured and implemented.
# Mirrors the step map in references/order_flow_notes.md.
# ---------------------------------------------------------------------------

LOGIN_IMPLEMENTED = True            # Step 1 — login
ADD_LINES_IMPLEMENTED = True        # Step 2 — product nav, size map, qty entry
CHECKOUT_IMPLEMENTED = True         # Step 3 — PO number + delivery + shipping
FINAL_SUBMIT_IMPLEMENTED = True     # Step 4 — Next → Calc Net Price → Order Now

_DEFAULT_TIMEOUT_MS = 30_000
# Navigation gets more headroom than ordinary actions: adidas sits behind
# Akamai Bot Manager and the login flow can redirect a few times before the
# authenticated app shell paints.
_NAV_TIMEOUT_MS = 60_000
# Present an ordinary desktop-Chrome fingerprint. adidas Click's Akamai edge
# withholds (stalls to timeout) the HTTP response for clients that look
# automated — a default headless Chromium advertises a "HeadlessChrome" user
# agent and navigator.webdriver=true and gets tarpitted even though the network
# path is fine (a browser-UA curl to the same host returns 200 in <1s).
# Override via ADIDAS_CLICK_USER_AGENT.
_DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)
# Drop the "Chrome is being controlled by automated test software" banner and
# the navigator.webdriver signal at the browser level.
_STEALTH_LAUNCH_ARGS = ["--disable-blink-features=AutomationControlled"]
_LOGIN_PATH = "/login"

# "You're logged in" tell: always-visible elements of the authenticated app
# shell (the login page has none of them). NOTE: the Logout link lives inside a
# collapsed account dropdown, so it is present but hidden — not a reliable
# *visible* tell. These header nav / search controls are always visible.
_LOGGED_IN_MARKER = (
    "#ReorderNavLink, #CartOverviewNavLink, #HeaderSearchButtonButton, "
    "#PersonalNavigationDropdownLabel"
)

# Carts side panel — create a fresh cart per run so shared/existing carts are
# never touched. New Cart opens a name form (the cart name IS the Customer PO /
# personalReference); saving creates it and switches the active cart.
_CARTS_PANEL_BUTTON = "#HeaderCartsTileButton"
_CARTS_LIST = ".o-headerCartsList"  # container of the ag-grid carts list
_CREATE_NEW_CART_BUTTON = "#CreateNewCartButton"
_EDIT_CART_FORM = "form.o-editCartForm"
_EDIT_CART_NAME_INPUT = "form.o-editCartForm input.m-input__field"
_EDIT_CART_SAVE_BUTTON = "#EditCartSaveButton"
_CART_NAME_MAX_LEN = 25  # the cart-name field allows more than the PO field (18)
# Deleting an existing cart with the same PO name (ticking its row checkbox
# reveals the mass-actions trash button; then confirm "Yes").
_DELETE_SELECTED_CARTS_BUTTON = "#DeleteAllCartsButton"
_DELETE_CART_CONFIRM_BUTTON = "#DeleteCartConfirmButton"

# Header search (collapsed by default: click the magnifier to expand, then the
# input appears and the submit button enables once text is entered).
_SEARCH_OPEN_BUTTON = "#HeaderSearchButtonButton"
_SEARCH_INPUT = "#HeaderSearchSearchInput"
_SEARCH_SUBMIT_BUTTON = "#HeaderSearchSubmitButton"

# Product page. adidas article numbers encode the color, so navigating straight
# to the product URL lands on the right color with no color picker.
_PRODUCT_PATH = "/adidas/reorder/product/{style}"

# Cart / checkout. /adidas/reorder/cart opens the *active* cart. Quantities that
# overflow availability (when spread is declined) go to a separate, inactive
# cart, so the active cart holds the order we are checking out.
_CART_PATH = "/adidas/reorder/cart"
_CART_HEADER = "#CartModule-CartHeader"
_PO_FIELD = "#CartModule-PersonalReference-InputField input"  # maxlength 18
_PO_MAX_LEN = 18
_DELIVERY_DROPDOWN_LABEL = "#DeliveryAddressOptionsDropdownLabel"
_DELIVERY_DROPDOWN_CONTENT = "#DeliveryAddressOptionsDropdownContent"
_ADD_ONE_TIME_BUTTON = "#DeliveryAddressAddOneTimeShipToButton"
_ONE_TIME_FORM = "#CartModule-DeliveryAddress-OneTimeShipToAddressForm"
_ONE_TIME_SUBMIT = "#DeliveryAddressFormSubmitButton"
_STATE_DROPDOWN_LABEL = "#StateInputFieldDropdownLabel"
_STATE_DROPDOWN_CONTENT = "#StateInputFieldDropdownContent"
_SHIPPING_DROPDOWN_LABEL = "#ShippingMethodsOptionsDropdownLabel"
_SHIPPING_DROPDOWN_CONTENT = "#ShippingMethodsOptionsDropdownContent"
# Shipping-method option codes (stable id suffix #OptionButton{CODE}Button).
_SHIPPING_METHOD_CODES = (
    "DFLT",  # Default
    "FDGP",  # FedEx Ground
    "FDGR",  # FedEx Ground Residential Only
    "FEDE",  # FedEx 2 Day
    "FEDZ",  # FedEx 2 Day Residential Only
    "FED4",  # FedEx 3 Day
    "FESO",  # FedEx Next Business Day
    "FEDN",  # FedEx Next Business Day 10:30
    "FEDY",  # FedEx Next Business Day Residential Only
    "FEDB",  # FedEx Saturday Delivery
)

# Checkout / submit (Step 4).
_CHECKOUT_PATH = "/adidas/reorder/checkout"
_CHECKOUT_NEXT_BUTTON = "#CartModuleCheckoutProgressNPCButton"  # cart -> checkout
# "Calc. Net Price" applies our wholesale discounts and MUST finish before
# ordering — it is slow. In the summary-table header (also per-row). When it
# completes, the button is replaced by a "Done!" message in the header cell.
_CALC_NET_PRICE_BUTTON = "#NPCCartSimulation"
_CALC_DONE_TEXT = "Done!"
_CALC_TIMEOUT_MS = 120_000  # net-price simulation is slow
_ORDER_NOW_BUTTON = "#CartModuleCheckoutProgressBarSubmitOrderButton"
# Order Now auto-redirects to /adidas/reorder/order/{number}/confirmation.
_CONFIRMATION_URL_GLOB = "**/adidas/reorder/order/*/confirmation"
_CONFIRMATION_URL_RE = re.compile(r"/adidas/reorder/order/([^/]+)/confirmation")

# Size table (stable id prefixes; the hashed `*--xxxx` CSS-module classes are
# volatile and deliberately NOT used).
_SIZE_TABLE = "#CartModule-SizeTable"
# The size row scrolls horizontally; off-screen sizes lazy-load when the
# forward/back arrows are clicked (ids carry a dynamic conversion-group number).
_SIZE_NAV_FORWARD = '[id^="CartModuleSizeBarNavigationForward"]'
_SIZE_NAV_BACK = '[id^="CartModuleSizeBarNavigationBack"]'
# Size-label -> numeric-code map lives in the size-bar header cells:
#   #CartModule-SizeBar-SizeTranslation-{group}-{code}  ->  <ins>{label}</ins>
_SIZE_TRANSLATION_PREFIX = "CartModule-SizeBar-SizeTranslation-"
# Per-style, per-size tiles carry the article number + numeric code:
#   quantities cell:  #CartModule-SizeTile-{style}-{code}
#   inventory text:   #CartModule-SizeTile-InventoryIndicator-{style}-{code}
#   material total:   #CartModule-MaterialRow-Summary-TotalQuantity-{style}
#   product name:     #CartModule-TinyProduct-{style}-ProductName


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


class AdidasClickDriver:
    """Drives the adidas Click portal to place one purchase order.

    Methods are filled in as each step's HTML is captured. Until then they
    raise :class:`AdidasConfigError` pointing at the flow-notes doc, so a
    premature run fails loudly instead of acting on invented selectors.
    """

    def __init__(self, page: "Page", base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")
        # Populated from the review page during complete_submission.
        self.order_total: str | None = None
        self.line_net_prices: list[str | None] = []

    # -- cart management --------------------------------------------------

    def create_new_cart(self, name: str) -> int:
        """Delete any pre-existing cart named ``name``, then create a fresh cart
        named ``name`` and activate it.

        adidas Click allows multiple carts; on a shared account this guarantees
        the run never adds to (or checks out) someone else's cart. Cart names
        must be **unique**, so a same-named leftover (e.g. from an errored prior
        run) is deleted **first**. The active cart cannot be deleted, so if the
        leftover is active, a different cart is activated before deleting it.
        The cart name is the Customer PO (personalReference). Returns the number
        of pre-existing same-named carts deleted.
        """

        self._ensure_carts_panel_open()
        deleted = self._delete_carts_named(name)

        # New Cart control returns once the mass-actions bar clears after a
        # delete (do not toggle the panel button here — that would close it).
        self.page.wait_for_selector(
            _CREATE_NEW_CART_BUTTON, state="visible", timeout=_DEFAULT_TIMEOUT_MS
        )
        self.page.click(_CREATE_NEW_CART_BUTTON)

        name_input = self.page.locator(_EDIT_CART_NAME_INPUT)
        name_input.wait_for(state="visible", timeout=_DEFAULT_TIMEOUT_MS)
        name_input.fill(name[:_CART_NAME_MAX_LEN])
        # Save enables once the name is valid + unique; fail fast + clear if not.
        try:
            self.page.wait_for_selector(
                f"{_EDIT_CART_SAVE_BUTTON}:not([disabled])", timeout=10_000
            )
        except Exception as exc:  # noqa: BLE001
            raise AdidasAPIError(
                f"Could not save the new cart {name!r} — the Save button stayed "
                "disabled (a cart with this name may still exist, or the name is "
                "invalid)."
            ) from exc
        self.page.click(_EDIT_CART_SAVE_BUTTON)
        try:
            self.page.wait_for_selector(
                _EDIT_CART_FORM, state="detached", timeout=_DEFAULT_TIMEOUT_MS
            )
        except Exception:  # noqa: BLE001 — form may just hide; continue
            pass
        self.page.wait_for_load_state("networkidle")
        return deleted

    def _ensure_carts_panel_open(self) -> None:
        """Open the carts side panel if it is not already showing."""

        if self.page.locator(_CREATE_NEW_CART_BUTTON).is_visible():
            return
        self.page.click(_CARTS_PANEL_BUTTON)
        self.page.wait_for_selector(
            _CREATE_NEW_CART_BUTTON, state="visible", timeout=_DEFAULT_TIMEOUT_MS
        )
        self.page.wait_for_load_state("networkidle")  # let the carts grid render

    def _cart_rows(self) -> list[dict]:
        """Snapshot the carts list: row-id, name (title), active flag, toggle id."""

        rows = self.page.locator(f'{_CARTS_LIST} div[role="row"]')
        out: list[dict] = []
        for i in range(rows.count()):
            row = rows.nth(i)
            row_id = row.get_attribute("row-id")
            if not row_id:
                continue
            link = row.locator("a.a-link")
            title = link.first.get_attribute("title") if link.count() else None
            toggle = row.locator('div.a-toggle[id$="ToggleActiveCartToggle"]')
            toggle_id = toggle.first.get_attribute("id") if toggle.count() else None
            out.append(
                {
                    "row_id": row_id,
                    "title": title,
                    "is_active": row.locator(".o-activeBadge").count() > 0,
                    "toggle_id": toggle_id,
                }
            )
        return out

    def _delete_carts_named(self, name: str) -> int:
        """Delete every cart named ``name`` in the (open) panel. Returns the count.

        Matches by name (== Customer PO), so only carts with this exact PO are
        touched. If a same-named cart is the active one, a different cart is
        activated first (the active cart cannot be deleted).
        """

        rows = self._cart_rows()
        old_ids = [r["row_id"] for r in rows if r["title"] == name]
        if not old_ids:
            return 0

        if any(r["is_active"] for r in rows if r["title"] == name):
            others = [
                r for r in rows if r["row_id"] not in set(old_ids) and r["toggle_id"]
            ]
            if not others:
                raise AdidasConfigError(
                    f"The active cart is a leftover named {name!r} and there is "
                    "no other cart to switch to, so it can't be auto-deleted. "
                    "Empty or rename it in the portal, or pass new_cart:false."
                )
            self.page.locator(f'[id="{others[0]["toggle_id"]}"]').click()
            self.page.wait_for_load_state("networkidle")

        return self._delete_cart_rows(old_ids)

    def _delete_cart_rows(self, row_ids: list[str]) -> int:
        """Tick the given (inactive) cart rows and delete them. Returns the count."""

        for row_id in row_ids:
            checkbox = self.page.locator(
                f'div[role="row"][row-id="{row_id}"] input.ag-checkbox-input'
            ).first
            checkbox.check()

        self.page.wait_for_selector(
            _DELETE_SELECTED_CARTS_BUTTON, state="visible", timeout=_DEFAULT_TIMEOUT_MS
        )
        self.page.click(_DELETE_SELECTED_CARTS_BUTTON)
        self.page.wait_for_selector(
            _DELETE_CART_CONFIRM_BUTTON, state="visible", timeout=_DEFAULT_TIMEOUT_MS
        )
        self.page.click(_DELETE_CART_CONFIRM_BUTTON)
        self.page.wait_for_load_state("networkidle")
        return len(row_ids)

    # -- Step 1: auth -----------------------------------------------------

    def login(self, credentials: AdidasClickCredentials) -> None:
        """Log into adidas Click via the standard username/password form.

        The login page (``/login``) posts ``#loginFormDsk`` to ``/login``. We
        fill the visible fields and click the real "Login" button
        (``#send2Dsk``) so any JS validation + CSRF hidden fields come along —
        the "Single Sign On for Sales Managers" path (``#send2SSO``) is a
        separate identity-provider flow we do not use here.
        """

        self.page.goto(self.base_url + _LOGIN_PATH, wait_until="domcontentloaded")
        try:
            self.page.wait_for_selector("#loginFormDsk", timeout=_DEFAULT_TIMEOUT_MS)
            self.page.fill("#usernameField", credentials.username)
            self.page.fill("#passwordField", credentials.password)
            # Leave "Remember me" (#form-reminder) unchecked.
            self.page.click("#send2Dsk")
        except Exception as exc:  # noqa: BLE001 — surface as transport
            raise AdidasTransportError(
                f"Could not submit the adidas Click login form: {exc}"
            )
        self.page.wait_for_load_state("networkidle")

        # Bad credentials: the form flips #login-error-alert visible in place
        # (JS, no navigation). An SSO misconfig surfaces on #sso-login-error-alert.
        if self._login_error_visible():
            raise AdidasConfigError(
                "adidas Click login failed — check ADIDAS_CLICK_USERNAME / "
                "ADIDAS_CLICK_PASSWORD. (The 'Single Sign On for Sales Managers' "
                "path is separate and not used by this skill.)"
            )
        # Success tell: a valid login lands on the re-order home and the
        # authenticated header renders. Wait for an always-visible shell control
        # (not the Logout link, which is hidden inside a collapsed dropdown).
        try:
            self.page.wait_for_selector(
                _LOGGED_IN_MARKER, state="visible", timeout=_DEFAULT_TIMEOUT_MS
            )
        except Exception as exc:  # noqa: BLE001
            raise AdidasConfigError(
                "adidas Click login did not complete — the authenticated header "
                "did not appear. The account may require SSO, or an interstitial "
                "is blocking the flow."
            ) from exc

    def _login_error_visible(self) -> bool:
        for selector in ("#login-error-alert", "#sso-login-error-alert"):
            try:
                if self.page.locator(selector).is_visible():
                    return True
            except Exception:  # noqa: BLE001
                continue
        return False

    # -- search -----------------------------------------------------------

    def _search_style(self, style: str) -> None:
        """Open the header search, enter a style number, and submit.

        The header search is collapsed by default — the input is revealed by
        the magnifier button (:data:`_SEARCH_OPEN_BUTTON`). The submit button
        (:data:`_SEARCH_SUBMIT_BUTTON`) is disabled until text is present.
        """

        field = self.page.locator(_SEARCH_INPUT)
        if not field.is_visible():
            self.page.click(_SEARCH_OPEN_BUTTON)
            field.wait_for(state="visible", timeout=_DEFAULT_TIMEOUT_MS)
        field.fill(style)
        self.page.click(_SEARCH_SUBMIT_BUTTON)
        self.page.wait_for_load_state("networkidle")

    # -- Step 2: add product lines ---------------------------------------

    def add_lines(self, request: OrderRequest) -> list["OrderLineResult"]:
        """Enter quantities for each requested {style, size, quantity}.

        First reads availability for every line (opening each product once), then
        applies the ``on_insufficient_stock`` policy for any line whose full
        quantity is not available:

        - ``pause`` (default): raise :class:`_InsufficientStockPause` — the entry
          point returns ``needs_confirmation`` and **nothing is ordered**.
        - ``order``: enter it anyway, accepting delayed delivery (spread).
        - ``skip``: do not enter it (removed from the order); order the rest.

        Lines are grouped by style so each product page is opened once; adidas
        encodes color in the article number, so no color selection is needed.
        """

        policy = (request.on_insufficient_stock or "pause").strip().lower()
        if policy not in {"pause", "order", "skip"}:
            raise AdidasConfigError(
                f"on_insufficient_stock must be 'pause', 'order', or 'skip'; "
                f"got {request.on_insufficient_stock!r}."
            )

        prepared = self._prepare_lines(request)

        problems = [p for p in prepared if p["status"] != "ok"]
        if policy == "pause" and problems:
            raise _InsufficientStockPause(
                out_of_stock=[self._shortfall_dict(p) for p in problems],
                lines=[
                    self._prepared_result(p, note=self._status_note(p))
                    for p in prepared
                ],
            )

        results: list[OrderLineResult] = []
        current_style: str | None = None
        entered_any = False
        for p in prepared:
            status, style, line, code = p["status"], p["style"], p["line"], p["code"]

            # "Not available" sizes can never be ordered (no quantity input) —
            # drop them under every policy, with a clear note.
            if status == "unavailable":
                results.append(
                    self._prepared_result(
                        p, quantity=0, note="not available — cannot be ordered"
                    )
                )
                continue

            if status == "short" and policy == "skip":
                results.append(
                    self._prepared_result(
                        p,
                        quantity=0,
                        note=(
                            f"removed — out of stock (requested {line.quantity}, "
                            f"available {p['indicator'] or 0})"
                        ),
                    )
                )
                continue

            if style != current_style:
                self._open_product(style)
                current_style = style
            spread = request.spread_delivery or (status == "short" and policy == "order")
            committed = self._set_size_quantity(style, code, line.quantity, spread)
            entered_any = True

            note = None
            if status == "short" and policy == "order":
                note = (
                    f"ordered with delayed delivery (requested {line.quantity}, "
                    f"available {p['indicator'] or 0})"
                )
            elif committed is not None and committed != line.quantity:
                note = f"committed {committed} of {line.quantity} requested"
            results.append(
                self._prepared_result(
                    p,
                    quantity=committed if committed is not None else line.quantity,
                    note=note,
                )
            )

        if not entered_any:
            raise AdidasConfigError(
                "No lines could be ordered — every requested size was out of "
                "stock or unavailable."
            )
        return results

    def _prepare_lines(self, request: OrderRequest) -> list[dict]:
        """Resolve each line to its size code and classify availability.

        Opens each product once; scrolls the horizontal size row to bring each
        requested size into view (it lazy-loads). Classifies each size as:
        ``ok`` (enough stock), ``short`` (orderable but < requested — e.g. 0 with
        a restock date), or ``unavailable`` (the "not available" / X cell, which
        can never be ordered). Raises if a requested size is not offered at all.
        """

        prepared: list[dict] = []
        for style, lines in _group_by_style(request.lines).items():
            self._open_product(style)
            product_name = self._read_product_name(style)
            code_map = self._size_code_map()
            for line in lines:
                code = next(
                    (code_map[key] for key in _size_lookup_keys(line.size)
                     if key in code_map),
                    None,
                )
                if code is None:
                    raise AdidasAPIError(
                        f"Size {line.size!r} is not offered for {style}. "
                        f"Available sizes: {', '.join(sorted(code_map)) or '(none read)'}."
                    )
                status, indicator, available = self._classify_size(
                    style, code, line.quantity
                )
                prepared.append(
                    {
                        "style": style,
                        "line": line,
                        "code": code,
                        "product_name": product_name,
                        "indicator": indicator,
                        "available": available,
                        "status": status,
                    }
                )
        return prepared

    def _classify_size(
        self, style: str, code: str, requested: int
    ) -> tuple[str, str | None, int | None]:
        """Return (status, indicator, available) for one size after scrolling it
        into view. status ∈ {"ok", "short", "unavailable"}."""

        if not self._ensure_size_in_view(style, code):
            return "unavailable", None, None
        not_available = self.page.locator(
            f"#CartModule-SizeTile-Status-NotAvailable-{style}-{code}"
        )
        if not_available.count() > 0:
            return "unavailable", None, None
        indicator = self._read_inventory(style, code)
        available = _parse_available(indicator)
        if available is not None and available < requested:
            return "short", indicator, available
        return "ok", indicator, available

    def _ensure_size_in_view(self, style: str, code: str) -> bool:
        """Scroll the horizontal size row until this size's cell is loaded.

        Off-screen sizes lazy-load via the row's forward/back arrows. Resets to
        the leftmost, then scans forward. Returns True if the size's wrapper cell
        (``#CartModule-SizeRow-SizeTile-Wrapper-{style}-{code}``) is present.
        """

        wrapper = f"#CartModule-SizeRow-SizeTile-Wrapper-{style}-{code}"
        if self.page.locator(wrapper).count() > 0:
            return True

        back = self.page.locator(_SIZE_NAV_BACK).first
        forward = self.page.locator(_SIZE_NAV_FORWARD).first
        # Reset to the leftmost sizes.
        for _ in range(20):
            try:
                if back.count() == 0 or not back.is_enabled():
                    break
            except Exception:  # noqa: BLE001
                break
            back.click()
            self.page.wait_for_timeout(200)
            if self.page.locator(wrapper).count() > 0:
                return True
        # Scan forward through the size run.
        for _ in range(20):
            if self.page.locator(wrapper).count() > 0:
                return True
            try:
                if forward.count() == 0 or not forward.is_enabled():
                    break
            except Exception:  # noqa: BLE001
                break
            forward.click()
            self.page.wait_for_timeout(250)
        return self.page.locator(wrapper).count() > 0

    @staticmethod
    def _shortfall_dict(p: dict) -> dict:
        return {
            "style": p["style"],
            "size": p["line"].size,
            "requested": p["line"].quantity,
            "available": p["indicator"],
            "status": p["status"],  # "short" (backorderable) or "unavailable"
        }

    @staticmethod
    def _status_note(p: dict) -> str | None:
        if p["status"] == "unavailable":
            return "not available — cannot be ordered"
        if p["status"] == "short":
            return (
                f"out of stock — requested {p['line'].quantity}, "
                f"available {p['indicator'] or 0}"
            )
        return None

    @staticmethod
    def _prepared_result(
        p: dict, *, quantity: int | None = None, note: str | None = None
    ) -> "OrderLineResult":
        line = p["line"]
        return OrderLineResult(
            style=p["style"],
            color=line.color or (p["product_name"] or ""),
            size=line.size,
            quantity=quantity if quantity is not None else line.quantity,
            available=p["indicator"],
            note=note,
        )

    # -- product page -----------------------------------------------------

    def _open_product(self, style: str) -> None:
        """Navigate straight to a style's product page and await the size table.

        The size grid sits below the fold and **lazy-renders its per-size tiles
        only when scrolled into view**, so after the table container appears we
        scroll it into view and wait for this style's tiles to attach.
        """

        url = self.base_url + _PRODUCT_PATH.format(style=style)
        self.page.goto(url, wait_until="domcontentloaded")
        try:
            self.page.wait_for_selector(_SIZE_TABLE, timeout=_DEFAULT_TIMEOUT_MS)
        except Exception as exc:  # noqa: BLE001
            raise AdidasAPIError(
                f"Could not open the product page for {style!r} — the size table "
                "did not render. Check the article number (it must include the "
                "color, e.g. JW4306)."
            ) from exc
        self._ensure_size_tiles_rendered(style)

    def _ensure_size_tiles_rendered(self, style: str) -> None:
        """Scroll the size grid into view so its per-size tiles render, then wait.

        Tiles (``#CartModule-SizeTile-{style}-{code}``) mount lazily when the
        grid enters the viewport. Scroll it to center; if the tiles still are
        not attached, nudge-scroll down while polling; finally wait explicitly.
        """

        tile_selector = f'[id^="CartModule-SizeTile-{style}-"]'
        if self.page.locator(tile_selector).count() > 0:
            return

        self.page.evaluate(
            "(sel) => { const el = document.querySelector(sel);"
            " if (el) el.scrollIntoView({block: 'center'}); }",
            _SIZE_TABLE,
        )
        try:
            self.page.wait_for_selector(
                tile_selector, state="attached", timeout=8_000
            )
            return
        except Exception:  # noqa: BLE001 — fall back to nudge-scrolling
            pass

        for _ in range(12):
            self.page.mouse.wheel(0, 500)
            self.page.wait_for_timeout(250)
            if self.page.locator(tile_selector).count() > 0:
                return
        self.page.wait_for_selector(
            tile_selector, state="attached", timeout=_DEFAULT_TIMEOUT_MS
        )

    def _read_product_name(self, style: str) -> str | None:
        try:
            name = self.page.locator(
                f"#CartModule-TinyProduct-{style}-ProductName"
            ).first.inner_text()
            return _clean(name) or None
        except Exception:  # noqa: BLE001
            return None

    def _size_code_map(self) -> dict[str, str]:
        """Build a ``{size_label_lower: numeric_code}`` map from the size bar.

        Reads the header translation cells (``…-SizeTranslation-{group}-{code}``
        with the label in an ``<ins>``). Assumes one conversion group per
        product page (true for a single article).
        """

        cells = self.page.locator(f'[id^="{_SIZE_TRANSLATION_PREFIX}"]')
        out: dict[str, str] = {}
        for i in range(cells.count()):
            cell = cells.nth(i)
            cid = cell.get_attribute("id") or ""
            code = cid.rsplit("-", 1)[-1]
            label = _norm(cell.inner_text())
            if code and label:
                out[label] = code
        return out

    def _read_inventory(self, style: str, code: str) -> str | None:
        """Return the inventory-indicator text for a size (e.g. '300+', '160', '0')."""

        try:
            text = self.page.locator(
                f"#CartModule-SizeTile-InventoryIndicator-{style}-{code}"
            ).first.inner_text()
            return _clean(text) or None
        except Exception:  # noqa: BLE001
            return None

    def _set_size_quantity(
        self, style: str, code: str, quantity: int, spread_delivery: bool
    ) -> int | None:
        """Enter a quantity into one size tile and return the committed value.

        Clicking the tile opens a shared floating overlay (``#quantityInput``)
        that repositions over the active cell; its field is a react-numeric
        input with no id of its own (``#quantityInput input``). Typing a value
        and pressing Enter commits it — the overlay closes and the ordered
        quantity renders in ``#CartModule-SizeTile-OrderedInDate-{style}-{code}``.
        If the requested quantity exceeds availability, an "Insufficient
        availability" proposal offers to spread it over dates.
        """

        self._ensure_size_in_view(style, code)
        tile = self.page.locator(f"#CartModule-SizeTile-{style}-{code}")
        tile.scroll_into_view_if_needed()
        tile.click()

        overlay = self.page.locator("#quantityInput")
        overlay.wait_for(state="visible", timeout=_DEFAULT_TIMEOUT_MS)
        field = overlay.locator("input")
        field.fill(str(quantity))
        field.press("Enter")

        self._handle_availability_proposal(spread_delivery)
        return self._read_ordered_quantity(style, code)

    def _handle_availability_proposal(self, spread_delivery: bool) -> None:
        """Resolve the "Insufficient availability" spread-delivery dialog if shown.

        Default (``spread_delivery`` false) declines → a single delivery. True
        accepts the spread across the proposed future dates.
        """

        proposal = self.page.locator("#CartModule-SizeItemProposals")
        try:
            proposal.wait_for(state="visible", timeout=2_000)
        except Exception:  # noqa: BLE001 — no proposal appeared; nothing to do
            return
        button = (
            "#CartModuleSpreadAcceptButton"
            if spread_delivery
            else "#CartModuleSpreadDeclineButton"
        )
        try:
            self.page.click(button)
            proposal.wait_for(state="hidden", timeout=_DEFAULT_TIMEOUT_MS)
        except Exception as exc:  # noqa: BLE001
            raise AdidasAPIError(
                f"Could not resolve the insufficient-availability dialog: {exc}"
            ) from exc

    def _read_ordered_quantity(self, style: str, code: str) -> int | None:
        """Read the committed ordered quantity from a size cell (post-entry)."""

        ordered = self.page.locator(
            f"#CartModule-SizeTile-OrderedInDate-{style}-{code}"
        )
        try:
            ordered.wait_for(state="visible", timeout=5_000)
            return _to_int(ordered.first.inner_text())
        except Exception:  # noqa: BLE001 — cell may not show a total; don't hard-fail
            return None

    # -- Step 3: checkout details ----------------------------------------

    def fill_checkout(self, request: OrderRequest) -> None:
        """Open the active cart and set the Customer PO, delivery location, and
        shipping method in the cart header.

        Delivery location precedence: ``delivery_location_id`` (pick a saved
        location) > ``ship_to`` (add a one-time / dropship location) > default
        (leave the cart's preset). Shipping method is left at the cart default
        unless ``ship_method`` is given.
        """

        self.page.goto(self.base_url + _CART_PATH, wait_until="domcontentloaded")
        try:
            self.page.wait_for_selector(_CART_HEADER, timeout=_DEFAULT_TIMEOUT_MS)
        except Exception as exc:  # noqa: BLE001
            raise AdidasAPIError(
                "Could not open the active cart at /adidas/reorder/cart — the "
                "cart header did not render."
            ) from exc

        self._set_customer_po(request.po_number)

        if request.delivery_location_id:
            self._select_saved_location(request.delivery_location_id)
        elif request.ship_to is not None:
            self._add_one_time_location(request.ship_to)
        # else: leave the cart's default delivery location.

        if request.ship_method:
            self._select_shipping_method(request.ship_method)

    def _set_customer_po(self, po_number: str) -> None:
        # Length + character validation happens up front in create_purchase_order
        # (po_number is already sanitized and length-checked here).
        field = self.page.locator(_PO_FIELD)
        try:
            field.wait_for(state="visible", timeout=_DEFAULT_TIMEOUT_MS)
            field.click()
            field.fill(po_number)  # replaces the default random reference
            field.press("Enter")
            field.blur()
        except Exception as exc:  # noqa: BLE001
            raise AdidasAPIError(f"Could not set the Customer PO #: {exc}") from exc
        # Verify the value stuck.
        actual = field.input_value()
        if _clean(actual) != _clean(po_number):
            raise AdidasAPIError(
                f"Customer PO # did not persist — expected {po_number!r}, "
                f"field shows {actual!r}."
            )

    def _select_saved_location(self, location_id: str) -> None:
        self.page.click(_DELIVERY_DROPDOWN_LABEL)
        self.page.wait_for_selector(_DELIVERY_DROPDOWN_CONTENT, timeout=_DEFAULT_TIMEOUT_MS)
        option = self.page.locator(f"#OptionButton{location_id}Button")
        if option.count() == 0:
            raise AdidasAPIError(
                f"Delivery location {location_id!r} was not found in the saved "
                "locations. Search/select it manually or pass a ship_to for a "
                "one-time location."
            )
        option.first.click()

    def _add_one_time_location(self, ship_to: "ShipTo") -> None:
        """Open the delivery dropdown and file a one-time (dropship) address.

        Field mapping: Attention 1 ← name, Attention 2 ← attention, Street ←
        address1 (+ address2), City ← city, State ← state (dropdown), ZIP ← zip.
        Country is fixed to United States by the form.
        """

        self.page.click(_DELIVERY_DROPDOWN_LABEL)
        self.page.wait_for_selector(_ADD_ONE_TIME_BUTTON, timeout=_DEFAULT_TIMEOUT_MS)
        self.page.click(_ADD_ONE_TIME_BUTTON)
        self.page.wait_for_selector(_ONE_TIME_FORM, timeout=_DEFAULT_TIMEOUT_MS)

        self.page.fill("#Attention1InputField", ship_to.name)
        if ship_to.attention:
            self.page.fill("#Attention2InputField", ship_to.attention)
        street = ", ".join(p for p in (ship_to.address1, ship_to.address2) if p)
        self.page.fill("#StreetInputField", street)
        self.page.fill("#CityTownInputField", ship_to.city)
        self._select_state(ship_to.state)
        self.page.fill("#ZipcodeInputField", ship_to.zip)
        self.page.click(_ONE_TIME_SUBMIT)
        try:
            self.page.wait_for_selector(
                _ONE_TIME_FORM, state="hidden", timeout=_DEFAULT_TIMEOUT_MS
            )
        except Exception:  # noqa: BLE001 — modal may stay if validation failed
            raise AdidasAPIError(
                "The one-time delivery address was not accepted — check the "
                "address fields (PO Boxes are rejected; Latin characters only)."
            )

    def _select_state(self, state: str) -> None:
        """Select a US state in the one-time-address State dropdown.

        Accepts a 2-letter abbreviation (mapped to the full name adidas shows) or
        the full state name; options are matched by exact text so "Virginia" is
        never confused with "West Virginia".
        """

        target = _resolve_state_name(state)
        self.page.click(_STATE_DROPDOWN_LABEL)
        self.page.wait_for_selector(_STATE_DROPDOWN_CONTENT, timeout=_DEFAULT_TIMEOUT_MS)
        if not self._click_option_by_exact_text(_STATE_DROPDOWN_CONTENT, target):
            raise AdidasConfigError(
                f"State {state!r} (resolved to {target!r}) is not in the adidas "
                "Click state list. Pass the full state name as adidas spells it."
            )

    def _select_shipping_method(self, method: str) -> None:
        """Select a shipping method by its 4-letter code (e.g. ``FDGP``) or its
        label (e.g. ``FedEx Ground``)."""

        self.page.click(_SHIPPING_DROPDOWN_LABEL)
        self.page.wait_for_selector(
            _SHIPPING_DROPDOWN_CONTENT, timeout=_DEFAULT_TIMEOUT_MS
        )
        code_button = self.page.locator(
            f"{_SHIPPING_DROPDOWN_CONTENT} #OptionButton{method.strip().upper()}Button"
        )
        if code_button.count() > 0:
            code_button.first.click()
            return
        if self._click_option_by_exact_text(_SHIPPING_DROPDOWN_CONTENT, method):
            return
        raise AdidasConfigError(
            f"Shipping method {method!r} not found. Pass a code "
            f"({', '.join(_SHIPPING_METHOD_CODES)}) or its exact label."
        )

    def _click_option_by_exact_text(self, content_selector: str, target: str) -> bool:
        """Click the option button under ``content_selector`` whose text exactly
        matches ``target`` (case-insensitive). Returns True on a match."""

        buttons = self.page.locator(f"{content_selector} button.m-button")
        target_norm = _norm(target)
        for i in range(buttons.count()):
            button = buttons.nth(i)
            if _norm(button.inner_text()) == target_norm:
                button.click()
                return True
        return False

    # -- Step 4: review + submit -----------------------------------------

    def price_cart(self) -> None:
        """Advance cart → checkout and run **Calc. Net Price**, reading the priced
        totals — but **without** placing the order.

        Shared by two callers: :meth:`complete_submission` (which then clicks
        Order Now) and the pricing check (which then deletes the cart). Sequence:
        click **Next** (cart → ``/adidas/reorder/checkout``) → click **Calc. Net
        Price** and wait for it to finish (it applies the wholesale discounts and
        is slow) → scrape the per-row net prices into ``line_net_prices`` /
        ``order_total``.
        """

        # 4a — advance from the cart to the checkout page. "Next" stays inactive
        # until the cart body is scrolled into view, so scroll it in + wait for
        # it to enable before clicking.
        self.page.wait_for_selector(
            _CHECKOUT_NEXT_BUTTON, state="visible", timeout=_DEFAULT_TIMEOUT_MS
        )
        self._activate_by_scroll(_CHECKOUT_NEXT_BUTTON)
        self.page.click(_CHECKOUT_NEXT_BUTTON)
        self.page.wait_for_url(f"**{_CHECKOUT_PATH}", timeout=_DEFAULT_TIMEOUT_MS)
        self.page.wait_for_load_state("networkidle")

        # 4b — apply wholesale pricing; MUST complete before ordering/reading.
        self.page.click(_CALC_NET_PRICE_BUTTON)
        self._await_net_price_calc()
        self._read_checkout_totals()  # net + retail totals, once priced

    def complete_submission(self) -> str | None:
        """Price the cart, then place the order and read the confirmation number.

        Runs :meth:`price_cart` (Next → Calc. Net Price → read totals) so the
        wholesale discount is applied before ordering, then clicks **Order Now**
        and parses the order number from the confirmation redirect.
        """

        self.price_cart()

        # 4c — place the order.
        submit = self.page.locator(_ORDER_NOW_BUTTON)
        submit.wait_for(state="visible", timeout=_DEFAULT_TIMEOUT_MS)
        submit.click()

        # 4d — Order Now auto-redirects to the confirmation page; the order
        # number is in that URL. (A Qualtrics feedback popup may open afterward;
        # it is ignored — reading the main page URL is unaffected.)
        try:
            self.page.wait_for_url(
                _CONFIRMATION_URL_GLOB, timeout=_DEFAULT_TIMEOUT_MS
            )
        except Exception as exc:  # noqa: BLE001
            raise AdidasAPIError(
                "Order Now was clicked but the confirmation page "
                "(/adidas/reorder/order/…/confirmation) did not load — the order "
                "status is uncertain; verify it in the portal before retrying."
            ) from exc
        return self._read_confirmation_number()

    def _await_net_price_calc(self) -> None:
        """Wait for "Calc. Net Price" to finish before "Order Now" is clicked.

        On completion the ``#NPCCartSimulation`` button is replaced by a "Done!"
        message in the summary-table header. We wait for that "Done!" text (its
        class is hashed, so we match the text) and **raise if it never appears**
        — clicking Order Now before the simulation completes would submit at
        list price instead of our wholesale net price.
        """

        # Best-effort: the button detaches when replaced. Primary gate is "Done!".
        try:
            self.page.wait_for_selector(
                _CALC_NET_PRICE_BUTTON, state="detached", timeout=_CALC_TIMEOUT_MS
            )
        except Exception:  # noqa: BLE001 — some builds hide rather than detach
            pass
        try:
            self.page.get_by_text(_CALC_DONE_TEXT, exact=False).first.wait_for(
                state="visible", timeout=_CALC_TIMEOUT_MS
            )
        except Exception as exc:  # noqa: BLE001
            raise AdidasAPIError(
                "Calc. Net Price did not report 'Done!' within the timeout — the "
                "wholesale pricing may not have applied, so the order was NOT "
                "placed. Retry, or check the cart in the portal."
            ) from exc

    def _read_checkout_totals(self) -> None:
        """Best-effort scrape of the priced per-row net prices on the review page.

        Each order row has a net-price cell ``#OrderReviewShardTotalsNetPrice{N}``
        (N = 1-based row index) whose **first** ``<span>`` is the net price and
        second is the retail comparison. Collects the per-row nets (exposed as
        ``line_net_prices`` for positional assignment to the result lines) and
        sums them into ``order_total``. Never raises — pricing display must not
        block placing the order.
        """

        nets: list[str | None] = []
        try:
            index = 1
            while index <= 500:  # safety cap
                cell = self.page.locator(f"#OrderReviewShardTotalsNetPrice{index}")
                if cell.count() == 0:
                    break
                spans = cell.locator("span")
                nets.append(_clean(spans.first.inner_text()) if spans.count() else None)
                index += 1
        except Exception as exc:  # noqa: BLE001 — informational only
            logger.warning("Could not read checkout net prices: %s", exc)
        self.line_net_prices = nets
        self.order_total = _sum_currency(nets)

    def _read_confirmation_number(self) -> str | None:
        """Extract the order number from the confirmation URL.

        The success page is ``/adidas/reorder/order/{number}/confirmation`` (e.g.
        order ``25709165``), so the number is parsed straight from the URL rather
        than scraped from the page body.
        """

        match = _CONFIRMATION_URL_RE.search(self.page.url)
        return match.group(1) if match else None

    # -- inventory / pricing checks --------------------------------------

    def read_inventory(self, request: OrderRequest) -> list["CheckLineResult"]:
        """Read live inventory for each requested line **without touching a cart**.

        Opens each style's product page once and reads the size-tile inventory
        indicator — the same read the order flow does before entering quantities,
        but here nothing is added to the cart. A line whose ``size`` is blank (or
        ``"*"`` / ``"all"``) expands to **every** size of that style, so a caller
        can ask "how much of JW4306 is in stock across sizes?" in one line.

        A size that isn't offered is reported with a note (not raised) so one bad
        size never aborts the whole check.
        """

        results: list[CheckLineResult] = []
        for style, lines in _group_by_style(request.lines).items():
            self._open_product(style)
            product_name = self._read_product_name(style)
            code_map = self._size_code_map()
            for line in lines:
                wants_all = _norm(line.size) in {"", "*", "all"}
                if wants_all:
                    for label, code in code_map.items():
                        results.append(
                            self._inventory_line(style, label, code, product_name, line, None)
                        )
                    continue
                code = next(
                    (code_map[key] for key in _size_lookup_keys(line.size)
                     if key in code_map),
                    None,
                )
                if code is None:
                    results.append(
                        CheckLineResult(
                            style=style,
                            size=line.size,
                            color=line.color or (product_name or ""),
                            requested_quantity=line.quantity,
                            note=(
                                f"size {line.size!r} is not offered for {style} "
                                f"(sizes: {', '.join(sorted(code_map)) or '(none read)'})"
                            ),
                        )
                    )
                    continue
                results.append(
                    self._inventory_line(style, line.size, code, product_name, line, line.quantity)
                )
        return results

    def _inventory_line(
        self,
        style: str,
        size_label: str,
        code: str,
        product_name: str | None,
        line: OrderLine,
        requested: int | None,
    ) -> "CheckLineResult":
        """Classify one size's stock into a :class:`CheckLineResult` (no cart)."""

        # Classify against 1 unit so "short" means "cannot even ship one" (== 0
        # with a restock date); the raw indicator carries the actual level.
        status, indicator, available = self._classify_size(style, code, 1)
        return CheckLineResult(
            style=style,
            size=size_label,
            color=line.color or (product_name or ""),
            requested_quantity=requested,
            available=indicator,
            available_count=available,
            status=_INVENTORY_STATUS.get(status, status),
            in_stock=status == "ok",
        )

    def delete_cart(self, name: str) -> int:
        """Delete the throwaway cart named ``name`` (cleanup after a pricing check).

        Reuses the same panel + delete path as ``create_new_cart``'s dedup, which
        first activates a different cart if ``name`` is the active one (the active
        cart can't be deleted). Returns the number of carts removed. Raises
        :class:`AdidasConfigError` if the check cart is the account's *only* cart
        (nothing to switch to) — the caller turns that into a warning.
        """

        self._ensure_carts_panel_open()
        return self._delete_carts_named(name)

    # -- helpers ----------------------------------------------------------

    def _activate_by_scroll(self, selector: str) -> None:
        """Scroll ``selector`` into view (and nudge-scroll) until it is enabled.

        Some controls (e.g. the cart "Next" button) stay inactive until the
        surrounding content is scrolled into the viewport. Best-effort: returns
        once the element reports enabled, or after the scroll budget — the
        subsequent ``click`` still enforces actionability.
        """

        element = self.page.locator(selector).first
        for _ in range(12):
            try:
                element.scroll_into_view_if_needed(timeout=2_000)
            except Exception:  # noqa: BLE001
                pass
            try:
                if element.is_enabled():
                    return
            except Exception:  # noqa: BLE001
                pass
            self.page.mouse.wheel(0, 500)
            self.page.wait_for_timeout(250)

    def screenshot(self, path: str) -> None:
        try:
            self.page.screenshot(path=path, full_page=True)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not capture screenshot at %s: %s", path, exc)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


@contextmanager
def _browser_page(headless: bool):
    """Launch a stealth Chromium and yield a ready page, tearing it down on exit.

    Centralizes the anti-bot browser setup shared by the order and check flows:
    the ``ADIDAS_CLICK_HEADLESS`` override, a desktop-Chrome User-Agent, the
    auto-started Xvfb virtual display, the ``navigator.webdriver`` mask, and
    teardown. adidas Click's Akamai edge stalls headless Chromium, so this runs
    **headed by default** (``ADIDAS_CLICK_HEADLESS=true`` forces headless).
    """

    # adidas Click is fronted by Akamai Bot Manager, which stalls the response
    # for automated-looking clients. A headless Chromium (UA "HeadlessChrome",
    # navigator.webdriver=true) is fingerprinted and tarpitted even with a
    # spoofed UA, so this skill runs HEADED by default (on a virtual display —
    # started below) and also presents an ordinary desktop-Chrome UA. Set
    # ADIDAS_CLICK_HEADLESS=true to force headless (expect WAF stalls); override
    # the UA via ADIDAS_CLICK_USER_AGENT.
    _headless_env = os.environ.get("ADIDAS_CLICK_HEADLESS")
    if _headless_env is not None:
        headless = _headless_env.strip().lower() not in ("0", "false", "no", "off")
    user_agent = os.environ.get("ADIDAS_CLICK_USER_AGENT") or _DEFAULT_USER_AGENT

    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:  # pragma: no cover — runtime guard
        raise AdidasConfigError(
            "playwright is required for the adidas Click flows. Install it with "
            "`pip install playwright` and then "
            "`python -m playwright install chromium`."
        ) from exc

    # A headed browser needs a display. adidas's WAF forces headed, so on a
    # *Linux* host with no X server we start a virtual display (Xvfb) and point
    # $DISPLAY at it; tear it down when the process exits. Windows/macOS render on
    # the native GUI and never need Xvfb (_headed_needs_virtual_display gates it).
    if not headless and _headed_needs_virtual_display():
        atexit.register(_stop_process, _start_virtual_display())

    with sync_playwright() as p:
        browser = _launch_chromium(p, headless)
        context = browser.new_context(
            user_agent=user_agent,
            viewport={"width": 1440, "height": 900},
            locale="en-US",
        )
        context.set_default_timeout(_DEFAULT_TIMEOUT_MS)
        context.set_default_navigation_timeout(_NAV_TIMEOUT_MS)
        # Belt-and-suspenders: also mask navigator.webdriver at the JS layer for
        # builds where the launch flag alone doesn't hide it.
        context.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
        )
        page = context.new_page()
        try:
            yield page
        finally:
            context.close()
            browser.close()


def create_purchase_order(
    *,
    request: OrderRequest,
    credentials: AdidasClickCredentials | None = None,
    confirm: bool = False,
    screenshot_path: str | None = None,
    headless: bool = False,
) -> OrderResult:
    """Fill (and optionally place) an adidas Click purchase order for one order.

    Logs in, adds each product line, fills the PO number + ship-to at checkout,
    then — with ``confirm`` true — places the order.

    With ``confirm`` false (default) it stops before submitting and returns a
    ``dry_run`` preview. Until the flow is fully reverse-engineered, it returns
    a ``not_implemented`` result at the first un-captured step (see the
    ``*_IMPLEMENTED`` gates and references/order_flow_notes.md).
    """

    if not request.po_number:
        raise AdidasConfigError("po_number is required to place an order.")
    if not request.lines:
        raise AdidasConfigError("at least one order line is required.")

    # Sanitize the Customer PO up front (fail fast, before launching a browser).
    original_po = request.po_number
    clean_po, po_changed = _sanitize_po_number(original_po)
    if not clean_po:
        raise AdidasConfigError(
            f"Customer PO {original_po!r} has no valid characters — adidas Click "
            "allows only letters, numbers, space, and / _ . ? &."
        )
    if len(clean_po) > _PO_MAX_LEN:
        raise AdidasConfigError(
            f"adidas Click Customer PO # is limited to {_PO_MAX_LEN} characters; "
            f"{clean_po!r} is {len(clean_po)}."
        )
    request.po_number = clean_po
    po_warning = (
        f"Customer PO sanitized from {original_po!r} to {clean_po!r} — adidas "
        "Click allows only letters, numbers, space, and / _ . ? &."
        if po_changed
        else None
    )

    if credentials is None:
        credentials = credentials_from_env()

    # Nothing is captured yet — short-circuit with a clear status so the tool
    # is runnable end-to-end while the flow is still being built.
    if not LOGIN_IMPLEMENTED:
        return OrderResult(
            status="not_implemented",
            po_number=request.po_number,
            message=(
                "The adidas Click ordering flow is still being reverse-"
                "engineered. Step 1 (login) has not been captured yet — see "
                "references/order_flow_notes.md."
            ),
        )

    with _browser_page(headless) as page:
        driver = AdidasClickDriver(page, credentials.base_url)
        try:
            driver.login(credentials)

            result = OrderResult(status="dry_run", po_number=request.po_number)
            if po_warning:
                result.warnings.append(po_warning)

            # Isolate this run in its own cart (named with the PO) so a shared
            # account's existing carts are never touched. Any leftover cart with
            # the same PO name (e.g. from an errored prior run) is deleted first.
            if request.new_cart:
                deleted = driver.create_new_cart(request.po_number)
                if deleted:
                    result.warnings.append(
                        f"Deleted {deleted} existing cart(s) named "
                        f"{request.po_number!r} before starting fresh."
                    )

            if not ADD_LINES_IMPLEMENTED:
                result.status = "not_implemented"
                result.message = "Logged in, but Step 2 (line entry) is not captured yet."
                if screenshot_path:
                    driver.screenshot(screenshot_path)
                    result.screenshot_path = screenshot_path
                return result

            try:
                result.lines = driver.add_lines(request)
            except _InsufficientStockPause as pause:
                # on_insufficient_stock == "pause" and something is short: place
                # nothing and hand the decision back to the agent/user.
                result.status = "needs_confirmation"
                result.lines = pause.lines
                result.out_of_stock = pause.out_of_stock
                result.total_quantity = sum(
                    ln.quantity for ln in pause.lines if ln.quantity
                ) or None
                result.message = _insufficient_stock_message(pause.out_of_stock)
                if screenshot_path:
                    driver.screenshot(screenshot_path)
                    result.screenshot_path = screenshot_path
                return result
            result.total_quantity = sum(
                ln.quantity for ln in result.lines if ln.quantity
            ) or None

            if not CHECKOUT_IMPLEMENTED:
                result.status = "not_implemented"
                result.message = "Lines added, but Step 3 (checkout) is not captured yet."
                if screenshot_path:
                    driver.screenshot(screenshot_path)
                    result.screenshot_path = screenshot_path
                return result

            driver.fill_checkout(request)

            if screenshot_path:
                driver.screenshot(screenshot_path)
                result.screenshot_path = screenshot_path

            if not confirm:
                result.message = (
                    "Dry run — the order was filled and validated but NOT "
                    "placed. Re-run with confirm=true to submit it."
                )
                return result

            if not FINAL_SUBMIT_IMPLEMENTED:
                result.status = "not_implemented"
                result.message = (
                    "confirm=true was requested, but Step 4 (review → place "
                    "order) is not captured yet. Nothing was submitted."
                )
                return result

            result.confirmation_number = driver.complete_submission()
            result.order_total = driver.order_total
            # Assign each review-page net price to its line (positional; the
            # review rows follow the order the lines were entered).
            nets = driver.line_net_prices
            if nets and len(nets) == len(result.lines):
                for line, net in zip(result.lines, nets):
                    line.line_total = net
                    line.unit_price = _unit_price(net, line.quantity)
            result.status = "submitted"
            result.message = (
                f"Order placed — confirmation #{result.confirmation_number}."
                if result.confirmation_number
                else "Order placed (confirmation number could not be read from "
                "the URL; verify in the portal)."
            )
            return result
        except (AdidasConfigError, AdidasAPIError, AdidasTransportError):
            raise
        except Exception as exc:  # noqa: BLE001 — normalize unexpected failures
            raise AdidasTransportError(
                f"Unexpected failure during the adidas Click order flow: {exc}"
            ) from exc


# ---------------------------------------------------------------------------
# Inventory / pricing check
# ---------------------------------------------------------------------------


def _line_stock(line: OrderLineResult) -> tuple[str | None, bool | None]:
    """Best-effort (status, in_stock) for a priced check line from its indicator.

    The order-flow line result carries the raw inventory indicator (``available``)
    and a note; re-derive the check's stock vocabulary from those.
    """

    note = (line.note or "").lower()
    if "not available" in note:
        return "unavailable", False
    count = _parse_available(line.available)
    if count is not None and count == 0:
        return "backorder", False
    if line.available or count is not None:
        return "in_stock", True
    return None, None


def _checkline_results(
    order_lines: list[OrderLineResult], nets: list[str | None]
) -> list[CheckLineResult]:
    """Turn add_lines' order-line results into check lines, attaching net prices.

    Review-page net prices exist only for lines actually entered into the cart
    (committed quantity > 0), in entry order — so map them positionally onto
    those lines and leave dropped/unavailable lines price-less.
    """

    entered = [ln for ln in order_lines if ln.quantity]
    net_by_line = (
        {id(ln): net for ln, net in zip(entered, nets)}
        if nets and len(nets) == len(entered)
        else {}
    )
    out: list[CheckLineResult] = []
    for ln in order_lines:
        net = net_by_line.get(id(ln))
        status, in_stock = _line_stock(ln)
        out.append(
            CheckLineResult(
                style=ln.style,
                size=ln.size,
                color=ln.color,
                requested_quantity=ln.quantity or None,
                available=ln.available,
                available_count=_parse_available(ln.available),
                status=status,
                in_stock=in_stock,
                unit_price=_unit_price(net, ln.quantity) if net else None,
                line_total=net,
                note=ln.note,
            )
        )
    return out


def _safe_delete_cart(
    driver: "AdidasClickDriver", name: str, result: CheckResult
) -> bool:
    """Delete the throwaway check cart, downgrading any failure to a warning.

    Cleanup must never mask the pricing the check already obtained, so a failed
    delete (e.g. the check cart was the account's only cart) is reported as a
    warning and the caller tells the user to remove it manually.
    """

    try:
        driver.delete_cart(name)
        return True
    except Exception as exc:  # noqa: BLE001 — cleanup is best-effort
        result.warnings.append(
            f"Could not delete the throwaway check cart {name!r}: {exc} "
            "Remove it in the portal — it is named to signal DO NOT BUY."
        )
        return False


def check_inventory_pricing(
    *,
    request: OrderRequest,
    credentials: AdidasClickCredentials | None = None,
    check: str = "both",
    screenshot_path: str | None = None,
    headless: bool = False,
) -> CheckResult:
    """Retrieve live inventory and/or wholesale pricing **without placing an order**.

    Reuses the ordering flow's login + product navigation. ``check`` selects the
    mode:

    - ``inventory`` — read each line's size-tile stock level. **No cart is
      created** (a line with a blank ``size`` expands to every size of the style).
    - ``pricing`` — fill a **throwaway cart**, advance to the priced checkout
      page, run **Calc. Net Price** to apply the wholesale discount, read the net
      unit/line prices and order total, then **delete the cart**.
    - ``both`` — pricing plus the inventory levels read while filling the cart.

    The throwaway cart / Customer PO is named with a loud "DO NOT BUY {rand}"
    marker (override via ``request.po_number``), and the cart is deleted once the
    prices are read, so nothing is ever purchased and no stray cart is left to
    buy. Since the order is never placed, the check never pauses on short stock —
    a ``pause`` policy is upgraded to ``order`` so every orderable line gets a
    price.
    """

    check = (check or "both").strip().lower()
    if check not in {"inventory", "pricing", "both"}:
        raise AdidasConfigError(
            f"check must be 'inventory', 'pricing', or 'both'; got {check!r}."
        )
    if not request.lines:
        raise AdidasConfigError(
            "at least one line ({style, size?[, quantity]}) is required for a check."
        )

    needs_cart = check in {"pricing", "both"}

    pre_warnings: list[str] = []
    po_number: str | None = None
    if needs_cart:
        # A pricing check fills a throwaway cart just to reach the priced
        # checkout page. Name it (and the Customer PO) with a DO-NOT-BUY marker
        # so a leftover from a crashed run is obviously safe; the caller may
        # override the marker via request.po_number.
        raw_po = request.po_number or _generate_check_po()
        clean_po, po_changed = _sanitize_po_number(raw_po)
        if not clean_po:
            raise AdidasConfigError(
                f"Check PO {raw_po!r} has no valid characters — adidas Click "
                "allows only letters, numbers, space, and / _ . ? &."
            )
        if len(clean_po) > _PO_MAX_LEN:
            raise AdidasConfigError(
                f"Check PO # is limited to {_PO_MAX_LEN} characters; "
                f"{clean_po!r} is {len(clean_po)}. Pass a shorter po_number."
            )
        po_number = clean_po
        request.po_number = clean_po
        request.new_cart = True  # a check always isolates its own throwaway cart
        if po_changed:
            pre_warnings.append(
                f"Check PO sanitized from {raw_po!r} to {clean_po!r}."
            )
        # A check never orders and deletes its cart, so it must never pause on
        # short stock: fill everything orderable to get its price.
        if (request.on_insufficient_stock or "pause").strip().lower() == "pause":
            request.on_insufficient_stock = "order"

    if credentials is None:
        credentials = credentials_from_env()

    with _browser_page(headless) as page:
        driver = AdidasClickDriver(page, credentials.base_url)
        try:
            driver.login(credentials)

            result = CheckResult(status="checked", check=check, po_number=po_number)
            result.warnings.extend(pre_warnings)

            # ---- inventory-only: read product pages, never touch a cart -------
            if not needs_cart:
                result.lines = driver.read_inventory(request)
                result.total_quantity = (
                    sum((ln.requested_quantity or 0) for ln in result.lines) or None
                )
                if screenshot_path:
                    driver.screenshot(screenshot_path)
                    result.screenshot_path = screenshot_path
                result.message = (
                    f"Inventory check complete for {len(result.lines)} line(s) — "
                    "no cart was created."
                )
                return result

            # ---- pricing / both: fill a throwaway cart, price it, delete it ---
            deleted_pre = driver.create_new_cart(po_number)
            if deleted_pre:
                result.warnings.append(
                    f"Deleted {deleted_pre} pre-existing cart(s) named "
                    f"{po_number!r} before starting the check."
                )

            try:
                order_lines = driver.add_lines(request)
            except AdidasConfigError as exc:
                # e.g. every requested size is unavailable — nothing to price.
                # Report inventory instead, then clean up the (empty) cart.
                result.lines = driver.read_inventory(request)
                result.total_quantity = (
                    sum((ln.requested_quantity or 0) for ln in result.lines) or None
                )
                result.cart_deleted = _safe_delete_cart(driver, po_number, result)
                if screenshot_path:
                    driver.screenshot(screenshot_path)
                    result.screenshot_path = screenshot_path
                result.message = (
                    "Pricing check could not add any line to the cart "
                    f"({exc}); inventory levels are reported instead."
                )
                return result

            driver.fill_checkout(request)  # sets the DO-NOT-BUY Customer PO
            driver.price_cart()            # Next → Calc. Net Price → read totals

            result.order_total = driver.order_total
            result.lines = _checkline_results(order_lines, driver.line_net_prices)
            result.total_quantity = (
                sum((ln.requested_quantity or 0) for ln in result.lines) or None
            )

            if screenshot_path:
                driver.screenshot(screenshot_path)
                result.screenshot_path = screenshot_path

            # Cleanup: delete the throwaway cart so nothing is left to purchase.
            result.cart_deleted = _safe_delete_cart(driver, po_number, result)

            priced = sum(1 for ln in result.lines if ln.line_total)
            tail = (
                " Throwaway cart deleted."
                if result.cart_deleted
                else f" NOTE: the throwaway cart {po_number!r} could NOT be "
                "auto-deleted — remove it in the portal."
            )
            result.message = (
                f"Pricing check complete — {priced} line(s) priced"
                + (f", order total {result.order_total}." if result.order_total else ".")
                + tail
            )
            return result
        except (AdidasConfigError, AdidasAPIError, AdidasTransportError):
            raise
        except Exception as exc:  # noqa: BLE001 — normalize unexpected failures
            raise AdidasTransportError(
                f"Unexpected failure during the adidas Click check flow: {exc}"
            ) from exc
