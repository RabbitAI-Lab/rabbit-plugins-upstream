#!/usr/bin/env node
/**
 * Local Spark key for a Zappi pot. Run this where the seed file should live.
 * Never POST the seed to Zappi. Never print the seed.
 *
 *   node new-key.mjs --file pot-ONCE.txt
 *   node new-key.mjs --file pot-ONCE.txt --check
 *   node new-key.mjs --file pot-ONCE.txt --open
 *   node new-key.mjs --open --sparkAddress spark1...
 *   node new-key.mjs --pull-signer
 *   node new-key.mjs --file pot-ONCE.txt --spend --to spark1... --amount 0.25
 *
 * Writes a BIP39 mnemonic to --file (wx, 0600) and prints JSON.
 * --check does not mint. It reports the same USDB shape as live /sign.mjs
 * so you can tell if Orchestra landed without spending. Live /sign.mjs
 * does not have --new yet; this file is the stopgap until that ships.
 */
import { spawnSync } from "node:child_process";
import { constants as fsConstants, writeSync } from "node:fs";
import { access, readFile, writeFile } from "node:fs/promises";

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
  if (payload && typeof payload === "object" && payload.neverPostSeed == null) {
    payload.neverPostSeed = true;
  }
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
  fail(
    "Usage: node new-key.mjs --file pot-ONCE.txt [--check] [--open] [--spend --to spark1... --amount 0.25] [--sourceChain base] [--sourceAsset USDC] [--ref id] [--expect spark1...]  |  node new-key.mjs --open --sparkAddress spark1...  |  node new-key.mjs --pull-signer",
    "usage",
    {
      flags: ["file", "check", "open", "spend", "to", "amount", "invoice", "units", "sourceChain", "sourceAsset", "ref", "expect", "sparkAddress", "pull-signer", "out", "signer"],
      codes: ["usage", "file", "deps", "signer", "empty", "insufficient", "expect", "pay", "mnemonic", "wallet", "spend", "open", "bad-input", "ref", "bridge", "rate"],
      nexts: ["mint", "open", "pay", "fund", "spend", "retry", "check", "install-deps", "pull-signer"],
      neverPostSeed: true,
      next: "mint",
    }
  );
}

if (process.argv.includes("--pull-signer")) {
  const dest = arg("out", "sign.mjs");
  const url = "https://pot.zappi.money/sign.mjs";
  let text;
  try {
    const res = await fetch(url);
    if (!res.ok) fail("Could not download signer (" + res.status + ")", "signer");
    text = await res.text();
  } catch (err) {
    fail(err?.message || "Could not download signer", "signer");
  }
  if (!text.includes("SparkWallet") || !text.includes("--check")) {
    fail("Downloaded signer did not look like live /sign.mjs", "signer");
  }
  try {
    await writeFile(dest, text, { encoding: "utf8", mode: 0o644 });
  } catch {
    fail("Could not write " + dest, "file");
  }
  const signerHasNew = text.includes("--new");
  emit({
    ok: true,
    mode: "pull-signer",
    file: dest,
    signer: url,
    signerHasNew,
    mintCli: signerHasNew
      ? "node " + dest + " --new --file pot-ONCE.txt"
      : "node new-key.mjs --file pot-ONCE.txt",
    spendCli: "node new-key.mjs --file pot-ONCE.txt --spend --to spark1... --amount 0.25",
    next: signerHasNew ? "mint-signer" : "mint",
  });
}



if (process.argv.includes("--spend")) {
  const file = arg("file", "pot-ONCE.txt");
  const signer = arg("signer", arg("out", "sign.mjs"));
  const to = arg("to");
  const amount = arg("amount");
  const invoice = arg("invoice");
  const units = arg("units");
  const expectAddr = arg("expect");
  if (!invoice && !to) {
    fail("Need --to and --amount, or --invoice", "usage", {
      next: "spend",
    });
  }
  if (!invoice && to && amount == null && units == null) {
    fail("Need --amount (or --units) with --to", "usage");
  }
  try {
    await access(file, fsConstants.R_OK);
  } catch {
    fail("Could not read --file", "file", {
      next: "mint",
      nextCli: "node new-key.mjs --file " + file,
    });
  }
  let pulledSigner = false;
  try {
    await access(signer, fsConstants.R_OK);
  } catch {
    const url = "https://pot.zappi.money/sign.mjs";
    let text;
    try {
      const res = await fetch(url);
      if (!res.ok) fail("Could not download signer (" + res.status + ")", "signer");
      text = await res.text();
    } catch (err) {
      fail(err?.message || "Could not download signer", "signer");
    }
    if (!text.includes("SparkWallet") || !text.includes("--check")) {
      fail("Downloaded signer did not look like live /sign.mjs", "signer");
    }
    try {
      await writeFile(signer, text, { encoding: "utf8", mode: 0o644 });
    } catch {
      fail("Could not write " + signer, "file");
    }
    pulledSigner = true;
  }
  const checkResult = spawnSync(process.execPath, [signer, "--file", file, "--check"], {
    encoding: "utf8",
    env: process.env,
  });
  if (checkResult.error) fail(checkResult.error.message || "Could not run signer", "spend");
  const checkErr = String(checkResult.stderr || "");
  const checkLines = String(checkResult.stdout || "").trim().split("\n").filter(Boolean);
  const checkLast = checkLines[checkLines.length - 1] || "";
  let checkJson;
  try {
    checkJson = JSON.parse(checkLast);
  } catch {
    if (/Cannot find package '@buildonspark\/spark-sdk'|ERR_MODULE_NOT_FOUND/.test(checkErr)) {
      fail("Missing @buildonspark/spark-sdk. Install it, then retry.", "deps", {
        next: "install-deps",
        signerFile: signer,
        pulledSigner,
      });
    }
    fail("Signer --check did not print JSON", "spend", {
      next: "check",
      nextCli: "node new-key.mjs --file " + file + " --check",
      pulledSigner,
    });
  }
  if (checkJson && checkJson.ok === false && checkJson.code) {
    fail(checkJson.error || "Spend precheck failed", checkJson.code, {
      next: checkJson.next || "check",
      nextCli: checkJson.nextCli || "node new-key.mjs --file " + file + " --check",
      signerFile: signer,
      pulledSigner,
    });
  }
  const usdb = checkJson && checkJson.usdb;
  const usdbAmount = usdb && usdb.amount != null ? String(usdb.amount) : "0";
  const empty = !usdb || usdbAmount === "0" || usdbAmount === "0.0";
  if (checkJson && checkJson.usdbAmbiguous) {
    fail("More than one USDB ticker on this pot; inspect --check", "empty", {
      next: "check",
      nextCli: "node new-key.mjs --file " + file + " --check",
      pulledSigner,
    });
  }
  if (empty) {
    emit({
      ok: false,
      mode: "spend",
      code: "empty",
      error: "Pot is empty. That is the cap.",
      sparkAddress: checkJson && checkJson.sparkAddress,
      usdb: usdb || null,
      next: "fund",
      nextCli: "node new-key.mjs --file " + file + " --check",
      checkCli: "node new-key.mjs --file " + file + " --check",
      signerFile: signer,
      pulledSigner,
    }, 1);
  }
  if (!invoice && amount != null) {
    const want = Number(amount);
    const have = Number(usdbAmount);
    if (Number.isFinite(want) && Number.isFinite(have) && want > have) {
      emit({
        ok: false,
        mode: "spend",
        code: "insufficient",
        error: "Not enough USDB in the pot. That is the cap.",
        sparkAddress: checkJson && checkJson.sparkAddress,
        usdb: usdb || null,
        want: amount,
        next: "fund",
        nextCli: "node new-key.mjs --file " + file + " --check",
        checkCli: "node new-key.mjs --file " + file + " --check",
        signerFile: signer,
        pulledSigner,
      }, 1);
    }
  }
  if (!invoice && units != null && usdb && usdb.units != null) {
    if (safeBigInt(units) > safeBigInt(usdb.units)) {
      emit({
        ok: false,
        mode: "spend",
        code: "insufficient",
        error: "Not enough USDB in the pot. That is the cap.",
        sparkAddress: checkJson && checkJson.sparkAddress,
        usdb: usdb || null,
        wantUnits: units,
        next: "fund",
        nextCli: "node new-key.mjs --file " + file + " --check",
        checkCli: "node new-key.mjs --file " + file + " --check",
        signerFile: signer,
        pulledSigner,
      }, 1);
    }
  }
  const childArgs = [signer, "--file", file];
  if (invoice) childArgs.push("--invoice", invoice);
  else {
    childArgs.push("--to", to);
    if (amount != null) childArgs.push("--amount", amount);
    if (units != null) childArgs.push("--units", units);
  }
  if (expectAddr) childArgs.push("--expect", expectAddr);
  const result = spawnSync(process.execPath, childArgs, {
    encoding: "utf8",
    env: process.env,
  });
  if (result.error) fail(result.error.message || "Could not run signer", "spend");
  const errText = String(result.stderr || "");
  const lines = String(result.stdout || "").trim().split("\n").filter(Boolean);
  const last = lines[lines.length - 1] || "";
  let parsed;
  try {
    parsed = JSON.parse(last);
  } catch {
    if (/Cannot find package '@buildonspark\/spark-sdk'|ERR_MODULE_NOT_FOUND/.test(errText)) {
      fail("Missing @buildonspark/spark-sdk. Install it, then retry.", "deps", {
        next: "install-deps",
        signerFile: signer,
        pulledSigner,
      });
    }
    fail("Signer did not print JSON", "spend", {
      next: pulledSigner ? "spend" : "pull-signer",
      nextCli: pulledSigner ? null : "node new-key.mjs --pull-signer",
      pulledSigner,
    });
  }
  if (errText && parsed && parsed.ok !== false) process.stderr.write(redact(errText));
  if (!parsed || typeof parsed !== "object") fail("Signer did not print JSON", "spend");
  parsed.mode = parsed.mode || "spend";
  parsed.signerFile = signer;
  parsed.pulledSigner = pulledSigner;
  const exitCode = parsed.ok === false ? (result.status || 1) : result.status === 0 ? 0 : result.status || 1;
  emit(parsed, exitCode);
}


if (process.argv.includes("--open")) {
  const OPEN_BASE = "https://pot.zappi.money/deposit";
  let sparkAddress = arg("sparkAddress");
  if (!sparkAddress) {
    const file = arg("file", "pot-ONCE.txt");
    try {
      await access(file, fsConstants.R_OK);
    } catch {
      fail("Could not read --file", "file", {
        next: "mint",
        nextCli: "node new-key.mjs --file " + file,
      });
    }
    let SparkWallet;
    try {
      ({ SparkWallet } = await import("@buildonspark/spark-sdk"));
    } catch {
      fail("Missing @buildonspark/spark-sdk. Install it, then retry.", "deps");
    }
    let raw;
    try {
      raw = await readFile(file, "utf8");
    } catch {
      fail("Could not read --file", "file", {
        next: "mint",
        nextCli: "node new-key.mjs --file " + file,
      });
    }
    const words = String(raw).trim().split(/\s+/).filter(Boolean);
    raw = null;
    if (words.length !== 12 && words.length !== 24) fail("No 12/24-word mnemonic in that file", "mnemonic");
    const mnemonic = words.join(" ");
    secrets.add(mnemonic);
    let wallet;
    try {
      ({ wallet } = await SparkWallet.initialize({
        mnemonicOrSeed: mnemonic,
        options: { network: process.env.SPARK_NETWORK || "MAINNET" },
      }));
    } catch {
      fail("Could not open the wallet from that mnemonic", "wallet");
    }
    try {
      sparkAddress = await wallet.getSparkAddress();
    } catch {
      fail("Could not read sparkAddress", "wallet");
    }
    const expect = arg("expect");
    if (expect && expect !== sparkAddress) {
      try {
        if (wallet && typeof wallet.cleanup === "function") await wallet.cleanup();
      } catch {}
      fail("Wrong wallet", "expect", { sparkAddress, expect }, 2);
    }
    let funded = null;
    try {
      const { balance, tokenBalances } = await wallet.getBalance();
      const balances = collectBalances(tokenBalances);
      const usdbMatches = balances.filter((b) => b.asset === "USDB");
      const usdb = usdbMatches.length === 1 ? usdbMatches[0] : null;
      const usdbAmount = usdb && usdb.amount != null ? String(usdb.amount) : "0";
      if (usdb && usdbAmount !== "0" && usdbAmount !== "0.0") {
        funded = {
          usdb,
          btcSats: typeof balance === "bigint" ? balance.toString() : String(balance ?? 0),
        };
      }
    } catch {
      funded = null;
    }
    try {
      if (wallet && typeof wallet.cleanup === "function") await wallet.cleanup();
    } catch {
      // ignore
    }
    if (funded) {
      emit({
        ok: true,
        mode: "open",
        http: 0,
        code: "funded",
        sparkAddress,
        usdb: funded.usdb,
        btcSats: funded.btcSats,
        next: "spend",
        nextCli: "node new-key.mjs --file " + file + " --spend --to spark1... --amount 0.25",
        spendCli: "node new-key.mjs --file " + file + " --spend --to spark1... --amount 0.25",
        checkCli: "node new-key.mjs --file " + file + " --check",
      });
    }
  }
  if (!sparkAddress || !String(sparkAddress).startsWith("spark1")) {
    fail("Need --file or --sparkAddress spark1...", "usage");
  }
  const sourceChain = arg("sourceChain", "base");
  const sourceAsset = arg("sourceAsset", "USDC");
  const ref = arg("ref");
  if (!/^[a-z0-9-]+$/i.test(sourceChain) || !/^[A-Za-z0-9]+$/.test(sourceAsset)) {
    fail("Bad --sourceChain or --sourceAsset", "usage");
  }
  if (ref && !/^[a-zA-Z0-9_-]{1,32}$/.test(ref)) {
    fail("Bad --ref", "usage");
  }
  let open =
    OPEN_BASE +
    "?sparkAddress=" +
    encodeURIComponent(sparkAddress) +
    "&sourceChain=" +
    encodeURIComponent(sourceChain) +
    "&sourceAsset=" +
    encodeURIComponent(sourceAsset);
  if (ref) open += "&ref=" + encodeURIComponent(ref);
  let retryCli =
    "node new-key.mjs --open --sparkAddress " +
    sparkAddress +
    " --sourceChain " +
    sourceChain +
    " --sourceAsset " +
    sourceAsset;
  if (ref) retryCli += " --ref " + ref;
  let res;
  try {
    res = await fetch(open);
  } catch (err) {
    fail(err?.message || "Could not open pot", "open");
  }
  const http = res.status;
  let body = {};
  try {
    body = await res.json();
  } catch {
    body = {};
  }
  function payFrom402(res, openUrl) {
    const fallback = {
      protocol: "x402",
      price: "$0.01",
      asset: "USDC",
      chain: "base",
      network: "eip155:8453",
      url: openUrl,
    };
    const hdr = res.headers.get("payment-required");
    if (!hdr) return fallback;
    try {
      const json = JSON.parse(Buffer.from(hdr, "base64").toString("utf8"));
      const acc = Array.isArray(json.accepts) ? json.accepts[0] : null;
      return {
        protocol: "x402",
        price: acc && acc.amount === "10000" ? "$0.01" : (acc && acc.amount) || fallback.price,
        asset: "USDC",
        chain: "base",
        network: (acc && acc.network) || fallback.network,
        payTo: acc && acc.payTo ? acc.payTo : undefined,
        url: openUrl,
      };
    } catch {
      return fallback;
    }
  }
  const fileForCheck = arg("file");
  const checkCli = fileForCheck
    ? "node new-key.mjs --file " + fileForCheck + " --check"
    : null;
  const spendCli = fileForCheck
    ? "node new-key.mjs --file " + fileForCheck + " --spend --to spark1... --amount 0.25"
    : null;
  if (http === 200) {
    emit({
      ok: true,
      mode: "open",
      http,
      sparkAddress: body.sparkAddress || sparkAddress,
      pot: body.pot || null,
      depositAddress: body.depositAddress || (body.pot && body.pot.depositAddress) || (body.howToFund && body.howToFund.depositAddress) || null,
      howToFund: body.howToFund || null,
      sourceChain,
      sourceAsset,
      ref: ref || null,
      open,
      next: "fund",
      checkCli,
      spendCli,
      nextCli: checkCli,
    });
  }
  if (http === 400) {
    fail((body && body.error) || "Bad input", "bad-input", { http, sparkAddress, open });
  }
  if (http === 404) {
    fail("Unknown ?ref= affiliate id", "ref", { http, sparkAddress, ref: ref || null, open });
  }
  if (http === 429) {
    const retryAfter = res.headers.get("retry-after");
    emit({
      ok: false,
      mode: "open",
      http,
      code: "rate",
      error: "Rate limited",
      retryAfter: retryAfter ? Number(retryAfter) || retryAfter : null,
      sparkAddress,
      open,
      next: "retry",
      nextCli: retryCli,
    });
  }
  if (http === 502) {
    fail((body && body.error) || "Upstream bridge unavailable", "bridge", { http, sparkAddress, open, ref: body && body.ref ? body.ref : undefined });
  }
  if (http === 402) {
    emit({
      ok: false,
      mode: "open",
      http,
      code: "pay",
      error: "Zappi still charges $0.01 for an Orchestra depositAddress. You already have sparkAddress. Send Spark USDB to it, then --check. Do not pay unless you need the Orchestra address. Never POST the seed.",
      sparkAddress,
      fundDirect: true,
      sourceChain,
      sourceAsset,
      ref: ref || null,
      open,
      pay: payFrom402(res, open),
      next: "fund",
      nextCli: checkCli,
      payCli: retryCli,
      checkCli,
      spendCli,
    });
  }
  fail("Open failed (" + http + ")", "open", { http, sparkAddress, open });
}


const file = arg("file", "pot-ONCE.txt");
const check = process.argv.includes("--check");

if (check) {
  try {
    await access(file, fsConstants.R_OK);
  } catch {
    fail("Could not read --file", "file", {
      next: "mint",
      nextCli: "node new-key.mjs --file " + file,
    });
  }
}

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
    fail("Could not read --file", "file", {
      next: "mint",
      nextCli: "node new-key.mjs --file " + file,
    });
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

const sourceChain = arg("sourceChain", "base");
const sourceAsset = arg("sourceAsset", "USDC");
const ref = arg("ref");
if (!/^[a-z0-9-]+$/i.test(sourceChain) || !/^[A-Za-z0-9]+$/.test(sourceAsset)) {
  fail("Bad --sourceChain or --sourceAsset", "usage");
}
if (ref && !/^[a-zA-Z0-9_-]{1,32}$/.test(ref)) {
  fail("Bad --ref", "usage");
}
let open =
  "https://pot.zappi.money/deposit?sparkAddress=" +
  encodeURIComponent(sparkAddress) +
  "&sourceChain=" +
  encodeURIComponent(sourceChain) +
  "&sourceAsset=" +
  encodeURIComponent(sourceAsset);
if (ref) open += "&ref=" + encodeURIComponent(ref);

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
  sourceChain,
  sourceAsset,
  ref: ref || null,
  signer: "https://pot.zappi.money/sign.mjs",
  checkCli: "node new-key.mjs --file " + file + " --check",
  openCli: "node new-key.mjs --file " + file + " --open",
  spendCli: "node new-key.mjs --file " + file + " --spend --to spark1... --amount 0.25",
};
if (checkPayload) Object.assign(payload, checkPayload);
payload.next = nextAction(payload.mode, checkPayload);
payload.fundDirect = payload.next === "fund";
payload.nextCli = {"open": payload.openCli, "fund": payload.checkCli, "spend": payload.spendCli}[payload.next] || payload.checkCli;
emit(payload);
