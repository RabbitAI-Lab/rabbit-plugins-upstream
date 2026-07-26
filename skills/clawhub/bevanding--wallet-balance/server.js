import "dotenv/config";
import crypto from "crypto";
import fs from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";
import express from "express";
import helmet from "helmet";
import { ethers } from "ethers";
import { createClient } from "redis";
import Decimal from "decimal.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const MEMORY_FILE = process.env.MEMORY_STORE_PATH || path.join(__dirname, "remembered-addresses.json");

const app = express();
app.set("trust proxy", true);
app.use(helmet());
app.use(express.json({ limit: "64kb" }));

const PORT = Number(process.env.PORT || 3000);
const REDIS_URL = process.env.REDIS_URL || "redis://127.0.0.1:6379";
const ETH_RPC_URL = process.env.ETH_RPC_URL || "https://ethereum-rpc.publicnode.com";
const BNB_RPC_URL = process.env.BNB_RPC_URL || "https://bsc-rpc.publicnode.com";

const MCP_SKILLS_URL = (process.env.MCP_SKILLS_URL || "https://mcp-skills.ai.antalpha.com/mcp").trim();
const MCP_TOOL_NAME = (process.env.MCP_TOOL_NAME || "wallet-balance-query").trim();
const MCP_API_KEY = (process.env.MCP_API_KEY || "").trim();
const ENABLE_MCP = (process.env.ENABLE_MCP || "true").toLowerCase() === "true";
const ENABLE_FALLBACK_PROVIDER = (process.env.ENABLE_FALLBACK_PROVIDER || "true").toLowerCase() === "true";
const MAX_MCP_RESPONSE_CHARS = Math.min(
  Math.max(Number(process.env.MAX_MCP_RESPONSE_CHARS || 12_000_000), 64_000),
  50_000_000
);
const MCP_MAX_TOKEN_ROWS = Math.min(Math.max(Number(process.env.MCP_MAX_TOKEN_ROWS || 50_000), 100), 500_000);

const redis = createClient({ url: REDIS_URL });
let redisReady = false;

redis.on("error", (err) => {
  console.error("[redis] error:", err.message);
  redisReady = false;
});

redis.on("ready", () => {
  redisReady = true;
  console.log("[redis] connected");
});

const ethProvider = new ethers.JsonRpcProvider(ETH_RPC_URL);
const bnbProvider = new ethers.JsonRpcProvider(BNB_RPC_URL);
const ERC20_ABI = ["function balanceOf(address owner) view returns (uint256)", "function decimals() view returns (uint8)"];
const ERC20_TRACKED = {
  Ethereum: [{ symbol: "USDT", address: "0xdAC17F958D2ee523a2206206994597C13D831ec7" }],
  BSC: [{ symbol: "USDT", address: "0x55d398326f99059fF775485246999027B3197955" }],
};
const SYMBOL_PRICE_ID = {
  BTC: "bitcoin",
  ETH: "ethereum",
  BNB: "binancecoin",
  USDT: "tether",
  USDC: "usd-coin",
  DAI: "dai",
};

/** Static USD hints when CoinGecko is unreachable (display only; UPDATED_AT: 2026-03) */
const COINGECKO_ID_FALLBACK_USD = {
  bitcoin: 95000,
  ethereum: 3200,
  binancecoin: 600,
  tether: 1,
  "usd-coin": 1,
  dai: 1,
};

/** Map MCP `chain` codes to display name and numeric chain_id where known.
 *  Covers common EVM chain codes returned by wallet-balance-query.
 *  Last updated: 2026-04-10 (v1.3.0)
 */
const CHAIN_CODE_TO_META = {
  // ── Tier-1 EVM ──
  eth: { chain: "Ethereum", chain_id: 1 },
  ethereum: { chain: "Ethereum", chain_id: 1 },
  bsc: { chain: "BNB Chain", chain_id: 56 },
  bnb: { chain: "BNB Chain", chain_id: 56 },
  "bnb chain": { chain: "BNB Chain", chain_id: 56 },
  base: { chain: "Base", chain_id: 8453 },
  arb: { chain: "Arbitrum", chain_id: 42161 },
  arbitrum: { chain: "Arbitrum", chain_id: 42161 },
  op: { chain: "Optimism", chain_id: 10 },
  optimism: { chain: "Optimism", chain_id: 10 },
  polygon: { chain: "Polygon", chain_id: 137 },
  matic: { chain: "Polygon", chain_id: 137 },
  avax: { chain: "Avalanche", chain_id: 43114 },
  avalanche: { chain: "Avalanche", chain_id: 43114 },
  // ── ZK Rollups ──
  era: { chain: "zkSync Era", chain_id: 324 },
  zksync: { chain: "zkSync Era", chain_id: 324 },
  linea: { chain: "Linea", chain_id: 59144 },
  scrl: { chain: "Scroll", chain_id: 534352 },
  scroll: { chain: "Scroll", chain_id: 534352 },
  zora: { chain: "Zora Network", chain_id: 7777777 },
  taiko: { chain: "Taiko", chain_id: 167000 },
  zircuit: { chain: "Zircuit", chain_id: 48900 },
  // ── OP Stack / Superchain ──
  blast: { chain: "Blast", chain_id: 81457 },
  mode: { chain: "Mode", chain_id: 34443 },
  manta: { chain: "Manta Pacific", chain_id: 169 },
  ink: { chain: "Ink", chain_id: 57073 },
  soneium: { chain: "Soneium", chain_id: 1868 },
  uni: { chain: "Unichain", chain_id: 130 },
  lisk: { chain: "Lisk", chain_id: 1135 },
  cyber: { chain: "Cyber", chain_id: 7560 },
  bob: { chain: "BOB", chain_id: 60808 },
  dbk: { chain: "DBK Chain", chain_id: 20482050 },
  // ── Other L2/L3 ──
  metis: { chain: "Metis", chain_id: 1088 },
  mnt: { chain: "Mantle", chain_id: 5000 },
  mantle: { chain: "Mantle", chain_id: 5000 },
  opbnb: { chain: "opBNB", chain_id: 204 },
  xlayer: { chain: "X Layer", chain_id: 196 },
  merlin: { chain: "Merlin", chain_id: 4200 },
  btr: { chain: "Bitlayer", chain_id: 200901 },
  core: { chain: "Core", chain_id: 1116 },
  // ── Alt-L1 EVM ──
  ftm: { chain: "Fantom", chain_id: 250 },
  fantom: { chain: "Fantom", chain_id: 250 },
  sonic: { chain: "Sonic", chain_id: 146 },
  cro: { chain: "Cronos", chain_id: 25 },
  cronos: { chain: "Cronos", chain_id: 25 },
  gnosis: { chain: "Gnosis", chain_id: 100 },
  xdai: { chain: "Gnosis", chain_id: 100 },
  celo: { chain: "Celo", chain_id: 42220 },
  aurora: { chain: "Aurora", chain_id: 1313161554 },
  klay: { chain: "Kaia", chain_id: 8217 },
  klaytn: { chain: "Kaia", chain_id: 8217 },
  movr: { chain: "Moonriver", chain_id: 1285 },
  mobm: { chain: "Moonbeam", chain_id: 1284 },
  moonbeam: { chain: "Moonbeam", chain_id: 1284 },
  tlos: { chain: "Telos EVM", chain_id: 40 },
  fuse: { chain: "Fuse", chain_id: 122 },
  iotx: { chain: "IoTeX", chain_id: 4689 },
  flr: { chain: "Flare", chain_id: 14 },
  // ── New / Emerging ──
  bera: { chain: "Berachain", chain_id: 80094 },
  abs: { chain: "Abstract", chain_id: 2741 },
  ape: { chain: "ApeChain", chain_id: 33139 },
  sei: { chain: "Sei EVM", chain_id: 1329 },
  story: { chain: "Story", chain_id: 1514 },
  plume: { chain: "Plume", chain_id: 98866 },
  gravity: { chain: "Gravity", chain_id: 1625 },
  hyper: { chain: "HyperEVM", chain_id: 999 },
  monad: { chain: "Monad Testnet", chain_id: 10143 },
  megaeth: { chain: "MegaETH Testnet", chain_id: 6342 },
  morph: { chain: "Morph", chain_id: 2818 },
  katana: { chain: "Katana", chain_id: 747474 },
  lens: { chain: "Lens Network", chain_id: 232 },
  world: { chain: "World Chain", chain_id: 480 },
  plasma: { chain: "Plasma", chain_id: 1559 },
  orderly: { chain: "Orderly Network", chain_id: 291 },
  ron: { chain: "Ronin", chain_id: 2020 },
  dfk: { chain: "DFK Chain", chain_id: 53935 },
  bb: { chain: "BounceBit", chain_id: 6001 },
  ethlink: { chain: "ETHLink", chain_id: 16777648 },
  frax: { chain: "Fraxtal", chain_id: 252 },
  g0: { chain: "GravityAlpha", chain_id: 1625 },
  tempo: { chain: "Tempo", chain_id: 16481 },
  itze: { chain: "Itteza", chain_id: 2025 },
  citrea: { chain: "Citrea Testnet", chain_id: 5115 },
};

function makeRequestId() {
  return crypto.randomUUID();
}

function errorBody(code, message, requestId) {
  return {
    status: "error",
    code,
    message,
    request_id: requestId,
  };
}

function okBody(payload, requestId) {
  return {
    status: "ok",
    request_id: requestId,
    ...payload,
  };
}

function metaForChainCode(codeRaw) {
  const key = String(codeRaw || "")
    .trim()
    .toLowerCase();
  if (CHAIN_CODE_TO_META[key]) {
    return { ...CHAIN_CODE_TO_META[key] };
  }
  const slug = key.replace(/[^a-z0-9]+/g, "_").replace(/^_|_$/g, "") || "unknown";
  const title = slug
    .split("_")
    .filter(Boolean)
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");
  return { chain: title || "Unknown", chain_id: slug };
}

async function readMemoryAddresses() {
  try {
    const raw = await fs.readFile(MEMORY_FILE, "utf8");
    const j = JSON.parse(raw);
    if (Array.isArray(j?.addresses)) {
      return [...new Set(j.addresses.map((a) => String(a || "").trim()).filter(Boolean))];
    }
    if (Array.isArray(j?.items)) {
      const xs = j.items.map((it) => String(it?.address || it || "").trim()).filter(Boolean);
      return [...new Set(xs)];
    }
  } catch {
    // missing or invalid file
  }
  return [];
}

async function writeMemoryAddresses(addresses) {
  const unique = [...new Set(addresses.map((a) => String(a || "").trim()).filter(Boolean))];
  const dir = path.dirname(MEMORY_FILE);
  await fs.mkdir(dir, { recursive: true });
  const tmp = `${MEMORY_FILE}.${process.pid}.tmp`;
  await fs.writeFile(tmp, JSON.stringify({ version: 1, addresses: unique }, null, 2), "utf8");
  await fs.rename(tmp, MEMORY_FILE);
  return unique;
}

function isLikelyBtcAddress(input) {
  const value = String(input || "").trim();
  if (!value) return false;
  return /^(bc1[ac-hj-np-z02-9]{11,71}|[13][a-km-zA-HJ-NP-Z1-9]{25,34})$/.test(value);
}

/**
 * Detect non-EVM chain from address format.
 * Returns chainHint string or null if not recognized.
 */
function detectNonEvmChain(input) {
  // Tron: T + 33 base58 chars
  if (/^T[1-9A-HJ-NP-Za-km-z]{33}$/.test(input)) return "tron";
  // TON: EQ/UQ/kQ/0Q prefix
  if (/^(EQ|UQ|kQ|0Q)[A-Za-z0-9_-]{46}$/.test(input)) return "ton";
  // XRP: r-prefix, 25-34 base58 chars
  if (/^r[1-9A-HJ-NP-Za-km-z]{24,34}$/.test(input)) return "xrp";
  // Litecoin: L/M/m/ltc1 prefix
  if (/^([LMm3][a-km-zA-HJ-NP-Z1-9]{26,33}|ltc1[a-z0-9]{39,59})$/.test(input)) return "litecoin";
  // NEAR: account.near or 64-char hex
  if (/^[a-zA-Z0-9._-]{2,64}\.near$/.test(input) || /^[0-9a-f]{64}$/.test(input)) return "near";
  // Sui: 0x + exactly 64 hex chars
  if (/^0x[0-9a-fA-F]{64}$/.test(input)) return "sui";
  // Aptos: 0x + 1-64 hex chars, but NOT 40 hex chars (which is EVM)
  if (/^0x(?![0-9a-fA-F]{40}$)[0-9a-fA-F]{1,63}$/.test(input)) return "aptos";
  // Polkadot SS58: 46-48 base58 chars
  if (/^[1-9A-HJ-NP-Za-km-z]{46,48}$/.test(input)) return "polkadot";
  // Cardano: addr1 prefix
  if (/^addr1[a-z0-9]{50,}$/.test(input)) return "cardano";
  // Kaspa: kaspa: prefix
  if (/^kaspa:[a-z0-9]{61,63}$/.test(input)) return "kaspa";
  // Solana: broad base58 fallback, kept last so more specific chains win first
  if (/^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(input)) return "solana";
  return null;
}

async function normalizeInput(inputRaw) {
  const input = String(inputRaw || "").trim();
  if (!input) {
    throw new Error("MISSING_INPUT");
  }

  // EVM 0x address (40 hex chars)
  if (/^0x[a-fA-F0-9]{40}$/.test(input)) {
    return {
      normalizedAddress: ethers.getAddress(input),
      chainHint: "evm",
      sourceInput: input,
    };
  }

  // Bitcoin
  if (isLikelyBtcAddress(input)) {
    return {
      normalizedAddress: input.toLowerCase().startsWith("bc1") ? input.toLowerCase() : input,
      chainHint: "btc",
      sourceInput: input,
    };
  }

  // ENS / .eth
  if (input.toLowerCase().endsWith(".eth")) {
    const resolved = await ethProvider.resolveName(input);
    if (!resolved) throw new Error("UNRESOLVABLE_NAME");
    return {
      normalizedAddress: ethers.getAddress(resolved),
      chainHint: "evm",
      sourceInput: input,
    };
  }

  // .bnb
  if (input.toLowerCase().endsWith(".bnb")) {
    const resolved = await bnbProvider.resolveName(input);
    if (!resolved) throw new Error("UNRESOLVABLE_NAME");
    return {
      normalizedAddress: ethers.getAddress(resolved),
      chainHint: "evm",
      sourceInput: input,
    };
  }

  // Non-EVM chains (Solana, Tron, TON, XRP, LTC, NEAR, Sui, Aptos, Polkadot, Cardano, Kaspa)
  const nonEvm = detectNonEvmChain(input);
  if (nonEvm) {
    return {
      normalizedAddress: input,
      chainHint: nonEvm,
      sourceInput: input,
    };
  }

  throw new Error("INVALID_INPUT");
}

async function checkRateLimit({ ip, normalizedAddress }) {
  if (!redisReady) return;
  const now = Date.now();
  const minuteWindow = Math.floor(now / 60000);
  const ipKey = `rl:ip:${ip}:${minuteWindow}`;
  const addrKey = `rl:addr:${normalizedAddress}:${minuteWindow}`;

  const ipCount = await redis.incr(ipKey);
  if (ipCount === 1) await redis.expire(ipKey, 70);

  const addrCount = await redis.incr(addrKey);
  if (addrCount === 1) await redis.expire(addrKey, 70);

  if (ipCount > 10) {
    const err = new Error("RATE_LIMIT_IP");
    err.httpStatus = 429;
    throw err;
  }
  if (addrCount > 5) {
    const err = new Error("RATE_LIMIT_ADDRESS");
    err.httpStatus = 429;
    throw err;
  }
}

async function readCache(normalizedAddress) {
  if (!redisReady) return null;
  const key = `assets:v1:${normalizedAddress}`;
  const val = await redis.get(key);
  if (!val) return null;
  return JSON.parse(val);
}

async function writeCache(normalizedAddress, payload) {
  if (!redisReady) return;
  const key = `assets:v1:${normalizedAddress}`;
  await redis.set(key, JSON.stringify(payload), { EX: 300 });
}

async function filterDustTokensAsync(response) {
  const copy = JSON.parse(JSON.stringify(response));
  const needPriceSymbols = new Set();
  for (const chain of copy.chains || []) {
    for (const token of chain.tokens || []) {
      const symbol = String(token?.symbol || "").toUpperCase();
      if (!SYMBOL_PRICE_ID[symbol]) continue;
      try {
        if (new Decimal(token?.value_usd || 0).gt(0)) continue;
      } catch {
        // ignore bad number
      }
      needPriceSymbols.add(symbol);
    }
  }

  const roughPrices = {};
  if (needPriceSymbols.size > 0) {
    const ids = [...new Set([...needPriceSymbols].map((s) => SYMBOL_PRICE_ID[s]))];
    const priceRaw = await fetchCoinPriceUsdSafe(ids);
    for (const symbol of needPriceSymbols) {
      const id = SYMBOL_PRICE_ID[symbol];
      roughPrices[symbol] = new Decimal(priceRaw?.[id]?.usd || 0);
    }
  }

  let total = new Decimal(0);
  for (const chain of copy.chains || []) {
    const normalizedTokens = (chain.tokens || []).map((t) => {
      const symbol = String(t?.symbol || "").toUpperCase();
      const rough = roughPrices[symbol];
      try {
        if (rough && rough.gt(0) && new Decimal(t.value_usd || 0).lte(0)) {
          const amount = new Decimal(t.amount || 0);
          return { ...t, value_usd: amount.mul(rough).toFixed(2), estimated_usd: true };
        }
      } catch {
        // ignore parse errors
      }
      return t;
    });
    for (const token of normalizedTokens) {
      try {
        total = total.plus(new Decimal(token.value_usd || 0));
      } catch {
        // ignore parse errors
      }
    }
    chain.tokens = normalizedTokens
      .filter((t) => {
        try {
          return new Decimal(t.value_usd || 0).gte(1);
        } catch {
          return false;
        }
      })
      .sort((a, b) => new Decimal(b.value_usd || 0).cmp(new Decimal(a.value_usd || 0)));
    const networkSlug = chainToNetworkSlug(chain.chain, chain.chain_id);
    for (const token of chain.tokens) {
      token.token_kind = inferTokenKind(chain.chain, token.symbol, token);
      token.network = networkSlug;
      try {
        token.value_usd = new Decimal(token.value_usd || 0).toFixed(2);
      } catch {
        token.value_usd = "0.00";
      }
      delete token.is_native;
    }
  }
  copy.total_usd = total.toFixed(2);
  return copy;
}

function withTimeout(promiseFactory, ms = 10000) {
  const controller = new AbortController();
  const timeoutPromise = new Promise((_, reject) => {
    const timer = setTimeout(() => {
      controller.abort();
      reject(new Error("UPSTREAM_TIMEOUT"));
    }, ms);
    controller.signal.addEventListener(
      "abort",
      () => {
        clearTimeout(timer);
      },
      { once: true }
    );
  });

  const workPromise = promiseFactory(controller.signal).finally(() => controller.abort());
  return Promise.race([workPromise, timeoutPromise]);
}

async function readResponseTextWithCap(response, maxChars) {
  if (!response.body) {
    const t = await response.text();
    if (t.length > maxChars) throw new Error("MCP_RESPONSE_TOO_LARGE");
    return t;
  }
  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let total = "";
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      total += decoder.decode(value, { stream: true });
      if (total.length > maxChars) {
        try {
          await reader.cancel();
        } catch {
          // ignore
        }
        throw new Error("MCP_RESPONSE_TOO_LARGE");
      }
    }
  } finally {
    try {
      reader.releaseLock();
    } catch {
      // ignore
    }
  }
  return total;
}

function collectSseDataJsonObjects(sseText) {
  const messages = [];
  for (const line of sseText.split("\n")) {
    if (!line.startsWith("data: ")) continue;
    const payload = line.slice(6).trim();
    if (!payload) continue;
    try {
      messages.push(JSON.parse(payload));
    } catch {
      // ignore non-JSON lines
    }
  }
  return messages;
}

function pickJsonRpcMessage(messages, id) {
  return messages.find((m) => m && typeof m === "object" && m.id === id) || null;
}

function parseMcpToolResultEnvelope(jsonRpcMsg) {
  if (!jsonRpcMsg) {
    throw new Error("MCP_EMPTY_RESPONSE");
  }
  if (jsonRpcMsg.error) {
    const err = new Error("MCP_JSONRPC_ERROR");
    err.mcpError = jsonRpcMsg.error;
    throw err;
  }
  const content = jsonRpcMsg.result?.content;
  if (!Array.isArray(content)) {
    throw new Error("UPSTREAM_FORMAT_ERROR");
  }
  const textPart = content.find((c) => c?.type === "text")?.text;
  if (typeof textPart !== "string" || !textPart.trim()) {
    throw new Error("UPSTREAM_FORMAT_ERROR");
  }
  try {
    return JSON.parse(textPart);
  } catch {
    throw new Error("UPSTREAM_FORMAT_ERROR");
  }
}

function buildMcpHeaders() {
  const h = {
    "Content-Type": "application/json",
    Accept: "application/json, text/event-stream",
  };
  if (MCP_API_KEY) {
    h.Authorization = `Bearer ${MCP_API_KEY}`;
  }
  return h;
}

/**
 * Streamable HTTP MCP: initialize session, then tools/call. Response bodies are SSE.
 */
async function mcpCallTool(toolName, toolArguments, signal) {
  const initRes = await fetch(MCP_SKILLS_URL, {
    method: "POST",
    headers: buildMcpHeaders(),
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: 1,
      method: "initialize",
      params: {
        protocolVersion: "2024-11-05",
        capabilities: {},
        clientInfo: { name: "wallet-balance-gateway", version: "1.4.0" },
      },
    }),
    signal,
  });

  const sessionId = initRes.headers.get("mcp-session-id");
  if (!sessionId) {
    throw new Error("MCP_SESSION_MISSING");
  }

  const initSse = await readResponseTextWithCap(initRes, 65536);
  const initMsgs = collectSseDataJsonObjects(initSse);
  const initAck = pickJsonRpcMessage(initMsgs, 1);
  if (initAck?.error) {
    const err = new Error("MCP_JSONRPC_ERROR");
    err.mcpError = initAck.error;
    throw err;
  }

  const callRes = await fetch(MCP_SKILLS_URL, {
    method: "POST",
    headers: { ...buildMcpHeaders(), "mcp-session-id": sessionId },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: 2,
      method: "tools/call",
      params: { name: toolName, arguments: toolArguments },
    }),
    signal,
  });

  const callSse = await readResponseTextWithCap(callRes, MAX_MCP_RESPONSE_CHARS);
  const callMsgs = collectSseDataJsonObjects(callSse);
  const callAck = pickJsonRpcMessage(callMsgs, 2) || callMsgs.find((m) => m?.result?.content);
  return parseMcpToolResultEnvelope(callAck);
}

function toDecimalText(v) {
  try {
    return new Decimal(v || 0).toFixed();
  } catch {
    return "0";
  }
}

function chainToNetworkSlug(chainName, chainId) {
  const n = String(chainName || "").toLowerCase();
  const id = chainId;
  if (id === 1 || (n.includes("ethereum") && !n.includes("classic"))) return "ethereum";
  if (id === 56 || n === "bnb chain" || n === "bsc" || n.includes("binance") || n.includes("bnb smart")) return "bsc";
  if (id === 8453 || n === "base") return "base";
  if (id === 42161 || n.includes("arbitrum")) return "arbitrum";
  if (id === 10 || n === "optimism") return "optimism";
  if (id === 137 || n.includes("polygon")) return "polygon";
  if (id === 43114 || n.includes("avalanche")) return "avalanche";
  if (id === 324 || n.includes("zksync") || n.includes("zk sync era")) return "zksync_era";
  if (id === 59144 || n === "linea") return "linea";
  if (id === 534352 || n === "scroll") return "scroll";
  if (id === 81457 || n === "blast") return "blast";
  if (id === 5000 || n === "mantle") return "mantle";
  if (id === 250 || n === "fantom") return "fantom";
  if (id === 100 || n === "gnosis") return "gnosis";
  if (id === 42220 || n === "celo") return "celo";
  if (id === 8217 || n === "kaia") return "kaia";
  if (id === "btc-mainnet" || n.includes("bitcoin")) return "bitcoin";
  // generic fallback: derive slug from chain name
  const slug = n.replace(/[^a-z0-9]+/g, "_").replace(/^_|_$/g, "");
  return slug || String(id ?? "unknown").toLowerCase();
}

function inferTokenKind(chainName, symbol, token) {
  if (token?.is_native || token?.token_kind === "native") return "native";
  const c = String(chainName || "").toLowerCase();
  const s = String(symbol || "").toUpperCase();
  if (s === "BTC" && (c.includes("bitcoin") || c.includes("btc"))) return "native";
  if (s === "ETH" && (c.includes("ethereum") || c === "eth")) return "native";
  if (s === "BNB" && (c.includes("bsc") || c.includes("bnb"))) return "native";
  return "erc20";
}

function normalizeToken(symbol, amount, valueUsd) {
  return {
    symbol: symbol || "UNKNOWN",
    amount: toDecimalText(amount),
    value_usd: toDecimalText(valueUsd),
  };
}

function normalizeNativeToken(symbol, amount, valueUsd) {
  return {
    symbol: symbol || "UNKNOWN",
    amount: toDecimalText(amount),
    value_usd: toDecimalText(valueUsd),
    is_native: true,
  };
}

function decimalFromUnknown(value, fallback = "0") {
  try {
    return new Decimal(value ?? fallback);
  } catch {
    return new Decimal(fallback);
  }
}

function normalizeMcpChainMeta(rawChain, rawChainId, chainSummaryMap) {
  const raw = String(rawChain || "").trim();
  const summary = raw ? chainSummaryMap.get(raw) : null;
  const meta = metaForChainCode(raw || summary?.chain_id || rawChainId);
  const knownCode = raw && CHAIN_CODE_TO_META[raw.toLowerCase()];
  return {
    chain: summary?.displayChain || meta.chain,
    chain_id: knownCode ? meta.chain_id : (summary?.chain_id ?? rawChainId ?? meta.chain_id),
  };
}

function mcpWalletBalanceToChains(inner) {
  const rows = Array.isArray(inner?.tokens) ? inner.tokens : [];
  const limited = rows.length > MCP_MAX_TOKEN_ROWS ? rows.slice(0, MCP_MAX_TOKEN_ROWS) : rows;
  const byKey = new Map();
  const chainSummaryMap = new Map();

  if (Array.isArray(inner?.by_chain)) {
    for (const summary of inner.by_chain) {
      const rawChain = String(summary?.chain || "").trim();
      if (!rawChain) continue;
      const meta = metaForChainCode(rawChain);
      chainSummaryMap.set(rawChain, {
        chain_id: summary?.chain_id ?? meta.chain_id,
        displayChain: meta.chain,
      });
    }
  }

  for (const t of limited) {
    const rawChain = String(t?.chain ?? inner?.chain ?? "").trim();
    const { chain, chain_id } = normalizeMcpChainMeta(rawChain, t?.chain_id, chainSummaryMap);
    const chainKey = `${chain}::${chain_id}`;
    const symbolRaw = t?.optimized_symbol || t?.display_symbol || t?.symbol || "UNKNOWN";
    const symbol = String(symbolRaw).trim() || "UNKNOWN";
    const amount = decimalFromUnknown(t?.balance ?? t?.amount ?? 0);
    const explicitValue = t?.value_usd;
    const derivedValue = amount.mul(decimalFromUnknown(t?.price_usd ?? t?.price ?? 0));
    const valueUsd = decimalFromUnknown(explicitValue ?? derivedValue.toFixed(2));
    const token = t?.is_native
      ? normalizeNativeToken(symbol, amount.toFixed(), valueUsd.toFixed(2))
      : normalizeToken(symbol, amount.toFixed(), valueUsd.toFixed(2));

    if (!byKey.has(chainKey)) {
      byKey.set(chainKey, { chain, chain_id, tokens: [] });
    }
    byKey.get(chainKey).tokens.push(token);
  }

  let chains = [...byKey.values()].filter((c) => c.tokens.length);
  if (!chains.length && inner?.chain && inner?.chain_id != null) {
    const { chain, chain_id } = normalizeMcpChainMeta(inner.chain, inner.chain_id, chainSummaryMap);
    chains = [{ chain, chain_id, tokens: [] }];
  }
  if (!chains.length) {
    throw new Error("UPSTREAM_FORMAT_ERROR");
  }
  return chains;
}

async function fetchFromMcpAggregation({ normalizedAddress, signal }) {
  const inner = await mcpCallTool(MCP_TOOL_NAME, { address: normalizedAddress }, signal);
  const chains = mcpWalletBalanceToChains(inner);
  return {
    input: normalizedAddress,
    address: normalizedAddress,
    chains,
    total_usd: toDecimalText(inner?.total_value_usd || 0),
    chain_scope: inner?.chain_scope || "unknown",
    updated_at: new Date().toISOString(),
    provider: "mcp-wallet-balance-query",
  };
}

async function fetchCoinPriceUsd(ids, signal) {
  const url = `https://api.coingecko.com/api/v3/simple/price?ids=${encodeURIComponent(ids.join(","))}&vs_currencies=usd`;
  const resp = await fetch(url, {
    method: "GET",
    headers: { Accept: "application/json" },
    signal,
  });
  if (!resp.ok) return {};
  return resp.json();
}

async function fetchCoinPriceUsdSafe(ids) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 2200);
  let raw = {};
  try {
    raw = await fetchCoinPriceUsd(ids, controller.signal);
  } catch {
    raw = {};
  } finally {
    clearTimeout(timer);
  }
  if (!raw || typeof raw !== "object") raw = {};
  for (const id of ids) {
    const u = raw[id]?.usd;
    const n = Number(u);
    if (u == null || !Number.isFinite(n) || n <= 0) {
      const fb = COINGECKO_ID_FALLBACK_USD[id];
      if (fb != null) raw[id] = { ...(raw[id] || {}), usd: fb };
    }
  }
  return raw;
}

async function fetchBtcBalance(address, signal) {
  const url = `https://blockstream.info/api/address/${encodeURIComponent(address)}`;
  const resp = await fetch(url, {
    method: "GET",
    headers: { Accept: "application/json" },
    signal,
  });
  if (!resp.ok) throw new Error("BTC_UPSTREAM_ERROR");
  const data = await resp.json();
  const funded = new Decimal(data?.chain_stats?.funded_txo_sum || 0);
  const spent = new Decimal(data?.chain_stats?.spent_txo_sum || 0);
  return funded.minus(spent).div(1e8);
}

async function fetchBtcBalanceSafe(address) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 3500);
  try {
    return await fetchBtcBalance(address, controller.signal);
  } catch {
    return new Decimal(0);
  } finally {
    clearTimeout(timer);
  }
}

async function safeNativeBalance(provider, address, timeoutMs = 3500) {
  try {
    const wei = await Promise.race([
      provider.getBalance(address),
      new Promise((resolve) => setTimeout(() => resolve(0n), timeoutMs)),
    ]);
    return new Decimal(ethers.formatEther(wei.toString()));
  } catch {
    return new Decimal(0);
  }
}

async function mergeEvmNativeFromRpc(chainHint, normalizedAddress, response) {
  if (chainHint !== "evm" || !response?.chains) return response;
  const prices = await fetchCoinPriceUsdSafe(["ethereum", "binancecoin"]);
  const ethUsd = new Decimal(prices?.ethereum?.usd || 0);
  const bnbUsd = new Decimal(prices?.binancecoin?.usd || 0);
  const [ethAmt, bnbAmt] = await Promise.all([
    safeNativeBalance(ethProvider, normalizedAddress),
    safeNativeBalance(bnbProvider, normalizedAddress),
  ]);

  const ethUsdVal = ethAmt.mul(ethUsd);
  const bnbUsdVal = bnbAmt.mul(bnbUsd);

  const isEthChain = (c) => c?.chain_id === 1 || String(c?.chain || "").toLowerCase() === "ethereum";
  const isBscChain = (c) => {
    const chainName = String(c?.chain || "").toLowerCase();
    return c?.chain_id === 56 || chainName === "bsc" || chainName === "bnb chain" || chainName.includes("binance");
  };

  const upsertNative = (chain, symbol, amount, usd) => {
    if (!chain) return;
    const tokens = chain.tokens || [];
    const rest = tokens.filter((t) => String(t?.symbol || "").toUpperCase() !== symbol);
    const native = normalizeNativeToken(symbol, amount.toFixed(8), usd.toFixed(2));
    chain.tokens = [native, ...rest];
  };

  let ethChain = response.chains.find(isEthChain);
  if (!ethChain) {
    ethChain = { chain: "Ethereum", chain_id: 1, tokens: [] };
    response.chains.push(ethChain);
  }
  upsertNative(ethChain, "ETH", ethAmt, ethUsdVal);

  let bscChain = response.chains.find(isBscChain);
  if (!bscChain) {
    bscChain = { chain: "BNB Chain", chain_id: 56, tokens: [] };
    response.chains.push(bscChain);
  }
  upsertNative(bscChain, "BNB", bnbAmt, bnbUsdVal);

  return response;
}

async function fetchErc20BalanceSafe(provider, tokenAddress, ownerAddress) {
  try {
    const contract = new ethers.Contract(tokenAddress, ERC20_ABI, provider);
    const [raw, decimals] = await Promise.all([
      Promise.race([contract.balanceOf(ownerAddress), new Promise((resolve) => setTimeout(() => resolve(0n), 2200))]),
      Promise.race([contract.decimals(), new Promise((resolve) => setTimeout(() => resolve(18), 2200))]),
    ]);
    return new Decimal(ethers.formatUnits(raw.toString(), Number(decimals)));
  } catch {
    return new Decimal(0);
  }
}

async function fetchFromFallbackAggregation({ normalizedAddress, chainHint, signal }) {
  const chains = [];
  const prices = await fetchCoinPriceUsdSafe(["bitcoin", "ethereum", "binancecoin", "tether"]);
  const ethUsd = new Decimal(prices?.ethereum?.usd || 0);
  const bnbUsd = new Decimal(prices?.binancecoin?.usd || 0);
  const btcUsd = new Decimal(prices?.bitcoin?.usd || 0);
  const usdtUsd = new Decimal(prices?.tether?.usd || 1);

  if (chainHint === "btc") {
    const btcBal = await fetchBtcBalanceSafe(normalizedAddress);
    chains.push({
      chain: "Bitcoin",
      chain_id: "btc-mainnet",
      tokens: [normalizeNativeToken("BTC", btcBal.toFixed(8), btcBal.mul(btcUsd).toFixed(2))],
    });
  } else {
    const safeNative = async (promise, timeoutMs = 2200) => {
      try {
        return await Promise.race([promise, new Promise((resolve) => setTimeout(() => resolve(0n), timeoutMs))]);
      } catch {
        return 0n;
      }
    };
    const [ethWei, bnbWei] = await Promise.all([
      safeNative(ethProvider.getBalance(normalizedAddress)),
      safeNative(bnbProvider.getBalance(normalizedAddress)),
    ]);
    const ethAmount = new Decimal(ethers.formatEther(ethWei.toString()));
    const bnbAmount = new Decimal(ethers.formatEther(bnbWei.toString()));
    const ethUsdt = await fetchErc20BalanceSafe(ethProvider, ERC20_TRACKED.Ethereum[0].address, normalizedAddress);
    chains.push({
      chain: "Ethereum",
      chain_id: 1,
      tokens: [
        normalizeNativeToken("ETH", ethAmount.toFixed(8), ethAmount.mul(ethUsd).toFixed(2)),
        normalizeToken("USDT", ethUsdt.toFixed(6), ethUsdt.mul(usdtUsd).toFixed(2)),
      ],
    });
    const bscUsdt = await fetchErc20BalanceSafe(bnbProvider, ERC20_TRACKED.BSC[0].address, normalizedAddress);
    chains.push({
      chain: "BNB Chain",
      chain_id: 56,
      tokens: [
        normalizeNativeToken("BNB", bnbAmount.toFixed(8), bnbAmount.mul(bnbUsd).toFixed(2)),
        normalizeToken("USDT", bscUsdt.toFixed(6), bscUsdt.mul(usdtUsd).toFixed(2)),
      ],
    });
  }

  return {
    input: normalizedAddress,
    address: normalizedAddress,
    chains,
    updated_at: new Date().toISOString(),
    provider: "fallback-mvp",
  };
}

/**
 * EVM + supported non-BTC chains: try wallet-balance-query first.
 * BTC: public providers only (Blockstream).
 * Non-EVM chains require MCP; only EVM can fall back to public providers.
 */
async function buildAssetsPayload({ sourceInput, normalizedAddress, chainHint, bypassCache }) {
  let upstreamRaw;
  let dataSource;

  if (chainHint === "btc") {
    upstreamRaw = await withTimeout(
      (signal) => fetchFromFallbackAggregation({ normalizedAddress, chainHint, signal }),
      12000
    );
    dataSource = "public_only";
  } else if (!ENABLE_MCP) {
    if (chainHint !== "evm") throw new Error("NON_EVM_REQUIRES_MCP");
    upstreamRaw = await withTimeout(
      (signal) => fetchFromFallbackAggregation({ normalizedAddress, chainHint, signal }),
      12000
    );
    dataSource = "public_only";
  } else {
    try {
      upstreamRaw = await withTimeout(
        (signal) => fetchFromMcpAggregation({ normalizedAddress, signal }),
        90000
      );
      dataSource = "mcp_wallet_balance_query";
    } catch (e) {
      if (chainHint !== "evm" || !ENABLE_FALLBACK_PROVIDER) throw e;
      upstreamRaw = await withTimeout(
        (signal) => fetchFromFallbackAggregation({ normalizedAddress, chainHint, signal }),
        12000
      );
      dataSource = "public_fallback";
    }
  }

  await mergeEvmNativeFromRpc(chainHint, normalizedAddress, upstreamRaw);
  const cleaned = await filterDustTokensAsync(upstreamRaw);
  const payload = {
    input: sourceInput,
    address: normalizedAddress,
    total_usd: cleaned.total_usd,
    chains: cleaned.chains,
    updated_at: cleaned.updated_at,
    data_source: dataSource,
  };
  if (!bypassCache) {
    await writeCache(normalizedAddress, payload);
  }
  return payload;
}

app.get("/healthz", async (_req, res) => {
  res.json({
    status: "ok",
    redis: redisReady ? "up" : "down",
    service: "wallet-balance-gateway",
    version: "1.4.0",
    mcp_enabled: ENABLE_MCP,
    now: new Date().toISOString(),
  });
});

app.get("/agent-skills/v1/memory", async (_req, res) => {
  const requestId = makeRequestId();
  try {
    const addresses = await readMemoryAddresses();
    return res.json(okBody({ addresses, count: addresses.length }, requestId));
  } catch {
    return res.status(500).json(errorBody("INTERNAL_ERROR", "Failed to read memory list.", requestId));
  }
});

app.post("/agent-skills/v1/memory", async (req, res) => {
  const requestId = makeRequestId();
  try {
    const body = req.body && typeof req.body === "object" ? req.body : {};
    let list = await readMemoryAddresses();

    if (body.remove != null) {
      const rm = String(body.remove).trim();
      const normRm = await normalizeInput(rm).catch(() => null);
      const key = normRm ? normRm.normalizedAddress : rm;
      list = list.filter((a) => a.toLowerCase() !== key.toLowerCase());
      await writeMemoryAddresses(list);
      return res.json(okBody({ addresses: list, count: list.length, action: "remove" }, requestId));
    }

    const rawAdds = body.add != null ? body.add : body.address != null ? body.address : null;
    if (rawAdds == null) {
      return res.status(400).json(errorBody("INVALID_BODY", "Provide add or remove in JSON body.", requestId));
    }
    const toAdd = Array.isArray(rawAdds) ? rawAdds : [rawAdds];
    for (const item of toAdd) {
      const n = await normalizeInput(String(item || "").trim());
      if (!list.some((a) => a.toLowerCase() === n.normalizedAddress.toLowerCase())) {
        list.push(n.normalizedAddress);
      }
    }
    await writeMemoryAddresses(list);
    return res.json(okBody({ addresses: list, count: list.length, action: "add" }, requestId));
  } catch (err) {
    const code = err?.message || "INTERNAL_ERROR";
    if (code === "INVALID_INPUT" || code === "MISSING_INPUT" || code === "UNRESOLVABLE_NAME") {
      return res.status(400).json(errorBody(code, "Invalid address or name; cannot update memory.", requestId));
    }
    return res.status(500).json(errorBody("INTERNAL_ERROR", "Failed to update memory.", requestId));
  }
});

app.get("/agent-skills/v1/assets", async (req, res) => {
  const requestId = makeRequestId();
  try {
    const ip = req.ip || req.headers["x-forwarded-for"] || "unknown";
    const bypassCache =
      String(req.query.refresh || req.query.nocache || "").toLowerCase() === "1" ||
      String(req.query.refresh || "").toLowerCase() === "true";

    const fromMemory =
      String(req.query.from_memory || "").toLowerCase() === "1" ||
      String(req.query.from_memory || "").toLowerCase() === "true";

    if (fromMemory) {
      const stored = await readMemoryAddresses();
      if (!stored.length) {
        return res.status(400).json(
          errorBody(
            "MEMORY_EMPTY",
            "No remembered addresses yet. Query an address first and confirm to remember it.",
            requestId
          )
        );
      }
      const results = [];
      let combined = new Decimal(0);
      for (const addr of stored) {
        try {
          const normalized = await normalizeInput(addr);
          await checkRateLimit({ ip: String(ip), normalizedAddress: normalized.normalizedAddress });
          if (!bypassCache) {
            const cached = await readCache(normalized.normalizedAddress);
            if (cached) {
              results.push({ ...cached, cached: true });
              try {
                combined = combined.plus(new Decimal(cached.total_usd || 0));
              } catch {
                // ignore
              }
              continue;
            }
          }
          const payload = await buildAssetsPayload({
            sourceInput: normalized.sourceInput,
            normalizedAddress: normalized.normalizedAddress,
            chainHint: normalized.chainHint,
            bypassCache,
          });
          results.push(payload);
          try {
            combined = combined.plus(new Decimal(payload.total_usd || 0));
          } catch {
            // ignore
          }
        } catch (e) {
          results.push({
            address: addr,
            status: "error",
            code: e?.message || "QUERY_FAILED",
          });
        }
      }
      return res.json(
        okBody(
          {
            query_mode: "memory",
            results,
            combined_total_usd: combined.toFixed(2),
          },
          requestId
        )
      );
    }

    const input = req.query.input;
    const normalized = await normalizeInput(input);
    await checkRateLimit({ ip: String(ip), normalizedAddress: normalized.normalizedAddress });

    if (!bypassCache) {
      const cached = await readCache(normalized.normalizedAddress);
      if (cached) {
        return res.json(okBody({ ...cached, cached: true }, requestId));
      }
    }

    const payload = await buildAssetsPayload({
      sourceInput: normalized.sourceInput,
      normalizedAddress: normalized.normalizedAddress,
      chainHint: normalized.chainHint,
      bypassCache,
    });
    return res.json(okBody(payload, requestId));
  } catch (err) {
    const code = err?.message || "INTERNAL_ERROR";
    const map = {
      MISSING_INPUT: { status: 400, message: "Missing input; provide an address or domain name." },
      INVALID_INPUT: { status: 400, message: "Input is not a valid address or resolvable name." },
      UNRESOLVABLE_NAME: { status: 400, message: "Name could not be resolved; try a raw address." },
      RATE_LIMIT_IP: { status: 429, message: "Too many requests; try again later." },
      RATE_LIMIT_ADDRESS: { status: 429, message: "Too many queries for this address; try again later." },
      REDIS_UNAVAILABLE: { status: 503, message: "Rate limit store unavailable; try again later." },
      MEMORY_EMPTY: { status: 400, message: "No remembered addresses." },
      INVALID_BODY: { status: 400, message: "Invalid JSON body." },
      UPSTREAM_HTTP_ERROR: { status: 502, message: "Upstream data error; try again later." },
      UPSTREAM_RATE_LIMIT: { status: 429, message: "Upstream rate limited; try again later." },
      UPSTREAM_FORMAT_ERROR: { status: 502, message: "Upstream response format not supported." },
      UPSTREAM_TIMEOUT: { status: 504, message: "Upstream timeout; try again later." },
      UPSTREAM_ABORTED: { status: 504, message: "Upstream request aborted; try again later." },
      MCP_SESSION_MISSING: { status: 502, message: "MCP session could not be established." },
      MCP_EMPTY_RESPONSE: { status: 502, message: "MCP returned an empty response." },
      MCP_JSONRPC_ERROR: { status: 502, message: "MCP tool returned an error." },
      MCP_RESPONSE_TOO_LARGE: { status: 502, message: "MCP response exceeded size limit." },
      MCP_TOOL_ERROR: { status: 502, message: "MCP tool execution failed." },
      NON_EVM_REQUIRES_MCP: { status: 503, message: "Non-EVM chain queries require MCP to be enabled." },
      UNSUPPORTED_CHAIN: { status: 400, message: "Chain not supported." },
      INTERNAL_ERROR: { status: 500, message: "Internal error; try again later." },
    };
    const hit = map[code] || map.INTERNAL_ERROR;
    return res.status(hit.status).json(errorBody(code, hit.message, requestId));
  }
});

async function bootstrap() {
  try {
    await Promise.race([
      redis.connect(),
      new Promise((_, reject) => setTimeout(() => reject(new Error("REDIS_CONNECT_TIMEOUT")), 1500)),
    ]);
  } catch (err) {
    console.error("[bootstrap] redis connect failed:", err.message);
  }
  app.listen(PORT, () => {
    console.log(`[server] listening on :${PORT}`);
  });
}

bootstrap();
