const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');
const { execSync } = require('child_process');

/**
 * 参数解析
 * 用法: node export_image.js <html> <output.png> [width] [--author "作者信息" | --no-footer]
 *
 * --author "文字"   在图片底部注入自定义 footer（覆盖 HTML 中已有的 .footer 内容）
 * --no-footer       完全移除 footer 区域
 * 不传任何 footer 参数：保留 HTML 原有内容（AI 生成时已按规范写入）
 */
const args = process.argv.slice(2);

const inputHtml  = args[0];
const outputImg  = args[1];
const width      = parseInt(args[2]) || 600;

let authorText  = null;   // null = 不注入，使用 HTML 原有内容
let noFooter    = false;

for (let i = 3; i < args.length; i++) {
    if (args[i] === '--no-footer') {
        noFooter = true;
    } else if (args[i] === '--author' && args[i + 1]) {
        authorText = args[i + 1];
        i++;
    }
}

if (!inputHtml || !outputImg) {
    console.error('Usage: node export_image.js <html> <output.png> [width] [--author "文字" | --no-footer]');
    process.exit(1);
}

function detectChromePath() {
    const candidates = [
        '/usr/bin/google-chrome',
        '/usr/bin/google-chrome-stable',
        '/usr/bin/chromium',
        '/usr/bin/chromium-browser',
        '/snap/bin/chromium',
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '/Applications/Chromium.app/Contents/MacOS/Chromium',
        '/mnt/c/Program Files/Google/Chrome/Application/chrome.exe',
    ];
    for (const p of candidates) {
        if (fs.existsSync(p)) return p;
    }
    try {
        const r = execSync('which google-chrome chromium chromium-browser 2>/dev/null | head -1', { encoding: 'utf8' }).trim();
        if (r) return r;
    } catch (_) {}
    return null;
}

const htmlUrl    = inputHtml.startsWith('http') ? inputHtml : `file://${path.resolve(inputHtml)}`;
const outputPath = path.resolve(outputImg);

const outputDir = path.dirname(outputPath);
if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

(async () => {
    const chromePath = detectChromePath();
    if (!chromePath) {
        console.error('[ERROR] 未找到 Chrome/Chromium，请先运行 bash scripts/setup.sh');
        process.exit(1);
    }
    console.log(`[INFO] 浏览器: ${chromePath}`);

    try {
        const browser = await puppeteer.launch({
            executablePath: chromePath,
            headless: 'new',
            args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
            defaultViewport: { width, height: 1000, deviceScaleFactor: 2 }
        });

        const page = await browser.newPage();
        await page.goto(htmlUrl, { waitUntil: 'networkidle0', timeout: 30000 });

        // ── Footer 注入逻辑 ──────────────────────────────────
        if (noFooter) {
            // 移除所有 footer 元素
            await page.evaluate(() => {
                document.querySelectorAll('.footer, footer, [data-footer]').forEach(el => el.remove());
            });
            console.log('[INFO] Footer 已移除');
        } else if (authorText !== null) {
            // 替换 footer 文字；如果页面没有 .footer 则追加一个
            await page.evaluate((text) => {
                const existing = document.querySelector('.footer, footer, [data-footer]');
                if (existing) {
                    existing.textContent = text;
                } else {
                    const container = document.querySelector('.container') || document.body;
                    const div = document.createElement('div');
                    div.className = 'footer';
                    div.style.cssText = 'text-align:center;padding-top:16px;font-size:0.75em;opacity:0.5;';
                    div.textContent = text;
                    container.appendChild(div);
                }
            }, authorText);
            console.log(`[INFO] Footer 已设置为：${authorText}`);
        }
        // authorText === null：不做任何操作，保留 HTML 原有 footer

        // ── 精确测量内容高度，裁掉底部多余空白 ────────────────
        const contentHeight = await page.evaluate(() => {
            // 优先测量 .container，没有则测量 body 实际内容高度
            const container = document.querySelector('.container');
            if (container) {
                const rect = container.getBoundingClientRect();
                // 加上容器距顶的偏移 + 自身高度，再加 2px 安全边距
                return Math.ceil(rect.top + rect.height) + 2;
            }
            // fallback：body scrollHeight
            return document.body.scrollHeight;
        });
        console.log(`[INFO] 内容高度: ${contentHeight}px（视口宽度 ${width}px）`);

        // 设置视口高度为内容高度，避免 fullPage 截到多余空白
        await page.setViewport({ width, height: contentHeight, deviceScaleFactor: 2 });

        await page.screenshot({
            path: outputPath,
            clip: { x: 0, y: 0, width, height: contentHeight }
        });
        await browser.close();
        console.log(`[SUCCESS] 长图已导出至：${outputPath}`);
    } catch (error) {
        console.error('[ERROR] 截图导出失败:', error.message);
        console.error('[FALLBACK] 在浏览器中手动打开：', htmlUrl);
        process.exit(1);
    }
})();
