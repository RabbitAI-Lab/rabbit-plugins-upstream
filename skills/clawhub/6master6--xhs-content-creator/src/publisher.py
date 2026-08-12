from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .audit import AuditLog
from .cloud_notify import CloudNotifier
from .content_validator import XhsContent
from .human_behavior import human_click, human_delay, human_wheel, warm_path
from .locator_utils import any_visible, click_first, fill_first, first_attached
from .login_state import LoginState


class XhsPublisher:
    def __init__(
        self,
        *,
        page: Any,
        app_config: dict[str, Any],
        selectors: dict[str, list[dict[str, Any]]],
        login_state: LoginState,
        audit: AuditLog,
        notifier: CloudNotifier,
        login_timeout_seconds: int = 180,
    ) -> None:
        self.page = page
        self.app_config = app_config
        self.selectors = selectors
        self.login_state = login_state
        self.audit = audit
        self.notifier = notifier
        self.login_timeout_seconds = login_timeout_seconds

    async def run(self, content: XhsContent) -> dict[str, Any]:
        self.audit.event("publish_run_start", mode=content.mode, title=content.title)
        await self.ensure_login()
        await self.open_publish_page()
        await self.fill_note(content)
        await self.audit.screenshot(self.page, "before_publish")
        await self.audit.dom_snapshot(self.page, "before_publish")

        if content.mode == "draft":
            result = await self.save_draft_and_wait()
            self.audit.event("draft_run_done", **result)
            return result

        result = await self.click_publish_and_wait()
        self.audit.event("publish_run_done", **result)
        return result

    async def ensure_login(self) -> None:
        home_url = str(self.app_config["creator_home_url"])
        if self.login_state.is_valid():
            self.audit.event("login_cache_hit")
            return

        self.audit.event("login_cache_miss", url=home_url)
        await self.page.goto(home_url, wait_until="domcontentloaded")
        await self._best_effort_settle(20_000)
        await self.audit.screenshot(self.page, "login_check")

        if await self._looks_logged_in():
            self.login_state.mark_logged_in(home_url=home_url)
            self.audit.event("login_confirmed")
            return

        self.audit.event("login_required", timeout_seconds=self.login_timeout_seconds)
        await self.prepare_qr_login()
        await self.wait_for_user_login()
        self.login_state.mark_logged_in(home_url=home_url)
        self.audit.event("login_confirmed_after_handoff")

    async def wait_for_user_login(self) -> None:
        deadline = self.login_timeout_seconds
        for second in range(deadline):
            if await self._looks_logged_in():
                return
            if second and second % 30 == 0:
                await self.audit.screenshot(self.page, f"login_wait_{second}s")
            await human_delay(800, 1300)
        await self.audit.screenshot(self.page, "login_timeout")
        await self.audit.dom_snapshot(self.page, "login_timeout")
        raise TimeoutError("login was not completed before timeout")

    async def prepare_qr_login(self) -> None:
        clicked = False
        candidates = [
            "img.css-wemwzq",
            "img[src^='data:image/png']",
            "[class*='qrcode']",
            "[class*='qr']",
        ]
        for selector in candidates:
            try:
                locator = self.page.locator(selector).first
                await locator.wait_for(state="visible", timeout=1500)
                await human_click(self.page, locator)
                clicked = True
                self.audit.event("qr_login_toggle_clicked", selector=selector)
                break
            except Exception:
                continue

        await human_delay(800, 1500)
        qr_path = await self.audit.screenshot(self.page, "login_qr")
        await self.audit.dom_snapshot(self.page, "login_qr")
        if self.notifier.qr_handoff_enabled():
            self.notifier.notify_qr(qr_path, run_dir=self.audit.run_dir)
        print(f"LOGIN_QR_SCREENSHOT={qr_path}", flush=True)
        self.audit.event("login_qr_screenshot_ready", path=str(qr_path), clicked=clicked)

    async def open_publish_page(self) -> None:
        publish_url = str(self.app_config["publish_url"])
        self.audit.event("open_publish_page", url=publish_url)
        await self.page.goto(publish_url, wait_until="domcontentloaded")
        await self._best_effort_settle(30_000)

        if not await self._looks_logged_in():
            self.audit.event("login_cache_invalidated_on_publish_page")
            self.login_state.invalidate()
            await self.ensure_login()
            await self.page.goto(publish_url, wait_until="domcontentloaded")
            await self._best_effort_settle(30_000)

        await self.audit.screenshot(self.page, "publish_page_opened")
        await self.audit.dom_snapshot(self.page, "publish_page_opened")
        # Tier 2 warm_path: visit homepage + scroll before publishing to build
        # a realistic referer chain (homepage -> publish page) instead of
        # going straight to publish/publish.
        await warm_path(self.page, self.audit, home_url="https://www.xiaohongshu.com/")
        await self.page.goto(publish_url, wait_until="domcontentloaded")
        await self._best_effort_settle(15_000)
        await self.select_image_tab()

    async def fill_note(self, content: XhsContent) -> None:
        self.audit.event("fill_note_start", image_count=len(content.images))
        if content.images:
            await self.upload_images(content.images)
        await fill_first(self.page, self.selectors["title_input_any"], content.title)
        self.audit.event("title_filled", length=len(content.title))
        await fill_first(self.page, self.selectors["body_input_any"], content.body_with_topics)
        self.audit.event("body_filled", length=len(content.body_with_topics), topic_count=len(content.topics))
        await self.page.keyboard.press("Escape")
        await human_delay(800, 1600)
        await self.verify_filled(content)

    async def upload_images(self, images: list[Path]) -> None:
        self.audit.event("upload_images_start", images=[str(image) for image in images])
        input_locator = await self.find_image_upload_input()
        await input_locator.set_input_files([str(path) for path in images])
        await human_delay(3500, 6000)
        await self.audit.screenshot(self.page, "after_image_upload")
        self.audit.event("upload_images_done", count=len(images))

    async def select_image_tab(self) -> None:
        tab_text = "上传图文"
        clicked = False
        try:
            locator = self.page.get_by_text(tab_text, exact=True).first
            await locator.wait_for(state="visible", timeout=5000)
            await human_click(self.page, locator)
            clicked = True
        except Exception as exc:  # noqa: BLE001
            self.audit.event("image_tab_direct_click_failed", error=str(exc))

        if not clicked:
            try:
                clicked = bool(
                    await self.page.evaluate(
                        """
                        text => {
                          const candidates = Array.from(document.querySelectorAll('span, div, button, a'));
                          const el = candidates.find(node => (node.innerText || node.textContent || '').trim() === text);
                          if (!el) return false;
                          el.scrollIntoView({block: 'center', inline: 'center'});
                          el.click();
                          return true;
                        }
                        """,
                        tab_text,
                    )
                )
            except Exception as exc:  # noqa: BLE001
                self.audit.event("image_tab_js_click_failed", error=str(exc))

        self.audit.event("image_tab_selected" if clicked else "image_tab_select_failed")
        await human_delay(1200, 2200)
        await self.audit.screenshot(self.page, "image_tab_selected")
        await self.audit.dom_snapshot(self.page, "image_tab_selected")

    async def find_image_upload_input(self) -> Any:
        try:
            return await first_attached(self.page, self.selectors["image_upload_input_any"], timeout_ms=5000)
        except Exception:
            pass

        handle = await self.page.evaluate_handle(
            """
            () => {
              const inputs = Array.from(document.querySelectorAll('input[type="file"]'));
              return inputs.find(input => {
                const accept = (input.getAttribute('accept') || '').toLowerCase();
                return accept.includes('image') || accept.includes('.jpg') || accept.includes('.jpeg') || accept.includes('.png') || accept.includes('.webp');
              }) || null;
            }
            """
        )
        element = handle.as_element()
        if element:
            return element
        raise RuntimeError("image upload input was not found; page may still be on the video upload tab")

    async def verify_filled(self, content: XhsContent) -> None:
        title_ok = await self._page_contains(content.title[:20])
        # ProseMirror/Tiptap renders each line as <p>, so document.body.innerText shows
        # \n\n between paragraphs. Using content.body[:20] can land on a single \n that
        # never matches the double \n\n in the rendered DOM. Use the first non-empty
        # line as the probe instead so the slice never spans a newline.
        first_line = next(
            (line for line in content.body.split("\n") if line.strip()),
            content.body,
        )
        body_probe = first_line[:20] if len(first_line) >= 20 else first_line
        body_ok = await self._page_contains(body_probe)
        self.audit.event("verify_filled", title_ok=title_ok, body_ok=body_ok)
        if not title_ok:
            raise RuntimeError("title fill verification failed")
        if body_probe and not body_ok:
            raise RuntimeError("body fill verification failed")

    async def click_publish_and_wait(self) -> dict[str, Any]:
        self.audit.event("click_publish")
        await self.click_bottom_publish_button()
        await human_delay(1500, 2800)
        await self.confirm_publish_if_needed()
        await human_delay(6000, 10000)
        await self.audit.screenshot(self.page, "after_publish_click")
        await self.audit.dom_snapshot(self.page, "after_publish_click")

        url_success = "published=true" in self.page.url
        success = url_success or await any_visible(self.page, self.selectors.get("success_any", []), timeout_ms=5_000)
        status = "published" if success else "publish_clicked_unconfirmed"
        return {
            "status": status,
            "mode": "publish",
            "url": self.page.url,
            "success_signal_found": success,
            "url_success_signal": url_success,
        }

    async def save_draft_and_wait(self) -> dict[str, Any]:
        """Click the web creator's 保存草稿 button and confirm the draft landed server-side.

        Without this, draft mode only filled the form fields and the content
        was lost the moment the browser closed. Returning the result lets
        `run()` surface draft_persisted vs draft_clicked_unconfirmed to the
        caller (and audit log).
        """
        self.audit.event("click_save_draft")
        clicked = await self.click_save_draft_button()
        if not clicked:
            await self.audit.screenshot(self.page, "save_draft_not_found")
            await self.audit.dom_snapshot(self.page, "save_draft_not_found")
            return {
                "status": "draft_save_failed",
                "mode": "draft",
                "url": self.page.url,
                "clicked": False,
                "message": "save draft button was not found; form data is in browser memory only",
            }

        await human_delay(1500, 3000)
        await self.audit.screenshot(self.page, "after_save_draft")
        await self.audit.dom_snapshot(self.page, "after_save_draft")

        url_success = "draft" in self.page.url.lower() and "/publish/publish" not in self.page.url
        toast_success = await any_visible(
            self.page, self.selectors.get("save_draft_success_any", []), timeout_ms=5_000
        )
        success = url_success or toast_success
        status = "draft_persisted" if success else "draft_clicked_unconfirmed"
        return {
            "status": status,
            "mode": "draft",
            "url": self.page.url,
            "clicked": True,
            "success_signal_found": success,
            "toast_success_signal": toast_success,
            "url_success_signal": bool(url_success),
        }

    async def click_save_draft_button(self) -> bool:
        """Try three strategies in order: Playwright role/text, JS deep walker, xhs component."""

        # Strategy 1: Playwright role/text selectors.
        for selector in self.selectors.get("save_draft_button_any", []):
            kind = selector.get("kind")
            value = selector.get("value")
            role = selector.get("role")
            if kind == "role" and role and value:
                try:
                    locator = self.page.get_by_role(role, name=value).first
                    await locator.wait_for(state="visible", timeout=2000)
                    await human_click(self.page, locator)
                    self.audit.event("save_draft_role_click", role=role, name=value)
                    return True
                except Exception as exc:  # noqa: BLE001
                    self.audit.event("save_draft_role_click_failed", role=role, name=value, error=str(exc))
                    continue
            if kind == "text" and value:
                try:
                    locator = self.page.get_by_text(value, exact=False).first
                    await locator.wait_for(state="visible", timeout=2000)
                    await human_click(self.page, locator)
                    self.audit.event("save_draft_text_click", value=value)
                    return True
                except Exception as exc:  # noqa: BLE001
                    self.audit.event("save_draft_text_click_failed", value=value, error=str(exc))
                    continue

        # Strategy 2: JS deep walker — same shape as click_visible_publish_button
        # but constrained to non-发布 (publish) candidates so we don't accidentally
        # click the publish button when the draft label is missing.
        result = await self.page.evaluate(
            """
            () => {
              const candidates_text = ['保存草稿', '存草稿', '暂存离开', '暂存', '保存并退出', '退出前保存', '草稿'];
              const publish_text = '发布';
              const viewportWidth = window.innerWidth || document.documentElement.clientWidth;
              const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
              const visibleRect = node => {
                const rect = node.getBoundingClientRect();
                const style = window.getComputedStyle(node);
                return rect.width > 0 && rect.height > 0 &&
                  rect.bottom > 0 && rect.right > 0 &&
                  rect.top < viewportHeight && rect.left < viewportWidth &&
                  style.visibility !== 'hidden' && style.display !== 'none' &&
                  style.pointerEvents !== 'none' ? rect : null;
              };
              const score = node => {
                const rect = node.getBoundingClientRect();
                const text = (node.innerText || node.textContent || '').trim();
                const tag = node.tagName.toLowerCase();
                const role = node.getAttribute('role') || '';
                let s = 0;
                if (text === '保存草稿') s += 10;
                else if (text === '存草稿') s += 9;
                else if (text === '暂存离开') s += 9;
                else if (text === '暂存') s += 8;
                else if (text === '保存并退出') s += 8;
                else if (text === '退出前保存') s += 7;
                else if (text === '草稿') s += 4;
                if (tag === 'button' || role === 'button') s += 3;
                if (rect.top > viewportHeight * 0.55) s += 2;
                if (rect.width >= 30 && rect.width <= 200 && rect.height >= 20 && rect.height <= 60) s += 2;
                return s;
              };
              const nodes = Array.from(document.querySelectorAll('button, [role="button"], div, span'))
                .filter(node => {
                  const text = (node.innerText || node.textContent || '').trim();
                  return candidates_text.includes(text);
                });
              const candidates = [];
              for (const node of nodes) {
                let current = node;
                for (let depth = 0; current && depth < 4; depth += 1, current = current.parentElement) {
                  const rect = visibleRect(current);
                  if (!rect) continue;
                  if (current.disabled || current.getAttribute('aria-disabled') === 'true') continue;
                  candidates.push({node: current, rect, score: score(current)});
                }
              }
              candidates.sort((a, b) => b.score - a.score || b.rect.top - a.rect.top);
              const best = candidates[0];
              if (!best) return {clicked: false, reason: 'no save draft candidate'};
              best.node.scrollIntoView({block: 'center', inline: 'center'});
              const rect = best.node.getBoundingClientRect();
              const x = Math.min(Math.max(rect.left + rect.width / 2, 4), viewportWidth - 4);
              const y = Math.min(Math.max(rect.top + rect.height / 2, 4), viewportHeight - 4);
              const target = document.elementFromPoint(x, y) || best.node;
              target.dispatchEvent(new MouseEvent('mousedown', {bubbles: true, clientX: x, clientY: y}));
              target.dispatchEvent(new MouseEvent('mouseup', {bubbles: true, clientX: x, clientY: y}));
              target.dispatchEvent(new MouseEvent('click', {bubbles: true, clientX: x, clientY: y}));
              return {
                clicked: true,
                strategy: 'dom_walker',
                x, y,
                text: best.node.innerText || best.node.textContent || '',
                tag: best.node.tagName,
                score: best.score,
              };
            }
            """
        )
        self.audit.event("save_draft_dom_walker", **result)
        return bool(result.get("clicked"))

    async def click_bottom_publish_button(self) -> None:
        if await self.click_publish_component_button():
            return

        if await self.click_visible_publish_button():
            return

        custom = self.page.locator("xhs-publish-btn[is-publish='true']").first
        try:
            await custom.wait_for(state="attached", timeout=5000)
            await custom.scroll_into_view_if_needed(timeout=5000)
            await human_delay(200, 500)
            box = await custom.bounding_box()
            if box:
                # The component renders two bottom buttons. The submit button is the right-side red pill.
                viewport = self.page.viewport_size or {"width": 1440, "height": 1000}
                x = min(box["x"] + box["width"] * 0.31, viewport["width"] - 20)
                y = min(box["y"] + box["height"] * 0.5, viewport["height"] - 20)
                self.audit.event("publish_button_mouse_click", x=x, y=y, box=box)
                await self.page.mouse.click(x, y)
                return
        except Exception as exc:  # noqa: BLE001
            self.audit.event("publish_button_component_click_failed", error=str(exc))

        clicked = bool(
            await self.page.evaluate(
                """
                () => {
                  const nodes = Array.from(document.querySelectorAll('button, [role="button"], div, span'));
                  const candidates = nodes
                    .filter(node => (node.innerText || node.textContent || '').trim() === '发布')
                    .map(node => {
                      const rect = node.getBoundingClientRect();
                      return {node, rect, visible: rect.width > 0 && rect.height > 0};
                    })
                    .filter(item => item.visible && item.rect.top > window.innerHeight * 0.55)
                    .sort((a, b) => b.rect.top - a.rect.top);
                  const item = candidates[0];
                  if (!item) return false;
                  item.node.click();
                  return true;
                }
                """
            )
        )
        if not clicked:
            raise RuntimeError("bottom publish button was not found")

    async def click_publish_component_button(self) -> bool:
        result = await self.page.evaluate(
            """
            async () => {
              const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
              const host = document.querySelector("xhs-publish-btn[is-publish='true'][submit-disabled='false']");
              if (!host) return {clicked: false, reason: 'publish component not found'};

              host.scrollIntoView({block: 'center', inline: 'center'});
              await sleep(300);

              const viewportWidth = window.innerWidth || document.documentElement.clientWidth;
              const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
              const submitText = host.getAttribute('submit-text') || '发布';
              const hostRect = host.getBoundingClientRect();

              if (typeof host._onPublish === 'function') {
                const maybePromise = host._onPublish();
                if (maybePromise && typeof maybePromise.then === 'function') {
                  await maybePromise;
                }
                return {
                  clicked: true,
                  strategy: 'component_private_onPublish',
                  ownKeys: Object.keys(host).slice(0, 40),
                  hostRect: {x: hostRect.x, y: hostRect.y, width: hostRect.width, height: hostRect.height},
                  submitText
                };
              }

              const allDeep = root => {
                const seen = [];
                const walk = node => {
                  if (!node) return;
                  if (node.nodeType === Node.ELEMENT_NODE) {
                    seen.push(node);
                    if (node.shadowRoot) walk(node.shadowRoot);
                  }
                  const children = node.children || [];
                  for (const child of children) walk(child);
                };
                walk(root);
                return seen;
              };
              const isVisible = node => {
                const rect = node.getBoundingClientRect();
                const style = window.getComputedStyle(node);
                return rect.width > 0 && rect.height > 0 &&
                  rect.bottom > 0 && rect.right > 0 &&
                  rect.top < viewportHeight && rect.left < viewportWidth &&
                  style.display !== 'none' && style.visibility !== 'hidden' &&
                  style.pointerEvents !== 'none';
              };
              const colorScore = node => {
                const style = window.getComputedStyle(node);
                const colors = [style.backgroundColor, style.borderColor, style.color].join(' ');
                const nums = colors.match(/\\d+(?:\\.\\d+)?/g)?.map(Number) || [];
                let score = 0;
                for (let i = 0; i + 2 < nums.length; i += 3) {
                  const r = nums[i], g = nums[i + 1], b = nums[i + 2];
                  if (r > 180 && g < 130 && b < 150) score += 3;
                  if (r > g + 50 && r > b + 50) score += 1;
                }
                return score;
              };

              const nodes = allDeep(host);
              const candidates = nodes
                .filter(node => isVisible(node))
                .map(node => {
                  const text = (node.innerText || node.textContent || '').trim();
                  const rect = node.getBoundingClientRect();
                  const role = node.getAttribute('role') || '';
                  const tag = node.tagName.toLowerCase();
                  const textScore = text === submitText ? 8 : text.includes(submitText) ? 4 : 0;
                  const roleScore = tag === 'button' || role === 'button' ? 3 : 0;
                  const sizeScore = rect.width >= 40 && rect.width <= 180 && rect.height >= 24 && rect.height <= 70 ? 2 : 0;
                  return {node, text, rect, score: textScore + roleScore + sizeScore + colorScore(node)};
                })
                .filter(item => item.score >= 6)
                .sort((a, b) => b.score - a.score);

              if (candidates.length) {
                const best = candidates[0];
                const x = Math.min(Math.max(best.rect.left + best.rect.width / 2, 4), viewportWidth - 4);
                const y = Math.min(Math.max(best.rect.top + best.rect.height / 2, 4), viewportHeight - 4);
                const target = document.elementFromPoint(x, y) || best.node;
                target.dispatchEvent(new PointerEvent('pointerdown', {bubbles: true, clientX: x, clientY: y}));
                target.dispatchEvent(new MouseEvent('mousedown', {bubbles: true, clientX: x, clientY: y}));
                target.dispatchEvent(new PointerEvent('pointerup', {bubbles: true, clientX: x, clientY: y}));
                target.dispatchEvent(new MouseEvent('mouseup', {bubbles: true, clientX: x, clientY: y}));
                target.dispatchEvent(new MouseEvent('click', {bubbles: true, clientX: x, clientY: y}));
                return {
                  clicked: true,
                  strategy: 'shadow_or_light_dom_candidate',
                  x,
                  y,
                  text: best.text,
                  tag: best.node.tagName,
                  score: best.score,
                  hostRect: {x: hostRect.x, y: hostRect.y, width: hostRect.width, height: hostRect.height}
                };
              }

              return {
                clicked: false,
                reason: 'no deep candidate',
                shadowRoot: Boolean(host.shadowRoot),
                ownKeys: Object.keys(host).slice(0, 40),
                protoKeys: Object.getOwnPropertyNames(Object.getPrototypeOf(host)).slice(0, 80),
                hostRect: {x: hostRect.x, y: hostRect.y, width: hostRect.width, height: hostRect.height},
                scrollY: window.scrollY,
                submitText
              };
            }
            """
        )
        self.audit.event("publish_component_click", **result)
        return bool(result.get("clicked"))

    async def click_visible_publish_button(self) -> bool:
        result = await self.page.evaluate(
            """
            () => {
              const publishText = '发布';
              const viewportWidth = window.innerWidth || document.documentElement.clientWidth;
              const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
              const visibleRect = node => {
                const rect = node.getBoundingClientRect();
                const style = window.getComputedStyle(node);
                const visible = rect.width > 0 && rect.height > 0 &&
                  rect.bottom > 0 && rect.right > 0 &&
                  rect.top < viewportHeight && rect.left < viewportWidth &&
                  style.visibility !== 'hidden' && style.display !== 'none' &&
                  style.pointerEvents !== 'none';
                return visible ? rect : null;
              };
              const redScore = node => {
                const style = window.getComputedStyle(node);
                const colors = [style.backgroundColor, style.borderColor, style.color].join(' ');
                const nums = colors.match(/\\d+(?:\\.\\d+)?/g)?.map(Number) || [];
                let score = 0;
                for (let i = 0; i + 2 < nums.length; i += 3) {
                  const r = nums[i], g = nums[i + 1], b = nums[i + 2];
                  if (r > 180 && g < 120 && b < 140) score += 3;
                  if (r > g + 50 && r > b + 50) score += 1;
                }
                return score;
              };
              const textNodes = Array.from(document.querySelectorAll('button, [role="button"], div, span'))
                .filter(node => (node.innerText || node.textContent || '').trim() === publishText);
              const candidates = [];
              for (const node of textNodes) {
                let current = node;
                for (let depth = 0; current && depth < 5; depth += 1, current = current.parentElement) {
                  const rect = visibleRect(current);
                  if (!rect) continue;
                  const disabled = current.disabled || current.getAttribute('aria-disabled') === 'true' ||
                    current.className?.toString().includes('disabled');
                  if (disabled) continue;
                  candidates.push({
                    node: current,
                    rect,
                    score: redScore(current) + (rect.top > viewportHeight * 0.55 ? 4 : 0) +
                      (rect.width >= 50 && rect.width <= 180 ? 2 : 0) +
                      (rect.height >= 28 && rect.height <= 70 ? 2 : 0)
                  });
                }
              }
              candidates.sort((a, b) => b.score - a.score || b.rect.top - a.rect.top);
              const best = candidates[0];
              if (!best) return {clicked: false, reason: 'no visible publish candidate'};
              best.node.scrollIntoView({block: 'center', inline: 'center'});
              const rect = best.node.getBoundingClientRect();
              const x = Math.min(Math.max(rect.left + rect.width / 2, 4), viewportWidth - 4);
              const y = Math.min(Math.max(rect.top + rect.height / 2, 4), viewportHeight - 4);
              const target = document.elementFromPoint(x, y) || best.node;
              target.dispatchEvent(new MouseEvent('mouseover', {bubbles: true, clientX: x, clientY: y}));
              target.dispatchEvent(new MouseEvent('mousedown', {bubbles: true, clientX: x, clientY: y}));
              target.dispatchEvent(new MouseEvent('mouseup', {bubbles: true, clientX: x, clientY: y}));
              target.dispatchEvent(new MouseEvent('click', {bubbles: true, clientX: x, clientY: y}));
              return {
                clicked: true,
                x,
                y,
                text: best.node.innerText || best.node.textContent || '',
                tag: best.node.tagName,
                className: String(best.node.className || ''),
                score: best.score,
                rect: {x: rect.x, y: rect.y, width: rect.width, height: rect.height}
              };
            }
            """
        )
        self.audit.event("publish_button_dom_click", **result)
        return bool(result.get("clicked"))

    async def confirm_publish_if_needed(self) -> None:
        result = await self.page.evaluate(
            """
            () => {
              const labels = new Set(['确定', '确认', '继续发布', '发布']);
              const viewportWidth = window.innerWidth || document.documentElement.clientWidth;
              const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
              const nodes = Array.from(document.querySelectorAll('button, [role="button"], div, span'));
              const candidates = nodes.map(node => {
                const text = (node.innerText || node.textContent || '').trim();
                const rect = node.getBoundingClientRect();
                const style = window.getComputedStyle(node);
                return {node, text, rect, style};
              }).filter(item =>
                labels.has(item.text) &&
                item.rect.width > 0 && item.rect.height > 0 &&
                item.rect.top >= 0 && item.rect.left >= 0 &&
                item.rect.top < viewportHeight && item.rect.left < viewportWidth &&
                item.style.display !== 'none' && item.style.visibility !== 'hidden'
              ).sort((a, b) => {
                const aModal = a.node.closest('[role="dialog"], .d-modal, .el-dialog, [class*="modal"], [class*="dialog"]') ? 1 : 0;
                const bModal = b.node.closest('[role="dialog"], .d-modal, .el-dialog, [class*="modal"], [class*="dialog"]') ? 1 : 0;
                return bModal - aModal || b.rect.top - a.rect.top;
              });
              const best = candidates[0];
              if (!best || !best.node.closest('[role="dialog"], .d-modal, .el-dialog, [class*="modal"], [class*="dialog"]')) {
                return {clicked: false};
              }
              const x = best.rect.left + best.rect.width / 2;
              const y = best.rect.top + best.rect.height / 2;
              best.node.click();
              return {clicked: true, text: best.text, x, y};
            }
            """
        )
        self.audit.event("confirm_publish_if_needed", **result)

    async def _looks_logged_in(self) -> bool:
        try:
            return await any_visible(self.page, self.selectors["login_success_any"], timeout_ms=1800)
        except Exception:
            return False

    async def _best_effort_settle(self, timeout_ms: int) -> None:
        try:
            await self.page.wait_for_load_state("networkidle", timeout=timeout_ms)
        except Exception as exc:  # noqa: BLE001 - modern apps may keep long-lived requests open.
            self.audit.event("networkidle_timeout_ignored", timeout_ms=timeout_ms, error=str(exc))
            await human_delay(800, 1500)

    async def _page_contains(self, text: str) -> bool:
        if not text:
            return True
        try:
            await self.page.get_by_text(text, exact=False).first.wait_for(state="visible", timeout=1500)
            return True
        except Exception:
            pass
        try:
            return bool(
                await self.page.evaluate(
                    """
                    needle => {
                      const nodes = Array.from(document.querySelectorAll('input, textarea, [contenteditable="true"]'));
                      return nodes.some(node => {
                        const value = node.value || node.innerText || node.textContent || '';
                        return value.includes(needle);
                      }) || document.body.innerText.includes(needle);
                    }
                    """,
                    text,
                )
            )
        except Exception:
            try:
                html = await self.page.content()
            except Exception:
                return False
            return text in html


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"JSON root must be object: {path}")
    return payload
