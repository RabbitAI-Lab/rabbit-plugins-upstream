#!/usr/bin/env node
/**
 * buildkey_direct.js —— 直接取出 at-rest build key（atRestSecretKey）
 *
 * 与 extract_buildkey.js / buildkey_cdp.js 的区别：
 *   - extract_buildkey.js 走 CDP：要给**正在运行**的客户端主进程开 V8 inspector
 *     （process._debugProcess 固定占用 9229），需要先找到主进程 PID，且可能撞端口。
 *   - 本脚本**不碰常驻客户端**：直接以 ELECTRON_RUN_AS_NODE 模式启动客户端自带的
 *     Electron/WorkBuddy 二进制，进程内调用原生绑定
 *       process._linkedBinding("electron_browser_workbuddy_storage").loggerGet()
 *     拿回 build key，进程随即退出。无需调试端口、无需找 PID、无需 GUI。
 *
 * 为什么不能用 require('electron')：
 *   RUN_AS_NODE 模式下没有 electron 模块，只有 process._linkedBinding 能拿到该绑定。
 *
 * 前置条件：已安装 WorkBuddy（或 CodeBuddy）**桌面端**（不必处于运行状态）；
 *          本脚本需要 Node.js 20+（内置 fetch 无关，仅用 child_process）。
 *
 * 用法:
 *   node buildkey_direct.js                 # 自动探测客户端 → 写 scripts/at_rest_buildkey.json
 *   node buildkey_direct.js --out <path>    # 指定输出路径
 *   node buildkey_direct.js --app <bin>     # 显式指定客户端可执行文件
 *   node buildkey_direct.js --show          # 额外打印完整密钥（默认只打印掩码）
 *   node buildkey_direct.js --json          # 只输出一行 JSON 结果，便于脚本消费
 *
 * 环境变量:
 *   WB_APP_BINARY   等价于 --app
 *
 * 退出码: 0 成功；1 失败。
 */
"use strict";

const fs = require("fs");
const os = require("os");
const path = require("path");
const { spawnSync } = require("child_process");

const HERE = __dirname;

// ---------------------------------------------------------------- 参数解析
function parseArgs(argv) {
  const out = { app: process.env.WB_APP_BINARY || "", out: "", show: false, json: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--app") out.app = argv[++i] || "";
    else if (a === "--out") out.out = argv[++i] || "";
    else if (a === "--show") out.show = true;
    else if (a === "--json") out.json = true;
    else if (a === "-h" || a === "--help") {
      console.log(fs.readFileSync(__filename, "utf8").split("*/")[0].replace(/^\/\*\*?/, ""));
      process.exit(0);
    }
  }
  return out;
}

// ------------------------------------------------- 客户端可执行文件候选路径
function appCandidates() {
  const c = [];
  const home = os.homedir();
  if (process.platform === "darwin") {
    c.push("/Applications/WorkBuddy.app/Contents/MacOS/Electron");
    c.push(path.join(home, "Applications/WorkBuddy.app/Contents/MacOS/Electron"));
    c.push("/Applications/CodeBuddy.app/Contents/MacOS/Electron");
    c.push(path.join(home, "Applications/CodeBuddy.app/Contents/MacOS/Electron"));
  } else if (process.platform === "win32") {
    const la = process.env.LOCALAPPDATA || "";
    const pf = process.env.ProgramFiles || "C:\\Program Files";
    const pf86 = process.env["ProgramFiles(x86)"] || "C:\\Program Files (x86)";
    if (la) {
      c.push(path.join(la, "Programs", "WorkBuddy", "WorkBuddy.exe"));
      c.push(path.join(la, "Programs", "CodeBuddy", "CodeBuddy.exe"));
    }
    c.push(path.join(pf, "WorkBuddy", "WorkBuddy.exe"));
    c.push(path.join(pf, "CodeBuddy", "CodeBuddy.exe"));
    c.push(path.join(pf86, "WorkBuddy", "WorkBuddy.exe"));
  } else {
    c.push("/opt/WorkBuddy/workbuddy");
    c.push("/usr/lib/workbuddy/workbuddy");
    c.push("/usr/bin/workbuddy");
    c.push("/opt/CodeBuddy/codebuddy");
  }
  return c;
}

function resolveApp(explicit) {
  const tried = [];
  if (explicit) {
    if (fs.existsSync(explicit)) return { bin: explicit, tried };
    tried.push(explicit + "（不存在）");
  }
  for (const p of appCandidates()) {
    tried.push(p);
    if (fs.existsSync(p)) return { bin: p, tried };
  }
  return { bin: "", tried };
}

// ------------------------------------------------- 子进程：仅做「取绑定」这一件事
// 输出协议：成功 -> WBKEY:<payload json>；失败 -> WBKEY_ERR:<message>
const CHILD_CODE = [
  "try {",
  "  var b = process._linkedBinding('electron_browser_workbuddy_storage');",
  "  var r = typeof b.loggerGet === 'function' ? b.loggerGet() : b.loggerGet;",
  "  var s = Buffer.isBuffer(r) ? r.toString('utf8') : String(r);",
  "  process.stdout.write('WBKEY:' + s);",
  "} catch (e) {",
  "  process.stdout.write('WBKEY_ERR:' + ((e && e.message) ? e.message : String(e)));",
  "}",
].join("\n");

function grab(bin) {
  const res = spawnSync(bin, ["-e", CHILD_CODE], {
    env: Object.assign({}, process.env, { ELECTRON_RUN_AS_NODE: "1" }),
    encoding: "utf8",
    timeout: 30000,
    maxBuffer: 8 * 1024 * 1024,
    windowsHide: true,
  });
  const stdout = (res.stdout || "").trim();
  const stderr = (res.stderr || "").trim();
  if (stdout.startsWith("WBKEY:")) {
    const raw = stdout.slice("WBKEY:".length);
    let obj;
    try {
      obj = JSON.parse(raw);
    } catch (e) {
      return { ok: false, error: "返回体不是 JSON: " + raw.slice(0, 200) };
    }
    return { ok: true, payload: obj };
  }
  if (stdout.startsWith("WBKEY_ERR:")) {
    return { ok: false, error: stdout.slice("WBKEY_ERR:".length) };
  }
  return {
    ok: false,
    error:
      "子进程未返回预期结果（exit=" +
      res.status +
      (res.error ? ", spawn=" + res.error.message : "") +
      "）" +
      (stderr ? " stderr: " + stderr.split("\n").slice(0, 3).join(" | ") : ""),
  };
}

function mask(k) {
  if (!k || k.length <= 10) return "***";
  return k.slice(0, 6) + "…" + k.slice(-4) + "（len=" + k.length + "）";
}

// ------------------------------------------------------------------ main
function main() {
  const args = parseArgs(process.argv.slice(2));
  const outPath = args.out
    ? path.resolve(args.out)
    : path.join(HERE, "at_rest_buildkey.json");

  const { bin, tried } = resolveApp(args.app);
  const fail = (msg) => {
    if (args.json) console.log(JSON.stringify({ ok: false, error: msg }));
    else console.error("FAILED: " + msg);
    process.exit(1);
  };

  if (!bin) {
    return fail(
      "未找到 WorkBuddy / CodeBuddy 桌面端可执行文件。已尝试：\n  " +
        tried.join("\n  ") +
        "\n请用 --app <可执行文件路径> 或环境变量 WB_APP_BINARY 指定。"
    );
  }

  const got = grab(bin);
  if (!got.ok) {
    return fail(
      "调用原生绑定失败：" +
        got.error +
        "\n  （二进制：" +
        bin +
        "）\n  常见原因：客户端版本过旧（无 workbuddyStorage 绑定）、二进制路径不是主可执行文件、" +
        "或该构建未启用 at-rest 加密。"
    );
  }

  const key = got.payload && got.payload.atRestSecretKey;
  if (!key || typeof key !== "string") {
    return fail(
      "返回体里没有 atRestSecretKey：" + JSON.stringify(got.payload).slice(0, 300)
    );
  }

  const data = {
    _comment:
      "WorkBuddy 客户端 at-rest build key（atRestSecretKey）。构建级常量，同版本全安装一致，用于解密本地凭据信封。",
    version: got.payload.version || 1,
    atRestSecretKey: key,
    developerPublicKeyId:
      got.payload.atRestDeveloperPublicKey && got.payload.atRestDeveloperPublicKey.id,
    source: "electron.workbuddyStorage.loggerGet() via ELECTRON_RUN_AS_NODE",
    capturedAt: new Date().toISOString().slice(0, 10),
  };

  try {
    fs.mkdirSync(path.dirname(outPath), { recursive: true });
    const tmp = outPath + ".tmp";
    fs.writeFileSync(tmp, JSON.stringify(data, null, 2) + "\n", "utf8");
    fs.renameSync(tmp, outPath);
  } catch (e) {
    return fail("写入缓存文件失败：" + outPath + " —— " + (e && e.message));
  }

  if (args.json) {
    console.log(
      JSON.stringify({ ok: true, app: bin, out: outPath, keyLength: key.length })
    );
    return;
  }
  console.log("✓ 已取出 build key");
  console.log("  客户端  : " + bin);
  console.log("  密钥    : " + (args.show ? key : mask(key) + "（用 --show 显示完整值）"));
  console.log("  已写入  : " + outPath);
  console.log("  提示    : 该文件等同本机凭据的解密钥匙，请勿外传；客户端升级换 key 后重新运行本脚本即可。");
}

main();
