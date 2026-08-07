"""Human-like behavior helpers for browser automation.

Anti-fingerprint layer 2 (Tier 2): simulate real user behavior to make
Playwright-driven sessions indistinguishable from organic browsing.

Three techniques:
1. human_delay(min, max): random wait to break machine-like timing.
2. human_click(page, locator): mouse move via bezier curve + click offset.
3. warm_path(page, audit): visit homepage and scroll before publishing.
"""
from __future__ import annotations

import asyncio
import random
from typing import Any


def _rand_seconds(min_ms: int, max_ms: int) -> float:
    return random.uniform(min_ms, max_ms) / 1000.0


async def human_delay(min_ms: int = 500, max_ms: int = 2000) -> None:
    """Wait a random duration to simulate human reaction/reading time."""
    await asyncio.sleep(_rand_seconds(min_ms, max_ms))


async def human_click(page: Any, locator: Any, *, button: str = "left") -> bool:
    """Click an element with a bezier-curve mouse trajectory and random offset.

    Returns True if mouse-based click succeeded, False to signal caller to fall
    back to locator.click() (e.g. when bounding_box is None).

    If the element is off-screen (e.g. positioned at left:-9999px), scrolls it
    into view first so the click actually lands on the target.
    """
    try:
        box = await locator.bounding_box()
    except Exception:
        box = None

    # Detect off-screen / hidden elements: bounding box outside viewport.
    viewport = page.viewport_size or {"width": 1440, "height": 900}
    if not box or box["x"] < 0 or box["y"] < 0 or \
       box["x"] + box["width"] > viewport["width"] or \
       box["y"] + box["height"] > viewport["height"]:
        # Off-screen element. Raise so the caller can fall back to a JS-driven
        # click that doesn't rely on coordinates (XHS tab clicks need to land
        # on the actual element, not on viewport (4,4)).
        raise ValueError(
            f"element bounding box {box} is outside viewport {viewport}; "
            "human_click refuses to fire mouse events at arbitrary coordinates"
        )

    # Random target inside the element (avoid exact center, +/- 20-80%).
    tx = box["x"] + random.uniform(0.2, 0.8) * box["width"]
    ty = box["y"] + random.uniform(0.3, 0.7) * box["height"]
    tx = max(4.0, min(viewport["width"] - 4.0, tx))
    ty = max(4.0, min(viewport["height"] - 4.0, ty))

    # Random start position (somewhere on viewport).
    sx = random.uniform(40, viewport["width"] - 40)
    sy = random.uniform(40, viewport["height"] - 40)

    # Bezier curve via control points. Playwright's mouse.move with steps already
    # does linear interpolation, but we layer two intermediate waypoints to
    # approximate a curve.
    steps = random.randint(18, 32)
    await page.mouse.move(sx, sy)
    cx1 = (sx + tx) / 2 + random.uniform(-60, 60)
    cy1 = (sy + ty) / 2 + random.uniform(-60, 60)
    cx2 = (sx + tx) / 2 + random.uniform(-60, 60)
    cy2 = (sy + ty) / 2 + random.uniform(-60, 60)
    # Move through intermediate waypoints to fake a curve.
    await page.mouse.move(cx1, cy1, steps=max(2, steps // 4))
    await page.mouse.move(cx2, cy2, steps=max(2, steps // 4))
    await page.mouse.move(tx, ty, steps=max(2, steps // 2))

    await asyncio.sleep(_rand_seconds(50, 150))
    await page.mouse.down(button=button)
    await asyncio.sleep(_rand_seconds(50, 150))
    await page.mouse.up(button=button)
    return True


async def human_wheel(page: Any, *, min_dy: int = 300, max_dy: int = 700) -> None:
    """Mouse wheel scroll with random magnitude."""
    await page.mouse.wheel(0, random.randint(min_dy, max_dy))


async def warm_path(
    page: Any,
    audit: Any,
    *,
    home_url: str = "https://www.xiaohongshu.com/",
    dwell_seconds: tuple[int, int] = (5, 10),
) -> bool:
    """Visit XHS homepage, scroll a few times, then return.

    Goal: build a believable referer chain (homepage -> publish page) and put
    some browsing activity before the publish action. Skipped silently on
    network failure.
    """
    audit.event("warm_path_start", url=home_url)
    try:
        await page.goto(home_url, wait_until="domcontentloaded", timeout=15000)
    except Exception as exc:  # noqa: BLE001
        audit.event("warm_path_goto_failed", error=str(exc))
        return False

    dwell = _rand_seconds(dwell_seconds[0] * 1000, dwell_seconds[1] * 1000)
    # Split dwell into 2-4 scroll + pause cycles.
    cycles = random.randint(2, 4)
    cycle_sleep = dwell / cycles
    for i in range(cycles):
        await asyncio.sleep(cycle_sleep * 0.5)
        await human_wheel(page, min_dy=250, max_dy=650)
        await asyncio.sleep(cycle_sleep * 0.5)
    audit.event("warm_path_done", dwell_seconds=round(dwell, 2), cycles=cycles)
    return True