#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多平台适配性与 DOM 结构诊断工具 (Platform Compatibility & DOM Diagnostics)
用于快速排查平台改版、网络超时、选择器失效等兼容性问题
"""

import os
import sys
import time
import argparse
from typing import Dict, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from platforms import get_platform, supported_platform_names

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("❌ 未检测到 Playwright 依赖，请在终端运行: pip install playwright && playwright install")
    sys.exit(1)


def diagnose_single_platform(platform_name: str, test_keyword: str = "科技", headless: bool = True, timeout: int = 15000) -> Dict:
    """诊断单个平台的首页连通性与搜索页 DOM 结构"""
    platform = get_platform(platform_name)
    if not platform:
        return {"platform": platform_name, "status": "ERROR", "message": f"不支持的平台: {platform_name}"}

    report = {
        "platform": platform.display_name,
        "name": platform.name,
        "home_url": platform.home_url,
        "home_status": "PENDING",
        "home_latency_ms": 0,
        "search_url": platform.get_search_url(test_keyword),
        "search_status": "PENDING",
        "captcha_detected": False,
        "selectors_status": {},
        "summary": "OK"
    }

    print(f"\n🔍 正在诊断平台: 【{platform.display_name}】 (测试关键词: '{test_keyword}')...")

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=headless, args=["--disable-blink-features=AutomationControlled"])
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            # 1. 检测首页连通性
            t0 = time.time()
            try:
                resp = page.goto(platform.home_url, wait_until="domcontentloaded", timeout=timeout)
                report["home_latency_ms"] = round((time.time() - t0) * 1000)
                status_code = resp.status if resp else 200
                report["home_status"] = f"SUCCESS (HTTP {status_code})"
                print(f"   ✅ 首页连通正常: 响应时间 {report['home_latency_ms']} ms")
            except Exception as e:
                report["home_status"] = f"FAILED ({e})"
                print(f"   ⚠️ 首页访问超时或网络异常: {e}")

            # 2. 检测搜索页面与选择器
            search_url = platform.get_search_url(test_keyword)
            try:
                page.goto(search_url, wait_until="domcontentloaded", timeout=timeout)
                time.sleep(2)
                report["search_status"] = "SUCCESS"
                print(f"   ✅ 搜索页加载成功: {search_url}")

                # 检查验证码
                has_captcha = platform.check_captcha(page)
                report["captcha_detected"] = has_captcha
                if has_captcha:
                    print("   🚨 触发了人机验证/滑块拦截")

                # 检查弹窗关闭
                platform.dismiss_popups(page)

                # 尝试解析博主卡片与元素
                # 这里只做探测性只读检查，不执行点击
                sample_cards = page.locator("div, li, ytd-channel-renderer, ytd-video-renderer").count()
                report["selectors_status"]["dom_nodes_found"] = sample_cards

            except Exception as e:
                report["search_status"] = f"FAILED ({e})"
                print(f"   ⚠️ 搜索页访问失败: {e}")

            browser.close()

        except Exception as ex:
            report["summary"] = f"ERROR: {ex}"
            print(f"   ❌ 诊断过程发生异常: {ex}")

    return report


def main():
    parser = argparse.ArgumentParser(description="多平台适配性与 DOM 结构诊断工具")
    parser.add_argument("-p", "--platform", type=str, default="all",
                        help="目标平台: douyin | xiaohongshu | bilibili | x | youtube | all (默认 all)")
    parser.add_argument("-k", "--keyword", type=str, default="数码科技",
                        help="诊断检索测试词")
    parser.add_argument("--headed", action="store_true",
                        help="以有头可视化窗口运行诊断")
    parser.add_argument("--timeout", type=int, default=15000,
                        help="页面超时时间 (毫秒)，默认 15000")

    args = parser.parse_args()

    targets = []
    if args.platform.lower() == "all":
        targets = ["douyin", "bilibili", "xiaohongshu", "x", "youtube"]
    else:
        targets = [args.platform]

    print("=" * 68)
    print("🩺 多平台适配性与网络连通健康诊断")
    print(f"📋 待诊断平台: {', '.join(targets)}")
    print("=" * 68)

    reports = []
    for plat in targets:
        rep = diagnose_single_platform(plat, test_keyword=args.keyword, headless=not args.headed, timeout=args.timeout)
        reports.append(rep)

    print("\n" + "=" * 68)
    print("📊 平台健康诊断报告汇总")
    print("=" * 68)
    for r in reports:
        print(f"【{r.get('platform', r.get('name'))}】")
        print(f"  - 首页状态: {r.get('home_status')} (延迟: {r.get('home_latency_ms', 0)}ms)")
        print(f"  - 搜索接口: {r.get('search_status')}")
        print(f"  - 验证码拦截: {'是' if r.get('captcha_detected') else '否'}")
    print("=" * 68)
    print("💡 提示：如果某个平台搜索页或首页提示 FAILED，请排查网络代理或运行 python3 scripts/start_chrome.py 复用本地登录环境。\n")


if __name__ == "__main__":
    main()
