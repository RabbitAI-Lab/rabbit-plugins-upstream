# -*- coding: utf-8 -*-
"""
抖音平台自动化关注适配器 (支持博主主页直达链接抓取)
"""

import urllib.parse
from typing import Tuple, Dict
from .base import BasePlatform


class DouyinPlatform(BasePlatform):
    name = "douyin"
    display_name = "抖音 (Douyin)"
    home_url = "https://www.douyin.com/"

    def get_search_url(self, blogger_name: str) -> str:
        return f"https://www.douyin.com/search/{urllib.parse.quote(blogger_name)}?type=user"

    def dismiss_popups(self, page):
        close_selectors = [
            'div[class*="close"]',
            'svg[class*="close"]',
            'div[data-e2e="modal-close-icon"]',
            '.dy-account-close',
            'button:has-text("我知道了")',
            'button:has-text("稍后再说")'
        ]
        for sel in close_selectors:
            try:
                for b in page.locator(sel).all():
                    if b.is_visible():
                        b.click(timeout=800)
            except Exception:
                pass

    def check_captcha(self, page) -> bool:
        try:
            loc = page.locator(".secsdk-captcha-drag-icon, #captcha-verify-image, .captcha_verify_container, div[class*='captcha']")
            return loc.count() > 0
        except Exception:
            return False

    def handle_follow(self, page, blogger_name: str) -> Tuple[str, str, Dict]:
        self.dismiss_popups(page)
        self.human_sleep(3.5, 5.5)

        meta = {
            "profile_url": "",
            "unique_id": "",
            "bio": ""
        }

        # 1. 查找用户卡片
        card_selectors = [
            'div[data-e2e="search-user-item"]',
            'div[class*="user-card"]',
            'div[class*="user-info-card"]',
            'div[class*="search-result-card"]',
            'li[class*="user-item"]'
        ]
        cards = []
        for sel in card_selectors:
            try:
                found = page.locator(sel).all()
                if found:
                    cards = found
                    break
            except Exception:
                pass

        target_card = None
        if cards:
            for c in cards[:4]:
                try:
                    text = c.inner_text()
                    if blogger_name in text or any(k in text for k in blogger_name.split() if len(k) > 1):
                        target_card = c
                        break
                except Exception:
                    pass
            if not target_card and len(cards) > 0:
                target_card = cards[0]

        scope = target_card if target_card else page

        # 提取主页链接与简介
        if target_card:
            try:
                link_elem = target_card.locator('a[href*="/user/"], a[href^="//www.douyin.com/user/"]').first
                if link_elem and link_elem.count() > 0:
                    href = link_elem.get_attribute("href") or ""
                    if href.startswith("//"):
                        meta["profile_url"] = "https:" + href
                    elif href.startswith("/"):
                        meta["profile_url"] = "https://www.douyin.com" + href
                    elif href.startswith("http"):
                        meta["profile_url"] = href
            except Exception:
                pass

            try:
                card_text = target_card.inner_text()
                # 尝试提取抖音号
                for line in card_text.split("\n"):
                    if "抖音号：" in line or "抖音号:" in line:
                        meta["unique_id"] = line.replace("抖音号：", "").replace("抖音号:", "").strip()
            except Exception:
                pass

        # 2. 检查是否已关注
        already_selectors = [
            'button:has-text("已关注")',
            'button:has-text("互相关注")',
            'button:has-text("特别关注")',
            'div[role="button"]:has-text("已关注")',
            'div[role="button"]:has-text("互相关注")',
            'span:text-is("已关注")',
            'span:text-is("互相关注")'
        ]
        for sel in already_selectors:
            try:
                for m in scope.locator(sel).all():
                    if m.is_visible():
                        status_text = m.inner_text().strip()
                        return "ALREADY_FOLLOWED", f"已处于关注状态 ({status_text})", meta
            except Exception:
                pass

        # 3. 查找“关注”按钮并点击
        all_btns = scope.locator('button, div[role="button"], span[class*="follow"]').all()
        for btn in all_btns:
            try:
                if btn.is_visible():
                    txt = btn.inner_text().strip()
                    if txt in ["关注", "+ 关注", "+关注", "加关注"]:
                        btn.scroll_into_view_if_needed()
                        self.human_sleep(1.0, 1.8)
                        btn.click()
                        self.human_sleep(2.0, 3.5)
                        try:
                            new_text = btn.inner_text().strip()
                            return "SUCCESS", f"关注成功 ({new_text})", meta
                        except Exception:
                            return "SUCCESS", "已点击关注", meta
            except Exception:
                pass

        # 全局匹配备选
        try:
            for btn in page.locator('button:text-is("关注")').all():
                if btn.is_visible():
                    btn.scroll_into_view_if_needed()
                    self.human_sleep(1.0, 1.8)
                    btn.click()
                    self.human_sleep(2.0, 3.0)
                    return "SUCCESS", "已点击关注", meta
        except Exception:
            pass

        return "NOT_FOUND", "未找到匹配用户或关注按钮", meta
