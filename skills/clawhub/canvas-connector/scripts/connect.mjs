#!/usr/bin/env node
/**
 * 画布连接器 · 连接信息脚本（无任何危险调用：只做下载/检测/读取/输出）
 * 用法：node connect.mjs [--canvas https://你的画布域名] [--port 17371] [--source <连接器下载地址或本地路径>]
 * 输出（JSON 单行）：
 *   { ok:true, url, token, pageUrl, alreadyRunning, needStart:false }         连接器已在运行
 *   { ok:false, needStart:true, startCommand:"nohup node … &" }               需要先启动连接器
 */
import { copyFileSync, existsSync, readFileSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const arg = (name, fallback = "") => {
    const index = args.indexOf(name);
    return index !== -1 && args[index + 1] ? args[index + 1] : fallback;
};

const port = Number(arg("--port", "17371"));
const canvas = arg("--canvas", "").replace(/\/$/, "");
const source = arg("--source", "https://aicanvas.miaotuntu.com/downloads/lobster-canvas-agent.mjs");
const configDir = join(homedir(), ".infinite-canvas");
const configFile = join(configDir, "canvas-agent.json");
const target = join(configDir, "canvas-agent.mjs");
const url = `http://127.0.0.1:${port}`;

const health = async () => {
    try {
        const res = await fetch(`${url}/health`, { signal: AbortSignal.timeout(1500) });
        return res.ok;
    } catch {
        return false;
    }
};

const readToken = () => {
    try {
        return String(JSON.parse(readFileSync(configFile, "utf8")).token || "");
    } catch {
        return "";
    }
};

const pageUrl = (token) => (canvas ? `${canvas}/app/#agentUrl=${encodeURIComponent(url)}&agentToken=${encodeURIComponent(token)}` : "");

if (await health()) {
    const token = readToken();
    console.log(JSON.stringify({ ok: true, url, token, pageUrl: pageUrl(token), alreadyRunning: true, needStart: false }));
    process.exit(0);
}

// 未在运行：确保连接器文件就位（本地路径直接拷贝；否则从分发地址下载）
try {
    if (source.startsWith("/") || source.startsWith(".")) {
        copyFileSync(resolve(source), target);
    } else {
        const res = await fetch(source, { signal: AbortSignal.timeout(60000) });
        if (!res.ok) throw new Error(`下载失败 HTTP ${res.status}`);
        const { writeFileSync, mkdirSync } = await import("node:fs");
        mkdirSync(configDir, { recursive: true });
        writeFileSync(target, Buffer.from(await res.arrayBuffer()));
    }
} catch (error) {
    console.log(JSON.stringify({ ok: false, needStart: false, error: `连接器文件准备失败：${error instanceof Error ? error.message : error}` }));
    process.exit(1);
}

console.log(JSON.stringify({
    ok: false,
    needStart: true,
    url,
    connectorFile: target,
    startCommand: `nohup node ${target} >> ${join(configDir, "connector.log")} 2>&1 &`,
    hint: "启动后等待约 2 秒，再次运行本脚本即可获得 pageUrl（自动连接链接）",
}));
