#!/usr/bin/env node
/**
 * 三立智期 OpenClaw — HTTP Open API (`/open/v1`) 的 MCP 封装。
 *
 * 配置读取顺序（先命中先用，互不覆盖）：
 *   1. /opt/data/skills/slzq-trading/config.json
 *   2. ~/.slzq-trading/credentials.json
 *   3. ~/.openclaw/openclaw.json（skills.entries.slzq-trading）
 *   4. 进程环境变量 SLZQ_OPENCLAW_DOMAIN / API_KEY / ENV
 *
 * 未配置 API Key 时服务端仍会启动：交易类工具会返回可执行的登录指引，
 * 用户可直接用 slzq_open_v1_auth_* 系列工具完成手机号验证码登录并自动落盘密钥。
 */
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { chmod, mkdir, readFile, rename, rm, writeFile } from "node:fs/promises";
import { homedir } from "node:os";
import { join } from "node:path";
import { z } from "zod";
const SKILL_NAME = "slzq-trading";
const DEFAULT_DOMAIN = "https://slzqapi.sxslqhsh.com";
const DOMAIN_ENV = "SLZQ_OPENCLAW_DOMAIN";
const API_KEY_ENV = "SLZQ_OPENCLAW_API_KEY";
const TRADING_ENV = "SLZQ_OPENCLAW_ENV";
/** 小立助理网关机权威配置（开机任务 skillConfig 落盘处） */
const SKILL_CONFIG_FILE = `/opt/data/skills/${SKILL_NAME}/config.json`;
/** 登录后落盘的凭据文件：宿主不是 OpenClaw 时也能让密钥跨重启生效 */
const CREDENTIALS_DIR = join(homedir(), `.${SKILL_NAME}`);
const CREDENTIALS_FILE = join(CREDENTIALS_DIR, "credentials.json");
/** 本机 skill 偏好（不含密钥）。止盈止损提醒关闭后跨会话生效 */
const PREFS_FILE = join(CREDENTIALS_DIR, "preferences.json");
const SL_TP_REMINDER_TEXT = "建议为当前持仓设置止盈止损，控制风险。不需要这个提醒请直接回复「不再提醒」。";
const SL_TP_REMINDER_MUTE_TOOL = "slzq_open_v1_skill_prefs_mute_stop_profit_loss_reminder";
/** OpenClaw 网关自身的配置；仅在用户确实装了 OpenClaw（目录已存在）时才合并写入 */
const OPENCLAW_CONFIG_FILE = join(homedir(), ".openclaw", "openclaw.json");
const NO_API_KEY_HINT = `尚未配置 ${API_KEY_ENV}。有两种取钥方式，先把两种都告诉用户让其选择，不要替他决定：` +
    `【方式 A · 会话内登录领取，最快】选 A 就直接按顺序执行，不要复述步骤、不要解释原理、不要在步骤之间征求同意：` +
    `1) slzq_open_v1_auth_agreement → 把 highlights 原文发给用户，让其回复同意；` +
    `2) 向用户要 11 位手机号 → slzq_open_v1_auth_send_code；` +
    `3) 用户报出验证码（位数照第 2 步返回的 codeLength，当前为 4 位纯数字，不要自己猜长度）` +
    `→ slzq_open_v1_auth_login（只传 mobileNum 和 verifyCode，验证码原样传字符串、保留前导零）。` +
    `方式 A 只需要用户提供手机号和验证码；服务端若已有可用的模拟盘密钥会原样返回那把（keyCreated=false），` +
    `不会顶掉用户其它设备上的配置。登录成功后密钥自动落盘并在本会话立即生效，无需重启，随后直接继续用户原本的任务。` +
    `【方式 B · 开通实盘】要 SIM_LIVE / live 时：请用户打开 App「我的 → 小立助理-智能体」，点聊天页顶栏提示进入个人中心，再点「实盘账号」绑定实盘交易（同意风险告知并输入交易密码）。` +
    `App 低于 1.6.9 没有该入口时才走旧页「我的 → 期货辅助交易」。不要在会话里向用户要交易密码。` +
    `若 auth 工具返回 10411，说明该地址上的服务端未上线登录接口（不是要你补密钥）：停止重试，模拟盘稍后再走方式 A；实盘改走方式 B。`;
let config;
/** 只保留首尾若干字符，日志与工具返回一律用这个，避免完整密钥落到会话记录里 */
function maskApiKey(apiKey) {
    if (!apiKey)
        return "";
    if (apiKey.length <= 12)
        return "***";
    return `${apiKey.slice(0, 7)}***${apiKey.slice(-4)}`;
}
function normalizeDomain(raw) {
    let domain = raw.trim().replace(/\/+$/, "");
    // 用户常把 /mobile-api 一起填进来；这里纠正并提示，而不是让后续每个请求都 404
    if (/\/mobile-api\/?$/i.test(domain)) {
        domain = domain.replace(/\/mobile-api\/?$/i, "");
        console.error(`WARN: ${DOMAIN_ENV} 不应包含 /mobile-api，已自动去除，实际使用：${domain}`);
    }
    return domain;
}
function pickString(obj, ...keys) {
    for (const key of keys) {
        const value = obj[key];
        if (typeof value === "string" && value.trim())
            return value.trim();
    }
    return "";
}
function parseTradingEnv(raw) {
    const value = raw.trim().toLowerCase();
    if (value === "sim" || value === "live")
        return value;
    if (value) {
        console.error(`WARN: ${TRADING_ENV}=${raw} 非法，已忽略（合法值：sim 或 live）`);
    }
    return undefined;
}
async function readJsonObject(filePath) {
    try {
        const raw = await readFile(filePath, "utf8");
        const parsed = JSON.parse(raw);
        if (parsed && typeof parsed === "object" && !Array.isArray(parsed)) {
            return parsed;
        }
    }
    catch {
        // 文件不存在或损坏：这一层当作没有
    }
    return null;
}
function layerFromEnvKeys(source, obj) {
    const tradingEnv = parseTradingEnv(pickString(obj, TRADING_ENV, "tradingEnv", "env"));
    const domain = pickString(obj, DOMAIN_ENV, "domain", "baseUrl");
    const apiKey = pickString(obj, API_KEY_ENV, "apiKey");
    return {
        source,
        ...(domain ? { domain } : {}),
        ...(apiKey ? { apiKey } : {}),
        ...(tradingEnv ? { tradingEnv } : {}),
    };
}
async function loadSkillConfigLayer() {
    const obj = await readJsonObject(SKILL_CONFIG_FILE);
    if (!obj)
        return null;
    const layer = layerFromEnvKeys("skill-config", obj);
    if (!layer.domain && !layer.apiKey && !layer.tradingEnv)
        return null;
    return layer;
}
async function loadCredentialsLayer() {
    const obj = await readJsonObject(CREDENTIALS_FILE);
    if (!obj)
        return null;
    const apiKey = pickString(obj, "apiKey", API_KEY_ENV);
    const domain = pickString(obj, "domain", DOMAIN_ENV);
    const tradingEnv = parseTradingEnv(pickString(obj, TRADING_ENV, "tradingEnv", "env"));
    if (!apiKey && !domain && !tradingEnv)
        return null;
    return {
        source: "file",
        ...(domain ? { domain } : {}),
        ...(apiKey ? { apiKey, apiKeyDomain: domain || undefined } : {}),
        ...(tradingEnv ? { tradingEnv } : {}),
    };
}
async function loadOpenclawLayer() {
    const root = await readJsonObject(OPENCLAW_CONFIG_FILE);
    if (!root)
        return null;
    const skills = root.skills;
    if (!skills || typeof skills !== "object")
        return null;
    const entries = skills.entries;
    if (!entries || typeof entries !== "object")
        return null;
    const entry = entries[SKILL_NAME];
    if (!entry || typeof entry !== "object")
        return null;
    const rec = entry;
    const envObj = rec.env && typeof rec.env === "object" && !Array.isArray(rec.env)
        ? rec.env
        : {};
    const apiKey = pickString(rec, "apiKey", API_KEY_ENV) || pickString(envObj, API_KEY_ENV, "apiKey");
    const domain = pickString(envObj, DOMAIN_ENV, "domain") || pickString(rec, DOMAIN_ENV, "domain");
    const tradingEnv = parseTradingEnv(pickString(envObj, TRADING_ENV, "tradingEnv") || pickString(rec, TRADING_ENV, "tradingEnv"));
    if (!apiKey && !domain && !tradingEnv)
        return null;
    return {
        source: "openclaw",
        ...(domain ? { domain } : {}),
        ...(apiKey ? { apiKey } : {}),
        ...(tradingEnv ? { tradingEnv } : {}),
    };
}
function loadEnvLayer() {
    const domain = (process.env[DOMAIN_ENV] ?? "").trim();
    const apiKey = (process.env[API_KEY_ENV] ?? "").trim();
    const tradingEnv = parseTradingEnv(process.env[TRADING_ENV] ?? "");
    return {
        source: "env",
        ...(domain ? { domain } : {}),
        ...(apiKey ? { apiKey } : {}),
        ...(tradingEnv ? { tradingEnv } : {}),
    };
}
/**
 * 先命中先用：skill config.json → 本地凭据 → OpenClaw 客户端配置 → 进程环境变量。
 * 凭据带域名限定：密钥是按域名签发的，测试域名领的密钥发到生产只会得到 10411，
 * 与其让用户对着「密钥无效」排查，不如跳过这一层继续往后找。
 */
async function loadConfig() {
    const layers = [];
    const skillLayer = await loadSkillConfigLayer();
    const fileLayer = await loadCredentialsLayer();
    const openclawLayer = await loadOpenclawLayer();
    if (skillLayer)
        layers.push(skillLayer);
    if (fileLayer)
        layers.push(fileLayer);
    if (openclawLayer)
        layers.push(openclawLayer);
    layers.push(loadEnvLayer());
    let domain = DEFAULT_DOMAIN;
    let domainSource = "default";
    for (const layer of layers) {
        if (layer.domain) {
            domain = normalizeDomain(layer.domain);
            domainSource = layer.source;
            break;
        }
    }
    let tradingEnv = "sim";
    for (const layer of layers) {
        if (layer.tradingEnv) {
            tradingEnv = layer.tradingEnv;
            break;
        }
    }
    let apiKey = "";
    let apiKeySource = "none";
    for (const layer of layers) {
        if (!layer.apiKey)
            continue;
        if (layer.apiKeyDomain && layer.apiKeyDomain !== domain) {
            console.error(`WARN: ${CREDENTIALS_FILE} 是为 ${layer.apiKeyDomain} 领取的，与当前域名 ${domain} 不符，已忽略这一层。`);
            continue;
        }
        apiKey = layer.apiKey;
        apiKeySource = layer.source;
        break;
    }
    if (!apiKey) {
        console.error(`WARN: 未配置 API Key，交易类工具将返回登录指引；可用 slzq_open_v1_auth_login 完成登录。`);
    }
    return { domain, domainSource, apiBase: `${domain}/mobile-api`, apiKey, apiKeySource, tradingEnv };
}
/**
 * 原子写：先写同目录临时文件再 rename。直接覆盖写在中途被杀/磁盘满时会留下一个被截断的文件，
 * 而这两个文件（凭据、OpenClaw 配置）损坏的代价分别是"密钥丢失"和"把用户整份网关配置写坏"。
 */
async function writeFileAtomic(filePath, content, mode) {
    const tmpPath = `${filePath}.tmp-${process.pid}`;
    await writeFile(tmpPath, content, { mode });
    try {
        await chmod(tmpPath, mode);
        await rename(tmpPath, filePath);
    }
    catch (e) {
        await rm(tmpPath, { force: true }).catch(() => { });
        throw e;
    }
}
/**
 * 把密钥写入本地凭据文件（0600）；若本机装了 OpenClaw，再合并写入其配置的 skill 条目。
 * 返回给用户看的落盘说明；任何一处失败都只降级为提示，不影响本次会话已经生效的内存密钥。
 */
async function persistApiKey(apiKey) {
    const notes = [];
    try {
        await mkdir(CREDENTIALS_DIR, { recursive: true, mode: 0o700 });
        const payload = { apiKey, domain: config.domain, updatedAt: new Date().toISOString() };
        await writeFileAtomic(CREDENTIALS_FILE, `${JSON.stringify(payload, null, 2)}\n`, 0o600);
        notes.push(`已写入本地凭据文件（仅当前用户可读）：${CREDENTIALS_FILE}`);
    }
    catch (e) {
        notes.push(`本地凭据文件写入失败（${errorMessage(e)}），请手动设置环境变量 ${API_KEY_ENV}`);
    }
    notes.push(...(await mergeIntoOpenclawConfig(apiKey)));
    const skillCfg = await readJsonObject(SKILL_CONFIG_FILE);
    const skillKey = skillCfg ? pickString(skillCfg, API_KEY_ENV, "apiKey") : "";
    if (skillKey && skillKey !== apiKey) {
        notes.push(`注意：${SKILL_CONFIG_FILE} 已有另一把密钥，重启后该文件优先于本次登录落盘；` +
            `小立助理请在个人中心重新绑定实盘以更新该文件。本流程不会改写该路径。`);
    }
    return notes;
}
/** 合并写入 ~/.openclaw/openclaw.json 的 skills.entries.<skill>；配置损坏时宁可不动也不覆盖用户文件 */
async function mergeIntoOpenclawConfig(apiKey) {
    let raw;
    try {
        raw = await readFile(OPENCLAW_CONFIG_FILE, "utf8");
    }
    catch {
        // 没装 OpenClaw 或还没生成配置：本地凭据文件已够用，静默跳过
        return [];
    }
    let parsed;
    try {
        parsed = raw.trim() ? JSON.parse(raw) : {};
    }
    catch (e) {
        return [`${OPENCLAW_CONFIG_FILE} 不是合法 JSON（${errorMessage(e)}），已跳过写入以免破坏原文件，请手动填写 API Key。`];
    }
    try {
        const skills = (parsed.skills ??= {});
        const entries = (skills.entries ??= {});
        const entry = (entries[SKILL_NAME] ??= {});
        entry.apiKey = apiKey;
        // 只补空缺，不覆盖用户已填的域名/交易环境：本进程的环境变量未必等于用户在网关里的设置，
        // 覆盖会把人家配好的 live 悄悄改成 sim。
        const env = { ...(entry.env ?? {}) };
        if (!env[DOMAIN_ENV])
            env[DOMAIN_ENV] = config.domain;
        if (!env[TRADING_ENV])
            env[TRADING_ENV] = config.tradingEnv;
        entry.env = env;
        await writeFileAtomic(OPENCLAW_CONFIG_FILE, `${JSON.stringify(parsed, null, 2)}\n`, 0o600);
        return [`已合并写入 OpenClaw 配置：${OPENCLAW_CONFIG_FILE}（skills.entries.${SKILL_NAME}）`];
    }
    catch (e) {
        return [`写入 ${OPENCLAW_CONFIG_FILE} 失败（${errorMessage(e)}），请在 OpenClaw Skills 界面手动填写 API Key。`];
    }
}
function errorMessage(e) {
    return e instanceof Error ? e.message : String(e);
}
function textResult(text, isError = false) {
    return { content: [{ type: "text", text }], isError };
}
function jsonResult(data, isError = false) {
    return {
        content: [{ type: "text", text: typeof data === "string" ? data : JSON.stringify(data, null, 2) }],
        isError,
    };
}
async function readSkillPrefs() {
    try {
        const raw = await readFile(PREFS_FILE, "utf8");
        const parsed = JSON.parse(raw);
        return parsed && typeof parsed === "object" ? parsed : {};
    }
    catch {
        return {};
    }
}
async function writeSkillPrefs(prefs) {
    await mkdir(CREDENTIALS_DIR, { recursive: true, mode: 0o700 });
    await writeFileAtomic(PREFS_FILE, `${JSON.stringify(prefs, null, 2)}\n`, 0o600);
}
function hasOpenPositions(payload) {
    const data = payload.data;
    if (!Array.isArray(data))
        return false;
    return data.some((row) => {
        if (!row || typeof row !== "object")
            return false;
        const rec = row;
        const vol = rec.volume ?? rec.position ?? 0;
        const n = typeof vol === "number" ? vol : Number(vol);
        return Number.isFinite(n) && n > 0;
    });
}
async function withStopProfitLossReminder(payload, shouldRemind) {
    if (!shouldRemind)
        return payload;
    const prefs = await readSkillPrefs();
    if (prefs.stopProfitLossReminderMuted)
        return payload;
    return {
        ...payload,
        skillReminder: {
            type: "stop_profit_loss",
            muted: false,
            text: SL_TP_REMINDER_TEXT,
            muteHint: `用户回复「不再提醒」后立即调用 ${SL_TP_REMINDER_MUTE_TOOL}，此后本机不再附带本提醒。没有这句话不得调用。`,
        },
    };
}
async function openApiFetch(path, options) {
    const url = new URL(`${config.apiBase}/open/v1${path.startsWith("/") ? path : `/${path}`}`);
    if (options.searchParams) {
        for (const [k, v] of Object.entries(options.searchParams)) {
            if (v === undefined || v === null || v === "")
                continue;
            url.searchParams.set(k, String(v));
        }
    }
    const headers = {};
    if (options.auth) {
        if (!config.apiKey) {
            throw new Error(NO_API_KEY_HINT);
        }
        headers.Authorization = `Bearer ${config.apiKey}`;
        headers["X-Trading-Env"] = config.tradingEnv;
    }
    if (options.body !== undefined) {
        headers["Content-Type"] = "application/json";
    }
    const res = await fetch(url, {
        method: options.method ?? "GET",
        headers,
        body: options.body !== undefined ? JSON.stringify(options.body) : undefined,
    });
    const raw = await res.text();
    let parsed = raw;
    try {
        parsed = raw ? JSON.parse(raw) : null;
    }
    catch {
        /* keep text */
    }
    return { ok: res.ok, status: res.status, body: parsed };
}
async function runTool(fn, transform) {
    try {
        const { ok, status, body } = await fn();
        let payload = typeof body === "object" && body !== null
            ? { httpStatus: status, ...body }
            : { httpStatus: status, raw: body };
        const apiFailed = typeof body === "object" && body !== null && body.success === false;
        const failed = !ok || apiFailed;
        if (transform) {
            payload = await transform(payload, failed);
        }
        return jsonResult(payload, failed);
    }
    catch (e) {
        const msg = e instanceof Error ? e.message : String(e);
        return textResult(msg, true);
    }
}
const directionEnum = z.enum(["BUY", "SELL"]);
const offsetFlagEnum = z.enum([
    "OPEN",
    "CLOSE",
    "CLOSE_TODAY",
    "CLOSE_YESTERDAY",
]);
/** 立即下单没有 MARKET；模型常把条件单市价写法套过来，提交前改成 ANY */
const priceTypeEnum = z.preprocess((v) => {
    if (typeof v !== "string") {
        return v;
    }
    const t = v.trim();
    if (/^(MARKET|市价|任意价)$/i.test(t)) {
        return "ANY";
    }
    return t;
}, z.enum(["ANY", "LIMIT", "BEST", "LAST"]));
/** 交易所可省：服务端能按合约代码解析，猜错反而拿到空数据 */
const EXCHANGE_OPTIONAL = " exchangeId 可以不传——服务端会按合约代码自动解析交易所；自己猜一个错的交易所只会拿到空数据，" +
    "而空数据很容易被误读成「这个合约没有行情」。要确认交易所请调 slzq_open_v1_catalog_contract。";
const exchangeIdOptional = z
    .string()
    .optional()
    .describe("可选。交易所代码，如 SHFE/DCE/CZCE/INE/CFFEX/GFEX。**不确定就不要传**，服务端会按合约代码自动解析");
const placeOrderSchema = z.object({
    instrumentId: z
        .string()
        .regex(/^[A-Za-z]+\d+$/, "instrumentId 必须为字母+数字，不带交易所后缀，如 cu2506 或 IF2506")
        .describe("合约代码。商品期货通常小写（cu2506），中金所通常大写（IF2506）——保持目录接口返回的原样大小写，不要自己改"),
    orderRef: z
        .string()
        .regex(/^\d{1,13}$/, "orderRef 必须为 1～13 位纯数字")
        .optional()
        .describe("报单引用。sim 必填，1～13 位纯数字且本会话内不重复；live 传了也会被忽略，服务端自己生成，撤单必须用返回结果里的 orderRef"),
    direction: directionEnum.describe("买卖方向。BUY=买入（开多 / 平空），SELL=卖出（开空 / 平多）。方向说的是这笔委托本身买还是卖，不是持仓方向"),
    offsetFlag: offsetFlagEnum.describe("开平标志。OPEN=开仓；CLOSE=平仓（SHFE/INE 今昨混合时服务端会自动拆成两笔）；CLOSE_TODAY=只平今；CLOSE_YESTERDAY=只平昨"),
    priceType: priceTypeEnum.describe("立即下单价格类型。市价必须传 ANY（任意价），禁止传 MARKET——MARKET 只用于条件单 orderPriceType。" +
        "LIMIT=限价（最常用，配合 limitPrice）；ANY=市价；BEST=最优价；LAST=最新价"),
    limitPrice: z.number().describe("报单价格，须符合合约最小变动价位 priceTick（见 catalog_contract）。市价单也要传一个合理价格，服务端用作参考"),
    count: z.number().int().positive().describe("委托手数，正整数。平仓时不得超过可用持仓，超了柜台会直接拒单"),
    positionDateType: z
        .enum(["今", "昨"])
        .optional()
        .describe("可选，只对区分今昨仓的交易所（SHFE/INE）平仓有效：'今'=只平今，'昨'=只平昨。不传由服务端按持仓自动选，不确定就不要传"),
    minCount: z.number().int().positive().optional().describe("可选，最小成交数量，不传按 1。没有特殊要求不要传"),
    timeCondition: z.enum(["GFD", "GTC"]).optional().describe("可选，有效期。GFD=当日有效（默认，当日未成交自动作废）；GTC=撤销前有效"),
    stopPriceType: z
        .number()
        .int()
        .min(1)
        .max(5)
        .optional()
        .describe("可选，**仅止盈止损场景用**：1=对手价 2=最新价 3=超价 4=排队价 5=市价。普通下单不要传，传了会覆盖 priceType 的换算"),
    orderPrice: z.number().optional().describe("可选，**仅止盈止损场景用**：触发后实际报单的价格。普通下单不要传"),
});
/** 撤单五个必填项全部来自下单回报或 orders_open，任何一个靠猜都会失败 */
const cancelOrderSchema = z.object({
    instrumentId: z
        .string()
        .regex(/^[A-Za-z]+\d+$/, "instrumentId 必须为字母+数字，不带交易所后缀，如 cu2506 或 IF2506")
        .describe("合约代码，取自下单回报或 orders_open，与下单时一致"),
    exchangeId: z.string().describe("交易所代码，**取自下单回报或 orders_open 的 exchangeId**，不要自己按品种猜"),
    orderRef: z
        .string()
        .regex(/^\d{1,13}$/, "orderRef 必须为 1～13 位纯数字")
        .describe("报单引用，**必须用下单回报里的 orderRef**。live 下服务端会重新生成，用你当初传入的那个撤不掉"),
    orderSysId: z.string().describe("交易所报单编号，取自下单回报或 orders_open"),
    frontID: z.number().int().describe("前置编号，取自下单回报或 orders_open"),
    sessionId: z.number().int().optional().describe("可选，会话编号，取自下单回报；不传则用当前 CTP 会话"),
});
const mobileNumSchema = z
    .string()
    .regex(/^\d{11}$/, "手机号必须是 11 位数字");
/**
 * 探测服务端是否支持免密钥登录。
 *
 * 关键点：老版本服务端上 /open/v1/auth/* 并不存在，但鉴权拦截器排在路由之前，
 * 会先返回 10411「缺少 API Key」——直接打 auth 接口是无法区分「未上线」和「真要密钥」的。
 * /open/v1/health 在新老版本上都免鉴权，新版会带 authLoginSupported=true，因此它才是权威判据。
 */
async function probeServerCapability() {
    try {
        const { ok, status, body } = await openApiFetch("/health", { auth: false });
        const data = body?.data;
        if (!ok || !data) {
            return { reachable: false, supported: false, detail: `health HTTP ${status}` };
        }
        return {
            reachable: true,
            supported: data.authLoginSupported === true,
            skillName: typeof data.skillName === "string" ? data.skillName : undefined,
            skillVersion: typeof data.skillVersion === "string" ? data.skillVersion : undefined,
            apiBase: typeof data.apiBase === "string" ? data.apiBase : undefined,
            detail: data.authLoginSupported === true
                ? "health 返回 authLoginSupported=true"
                : "health 未返回 authLoginSupported，服务端版本早于登录领钥功能",
        };
    }
    catch (e) {
        return { reachable: false, supported: false, detail: errorMessage(e) };
    }
}
/**
 * auth 系列专用包装：把 10411 翻译成「服务端未上线该接口」。
 * 免鉴权接口不可能真的缺密钥，收到 10411 只可能是老版本的鉴权拦截器拦下了不存在的路由。
 */
async function runAuthTool(fn) {
    const result = await runTool(fn);
    const text = result.content?.[0];
    if (result.isError && text && text.type === "text" && text.text.includes("10411")) {
        return jsonResult({
            raw: text.text,
            verdict: "SERVER_TOO_OLD",
            explain: "该接口免鉴权，收到 10411 只说明服务端版本过旧、路由尚未上线（旧版鉴权拦截器会先拦下不存在的 /open/v1/* 路径）。",
            nextStep: "不要再重试、也不要尝试其它域名或伪造密钥。模拟盘请确认域名后用方式 A 领取；实盘请走 App「我的 → 小立助理-智能体」个人中心绑定实盘交易。" +
                `可用 slzq_open_v1_auth_status 查看服务端版本佐证。`,
        }, true);
    }
    return result;
}
/** 首次安装引导：查看密钥状态、风险告知、发送验证码、登录领钥 */
function registerAuthTools(server) {
    server.registerTool("slzq_open_v1_auth_status", {
        description: "【任何工具报未配置密钥/10411 时，先且只需调用它】一次性给出终局判定：本机是否已配置密钥、" +
            "服务端是否支持免密钥登录、下一步该做什么（verdict 字段）。不要靠 curl 试错去猜服务端行为。",
    }, async () => {
        const base = {
            configured: Boolean(config.apiKey),
            apiKeySource: config.apiKeySource,
            apiKeyMasked: maskApiKey(config.apiKey),
            domain: config.domain,
            domainSource: config.domainSource,
            apiBase: config.apiBase,
            tradingEnv: config.tradingEnv,
            configSearchOrder: [SKILL_CONFIG_FILE, CREDENTIALS_FILE, OPENCLAW_CONFIG_FILE, "process.env"],
            skillConfigFile: SKILL_CONFIG_FILE,
            credentialsFile: CREDENTIALS_FILE,
            openclawConfigFile: OPENCLAW_CONFIG_FILE,
        };
        if (config.apiKey) {
            try {
                const { ok, status, body } = await openApiFetch("/me", { auth: true });
                const failed = typeof body === "object" && body !== null && body.success === false;
                return jsonResult({ ...base, verdict: ok && !failed ? "READY：密钥可用，直接开始业务调用" : "KEY_REJECTED：密钥被服务端拒绝，按 me 返回的 errorInfo 处理", httpStatus: status, me: body }, !ok || failed);
            }
            catch (e) {
                return jsonResult({ ...base, verdict: "NETWORK_ERROR：请求失败，检查域名是否可达", error: errorMessage(e) }, true);
            }
        }
        // 没有密钥时先探测服务端能力：health 在新老版本上都免鉴权，是唯一可靠的判定信号
        const probe = await probeServerCapability();
        return jsonResult({
            ...base,
            serverAuthLoginSupported: probe.supported,
            serverSkillName: probe.skillName,
            serverSkillVersion: probe.skillVersion,
            serverApiBase: probe.apiBase,
            verdict: probe.supported
                ? "NEED_LOGIN：服务端支持免密钥登录。按 nextStep 把方式 A / 方式 B 两种取钥方式给用户选，选定后立即执行，不要再问是否继续"
                : probe.reachable
                    ? config.domainSource === "default"
                        ? `SERVER_TOO_OLD_MAYBE_WRONG_DOMAIN：当前用的是内置默认域名 ${config.domain}（未配置 ${DOMAIN_ENV}），该服务端未上线登录接口。` +
                            `先确认 skill 包是从哪个环境下载的：下载地址中 /mobile-api 之前的整段就是应填的域名（可能含 /sanli 之类的网关前缀）。` +
                            `配好 ${DOMAIN_ENV} 后重新调用本工具；若确认域名无误，实盘改走方式 B（小立助理个人中心绑定实盘交易）。`
                        : `SERVER_TOO_OLD：${config.domain} 未上线登录接口，方式 A 不可用，不要再试 auth 工具；实盘请走方式 B——App「我的 → 小立助理-智能体」→ 顶栏进个人中心 → 绑定实盘交易（App 低于 1.6.9 才走「我的 → 期货辅助交易」）`
                    : "NETWORK_ERROR：域名不可达，先确认 " + DOMAIN_ENV + " 是否正确（可带网关路径前缀，如 https://host/sanli）",
            nextStep: probe.supported ? NO_API_KEY_HINT : undefined,
            probeDetail: probe.detail,
        });
    });
    server.registerTool("slzq_open_v1_auth_agreement", {
        description: "GET /open/v1/auth/agreement — 登录前必须取回并向用户原文展示的风险告知，无需鉴权。" +
            "用户明确同意后，把返回的 version 作为 agreementVersion 传给 slzq_open_v1_auth_login。",
    }, async () => runAuthTool(() => openApiFetch("/auth/agreement", { auth: false })));
    server.registerTool("slzq_open_v1_auth_send_code", {
        description: "发送登录/注册短信验证码（POST /open/v1/auth/sms/send，无需鉴权）。" +
            "codeKey 由服务端按手机号暂存，调用 slzq_open_v1_auth_login 时无需回传、也不必自己保存。" +
            "同一手机号 1 分钟内只能发 1 条，收到限流提示就等，不要立刻重发。" +
            "返回的 codeLength 就是本次验证码的位数（纯数字，当前为 4 位）——按它向用户索取，不要猜长度；该值由服务端动态决定，以每次返回为准，不要硬编码。",
        inputSchema: { mobileNum: mobileNumSchema },
    }, async (args) => runAuthTool(() => openApiFetch("/auth/sms/send", { method: "POST", auth: false, body: { mobileNum: args.mobileNum } })));
    server.registerTool("slzq_open_v1_auth_login", {
        description: "手机号+验证码登录/注册并领取【模拟盘】API Key（POST /open/v1/auth/login，无需鉴权）。" +
            "拿到用户报的验证码后直接调用即可，只需 mobileNum + verifyCode（codeKey 由服务端按手机号取回）。" +
            "成功后密钥自动落盘并在本会话立即生效，无需重启；模拟盘账户同时自动开通，返回的 simAccountReady/simAccountBalance " +
            "即为账户状态，simAccountReady=false 时告知用户账户未就绪即可，不要去 App 找开户入口。" +
            "实盘权限不从这里开通：请用户走 App「我的 → 小立助理-智能体」→ 顶栏进个人中心 → 绑定实盘交易（App 低于 1.6.9 才走「期货辅助交易」）。" +
            "返回内容不含完整密钥，不要要求用户或自行复述密钥明文。",
        inputSchema: {
            mobileNum: mobileNumSchema,
            verifyCode: z
                .string()
                .min(1, "验证码不能为空")
                .describe("短信验证码，位数以 slzq_open_v1_auth_send_code 返回的 codeLength 为准（当前 4 位纯数字）；" +
                "原样传字符串，保留前导零，不要转成数字"),
            codeKey: z
                .string()
                .optional()
                .describe("不用传：服务端按手机号自动取回本次发码的 codeKey"),
            agreementVersion: z
                .string()
                .optional()
                .describe("用户已确认的风险告知版本号，取自 slzq_open_v1_auth_agreement；首次登录必填"),
            name: z.string().optional().describe("密钥备注名，可选"),
            forceRotate: z
                .boolean()
                .optional()
                .describe("true=吊销原模拟盘密钥并重新签发（其它设备上的旧密钥会立即失效）。默认 false，复用已有密钥"),
        },
    }, async (args) => {
        let response;
        try {
            response = await openApiFetch("/auth/login", { method: "POST", auth: false, body: args });
        }
        catch (e) {
            return textResult(errorMessage(e), true);
        }
        const body = response.body;
        const apiKey = typeof body?.data?.apiKey === "string" ? body.data.apiKey.trim() : "";
        if (!response.ok || body?.success === false || !apiKey) {
            return jsonResult({ httpStatus: response.status, ...body }, true);
        }
        // 先让本次会话立即可用，再落盘：即使写盘失败，用户当前会话也不至于卡住
        config = { ...config, apiKey, apiKeySource: "login" };
        const persistNotes = await persistApiKey(apiKey);
        // data 里剔除 apiKey 再回给模型，避免完整密钥进入会话上下文与日志
        const { apiKey: _omitted, ...safeData } = (body?.data ?? {});
        return jsonResult({
            httpStatus: response.status,
            success: true,
            data: { ...safeData, apiKeyMasked: maskApiKey(apiKey) },
            applied: `密钥已在本次会话生效（交易环境 ${config.tradingEnv}）`,
            persisted: persistNotes,
            nextStep: "调用 slzq_open_v1_auth_status 或 slzq_open_v1_me 确认权限档位，随后即可查询行情与持仓。",
        });
    });
}
// ==================== 云条件单 / 止盈止损（替代自己盯盘） ====================
/**
 * 拼在行情工具的 description 里。模型最容易在这里起念头「循环查快照等价格」，
 * 直接在工具说明上堵死，并指向真正该用的云单接口。
 */
const NO_SELF_POLLING = " 【不要用它盯盘】禁止为了等一个触发价而循环/定时/sleep 后重查本工具。" +
    "带触发条件的需求（跌到 X 就买、涨到 Y 就平、帮我盯着、设止损）一律建云单：" +
    "开仓/平仓条件用 slzq_open_v1_cloud_condition_order_create，已有持仓的止盈止损用 slzq_open_v1_cloud_stop_profit_loss_create，" +
    "由服务端 cloud-ctp 7×24 盯行情自动报单。";
/** 云单共用的提示语：拼在每个工具的 description 里，避免模型在 sim 下反复重试 */
const CLOUD_LIVE_ONLY = " 仅 X-Trading-Env: live 可用——云条件单由服务端 cloud-ctp 托管真实 CTP 账号执行，模拟盘无此机制；" +
    "sim 下会报错并指回下单接口，那是环境能力差异，不要重试、不要换参数再试；" +
    "也不要因为云单用不了就退回去轮询行情——如实告诉用户到价触发需要实盘。";
/** 建单类工具的开场白：这组接口就是用来代替智能体自己盯盘的 */
const CLOUD_TRIGGER_INTRO = "【这就是替代自己盯盘的正式能力】用户说「跌到 X 就买」「涨到 Y 帮我平」「帮我盯着」「设个止损」时用它；" +
    "建完单这一轮就结束，条件由服务端 cloud-ctp 7×24 盯着，会话关掉也照样生效。" +
    "禁止改用行情/持仓接口循环轮询等价格。 ";
/** 挂单的创建与修改在当前服务端未开放，说明里直接讲死，省得模型反复试 */
const PENDING_DISABLED = "【服务端当前未开放，别调】本接口在当前服务端没有开放，调用必失败，不要重试、不要换域名。" +
    "收盘后想先把单子挂上，改用 slzq_open_v1_cloud_condition_order_create（timeCondition=GTC），效果等价。 ";
/** 会改动实盘状态的云单操作共用的提示语 */
const CLOUD_MUTATION = CLOUD_LIVE_ONLY +
    " 本操作动实盘真钱，必须有用户的明确指令；调用前把合约、方向、手数、触发价、有效期复述给用户确认。" +
    "请求体里的 account/company/sessionId 会被服务端按 Api-Key 覆盖，传了不作数。";
/** GFD=当日有效，GTC=撤销前长期有效（会一直挂到触发或撤销，替用户建 GTC 单要说明） */
const timeConditionEnum = z.enum(["GFD", "GTC"]);
const cloudPendingOrderSchema = {
    instrumentId: z.string().describe("合约代码，如 rb2601"),
    exchangeId: z.string().describe("交易所代码，如 SHFE"),
    direction: z.number().int().describe("0=买入，1=卖出"),
    offsetFlag: z.number().int().describe("0=开仓 1=平仓 3=平今 4=平昨"),
    volume: z.number().int().describe("委托手数"),
    limitPrice: z.number().describe("委托限价，须在涨跌停范围内"),
    timeCondition: timeConditionEnum.optional(),
    remark: z.string().optional(),
};
const cloudStopProfitLossSchema = {
    instrumentId: z.string(),
    exchangeId: z
        .string()
        .optional()
        .describe("交易所代码，如 SHFE。**不确定就不要传**，服务端会按合约代码解析；解析不到会拒绝，向用户确认合约代码，不要猜"),
    positionDirection: z.number().int().describe("0=买入持仓，1=卖出持仓"),
    volume: z.number().int().describe("委托平仓手数，不得超过实际持仓"),
    offsetFlag: z
        .number()
        .int()
        .optional()
        .describe("可选。1=平仓/平昨，3=平今。整仓止盈止损不要传，由服务端按持仓拆。" +
        "**禁止传 positionDateType**（立即下单字段，本接口没有，传「今」「昨」会被丢掉）。要指定今仓传 3，昨仓传 1，不必传 4。"),
    conditionType: z.number().int().describe("2=止损，3=止盈"),
    triggerPrice: z.number().describe("触发价格"),
    stopPriceType: z.number().int().optional().describe("1对手价 2最新价 3超价 4排队价 5涨跌停价(默认)"),
    timeCondition: timeConditionEnum.optional().describe("GFD=当日有效，GTC=长期有效。**平今不能传 GTC**：先说明只能当日有效（当天 15:00），等用户确认后再用 GFD 建单，不要带着 GTC 建。"),
    remark: z.string().optional(),
};
const triggerModeEnum = z
    .union([z.literal("ge"), z.literal("le"), z.literal("range")])
    .describe("触发模式。ge=最新价涨到 triggerPrice 才动手；le=最新价跌到 triggerPrice 才动手；" +
    "range=最新价落进 [triggerPriceMin, triggerPriceMax] 才动手。触发价只看最新价，没有买一价/卖一价可选");
const conditionOrderPriceTypeEnum = z
    .union([
    z.literal("MARKET"),
    z.literal("LIMIT"),
    z.literal("LAST"),
    z.literal("OPPONENT"),
    z.literal("QUEUE"),
])
    .describe("条件单触发之后按什么价报单：MARKET=市价（用户没特别要求就用它） LIMIT=限价（必须同时给 limitPrice） " +
    "LAST=最新价 OPPONENT=对手价 QUEUE=排队价。这是条件单 orderPriceType，禁止写到立即下单的 priceType（那里市价是 ANY）。不是旧版的 1/2 数字");
const stopProfitConfigSchema = z
    .object({
    spread: z.number().describe("相对成交价的价差，正数"),
    orderPriceType: z.string().optional().describe("固定传 \"市价\""),
})
    .describe("用户没主动要求就不要传");
const cloudConditionOrderSchema = {
    instrumentId: z.string().describe("合约代码，如 rb2601"),
    exchangeId: z
        .string()
        .optional()
        .describe("交易所代码，如 SHFE。**不确定就不要传**，服务端会按合约代码解析；解析不到会拒绝，向用户确认合约代码，不要猜"),
    direction: z
        .number()
        .int()
        .describe("0=买入，1=卖出。说的是这笔委托本身买还是卖，不是持仓方向：平多仓传 1(卖出)，平空仓传 0(买入)"),
    offsetFlag: z
        .number()
        .int()
        .describe("0=开仓 1=平仓（平昨传 1，不必传 4）3=平今。上期所/能源/中金所要平今必须传 3，传 1 只平昨、平不到今仓。今仓和昨仓都有且要整仓到价平掉时，改用止盈止损。"),
    volume: z.number().int().describe("委托手数"),
    triggerMode: triggerModeEnum,
    triggerPrice: z.number().optional().describe("触发价。triggerMode=ge/le 时必填，range 时不要传"),
    triggerPriceMin: z.number().optional().describe("区间下限。仅 triggerMode=range 时传"),
    triggerPriceMax: z.number().optional().describe("区间上限。仅 triggerMode=range 时传"),
    orderPriceType: conditionOrderPriceTypeEnum,
    limitPrice: z.number().optional().describe("委托限价。仅 orderPriceType=LIMIT 时必填，其余类型不要传"),
    timeCondition: timeConditionEnum.optional(),
    validUntil: z
        .string()
        .optional()
        .describe("有效期截止日 yyyy-MM-dd。不传由服务端按 timeCondition 算，正常不用传"),
    stopLossConfig: stopProfitConfigSchema.optional().describe("可选：这张单触发成交后自动再挂一个止损"),
    takeProfitConfig: stopProfitConfigSchema.optional().describe("可选：触发成交后自动挂的止盈"),
    remark: z.string().optional(),
};
const cloudConditionOrderModifySchema = {
    id: z.number().int().describe("条件单 id（创建返回的 id、列表里的 id）"),
    direction: z.number().int().optional().describe("0=买入 1=卖出；不传保持原方向"),
    volume: z.number().int().optional().describe("新的委托手数"),
    triggerMode: triggerModeEnum.optional().describe("改触发条件时必须连它一起传，否则条件重建不出来"),
    triggerPrice: z.number().optional().describe("新的触发价（triggerMode=ge/le）"),
    triggerPriceMin: z.number().optional().describe("新的区间下限（triggerMode=range）"),
    triggerPriceMax: z.number().optional().describe("新的区间上限（triggerMode=range）"),
    orderPriceType: conditionOrderPriceTypeEnum.optional(),
    limitPrice: z.number().optional().describe("限价，orderPriceType=LIMIT 时必填"),
    timeCondition: timeConditionEnum.optional(),
    validUntil: z.string().optional().describe("有效期截止日 yyyy-MM-dd"),
    remark: z.string().optional(),
};
function registerSlzqTools(server) {
    registerAuthTools(server);
    server.registerTool("slzq_open_v1_health", {
        description: "GET /open/v1/health — 健康检查 + 能力探测，无需 Api-Key。返回 status、authLoginSupported、skillName、skillVersion，" +
            "以及 apiBase=服务端实际生效的路径前缀（部署可能带 /sanli 之类网关前缀，与你拼的不一致时以它为准）。" +
            "判断服务端是否支持免密钥登录**只能**看 authLoginSupported，不要拿 /open/v1/auth/* 的 10411 去推断。",
    }, async () => runTool(() => openApiFetch("/health", { auth: false })));
    server.registerTool("slzq_open_v1_skill_version", {
        description: "GET /open/v1/skill/version — skill 版本检查，无需 Api-Key。传 clientVersion（本地 VERSION 文件或 SKILL.md frontmatter 的 version）" +
            "才会返回 updateAvailable，不传时该字段为 null（**null 不等于已是最新**）。" +
            "先看返回的 skillName：与本地包名不一致说明该服务端跑的是另一套品牌配置，它给的 latestVersion 是别的包的，不要据此让用户升级或降级。",
        inputSchema: { clientVersion: z.string().optional().describe("本地 skill 版本号，如 1.4.0；不传则 updateAvailable 恒为 null") },
    }, async (args) => runTool(() => openApiFetch("/skill/version", {
        auth: false,
        searchParams: { clientVersion: args?.clientVersion },
    })));
    server.registerTool("slzq_open_v1_skill_upgrade", {
        description: "GET /open/v1/skill/upgrade — 升级指引，无需 Api-Key",
    }, async () => runTool(() => openApiFetch("/skill/upgrade", { auth: false })));
    server.registerTool("slzq_open_v1_me", {
        description: "GET /open/v1/me — 当前密钥上下文与权限档位。返回 userId、keyId、tradingEnv（本次请求实际生效的环境）、" +
            "scope（SIM=仅模拟盘，SIM_LIVE=模拟盘+实盘）、canTradeLive、liveUpgradeSteps。" +
            "下实盘单前先用它确认 canTradeLive=true 且 tradingEnv=live；canTradeLive=false 时把 liveUpgradeSteps 原样转述给用户，" +
            "实盘权限只能由用户本人在 App 内开通，不要在会话里向用户索要 CTP 交易密码。",
    }, async () => runTool(() => openApiFetch("/me", { auth: true })));
    server.registerTool("slzq_open_v1_account_summary", {
        description: "GET /open/v1/account/summary — 账户资金摘要。**数据按环境分字段嵌套，且两个环境字段名完全不同**：" +
            "sim → data.simAccount：全部资金 equity(=accountEquity)、可用 availableEquity、持仓占用保证金 usedMargin、" +
            "委托冻结 frozenEquity、持仓浮动盈亏 positionProfit、月累计盈亏 totalProfitLoss、月收益率 profitRate、风险度 riskRate；" +
            "**sim 没有 balance / available / margin 这三个字段**。" +
            "live → data.liveTradeAccount（CTP TradeAccountModel）：账户权益 balance、可用 available、" +
            "当前占用保证金 currMargin（**不是 margin**）、持仓盈亏 positionProfit、平仓盈亏 closeProfit、" +
            "冻结 frozenMargin/frozenCash/frozenCommission、手续费 commission、accountId、tradingDay。" +
            "所以「还有多少钱」sim 读 equity、live 读 balance；「可用」sim 读 availableEquity、live 读 available。" +
            "解析前先看 data.tradingEnv，**不要猜字段名**。" +
            "sim 无需事先在 App 开户，服务端会幂等自动开通；live 未绑定实盘 CTP 凭据时报 10413。",
    }, async () => runTool(() => openApiFetch("/account/summary", { auth: true })));
    server.registerTool("slzq_open_v1_account_pnl_history", {
        description: "GET /open/v1/account/pnl/history — 账户历史盈亏（日/周序列 + 区间合计）。" +
            "用户问「这个月赚了多少」「最近一周盈亏」「收益率多少」时用它，**不要自己拉成交记录手工累加**——" +
            "那样算不出持仓盯市盈亏，结果一定和 App 对不上。区间用 preset 或 startTradingDay+endTradingDay 二选一，都不传默认 last90d。" +
            "periodTotalProfit=区间内各日「平仓盈亏+持仓盯市盈亏」之和（元）；" +
            "periodTotalRate=区间收益率(%)，**仅 sim 有值，live 恒为 null**（实盘没有统一初始资金口径，不要自己编一个去算）；" +
            "detail.dailyData/weeklyData=日/周明细，detail.summary 仅 sim 有。" +
            "live 数据来自已落库的结算单解析：**区间内没落库结算单的交易日就是没有数据**，不代表那天没交易或盈亏为 0，" +
            "按 liveNote 如实说明，不要补零、不要外推。",
        inputSchema: {
            preset: z
                .enum(["last7d", "last30d", "last90d", "monthToDate"])
                .optional()
                .describe("区间预设，仅在未传 startTradingDay+endTradingDay 时生效，不传默认 last90d。" +
                "last7d/last30d/last90d=从当前交易日往前推 7/30/90 个自然日（含边界）；monthToDate=当月 1 日至当前交易日"),
            startTradingDay: z
                .string()
                .optional()
                .describe("自定义区间起始交易日，yyyyMMdd 或 yyyy-MM-dd。必须与 endTradingDay 成对传，只传一个会报参数错误；传了则 preset 被忽略"),
            endTradingDay: z.string().optional().describe("自定义区间结束交易日（含），格式同 startTradingDay。必须与 startTradingDay 成对传"),
        },
    }, async (args) => runTool(() => openApiFetch("/account/pnl/history", {
        auth: true,
        searchParams: {
            preset: args?.preset,
            startTradingDay: args?.startTradingDay,
            endTradingDay: args?.endTradingDay,
        },
    })));
    server.registerTool("slzq_open_v1_positions", {
        description: "GET /open/v1/positions — 当前持仓。**同一个接口在两个环境返回的结构不一样，解析前先确认环境（me 的 tradingEnv）**：" +
            "sim 返回 PositionDetailResponseModel 数组，字段是 direction(1=买涨 2=买跌)/volume/costPrice/openAvgPrice/currentPrice/" +
            "estimatedProfitLoss/mtmProfit/margin/commission/openDetails/stopLossInfoList/stopProfitInfoList，SHFE 与 INE 会拆成今、昨两行；" +
            "live 返回 CTP PositionModel 数组，字段是 posiDirection(LONG/SHORT)/position/todayPosition/ydPosition/openCost/" +
            "openAveragePrice/positionProfit/useMargin。**两套字段名不通用**，拿 sim 的字段名读 live 数据只会全是 undefined——" +
            "不要猜字段名。算浮动盈亏必须用合约乘数 volumeMultiple（见 catalog_contract）。" +
            "有仓且用户未关闭提醒时，响应会带 skillReminder：把 text 原样告诉用户；用户回复「不再提醒」后调用 " +
            SL_TP_REMINDER_MUTE_TOOL + "。没有 skillReminder 就不要自己补提醒。",
        inputSchema: {
            positionDateType: z
                .enum(["今", "昨"])
                .optional()
                .describe("可选，**仅 sim 生效**：只保留 SHFE/INE 对应今仓或昨仓的行，其它交易所的汇总行会被过滤掉。live 忽略此参数"),
        },
    }, async (args) => runTool(() => openApiFetch("/positions", {
        auth: true,
        searchParams: { positionDateType: args?.positionDateType },
    }), async (payload, failed) => failed ? payload : withStopProfitLossReminder(payload, hasOpenPositions(payload))));
    server.registerTool(SL_TP_REMINDER_MUTE_TOOL, {
        description: "关闭「开仓/查看持仓时提醒设置止盈止损」。仅当用户明确回复「不再提醒」（或「不要再提醒」「不用提醒了」）后调用。" +
            "写入本机 ~/.slzq-trading/preferences.json，跨会话生效。没有用户这句话不得调用，也不得替用户默认关闭。",
    }, async () => {
        try {
            const prefs = await readSkillPrefs();
            prefs.stopProfitLossReminderMuted = true;
            prefs.stopProfitLossReminderMutedAt = new Date().toISOString();
            await writeSkillPrefs(prefs);
            return jsonResult({
                success: true,
                data: {
                    stopProfitLossReminderMuted: true,
                    message: "已关闭止盈止损提醒，之后开仓或查看持仓都不会再提。",
                },
            });
        }
        catch (e) {
            return textResult(`写入提醒偏好失败：${errorMessage(e)}`, true);
        }
    });
    server.registerTool("slzq_open_v1_catalog_goods", {
        description: "GET /open/v1/catalog/goods — 品种列表及其主力合约与实时行情，分页。返回交易时段 tradeTime、" +
            "**nextDayFlag（1=该品种有夜盘，0=没有；不要用 deleteFlag，那是软删除标记）**、isPrincipal（1=主力合约）、" +
            "mainContractCode 与主力行情。要找「现在能交易的活跃合约」优先用 catalog_hot。",
        inputSchema: {
            excode: z.string().optional().describe("交易所代码，如 SHFE/DCE/CZCE/INE/CFFEX/GFEX；特殊值 '__NIGHT__' 表示只看有夜盘的品种。不传=全部交易所"),
            page: z.number().int().optional().describe("页码，从 1 开始，默认 1"),
            pageSize: z.number().int().optional().describe("每页条数，默认 20，服务端最大 100"),
            sortType: z.number().int().optional().describe("排序：1=涨幅 2=跌幅 3=成交量 4=增仓。只认 1-4，其它值等于不排序"),
            category: z.string().optional().describe("按商品分类过滤"),
            productId: z.string().optional().describe("品种代码，如 au、cu。与 excode 同传时返回该品种下全部合约"),
            onlyMainInCategory: z.boolean().optional().describe("与 category 联用：只返回该分类的主力合约"),
            allContractsByExcode: z.boolean().optional().describe("与 excode 联用：返回该交易所全部有效合约，而不只是主力"),
        },
    }, async (args) => runTool(() => openApiFetch("/catalog/goods", {
        auth: true,
        searchParams: {
            excode: args?.excode,
            page: args?.page,
            pageSize: args?.pageSize,
            sortType: args?.sortType,
            category: args?.category,
            productId: args?.productId,
            onlyMainInCategory: args?.onlyMainInCategory,
            allContractsByExcode: args?.allContractsByExcode,
        },
    })));
    server.registerTool("slzq_open_v1_catalog_goods_detail", {
        description: "GET /open/v1/catalog/goods/detail — 品种（商品）详情：完整交易时段、" +
            "goods.nextDayFlag（1=该品种有夜盘，0=没有）与 calendarNightSessionTonight（交易日历今晚是否排夜盘）。" +
            "**两者是独立维度，都为真今晚才真的有夜盘**。goods.deleteFlag 是软删除标记，跟夜盘无关，别拿它判断。",
        inputSchema: {
            excode: z.string().describe("交易所代码，如 SHFE。必填"),
            code: z.string().describe("品种代码（不是合约代码），如 au、cu、rb。必填"),
        },
    }, async (args) => runTool(() => openApiFetch("/catalog/goods/detail", {
        auth: true,
        searchParams: { excode: args.excode, code: args.code },
    })));
    server.registerTool("slzq_open_v1_catalog_contract", {
        description: "GET /open/v1/catalog/contract — 合约规格。返回 isPrincipal（1=主力）、volumeMultiple（合约乘数，**算盈亏必须用它**）、" +
            "priceTick（最小变动价位，**下单价格必须是它的整数倍**）、priceLimit（涨跌停幅度，**行情快照里没有涨跌停，要就查这里**）、" +
            "shortMarginRatioByMoney（保证金率）、minTradeLots（最小下单手数）、nextDayFlag（1=该品种有夜盘）、" +
            "tradeTime/startTime/middleTime/endTime（交易时段）、expireDate 与交割日期、excode（所属交易所，**不确定交易所时用它查，不要猜**）。" +
            "对不熟悉的合约下单前先调它核对，不要凭记忆猜乘数、价位或合约月份。" +
            "保证金率与涨跌停**仅供参考**，实际以交易所和期货公司结算为准，转述时要带上这句。",
        inputSchema: { contractCode: z.string().describe("合约代码，如 rb2601、au2606、IF2506。保持目录接口返回的原样大小写") },
    }, async (args) => runTool(() => openApiFetch("/catalog/contract", { auth: true, searchParams: { contractCode: args.contractCode } })));
    server.registerTool("slzq_open_v1_catalog_contract_f10", {
        description: "GET /open/v1/catalog/contract/f10 — 合约的东财 F10 扩展资料（交割单位、交易单位、报价单位、交割品级、交割地点、保证金比例等）。" +
            "该合约不在东财库里时 eastmoneyDetail 为 null——**这只说明没有这份扩展资料，不代表合约不存在或不能交易**。",
        inputSchema: { contractCode: z.string() },
    }, async (args) => runTool(() => openApiFetch("/catalog/contract/f10", {
        auth: true,
        searchParams: { contractCode: args.contractCode },
    })));
    server.registerTool("slzq_open_v1_catalog_hot", {
        description: "GET /open/v1/catalog/hot — 近 30 分钟成交量前 10 的合约，含合约乘数、最小变动价位、交易时段、到期日。" +
            "用户说「买点黄金」「螺纹现在怎么样」这类没指明具体合约的需求时，先用它拿当前活跃合约，**不要凭记忆编一个合约月份**。",
    }, async () => runTool(() => openApiFetch("/catalog/hot", { auth: true })));
    server.registerTool("slzq_open_v1_catalog_exchanges", {
        description: "GET /open/v1/catalog/exchanges — 可用交易所列表（按商品数量降序），返回交易所代码与商品数量。不确定某品种属于哪个交易所时，用 catalog_contract 查，不要靠印象。",
    }, async () => runTool(() => openApiFetch("/catalog/exchanges", { auth: true })));
    server.registerTool("slzq_open_v1_catalog_session_night_today", {
        description: "GET /open/v1/catalog/session/night-today — **交易日历**层面今晚是否排夜盘（hasNightSessionTonight）。" +
            "这只是日历维度：**某个品种今晚是否交易，还要它自己的 nextDayFlag=1**，两个条件同时成立才有夜盘。" +
            "回答「今晚能不能交易 XX」时两个都要查，不能只看一个。",
    }, async () => runTool(() => openApiFetch("/catalog/session/night-today", { auth: true })));
    server.registerTool("slzq_open_v1_market_snapshot", {
        description: "GET /open/v1/market/snapshot — 单合约行情快照（读 Redis 缓存）。instrumentId 与 contractCode 是等价别名，" +
            "至少填一个（都不填会报参数错误并指引你先调 catalog_hot）。返回 lastPrice/openPrice/highestPrice/lowestPrice/" +
            "bidPrice1/bidVolume1/askPrice1/askVolume1/preSettlementPrice/settlementPrice/tradingDay/updateTime，" +
            "以及 volumeMultiple（合约乘数，算盈亏必须用它）与 priceTick。" +
            "**本接口不返回涨停价/跌停价，也不返回成交量与持仓量**——要涨跌停去查 catalog_contract，缺什么就说缺什么，不要编造。" +
            "除 volumeMultiple 是整数外**价格与量都是字符串**，算术前先转数字；priceTick 可能为 null。" +
            "缓存缺失时字段为 null——**null 表示这一刻缓存里没有，不代表该合约停牌或不存在**。" +
            NO_SELF_POLLING,
        inputSchema: {
            instrumentId: z.string().optional(),
            contractCode: z.string().optional(),
        },
    }, async (args) => runTool(() => openApiFetch("/market/snapshot", {
        auth: true,
        searchParams: {
            instrumentId: args?.instrumentId,
            contractCode: args?.contractCode,
        },
    })));
    server.registerTool("slzq_open_v1_market_snapshots", {
        description: "GET /open/v1/market/snapshots — 批量行情快照。instrumentIds 用英文逗号分隔，建议一次不超过 20 个。" +
            "返回数组顺序与传入顺序一致，每条结构与单合约快照完全相同（同样不含涨跌停与持仓量）。" + NO_SELF_POLLING,
        inputSchema: { instrumentIds: z.string() },
    }, async (args) => runTool(() => openApiFetch("/market/snapshots", {
        auth: true,
        searchParams: { instrumentIds: args.instrumentIds },
    })));
    server.registerTool("slzq_open_v1_market_tick", {
        description: "GET /open/v1/market/tick — 今日分时（每分钟一条）。返回 ticks 数组，每条 {t,p,v,i,a}：" +
            "t=**毫秒**时间戳字符串（13 位，按秒解析会算出五万年后的日期，要先除以 1000）、p=价格、v=该分钟成交量、i=持仓量；" +
            "**a 恒为 0**（服务端在分时路径上从未赋值，不要当成交额用）。" +
            "外层 startTime/endTime/closeTime/totalVolume/reqTime，其中 reqTime 是**秒**，与数组里的毫秒 t 单位不同，别混用。" +
            EXCHANGE_OPTIONAL + NO_SELF_POLLING,
        inputSchema: {
            exchangeId: exchangeIdOptional,
            instrumentId: z.string().optional().describe("合约代码，如 au2606。与 contractCode 二选一，优先 instrumentId"),
            contractCode: z.string().optional().describe("合约代码的别名，与 instrumentId 等价"),
        },
    }, async (args) => runTool(() => openApiFetch("/market/tick", {
        auth: true,
        searchParams: {
            exchangeId: args?.exchangeId,
            instrumentId: args?.instrumentId,
            contractCode: args?.contractCode,
        },
    })));
    server.registerTool("slzq_open_v1_market_kline", {
        description: "GET /open/v1/market/kline — K 线，数组在 chats 字段、从旧到新。每条 {t,o,h,l,c,v,a,u,i,s}：" +
            "t=格式化时间标签（分钟线 MM-dd HH:mm，日/周线 yyyy-MM-dd）、o/h/l/c=开高低收、v=成交量、" +
            "u=**秒**级时间戳（排序计算用它，不要去解析 t）、i=持仓量、" +
            "s=结算价（**只有 type=6 日线才赋值**，其余周期为 null，不要当 0）；" +
            "**a 恒为 0**（服务端从未赋值，不要当成交额用）。除 u 是数字外其余都是字符串，算术前先转数字。" +
            EXCHANGE_OPTIONAL + NO_SELF_POLLING,
        inputSchema: {
            exchangeId: exchangeIdOptional,
            instrumentId: z.string().optional().describe("合约代码，如 au2606。与 contractCode 二选一，优先 instrumentId"),
            contractCode: z.string().optional().describe("合约代码的别名，与 instrumentId 等价"),
            type: z
                .union([z.literal(10), z.literal(2), z.literal(3), z.literal(4), z.literal(5), z.literal(9), z.literal(6), z.literal(7)])
                .optional()
                .describe("K 线周期，只接受这 8 个值：10=1分钟，2=5分钟，3=15分钟，4=30分钟，5=1小时，9=4小时，6=日线，7=周线。" +
                "不传默认 10（1分钟）。**没有月线，也没有 1 或 8**，传别的数字拿不到数据——不要按「1=1分钟」之类的直觉推"),
        },
    }, async (args) => runTool(() => openApiFetch("/market/kline", {
        auth: true,
        searchParams: {
            exchangeId: args?.exchangeId,
            instrumentId: args?.instrumentId,
            contractCode: args?.contractCode,
            type: args?.type,
        },
    })));
    server.registerTool("slzq_open_v1_orders_open", {
        description: "GET /open/v1/orders/open — 未完结委托（已报、部分成交等，不含已成交/已撤销）。sim 与 live 都**只看近 3 日**，" +
            "更早的这里查不到——查不到不等于用户没下过单。字段有 orderRef / orderSysId / frontID / sessionId / orderStatus / statusMsg / " +
            "instrumentId / exchangeId / direction / offsetFlag / limitPrice / volume（委托手数）/ volumeTraded（已成交）/ volumeTotal（剩余未成交）。" +
            "**要撤单就从这里取 orderRef、orderSysId、frontID、exchangeId 原样传给撤单工具**，不要自己拼，也不要用下单时传入的值。",
    }, async () => runTool(() => openApiFetch("/orders/open", { auth: true })));
    server.registerTool("slzq_open_v1_trades", {
        description: "GET /open/v1/trades — 成交记录。live 未传时间范围时默认近 3 日；sim 不传时间就是全部历史。" +
            "⚠️ live 下 insertTimeStart 与 insertTimeEnd **必须成对传**——只传一个的话服务端会把两个一起改回近 3 日默认值，" +
            "你以为在查某段历史，实际拿到的是近 3 日。平仓成交的 profit 是柜台返回的实际盈亏，开仓成交为 null（不是 0，别累加进去）。" +
            "要算区间盈亏请用 account_pnl_history，自己累加成交算不出盯市盈亏。",
        inputSchema: {
            instrumentId: z.string().optional().describe("可选，按合约代码过滤，如 cu2506"),
            exchangeId: z.string().optional().describe("可选，按交易所过滤，如 SHFE。不确定就不要传"),
            insertTimeStart: z.string().optional().describe("可选，开始时间 'yyyy-MM-dd HH:mm:ss'。live 下必须与 insertTimeEnd 同时传，否则两个都会被忽略"),
            insertTimeEnd: z.string().optional().describe("可选，结束时间 'yyyy-MM-dd HH:mm:ss'。live 下必须与 insertTimeStart 同时传"),
        },
    }, async (args) => runTool(() => openApiFetch("/trades", {
        auth: true,
        searchParams: {
            instrumentId: args?.instrumentId,
            exchangeId: args?.exchangeId,
            insertTimeStart: args?.insertTimeStart,
            insertTimeEnd: args?.insertTimeEnd,
        },
    })));
    server.registerTool("slzq_open_v1_orders_place", {
        description: "POST /open/v1/orders — 下单，**只用于当下立即成交**（带「到价才买/才平」条件的需求走云条件单，见 cloud 系列工具）。" +
            "priceType 市价必须传 ANY，禁止 MARKET（MARKET 是条件单字段）。" +
            "未经用户明确指令**不得**对 live 自动下单；下单前把合约、方向、开平、手数、价格复述给用户确认。" +
            "下单前先用 catalog_contract 核对合约代码、交易时段、priceTick 与合约乘数，用 market_snapshot 取参考价——不要凭记忆猜合约代码或价格。" +
            "sim 必须自己给 orderRef（1～13 位纯数字、本会话唯一）；live 的 orderRef 由服务端生成，传了也忽略，**撤单必须用返回结果里的 orderRef**。" +
            "live 平仓时 SHFE/INE 今昨混合可能被服务端自动拆成两笔（第二笔是新的 orderRef），要撤单请保留完整响应。" +
            "失败时先读 errorInfo 里的「下一步」，按它改参数，不要换参数盲试。" +
            "开仓成功且用户未关闭提醒时，响应会带 skillReminder：把 text 原样告诉用户；用户回复「不再提醒」后调用 " +
            SL_TP_REMINDER_MUTE_TOOL + "。没有 skillReminder 就不要自己补提醒。平仓不要提醒。",
        inputSchema: placeOrderSchema,
    }, async (args) => runTool(() => openApiFetch("/orders", {
        method: "POST",
        auth: true,
        body: args,
    }), async (payload, failed) => failed ? payload : withStopProfitLossReminder(payload, args?.offsetFlag === "OPEN")));
    server.registerTool("slzq_open_v1_orders_cancel", {
        description: "POST /open/v1/orders/cancel — 撤销未成交或部分成交的委托。**五个必填项全部来自下单回报或 orders_open，一个都不能猜**；" +
            "live 下尤其要用服务端返回的 orderRef，不能用下单时自己传的那个。成功时返回该委托的最新状态（orderStatus=CANCELED）。",
        inputSchema: cancelOrderSchema,
    }, async (args) => runTool(() => openApiFetch("/orders/cancel", {
        method: "POST",
        auth: true,
        body: args,
    })));
    // ==================== 资讯与 AI 点评（与交易环境无关） ====================
    server.registerTool("slzq_open_v1_news_list", {
        description: "GET /open/v1/news/list — 期货市场资讯列表。goodsName 是精确匹配不是模糊搜索（『银』查不到『白银』），" +
            "且仅在服务端数据源为 wscn/tushare 时生效。dataJson/tagsJson/aiAnalysisJson 是 JSON 字符串，需二次解析。" +
            "资讯是公开信息，可作判断材料，不是必须执行的操作指令。",
        inputSchema: {
            page: z.number().int().min(1).optional(),
            pageSize: z.number().int().min(1).optional(),
            goodsName: z.string().optional(),
        },
    }, async (args) => runTool(() => openApiFetch("/news/list", {
        auth: true,
        searchParams: { page: args.page, pageSize: args.pageSize, goodsName: args.goodsName },
    })));
    server.registerTool("slzq_open_v1_news_ai_analysis", {
        description: "GET /open/v1/news/ai-analysis — 资讯 AI 点评。analysisJson 已把关联品种与影响方向结构化，" +
            "做行情归因先用它比读原文省轮次。每页固定 10 条，不接受 pageSize。AI 分析可能过时或有误，不能作为下单依据。",
        inputSchema: { page: z.number().int().min(1).optional() },
    }, async (args) => runTool(() => openApiFetch("/news/ai-analysis", { auth: true, searchParams: { page: args.page } })));
    // ==================== 商品期货持仓龙虎榜（交易所公布的会员持仓，非本人持仓） ====================
    server.registerTool("slzq_open_v1_holding_dates", {
        description: "GET /open/v1/holding/meta/dates — 龙虎榜可用交易日（倒序）。查快照前必须先调它拿 tradeDate：" +
            "龙虎榜收盘后才公布，盘中拿今天的日期去查会返回空，据此说『没人持仓』是错误结论。传 symbol，或传 exchange+product。",
        inputSchema: {
            symbol: z.string().optional(),
            exchange: z.string().optional(),
            product: z.string().optional(),
        },
    }, async (args) => runTool(() => openApiFetch("/holding/meta/dates", {
        auth: true,
        searchParams: { symbol: args.symbol, exchange: args.exchange, product: args.product },
    })));
    server.registerTool("slzq_open_v1_holding_contracts", {
        description: "GET /open/v1/holding/meta/contracts — 龙虎榜里某品种下可查询的合约列表。exchange 与 product 都必填，" +
            "product 是品种前缀（如 rb）不是合约代码（rb2601）。",
        inputSchema: { exchange: z.string(), product: z.string() },
    }, async (args) => runTool(() => openApiFetch("/holding/meta/contracts", {
        auth: true,
        searchParams: { exchange: args.exchange, product: args.product },
    })));
    server.registerTool("slzq_open_v1_holding_brokers", {
        description: "GET /open/v1/holding/meta/brokers — 龙虎榜里可选的期货公司会员列表，用来拿 broker_summary 需要的 brokerPrefix。" +
            "会员简称是交易所口径，与期货公司全称不一定一致——**要用就从这里取，不要自己拼公司名**。",
        inputSchema: {
            symbol: z.string().optional(),
            exchange: z.string().optional(),
            product: z.string().optional(),
            tradeDate: z.string().optional(),
        },
    }, async (args) => runTool(() => openApiFetch("/holding/meta/brokers", {
        auth: true,
        searchParams: {
            symbol: args.symbol,
            exchange: args.exchange,
            product: args.product,
            tradeDate: args.tradeDate,
        },
    })));
    server.registerTool("slzq_open_v1_holding_update_time", {
        description: "GET /open/v1/holding/meta/update-time — 该维度下龙虎榜数据的最新交易日（MAX(trade_date)），" +
            "用来判断数据是否已更新到最近一个交易日。查快照要用的日期请用 holding_dates 取。",
        inputSchema: {
            symbol: z.string().optional(),
            exchange: z.string().optional(),
            product: z.string().optional(),
        },
    }, async (args) => runTool(() => openApiFetch("/holding/meta/update-time", {
        auth: true,
        searchParams: { symbol: args.symbol, exchange: args.exchange, product: args.product },
    })));
    server.registerTool("slzq_open_v1_holding_snapshot", {
        description: "GET /open/v1/holding/snapshot — 持仓龙虎榜快照：交易所公布的会员持买/持卖仓量、多空占比、会员排行。" +
            "这是市场整体多空分布，不是用户本人持仓（本人持仓用 slzq_open_v1_positions）。" +
            "tradeDate 必填且须来自 slzq_open_v1_holding_dates。数据滞后一个交易日，不能当实时行情；可以辅助判断，但须说明数据滞后。不要解读成某公司看多。",
        inputSchema: {
            tradeDate: z.string(),
            symbol: z.string().optional(),
            exchange: z.string().optional(),
            product: z.string().optional(),
            summary: z.boolean().optional(),
        },
    }, async (args) => runTool(() => openApiFetch("/holding/snapshot", {
        auth: true,
        searchParams: {
            tradeDate: args.tradeDate,
            symbol: args.symbol,
            exchange: args.exchange,
            product: args.product,
            summary: args.summary,
        },
    })));
    server.registerTool("slzq_open_v1_holding_position_trend", {
        description: "GET /open/v1/holding/position-trend — 龙虎榜多空持仓趋势（近 90 自然日）。" +
            "返回 categories/longSeries/shortSeries 三个等长数组；按自然日补全，非交易日与无数据日的值是 null 不是 0，" +
            "算变化率或求和时必须跳过 null，当成 0 会凭空造出持仓归零的暴跌。",
        inputSchema: {
            endDate: z.string(),
            symbol: z.string().optional(),
            exchange: z.string().optional(),
            product: z.string().optional(),
            summary: z.boolean().optional(),
        },
    }, async (args) => runTool(() => openApiFetch("/holding/position-trend", {
        auth: true,
        searchParams: {
            endDate: args.endDate,
            symbol: args.symbol,
            exchange: args.exchange,
            product: args.product,
            summary: args.summary,
        },
    })));
    server.registerTool("slzq_open_v1_holding_broker_summary", {
        description: "GET /open/v1/holding/broker-summary — 某会员在某品种上的持仓结构。会员持仓含其全部客户的净头寸与套保盘，" +
            "方向与盈亏没有必然联系，不要解读成『该公司看多』，也不要据此评价任何一家期货公司的优劣。",
        inputSchema: {
            exchange: z.string(),
            product: z.string(),
            brokerPrefix: z.string(),
            tradeDate: z.string(),
        },
    }, async (args) => runTool(() => openApiFetch("/holding/broker-summary", {
        auth: true,
        searchParams: {
            exchange: args.exchange,
            product: args.product,
            brokerPrefix: args.brokerPrefix,
            tradeDate: args.tradeDate,
        },
    })));
    server.registerTool("slzq_open_v1_holding_broker_volume_trend", {
        description: "GET /open/v1/holding/broker-volume-trend — 某家期货公司会员在某品种上的成交量趋势。" +
            "exchange/product/brokerPrefix/endDate 必填，range 取 1m/3m/6m（默认 1m）。" +
            "成交量只反映活跃度，**与看多看空、与该公司好坏都没有关系**，不要据此评价任何一家期货公司。",
        inputSchema: {
            exchange: z.string(),
            product: z.string(),
            brokerPrefix: z.string(),
            endDate: z.string(),
            range: z.enum(["1m", "3m", "6m"]).optional(),
            productName: z.string().optional(),
        },
    }, async (args) => runTool(() => openApiFetch("/holding/broker-volume-trend", {
        auth: true,
        searchParams: {
            exchange: args.exchange,
            product: args.product,
            brokerPrefix: args.brokerPrefix,
            endDate: args.endDate,
            range: args.range,
            productName: args.productName,
        },
    })));
    // ==================== 云条件单 / 止盈止损（仅 live，替代自己盯盘） ====================
    server.registerTool("slzq_open_v1_cloud_orders", {
        description: "GET /open/v1/cloud/orders — 云挂单/止盈止损分页查询。orderCategory：0=条件单 1=挂单 2=止盈止损；" +
            "status：0待触发 1已触发 2委托中 3已成交 4已撤销 5失败 6部分成交。返回项的 id 即后续修改/撤销要用的 orderId。" +
            "【条件单不要用它查】这里是旧口径，状态码和字段与用户在 App 里看到的对不上；查条件单用 slzq_open_v1_cloud_condition_order_list。" +
            " 建完单不要定时回来查有没有触发——用户问了才查，那等于换个接口继续盯盘。" +
            CLOUD_LIVE_ONLY,
        inputSchema: {
            orderCategory: z.number().int().optional(),
            status: z.number().int().optional(),
            instrumentId: z.string().optional(),
            pageNum: z.number().int().min(1).optional(),
            pageSize: z.number().int().min(1).optional(),
        },
    }, async (args) => runTool(() => openApiFetch("/cloud/orders", {
        auth: true,
        searchParams: {
            orderCategory: args.orderCategory,
            status: args.status,
            instrumentId: args.instrumentId,
            pageNum: args.pageNum,
            pageSize: args.pageSize,
        },
    })));
    server.registerTool("slzq_open_v1_cloud_order_actions", {
        description: "GET /open/v1/cloud/orders/actions — 云条件单动作历史（操作日志、状态变更、触发价、失败原因）。" +
            "排查『为什么没触发/为什么失败』先看这里，比反复查列表有效。" + CLOUD_LIVE_ONLY,
        inputSchema: { orderId: z.number().int() },
    }, async (args) => runTool(() => openApiFetch("/cloud/orders/actions", { auth: true, searchParams: { orderId: args.orderId } })));
    server.registerTool("slzq_open_v1_cloud_pending_order_create", {
        description: PENDING_DISABLED +
            "POST /open/v1/cloud/orders/pending — 创建挂单（非交易时段先挂上、开盘自动报出）。" +
            CLOUD_MUTATION,
        inputSchema: cloudPendingOrderSchema,
    }, async (args) => runTool(() => openApiFetch("/cloud/orders/pending", { method: "POST", auth: true, body: args })));
    server.registerTool("slzq_open_v1_cloud_stop_profit_loss_create", {
        description: CLOUD_TRIGGER_INTRO +
            "POST /open/v1/cloud/orders/stop-profit-loss — 对已有持仓创建止盈止损（任何时间可创建）。" +
            "**禁止传 positionDateType**（立即下单字段，本接口没有，传「今」「昨」会被丢掉）。" +
            "要指定今/昨传可选 offsetFlag：今=3，昨=1，不必传 4；整仓不要传 offsetFlag。" +
            "**平今不能传 GTC**：先说明只能当日有效（当天 15:00），等用户确认后再用 GFD 建单。" +
            "exchangeId 不确定就不要传，服务端按合约代码补齐；**补不上会拒绝**，向用户确认合约代码，不要猜。" +
            "服务端会查 CTP 实际持仓校验合约/方向/数量，报『持仓不足』就是真的不足，不要改大数量重试。" +
            "上期所、能源、中金所整仓止盈止损由服务端拆成两张：平昨用普通平仓 offsetFlag=1，平今用 offsetFlag=3，与 App 相同。用户只要平今时可在本接口传 offsetFlag=3，或改用条件单并传 3；只要平昨时传 1，不必传 4。" +
            CLOUD_MUTATION,
        inputSchema: cloudStopProfitLossSchema,
    }, async (args) => runTool(() => openApiFetch("/cloud/orders/stop-profit-loss", { method: "POST", auth: true, body: args })));
    server.registerTool("slzq_open_v1_cloud_condition_order_create", {
        description: CLOUD_TRIGGER_INTRO +
            "POST /open/v1/cloud/orders/condition — 创建条件单（任何时间可创建，由 cloud-ctp 盯行情、条件满足自动报单）。" +
            "**建出来的单和用户自己在 App 里下的是同一种**，他能在 App「交易 → 条件单」里看到、自己改自己撤。" +
            "触发条件只用 triggerMode + 触发价表达；**没有 conditionType / triggerPriceType 这两个参数了**，" +
            "那是旧版字段，不要再传（传 triggerPriceType=2/3 会直接报错）。" +
            CLOUD_MUTATION,
        inputSchema: cloudConditionOrderSchema,
    }, async (args) => runTool(() => openApiFetch("/cloud/orders/condition", { method: "POST", auth: true, body: args })));
    server.registerTool("slzq_open_v1_cloud_condition_order_list", {
        description: "GET /open/v1/cloud/orders/condition — 查条件单：**全部盯盘中的单**（不限创建日） ∪ 时间窗内创建的任意状态，" +
            "和用户在 App「交易 → 条件单」里看到的是同一份数据。不传时间窗时窗口就是当前交易日。" +
            "用户问『我那单还在吗/触发没有』时查这里。" +
            "状态 status：0 盯盘中 1 已触发 2 已暂停 3 已撤销 4 已失效 5 失败——" +
            "**和 slzq_open_v1_cloud_orders 的状态码不是一套**，念给用户直接用 statusLabel，不要按数字自己编文案。" +
            "返回项 type=group 的是同合约分组，真正的单在它的 orders[] 里，别把分组行当成一张单。" +
            NO_SELF_POLLING +
            CLOUD_LIVE_ONLY,
        inputSchema: {
            tabType: z
                .union([z.literal("OPEN"), z.literal("CLOSE")])
                .optional()
                .describe("OPEN=只看开仓条件单，CLOSE=只看平仓条件单；不传看全部"),
            startTime: z.string().optional().describe("创建时间起 yyyy-MM-dd HH:mm:ss，要和 endTime 成对传"),
            endTime: z.string().optional().describe("创建时间止 yyyy-MM-dd HH:mm:ss"),
        },
    }, async (args) => runTool(() => openApiFetch("/cloud/orders/condition", {
        auth: true,
        searchParams: { tabType: args.tabType, startTime: args.startTime, endTime: args.endTime },
    })));
    server.registerTool("slzq_open_v1_cloud_condition_order_detail", {
        description: "GET /open/v1/cloud/orders/condition/detail — 条件单详情，含触发条件 conditions 与动作历史 actions。" +
            "排查『为什么没触发/为什么失败』先看 actions，比反复查列表有效。" +
            CLOUD_LIVE_ONLY,
        inputSchema: { orderId: z.number().int().describe("条件单 id") },
    }, async (args) => runTool(() => openApiFetch("/cloud/orders/condition/detail", { auth: true, searchParams: { orderId: args.orderId } })));
    server.registerTool("slzq_open_v1_cloud_pending_order_modify", {
        description: PENDING_DISABLED +
            "POST /open/v1/cloud/orders/pending/modify — 修改挂单。" + CLOUD_MUTATION,
        inputSchema: {
            orderId: z.number().int(),
            limitPrice: z.number().optional(),
            volume: z.number().int().optional(),
            direction: z.number().int().optional(),
            offsetFlag: z.number().int().optional(),
            orderPriceType: z.number().int().optional(),
            timeCondition: timeConditionEnum.optional(),
            remark: z.string().optional(),
        },
    }, async (args) => runTool(() => openApiFetch("/cloud/orders/pending/modify", { method: "POST", auth: true, body: args })));
    server.registerTool("slzq_open_v1_cloud_stop_profit_loss_modify", {
        description: "POST /open/v1/cloud/orders/stop-profit-loss/modify — 修改止盈止损的触发价/数量/有效期/触发后下单价格类型。" +
            CLOUD_MUTATION,
        inputSchema: {
            orderId: z.number().int(),
            triggerPrice: z.number().optional(),
            volume: z.number().int().optional(),
            stopPriceType: z.number().int().optional(),
            orderPrice: z.number().optional(),
            timeCondition: timeConditionEnum.optional(),
            remark: z.string().optional(),
        },
    }, async (args) => runTool(() => openApiFetch("/cloud/orders/stop-profit-loss/modify", { method: "POST", auth: true, body: args })));
    server.registerTool("slzq_open_v1_cloud_condition_order_modify", {
        description: "POST /open/v1/cloud/orders/condition/modify — 修改条件单：触发条件/数量/报单价格类型/有效期。" +
            "只传 id 和要改的字段，没传的保持不变；**要改触发价就把 triggerMode 和触发价一起传**，条件是整体重建的。" +
            "**仅盯盘中或已暂停的单可改**；报『状态不允许』就是已经触发/撤销/失效了，不要换参数重试，要换条件就撤了重建。" +
            CLOUD_MUTATION,
        inputSchema: cloudConditionOrderModifySchema,
    }, async (args) => runTool(() => openApiFetch("/cloud/orders/condition/modify", { method: "POST", auth: true, body: args })));
    server.registerTool("slzq_open_v1_cloud_order_cancel", {
        description: "POST /open/v1/cloud/orders/cancel — 撤销云条件单/挂单/止盈止损（三类通用，按 orderId）。" +
            "服务端按单子自己的类型走对应的撤销链路，不用先判断是哪一类。" +
            CLOUD_MUTATION,
        inputSchema: { orderId: z.number().int() },
    }, async (args) => runTool(() => openApiFetch("/cloud/orders/cancel", { method: "POST", auth: true, searchParams: { orderId: args.orderId } })));
}
async function main() {
    config = await loadConfig();
    const server = new McpServer({
        name: "slzq-trading-mcp",
        version: "1.5.3",
    });
    registerSlzqTools(server);
    const transport = new StdioServerTransport();
    await server.connect(transport);
}
main().catch((err) => {
    console.error(err);
    process.exit(1);
});
