#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通用多平台博主批量自动添加/关注工具 (全行业支持 / 防风控安全版)
- 支持各平台手动扫码/密码/短信登录确认（不限时等待，登录成功按回车继续）
- 超低频拟人化操作（默认 10~18 秒随机间隔 + 阶段性深度休眠，强力防风控）
- 自动提取博主主页直达 URL 与唯一 UID 并智能归入全行业资产库
- 自动生成/同步 data/FOLLOWED_BLOGGERS.md 全行业导航手册
"""

import os
import sys
import json
import time
import random
import argparse
import platform

# 导入平台与存储模块
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from platforms import get_platform, supported_platform_names
from storage import BloggerDB

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("❌ 未检测到 Playwright 依赖，请在终端运行: pip install playwright && playwright install")
    sys.exit(1)


def parse_arguments():
    parser = argparse.ArgumentParser(description="多平台博主批量自动关注工具 (全行业防风控安全版)")
    parser.add_argument("-p", "--platform", type=str, required=True,
                        help="目标平台: douyin | xiaohongshu | bilibili | x | youtube")
    parser.add_argument("-f", "--file", type=str, default="examples/douyin_34_bloggers_example.json",
                        help="博主 JSON 文件路径")
    parser.add_argument("-n", "--names", type=str, default="",
                        help="直接指定博主名称，多个用英文逗号分隔 (优先级高于 --file)")
    parser.add_argument("-i", "--industry", type=str, default="",
                        help="指定这批博主的行业大类 (若留空则自动智能推断)")
    parser.add_argument("--min-delay", type=float, default=10.0,
                        help="每个博主处理后的最小休息时间(秒)，默认 10.0")
    parser.add_argument("--max-delay", type=float, default=18.0,
                        help="每个博主处理后的最大休息时间(秒)，默认 18.0")
    parser.add_argument("--batch-size", type=int, default=5,
                        help="触发深度休眠的连续博主数，默认 5")
    parser.add_argument("--deep-sleep-min", type=float, default=20.0,
                        help="深度休眠最小时间(秒)，默认 20.0")
    parser.add_argument("--deep-sleep-max", type=float, default=35.0,
                        help="深度休眠最大时间(秒)，默认 35.0")
    parser.add_argument("--cdp-port", type=int, default=9222,
                        help="Chrome 调试端口，默认 9222")
    return parser.parse_args()


def load_bloggers_data(file_path: str, names_str: str, default_industry: str = ""):
    if names_str.strip():
        names = [n.strip() for n in names_str.split(",") if n.strip()]
        return [{"id": i + 1, "name": name, "industry": default_industry, "category": "默认", "fans": ""} for i, name in enumerate(names)]

    candidates = [
        file_path,
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), file_path),
        os.path.join(os.getcwd(), file_path)
    ]
    target_file = None
    for cand in candidates:
        if os.path.exists(cand):
            target_file = cand
            break

    if not target_file:
        print(f"❌ 找不到博主数据文件: {file_path}")
        sys.exit(1)

    with open(target_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        if isinstance(data, list):
            if default_industry:
                for item in data:
                    if not item.get("industry"):
                        item["industry"] = default_industry
            return data
        else:
            print("❌ 数据文件格式错误，必须为博主列表 JSON 数组。")
            sys.exit(1)


def safe_goto(page, url: str, max_retries: int = 2, timeout: int = 35000) -> bool:
    """具备自动重试与友好排查指引的页面导航函数"""
    for attempt in range(1, max_retries + 1):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=timeout)
            return True
        except Exception as e:
            if attempt < max_retries:
                print(f"   ⚠️ 网络连接波动/加载超时 (第 {attempt} 次重试中...): {e}")
                time.sleep(2.5)
            else:
                print(f"   ❌ 页面加载超时或失败: {e}")
                print("   💡 排查建议: 请检查本地网络/Wi-Fi，若为海外平台 (X/YouTube) 请检查系统代理或科学上网分流规则。")
                return False
    return False


def handle_captcha_interactive(page, target_platform, blogger_name: str) -> str:
    """
    交互式验证码处理流程
    返回指令: 'CONTINUE' | 'RETRY' | 'SKIP' | 'QUIT'
    """
    print("\a", end="")  # 触发终端提示音
    print("\n" + "╔" + "═" * 66 + "╗")
    print("║ 🚨【平台安全风控提示】检测到人机验证（滑块拼图 / 点选 / 短信验证）║")
    print("╠" + "═" * 66 + "╣")
    print(f"║ 目标平台: {target_platform.display_name:<20} 正在检索: {blogger_name:<20} ║")
    print("║                                                                  ║")
    print("║ 👉 请在弹出的浏览器窗口中【手动完成验证】。                      ║")
    print("║ 完成后请选择下一步操作:                                          ║")
    print("║   - 直接按 [Enter 回车] 或输入 'c': 已完成验证，继续处理该博主   ║")
    print("║   - 输入 'r' 并按回车:             刷新页面重新检测              ║")
    print("║   - 输入 's' 并按回车:             跳过当前博主，处理下一位      ║")
    print("║   - 输入 'q' 并按回车:             安全保存并退出任务            ║")
    print("╚" + "═" * 66 + "╝\n")

    choice = input("👉 请输入操作选项 [Enter/r/s/q]: ").strip().lower()
    if choice in ["", "c", "continue"]:
        time.sleep(2)
        return "CONTINUE"
    elif choice in ["r", "retry"]:
        return "RETRY"
    elif choice in ["s", "skip"]:
        return "SKIP"
    elif choice in ["q", "quit", "exit"]:
        return "QUIT"
    else:
        return "CONTINUE"


def main():
    args = parse_arguments()
    target_platform = get_platform(args.platform)

    if not target_platform:
        print(f"❌ 不支持的平台: '{args.platform}'")
        print("💡 当前支持的平台清单:")
        for sp in supported_platform_names():
            print(f"   - {sp}")
        sys.exit(1)

    bloggers = load_bloggers_data(args.file, args.names, args.industry)
    db = BloggerDB()

    print("=" * 68)
    print(f"   🚀 全行业博主批量自动添加工具 -> 当前平台: 【{target_platform.display_name}】")
    print(f"   🛡️ 已启用【超低频拟人防风控模式】(间隔: {args.min_delay}~{args.max_delay}s | 深度休眠: {args.deep_sleep_min}~{args.deep_sleep_max}s)")
    print(f"   💾 全行业资产库同步开启: data/followed_bloggers.json & FOLLOWED_BLOGGERS.md")
    print("=" * 68)
    print(f"📋 共加载了 {len(bloggers)} 位博主待处理。\n")

    current_os = platform.system()
    cdp_url = f"http://127.0.0.1:{args.cdp_port}"
    user_data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f".browser_data_{target_platform.name}")

    results = []

    with sync_playwright() as p:
        browser = None
        context = None

        # 1. 尝试接管本地 Chrome 调试端口
        try:
            print(f"🔌 尝试接管本地 Chrome 浏览器 (CDP: {cdp_url})...")
            browser = p.chromium.connect_over_cdp(cdp_url, timeout=3000)
            context = browser.contexts[0] if browser.contexts else browser.new_context()
            print("✅ 成功接管本地 Chrome 浏览器！直接复用您的登录环境与指纹。")
        except Exception:
            print(f"ℹ️ 未检测到已开启 {args.cdp_port} 调试端口的本地 Chrome。")
            print(f"👉 启动独立 Chrome 窗口 (运行系统: {current_os} | 会话目录: .browser_data_{target_platform.name})...")
            
            os.makedirs(user_data_dir, exist_ok=True)
            context = p.chromium.launch_persistent_context(
                user_data_dir=user_data_dir,
                headless=False,
                channel="chrome",
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-first-run",
                    "--no-default-browser-check",
                    "--start-maximized"
                ],
                viewport=None
            )

        page = context.pages[0] if context.pages else context.new_page()

        # 打开该平台首页
        print(f"\n🌐 正在打开【{target_platform.display_name}】首页: {target_platform.home_url}")
        safe_goto(page, target_platform.home_url, max_retries=2, timeout=45000)
        time.sleep(2)

        # ⭐️ 各平台手动扫码/密码登录确认（不限时等待）
        print("\n" + "╔" + "═" * 64 + "╗")
        print(f"║        📢 请在弹出的浏览器中登录【{target_platform.display_name}】 (不限时等待)         ║")
        print("╠" + "═" * 64 + "╣")
        print("║ 1. 您可以使用【扫码登录】、【账号密码】或【短信验证码】登录    ║")
        print("║ 2. 完成登录后，请确认能看到您自己的头像与个人主页             ║")
        print("║ 3. 准备就绪后，回到本终端，按 【Enter 回车键】 正式开始批量关注 ║")
        print("╚" + "═" * 64 + "╝\n")

        input("👉 完成登录后，请按 [Enter 回车键] 开始自动关注: ")
        print(f"\n🚀 收到启动确认！开始以【超低频拟人安全保护模式】逐一关注...\n")

        # 逐个处理博主
        aborted_early = False
        for idx, item in enumerate(bloggers, 1):
            name = item.get("name", "").strip()
            ind = item.get("industry", "")
            category = item.get("category", "默认")
            fans = item.get("fans", "")

            if not name:
                continue

            print("-" * 68)
            print(f"进度: [{idx}/{len(bloggers)}] | 平台: {target_platform.display_name} | 博主: 【{name}】 | 分类: {category}")

            search_url = target_platform.get_search_url(name)
            print(f"🔍 检索链接: {search_url}")

            nav_ok = safe_goto(page, search_url, max_retries=2, timeout=35000)
            if not nav_ok:
                results.append({
                    "id": item.get("id", idx),
                    "name": name,
                    "industry": ind,
                    "category": category,
                    "platform": target_platform.name,
                    "profile_url": "",
                    "fans": fans,
                    "status": "TIMEOUT",
                    "message": "页面加载超时/网络波动",
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                })
                continue

            # 检查是否有滑块或人机验证
            if target_platform.check_captcha(page):
                captcha_action = handle_captcha_interactive(page, target_platform, name)
                if captcha_action == "QUIT":
                    print("🛑 用户选择退出任务，正在保存已处理的资产...")
                    aborted_early = True
                    break
                elif captcha_action == "SKIP":
                    print(f"⏩ 已跳过博主 【{name}】")
                    results.append({
                        "id": item.get("id", idx),
                        "name": name,
                        "industry": ind,
                        "category": category,
                        "platform": target_platform.name,
                        "profile_url": "",
                        "fans": fans,
                        "status": "SKIPPED_CAPTCHA",
                        "message": "用户手动跳过验证码",
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                    })
                    continue
                elif captcha_action == "RETRY":
                    safe_goto(page, search_url, max_retries=2, timeout=35000)
                    time.sleep(2)

            # 执行智能识别与关注
            meta = {"profile_url": "", "unique_id": "", "bio": ""}
            try:
                status, msg, meta = target_platform.handle_follow(page, name)
            except Exception as ex:
                status, msg = "FAILED", str(ex)
                print(f"   ❌ 操作异常: {ex}")

            if status == "SUCCESS":
                print(f"   🎉 状态: {msg}")
            elif status == "ALREADY_FOLLOWED":
                print(f"   📌 状态: {msg}")
            elif status == "NOT_FOUND":
                print(f"   ⚠️ 状态: {msg}")
            else:
                print(f"   ❌ 状态: {msg}")

            if meta.get("profile_url"):
                print(f"   🔗 抓取到主页直达链接: {meta['profile_url']}")

            # 增量存入本地博主资产库
            db_record = {
                "name": name,
                "industry": ind,
                "platform": target_platform.name,
                "profile_url": meta.get("profile_url", ""),
                "unique_id": meta.get("unique_id", ""),
                "category": category,
                "fans": fans,
                "bio": meta.get("bio", ""),
                "status": status
            }
            saved_record = db.upsert_blogger(db_record)

            results.append({
                "id": item.get("id", idx),
                "name": name,
                "industry": saved_record.get("industry", ""),
                "category": category,
                "platform": target_platform.name,
                "profile_url": meta.get("profile_url", ""),
                "fans": fans,
                "status": status,
                "message": msg,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })

            # 防风控与超低频拟人休眠
            if idx < len(bloggers):
                delay = round(random.uniform(args.min_delay, args.max_delay), 1)
                if idx % args.batch_size == 0:
                    deep_sleep = round(random.uniform(args.deep_sleep_min, args.deep_sleep_max), 1)
                    print(f"☕ 已连续安全处理 {args.batch_size} 位博主，正在执行深度休眠 {deep_sleep} 秒（模拟人类浏览与休息）...")
                    time.sleep(deep_sleep)
                else:
                    print(f"⏳ 拟人安全间隔等待 {delay} 秒后处理下一位博主...")
                    time.sleep(delay)

        print("\n" + "=" * 68)
        processed_count = len(results)
        if aborted_early:
            print(f"⏸️ 【{target_platform.display_name}】任务已暂停 (已处理 {processed_count}/{len(bloggers)} 位博主)")
        else:
            print(f"🎉 【{target_platform.display_name}】共 {len(bloggers)} 位博主全部处理完毕！")
        print("=" * 68)

        success_cnt = sum(1 for r in results if r["status"] == "SUCCESS")
        already_cnt = sum(1 for r in results if r["status"] == "ALREADY_FOLLOWED")
        not_found_cnt = sum(1 for r in results if r["status"] == "NOT_FOUND")
        skipped_cnt = sum(1 for r in results if r["status"] == "SKIPPED_CAPTCHA")
        timeout_cnt = sum(1 for r in results if r["status"] == "TIMEOUT")
        failed_cnt = sum(1 for r in results if r["status"] == "FAILED")

        print(f"\n📊 关注统计结果汇总：")
        print(f"   ✅ 本次新增关注:     {success_cnt} 位")
        print(f"   📌 此前已处于关注:   {already_cnt} 位 (自动跳过，防止误取消)")
        print(f"   ⚠️ 未搜到对应博主:   {not_found_cnt} 位")
        if skipped_cnt > 0:
            print(f"   ⏩ 验证码跳过博主:   {skipped_cnt} 位")
        if timeout_cnt > 0:
            print(f"   ⏳ 网络超时博主:     {timeout_cnt} 位")
        print(f"   ❌ 执行异常/失败:    {failed_cnt} 位")
        print(f"\n💾 本地资产数据库已更新: data/followed_bloggers.json")
        print(f"📄 全行业主页直达导航手册已同步: data/FOLLOWED_BLOGGERS.md")
        print("\n浏览器将保持开启，方便您在网页端核验关注列表。")


if __name__ == "__main__":
    main()
