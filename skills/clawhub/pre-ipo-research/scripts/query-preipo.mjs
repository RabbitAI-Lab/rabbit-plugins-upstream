#!/usr/bin/env node

const DEFAULT_BASE_URL = "https://preipo.polyos.ai";
const VALID_MARKETS = new Set(["live", "presale"]);
const VALID_TRADES = new Set(["buy_sell", "buy_only", "sell_only", "inactive"]);
const VALID_SORTS = new Set(["valuation_desc", "price_desc", "updated_desc", "name_asc"]);
const VALID_STAGES = new Set(["Live", "Locking Period", "Presale", "Early Access"]);

function usage(exitCode = 0) {
  const message = `
Pre-IPO Observer query client

Usage:
  node query-preipo.mjs summary [--base URL] [--json]
  node query-preipo.mjs search <keywords> [filters] [--base URL] [--json]
  node query-preipo.mjs list [filters] [--base URL] [--json]

Filters:
  --market live|presale
  --stage "Live"|"Locking Period"|Presale|"Early Access"
  --trade buy_sell|buy_only|sell_only|inactive
  --sort valuation_desc|price_desc|updated_desc|name_asc
  --page N                 Defaults to 1
  --page-size N            6–48; defaults to 12

Options:
  --base URL               Defaults to PREIPO_API_BASE_URL or ${DEFAULT_BASE_URL}
  --json                   Print raw JSON
  --help                   Show this help
`;
  console.log(message.trim());
  process.exit(exitCode);
}

function fail(message) {
  console.error(`Error: ${message}`);
  process.exit(1);
}

function parseArgs(argv) {
  const positional = [];
  const options = {};
  const optionNames = new Set(["base", "market", "stage", "trade", "sort", "page", "page-size"]);

  for (let index = 0; index < argv.length; index += 1) {
    const value = argv[index];
    if (value === "--help" || value === "-h") usage();
    if (value === "--json") {
      options.json = true;
      continue;
    }
    if (value.startsWith("--")) {
      const [rawName, inlineValue] = value.slice(2).split(/=(.*)/s, 2);
      if (!optionNames.has(rawName)) fail(`Unsupported option --${rawName}. Run with --help.`);
      const optionValue = inlineValue ?? argv[index + 1];
      if (!optionValue || optionValue.startsWith("--")) fail(`--${rawName} requires a value.`);
      options[rawName] = optionValue;
      if (inlineValue === undefined) index += 1;
      continue;
    }
    positional.push(value);
  }
  return { positional, options };
}

function validateOptions(options) {
  if (options.market && !VALID_MARKETS.has(options.market)) fail("--market must be live or presale.");
  if (options.trade && !VALID_TRADES.has(options.trade)) fail("--trade has an unsupported value.");
  if (options.sort && !VALID_SORTS.has(options.sort)) fail("--sort has an unsupported value.");
  if (options.stage && !VALID_STAGES.has(options.stage)) {
    fail('--stage must be "Live", "Locking Period", "Presale", or "Early Access".');
  }
  for (const name of ["page", "page-size"]) {
    if (options[name] && !/^\d+$/.test(options[name])) fail(`--${name} must be a positive integer.`);
  }
  if (options.page && Number(options.page) < 1) fail("--page must be at least 1.");
  if (options["page-size"] && (Number(options["page-size"]) < 6 || Number(options["page-size"]) > 48)) {
    fail("--page-size must be between 6 and 48.");
  }
}

function resolveBaseUrl(candidate) {
  try {
    const url = new URL(candidate || process.env.PREIPO_API_BASE_URL || DEFAULT_BASE_URL);
    if (!["http:", "https:"].includes(url.protocol)) throw new Error("protocol");
    return url.toString().replace(/\/$/, "");
  } catch {
    fail("--base or PREIPO_API_BASE_URL must be an http(s) URL.");
  }
}

async function requestJson(baseUrl, path, params) {
  const url = new URL(path, `${baseUrl}/`);
  for (const [key, value] of Object.entries(params)) {
    if (value !== undefined && value !== "") url.searchParams.set(key, value);
  }

  let response;
  try {
    response = await fetch(url, { headers: { accept: "application/json" } });
  } catch (error) {
    fail(`Could not reach ${url.origin}: ${error.message}. Set PREIPO_API_BASE_URL to a reachable compatible deployment if needed.`);
  }

  const contentType = response.headers.get("content-type") || "";
  const payload = contentType.includes("application/json")
    ? await response.json()
    : { error: (await response.text()).slice(0, 200) };
  if (!response.ok) fail(`API returned HTTP ${response.status}: ${payload.error || "request failed"}`);
  return payload;
}

function timestamp(value) {
  if (!value) return "未提供";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return String(value);
  return `${new Intl.DateTimeFormat("zh-CN", {
    dateStyle: "medium",
    timeStyle: "medium",
    timeZone: "Asia/Shanghai",
    hour12: false,
  }).format(date)}（中国标准时间；${date.toISOString()}）`;
}

function number(value, { suffix = "", digits = 2 } = {}) {
  if (value === null || value === undefined) return "未提供";
  const numeric = Number(value);
  if (!Number.isFinite(numeric)) return String(value);
  return `${new Intl.NumberFormat("en-US", { maximumFractionDigits: digits }).format(numeric)}${suffix}`;
}

function money(value, { millions = false } = {}) {
  if (value === null || value === undefined) return "未提供";
  return millions ? `US$${number(value, { suffix: "m" })}` : `US$${number(value)}`;
}

function tradeStatus(asset) {
  const buy = asset.buyActive ? "可买" : "不可买";
  const sell = asset.sellActive ? "可卖" : "不可卖";
  return `${buy} / ${sell}`;
}

function printSummary(data) {
  const stats = data.stats || {};
  console.log("数据源：Jarsy（Private Equity Live 与 Presale 点时快照）");
  console.log(`数据更新时间（最近成功导入）：${timestamp(data.lastImport?.importedAt)}`);
  console.log(`标的记录最新时间（全体最大值）：${timestamp(data.latestSourceRecordAt)}`);
  console.log(`标的：${number(stats.total, { digits: 0 })}；Live：${number(stats.liveCount, { digits: 0 })}；Presale：${number(stats.presaleCount, { digits: 0 })}`);
  console.log(`可买：${number(stats.buyEnabledCount, { digits: 0 })}；可卖：${number(stats.sellEnabledCount, { digits: 0 })}`);
  if (Array.isArray(data.stages) && data.stages.length) {
    console.log(`阶段分布：${data.stages.map((entry) => `${entry.stage} ${entry.count}`).join("；")}`);
  }
  if (Array.isArray(data.valuations) && data.valuations.length) {
    console.log("估值 Top 10：");
    for (const [index, item] of data.valuations.entries()) {
      console.log(`  ${index + 1}. ${item.companyName} (${item.token}) — ${money(item.valuationMillions, { millions: true })}`);
    }
  }
  console.log("说明：价格、估值和交易状态为 Jarsy 快照，不构成投资建议。");
}

function printAssets(data) {
  console.log(`匹配 ${number(data.total, { digits: 0 })} 个标的；第 ${data.page} 页，每页 ${data.pageSize} 个。`);
  if (!Array.isArray(data.items) || data.items.length === 0) {
    console.log("没有匹配结果。");
    return;
  }
  for (const [index, asset] of data.items.entries()) {
    const identity = asset.underlyingTicker || asset.underlyingName;
    console.log(`\n${(data.page - 1) * data.pageSize + index + 1}. ${asset.companyName} (${asset.token})`);
    console.log(`   市场/阶段：${asset.market} / ${asset.stage}${identity ? `；底层标的：${identity}` : ""}`);
    console.log(`   交易状态：${tradeStatus(asset)}；价格：${money(asset.priceUsd)}；估值：${money(asset.valuationMillions, { millions: true })}`);
    console.log(`   成交量：${money(asset.volumeUsd)}；标的记录更新时间：${timestamp(asset.sourceUpdatedAt)}`);
    if (asset.sourceUrl) console.log(`   Jarsy 来源：${asset.sourceUrl}`);
  }
  console.log("\n说明：每项“标的记录更新时间”与全站“数据更新时间”不同；所有数值均为 Jarsy 点时快照，不构成投资建议。");
}

async function main() {
  const { positional, options } = parseArgs(process.argv.slice(2));
  const command = positional.shift();
  if (!command) usage(1);
  validateOptions(options);
  const baseUrl = resolveBaseUrl(options.base);

  if (command === "summary") {
    if (positional.length) fail("summary does not accept extra positional arguments.");
    const data = await requestJson(baseUrl, "/api/summary", {});
    console.log(options.json ? JSON.stringify(data, null, 2) : "");
    if (!options.json) printSummary(data);
    return;
  }

  if (command !== "search" && command !== "list") fail(`Unsupported command ${command}. Run with --help.`);
  const query = command === "search" ? positional.join(" ").trim() : "";
  if (command === "search" && !query) fail("search requires one or more keywords.");
  if (command === "list" && positional.length) fail("list does not accept positional arguments.");

  const data = await requestJson(baseUrl, "/api/assets", {
    q: query || undefined,
    market: options.market,
    stage: options.stage,
    trade: options.trade,
    sort: options.sort,
    page: options.page,
    pageSize: options["page-size"],
  });
  console.log(options.json ? JSON.stringify(data, null, 2) : "");
  if (!options.json) printAssets(data);
}

main();
