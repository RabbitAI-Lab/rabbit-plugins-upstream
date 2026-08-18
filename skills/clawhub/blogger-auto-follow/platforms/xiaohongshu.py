# -*- coding: utf-8 -*-
"""
小红书 (RED) 平台自动化关注适配器 (支持主页直达链接抓取)
"""

import urllib.parse
from typing import Tuple, Dict
from .base import BasePlatform


class XiaohongshuPlatform(BasePlatform):
    name = "xiaohongshu"
    display_name = "小红书 (Xiaohongshu)"
    home_url = "https://www.xiaohongshu.com/"

    def get_search_url(self, blogger_name: str) -> str:
        return f"https://www.xiaohongshu.com/search_result?keyword={urllib.parse.quote(blogger_name)}&type=user"

    def dismiss_popups(self, page):
        close_selectors = [
            '.close-button',
            'div[class*="close"]',
            'svg[class*="close"]',
            'button:has-text("我知道了")'
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
            return page.locator('.captcha-modal, div[class*="captcha"]').count() > 0
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
            'div.user-item',
            'div[class*="user-item"]',
            'div[class*="user-card"]',
            'div[class*="author-card"]'
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

        # 提取个人主页链接
        if target_card:
            try:
                link_elem = target_card.locator('a[href*="/user/profile/"]').first
                if link_elem and link_elem.count() > 0:
                    href = link_elem.get_attribute("href") or ""
                    if href.startswith("/"):
                        meta["profile_url"] = "https://www.xiaohongshu.com" + href
                    elif href.startswith("http"):
                        meta["profile_url"] = href
                    # 提取 user id
                    meta["unique_id"] = href.split("/user/profile/")[-1].split("?")[0]
            except Exception:
                pass

        # 2. 检查是否已关注
        already_selectors = [
            'button:has-text("已关注")',
            'button:has-text("互相关注")',
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

        # 3. 查找“关注”按钮
        all_btns = scope.locator('button, div[role="button"]').all()
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

        return "NOT_FOUND", "未找到匹配博主或关注按钮", meta
