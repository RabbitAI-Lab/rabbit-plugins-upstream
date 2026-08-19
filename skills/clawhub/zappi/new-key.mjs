#!/usr/bin/env node
/**
 * Local Spark key for a Zappi pot. Run this where the seed file should live.
 * Never POST the seed to Zappi. Never print the seed.
 *
 *   node new-key.mjs --file pot-ONCE.txt
 *   node new-key.mjs --file pot-ONCE.txt --check
 *
 * Writes a BIP39 mnemonic to --file (wx, 0600) and prints JSON.
 * --check does not mint. It reports the same USDB shape as live /sign.mjs
 * so you can tell if Orchestra landed without spending. Live /sign.mjs
 * does not have --new yet; this file is the stopgap until that ships.
 */
import { writeSync } from "node:fs";
import { readFile, writeFile } from "node:fs/promises";

function arg(name, fallback) {
  const i = process.argv.indexOf("--" + name);
  if (i >= 0 && process.argv[i + 1] && !String(process.argv[i + 1]).startsWith("--")) {
    return process.argv[i + 1];
  }
  return fallback;
}

const secrets = new Set();
const USDB_DECIMALS = 6;

function redact(text) {
  let out = String(text);
  for (const secret of secrets) {
    if (secret && out.includes(secret)) out = out.split(secret).join("[redacted]");
  }
  return out;
}

function guardStream(stream) {
  const original = stream.write.bind(stream);
  stream.write = (chunk, encoding, callback) => {
    if (typeof chunk === "string") return original(redact(chunk), encoding, callback);
    if (Buffer.isBuffer(chunk)) {
      const text = chunk.toString("utf8");
      const clean = redact(text);
      if (clean !== text) return original(Buffer.from(clean, "utf8"), encoding, callback);
    }
    return original(chunk, encoding, callback);
  };
}

guardStream(process.stdout);
guardStream(process.stderr);

const toStderr = (...args) => {
  process.stderr.write(args.map((a) => (typeof a === "string" ? a : String(a))).join(" ") + "\n");
};
console.log = toStderr;
console.info = toStderr;
console.debug = toStderr;

function jsonReplacer(_key, value) {
  if (typeof value === "bigint") return value.toString();
  if (value instanceof Error) return { name: value.name, message: value.message };
  return value;
}

function writeStdout(text) {
  const buf = Buffer.from(text, "utf8");
  let offset = 0;
  let attempts = 0;
  while (offset < buf.length && attempts < 10_000) {
    attempts += 1;
    try {
      offset += writeSync(1, buf, offset, buf.length - offset);
    } catch (err) {
      if (err.code === "EAGAIN") continue;
      return;
    }
  }
}

function emit(payload, exitCode = 0) {
  writeStdout(redact(JSON.stringify(payload, jsonReplacer)) + "\n");
  process.exit(exitCode);
}

function fail(error, code = "error", extra = {}, exitCode = 1) {
  emit({ ok: false, error: redact(String(error)), code, ...extra }, exitCode);
}

function tokenAmount(value) {
  const n = value?.balance ?? value?.ownedBalance ?? value?.availableToSendBalance;
  if (n == null) return "0";
  return typeof n === "bigint" ? n.toString() : String(n);
}

function unitsToHuman(units, decimals = USDB_DECIMALS) {
  const negative = units < 0n;
  const abs = negative ? -units : units;
  const base = 10n ** BigInt(decimals);
  const whole = abs / base;
  const frac = (abs % base).toString().padStart(decimals, "0").replace(/0+$/, "");
  const text = frac ? `${whole.toString()}.${frac}` : whole.toString();
  return negative ? `-${text}` : text;
}

function safeBigInt(value) {
  try {
    return BigInt(value);
  } catch {
    return 0n;
  }
}

function collectBalances(tokenBalances) {
  const balances = [];
  if (!tokenBalances || typeof tokenBalances.forEach !== "function") return balances;
  tokenBalances.forEach((value, key) => {
    const ticker = value.tokenMetadata?.tokenTicker || value.tokenMetadata?.ticker;
    const asset = ticker ? String(ticker).toUpperCase() : null;
    const raw = Number(value.tokenMetadata?.decimals ?? USDB_DECIMALS);
    const decimals = Number.isFinite(raw) ? raw : USDB_DECIMALS;
    const units = tokenAmount(value);
    balances.push({
      asset,
      tokenIdentifier: key,
      // Tickers are not unique on Spark: anyone can issue a token that calls
      // itself USDB. The identifier and issuer are what actually pin a token.
      issuer: value.tokenMetadata?.tokenPublicKey || null,
      name: value.tokenMetadata?.tokenName || null,
      units,
      amount: unitsToHuman(safeBigInt(units), decimals),
      decimals,
    });
  });
  return balances;
}

if (process.argv.includes("--help") || process.argv.includes("-h")) {
  fail("Usage: node new-key.mjs --file pot-ONCE.txt [--check] [--expect spark1...]", "usage");
}

const file = arg("file", "pot-ONCE.txt");
const check = process.argv.includes("--check");

let generateMnemonic;
let wordlist;
let SparkWallet;
try {
  ({ generateMnemonic } = await import("@scure/bip39"));
  ({ wordlist } = await import("@scure/bip39/wordlists/english.js"));
  ({ SparkWallet } = await import("@buildonspark/spark-sdk"));
} catch {
  fail("Missing @buildonspark/spark-sdk or @scure/bip39. Install both, then retry.", "deps");
}

let mnemonic;
if (check) {
  let raw;
  try {
    raw = await readFile(file, "utf8");
  } catch {
    fail("Could not read --file", "file");
  }
  const words = String(raw).trim().split(/\s+/).filter(Boolean);
  raw = null;
  if (words.length !== 12 && words.length !== 24) fail("No 12/24-word mnemonic in that file", "mnemonic");
  mnemonic = words.join(" ");
  secrets.add(mnemonic);
} else {
  try {
    mnemonic = generateMnemonic(wordlist);
  } catch (err) {
    fail(err?.message || "could not generate mnemonic", "mnemonic");
  }
  secrets.add(mnemonic);
  try {
    await writeFile(file, mnemonic + "\n", { encoding: "utf8", flag: "wx", mode: 0o600 });
  } catch (err) {
    if (err && err.code === "EEXIST") fail("file exists; refusing to overwrite", "file");
    fail("Could not write --file", "file");
  }
}

let wallet;
try {
  ({ wallet } = await SparkWallet.initialize({
    mnemonicOrSeed: mnemonic,
    options: { network: process.env.SPARK_NETWORK || "MAINNET" },
  }));
} catch {
  fail("Could not open the wallet from that mnemonic", "wallet");
}

let sparkAddress;
try {
  sparkAddress = await wallet.getSparkAddress();
} catch {
  fail("Could not read sparkAddress", "wallet");
}

const expect = arg("expect");
if (expect && expect !== sparkAddress) {
  try {
    if (wallet && typeof wallet.cleanup === "function") await wallet.cleanup();
  } catch {
    // ignore
  }
  fail("Wrong wallet", "expect", { sparkAddress, expect }, 2);
}

let checkPayload = null;
if (check) {
  try {
    const { balance, tokenBalances } = await wallet.getBalance();
    const balances = collectBalances(tokenBalances);
    const usdbMatches = balances.filter((b) => b.asset === "USDB");
    checkPayload = {
      btcSats: typeof balance === "bigint" ? balance.toString() : String(balance ?? 0),
      usdb: usdbMatches.length === 1 ? usdbMatches[0] : null,
      // More than one token can claim the USDB ticker, so say so instead of
      // silently reporting the first one as "the" balance.
      usdbAmbiguous: usdbMatches.length > 1 ? usdbMatches : undefined,
      balances,
    };
  } catch (err) {
    fail(err?.message || "Could not read balance", "balance");
  }
}

try {
  if (wallet && typeof wallet.cleanup === "function") await wallet.cleanup();
} catch {
  // ignore
}

const open =
  "https://pot.zappi.money/deposit?sparkAddress=" +
  encodeURIComponent(sparkAddress) +
  "&sourceChain=base&sourceAsset=USDC";

function nextAction(mode, checkPayload) {
  if (mode === "new") return "open";
  if (!checkPayload) return "fund";
  if (checkPayload.usdbAmbiguous) return "fund";
  const usdb = checkPayload.usdb;
  const amount = usdb && usdb.amount != null ? String(usdb.amount) : "0";
  if (!usdb || amount === "0" || amount === "0.0") return "fund";
  return "spend";
}

const payload = {
  ok: true,
  mode: check ? "check" : "new",
  sparkAddress,
  file,
  open,
  signer: "https://pot.zappi.money/sign.mjs",
};
if (checkPayload) Object.assign(payload, checkPayload);
payload.next = nextAction(payload.mode, checkPayload);
emit(payload);
