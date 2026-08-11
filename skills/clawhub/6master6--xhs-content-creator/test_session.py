"""独立验证脚本：检查修改后的 BrowserSession 是否真的覆盖了指纹。"""
import asyncio
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR
sys.path.insert(0, str(PROJECT_ROOT))

from src.browser_session import BrowserSession


async def main():
    print("=== 启动 BrowserSession（用现有 profile）===")
    profile_dir = PROJECT_ROOT / "runtime" / "browser-profile"
    async with BrowserSession(
        profile_dir=profile_dir,
        headless=True,
        slow_mo_ms=0,
        audit=None,
    ) as session:
        page = session.page

        # 1. 创建一个空白页（不访问 XHS，避免触发 XHS 风控）
        await page.goto("about:blank")

        print()
        print("=== 1. navigator.webdriver ===")
        wd = await page.evaluate("() => navigator.webdriver")
        print(f"  navigator.webdriver = {wd!r}")
        print(f"  {'✓ PASS' if wd is None else '✗ FAIL'}")

        print()
        print("=== 2. window.chrome ===")
        chrome_exists = await page.evaluate("() => typeof window.chrome === 'object'")
        chrome_runtime = await page.evaluate("() => typeof (window.chrome && window.chrome.runtime)")
        chrome_csi = await page.evaluate("() => typeof (window.chrome && window.chrome.csi)")
        print(f"  window.chrome exists: {chrome_exists}")
        print(f"  chrome.runtime type: {chrome_runtime}")
        print(f"  chrome.csi type: {chrome_csi}")
        print(f"  {'✓ PASS' if chrome_exists and chrome_runtime == 'object' and chrome_csi == 'function' else '✗ FAIL'}")

        print()
        print("=== 3. UA ===")
        ua = await page.evaluate("() => navigator.userAgent")
        print(f"  navigator.userAgent = {ua!r}")
        print(f"  {'✓ PASS (Mac Chrome)' if 'Macintosh' in ua and 'Chrome/126' in ua else '✗ FAIL'}")

        print()
        print("=== 4. Playwright 痕迹清理 ===")
        traces = await page.evaluate("""() => {
            return ['__webdriver_evaluate', '__driver_evaluate', '__selenium_evaluate', 
                    '__selenium_unwrap', '_Selenium_IDE_Recorder', '__fxdriver_evaluate',
                    '__driver_unwrap', 'domAutomation', 'domAutomationController'].filter(k => k in window);
        }""")
        print(f"  residual playwright traces: {traces}")
        print(f"  {'✓ PASS' if not traces else '✗ FAIL'}")

        print()
        print("=== 5. Client Hints headers（实际请求发出的） ===")
        # 用一个不可达域名，捕获请求 headers
        captured = []
        async def handle_request(req):
            captured.append(dict(req.headers))
        page.on("request", lambda r: asyncio.create_task(handle_request(r)))
        try:
            await page.goto("http://127.0.0.1:1/test", timeout=3000)
        except Exception:
            pass
        if captured:
            hdrs = captured[0]
            for k in ["user-agent", "sec-ch-ua", "sec-ch-ua-mobile", "sec-ch-ua-platform"]:
                v = hdrs.get(k, "<MISSING>")
                print(f"  {k}: {v[:120] if isinstance(v, str) else v}")
        else:
            print("  (no request captured, skip)")

        print()
        print("=== 6. plugins + languages ===")
        plugins_len = await page.evaluate("() => navigator.plugins.length")
        langs = await page.evaluate("() => navigator.languages")
        print(f"  navigator.plugins.length: {plugins_len}")
        print(f"  navigator.languages: {langs}")
        print(f"  {'✓ PASS' if plugins_len > 0 and 'zh-CN' in langs else '⚠ partial'}")


if __name__ == "__main__":
    asyncio.run(main())