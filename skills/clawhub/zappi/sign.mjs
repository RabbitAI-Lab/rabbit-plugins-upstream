#!/usr/bin/env node
/**
 * Local Zappi spender. Run this where the seed file lives.
 * Never POST the seed to Zappi. Never print the seed.
 *
 *   node sign.mjs --file pot-ONCE.txt --new
 *   node sign.mjs --file pot-ONCE.txt --check
 *   node sign.mjs --file pot-ONCE.txt --open
 *   node sign.mjs --file pot-ONCE.txt --to spark1... --amount 0.25
 *   node sign.mjs --file pot-ONCE.txt --invoice <invoice>
 *
 * --new creates a MAINNET Spark mnemonic in --file (refuses if it already exists).
 * --open GETs /deposit?sparkAddress=… from the local key (never POSTs the seed).
 * --amount is human USDB (0.25 = 0.25 USDB). USDB has 6 decimals.
 * --units is the escape hatch for smallest units (0.25 USDB = 250000).
 * --token pins an exact tokenIdentifier when more than one token claims a ticker.
 * --expect spark1... refuses to act if the seed file opens a different wallet.
 *
 * JSON result goes to stdout. Everything else goes to stderr.
 * --new JSON includes sparkAddress only — never the mnemonic.
 * --open JSON includes depositAddress and neverPostSeed — never the mnemonic.
 */
import { constants as fsConstants, writeSync } from "node:fs";
import { access, readFile, writeFile } from "node:fs/promises";
import { generateMnemonic } from "@scure/bip39";
import { wordlist } from "@scure/bip39/wordlists/english";
import { SparkWallet } from "@buildonspark/spark-sdk";

const USDB_DECIMALS = 6;

function hasFlag(name) {
  return process.argv.includes("--" + name);
}

function arg(name, fallback) {
  const i = process.argv.indexOf("--" + name);
  if (i >= 0 && process.argv[i + 1] && !String(process.argv[i + 1]).startsWith("--")) {
    return process.argv[i + 1];
  }
  return fallback;
}

// Anything derived from the seed file is scrubbed from every byte this process
// writes, including output from dependencies. Nothing here should ever print the
// seed; this is the backstop for when something does.
const secrets = new Set();

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

// stdout is the machine-readable channel an agent parses. Keep dependency chatter
// (the Spark SDK can attach a console span exporter) off it.
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

// console.log to a pipe is asynchronous, so process.exit() could truncate the
// result an agent is reading. Write to fd 1 synchronously instead.
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

const MNEMONIC_WORD_COUNTS = new Set([12, 15, 18, 21, 24]);

function asMnemonic(value) {
  if (typeof value !== "string") return "";
  const words = value.trim().toLowerCase().split(/\s+/);
  if (!MNEMONIC_WORD_COUNTS.has(words.length)) return "";
  if (!words.every((w) => /^[a-z]{3,8}$/.test(w))) return "";
  return words.join(" ");
}

function fromJson(value, depth = 0) {
  if (depth > 4 || !value || typeof value !== "object") return "";
  for (const key of ["mnemonic", "seedPhrase", "seed"]) {
    const found = asMnemonic(value[key]);
    if (found) return found;
  }
  for (const key of ["pot", "data", "result"]) {
    const found = fromJson(value[key], depth + 1);
    if (found) return found;
  }
  return "";
}

// Extracts only the mnemonic, never the surrounding document. The previous order
// (word-count heuristic before JSON.parse) handed whole files to the SDK, whose
// error text is echoed on stdout — so an unrelated --file leaked its size and a
// character of its contents, and a saved /deposit JSON never worked at all.
function mnemonicFrom(raw) {
  const text = String(raw ?? "").trim();
  if (!text) return "";
  try {
    const fromDocument = fromJson(JSON.parse(text));
    if (fromDocument) return fromDocument;
  } catch {
    // not JSON; fall through to the text forms
  }
  const whole = asMnemonic(text);
  if (whole) return whole;
  for (const line of text.split(/\r?\n/)) {
    const stripped = line.replace(/^\s*[\w.-]+\s*[:=]\s*/, "").replace(/^["']|["',]*$/g, "");
    const found = asMnemonic(stripped);
    if (found) return found;
  }
  return "";
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

function parseHumanAmount(raw, decimals = USDB_DECIMALS) {
  const s = String(raw).trim();
  if (!/^\d+(\.\d+)?$/.test(s)) {
    throw new Error("invalid --amount; expected a non-negative decimal like 0.25");
  }
  const [whole, frac = ""] = s.split(".");
  if (frac.length > decimals) {
    throw new Error(`invalid --amount; max ${decimals} decimal places`);
  }
  const padded = frac.padEnd(decimals, "0");
  return BigInt(whole || "0") * 10n ** BigInt(decimals) + BigInt(padded || "0");
}

function parseUnits(raw) {
  const s = String(raw).trim();
  if (!/^\d+$/.test(s)) {
    throw new Error("invalid --units; expected a non-negative integer in smallest units");
  }
  return BigInt(s);
}

function resolveTokenAmount({ amountRaw, unitsRaw, decimals = USDB_DECIMALS }) {
  if (unitsRaw != null && amountRaw != null) {
    throw new Error("pass either --amount (human) or --units (smallest), not both");
  }
  if (unitsRaw != null) {
    const units = parseUnits(unitsRaw);
    return { units, amount: unitsToHuman(units, decimals), source: "units" };
  }
  if (amountRaw != null) {
    const units = parseHumanAmount(amountRaw, decimals);
    return { units, amount: unitsToHuman(units, decimals), source: "amount" };
  }
  return null;
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

// Resolves which token to move. A pinned identifier wins; otherwise the ticker
// must match exactly one token, or we refuse rather than guess — picking "the
// last one that called itself USDB" is how a counterfeit token gets spent.
function selectToken(balances, asset, pinned) {
  if (pinned) {
    const exact = balances.find((b) => b.tokenIdentifier === pinned);
    if (!exact) {
      return { error: `--token ${pinned} is not held by this wallet`, code: "token" };
    }
    return { token: exact };
  }
  const matches = balances.filter((b) => b.asset === asset);
  if (matches.length > 1) {
    return {
      error: `More than one token calls itself ${asset}. Re-run with --token <tokenIdentifier> to say which one you mean.`,
      code: "ambiguous-token",
      candidates: matches.map((m) => ({
        tokenIdentifier: m.tokenIdentifier,
        issuer: m.issuer,
        amount: m.amount,
      })),
    };
  }
  if (matches.length === 0) {
    return { token: { asset, tokenIdentifier: asset, units: "0", decimals: USDB_DECIMALS } };
  }
  return { token: matches[0] };
}

function summarizeInvoiceResult(result) {
  return {
    satsTransactionSuccess: (result?.satsTransactionSuccess || []).map((row) => ({
      invoice: row.invoice,
      transferId: row.transferResponse?.id || null,
    })),
    tokenTransactionSuccess: (result?.tokenTransactionSuccess || []).map((row) => ({
      tokenIdentifier: row.tokenIdentifier,
      invoices: row.invoices,
      txid: row.txid,
    })),
    satsTransactionErrors: (result?.satsTransactionErrors || []).map((row) => ({
      invoice: row.invoice,
      error: row.error?.message || String(row.error),
    })),
    tokenTransactionErrors: (result?.tokenTransactionErrors || []).map((row) => ({
      tokenIdentifier: row.tokenIdentifier,
      invoices: row.invoices,
      error: row.error?.message || String(row.error),
    })),
    invalidInvoices: (result?.invalidInvoices || []).map((row) => ({
      invoice: row.invoice,
      error: row.error?.message || String(row.error),
    })),
  };
}

function invoiceSucceeded(summary) {
  const ok =
    summary.satsTransactionSuccess.length > 0 ||
    summary.tokenTransactionSuccess.length > 0;
  const failed =
    summary.satsTransactionErrors.length > 0 ||
    summary.tokenTransactionErrors.length > 0 ||
    summary.invalidInvoices.length > 0;
  return ok && !failed;
}

const file = arg("file");
const to = arg("to");
const amountRaw = arg("amount");
const unitsRaw = arg("units");
const invoice = arg("invoice");
const asset = (arg("asset", "USDB") || "USDB").toUpperCase();
const token = arg("token");
const expect = arg("expect");
const check = hasFlag("check");
const isNew = hasFlag("new");
const isOpen = hasFlag("open");
const network = process.env.SPARK_NETWORK || "MAINNET";
const zappiOrigin = (process.env.ZAPPI_ORIGIN || "https://pot.zappi.money").replace(/\/$/, "");

if (!file) {
  fail(
    "Usage: node sign.mjs --file pot-ONCE.txt (--new | --check | --open | --to spark1... --amount 0.25 | --invoice <invoice>) [--sourceChain base] [--sourceAsset USDC] [--ref id] [--units N] [--asset USDB] [--token <tokenIdentifier>] [--expect spark1...]",
    "usage",
  );
}

const modeCount = [isNew, check, isOpen, Boolean(invoice), Boolean(to)].filter(Boolean).length;
if (modeCount !== 1) {
  fail(
    "Pick exactly one mode: --new, --check, --open, --to + (--amount|--units), or --invoice",
    "usage",
  );
}

if (isOpen) {
  if (amountRaw != null || unitsRaw != null || invoice || to || token) {
    fail(
      "--open only takes --file and optional --sourceChain/--sourceAsset/--ref/--expect",
      "usage",
    );
  }
}

if (isNew) {
  if (amountRaw != null || unitsRaw != null || invoice || to || token || expect) {
    fail("--new only takes --file (and optional SPARK_NETWORK)", "usage");
  }
  try {
    await access(file, fsConstants.F_OK);
    fail("Seed file already exists; refusing to overwrite", "file");
  } catch (err) {
    if (err?.code !== "ENOENT") fail("Could not access --file", "file");
  }

  // Generate first (same BIP39 path the SDK uses), scrub before any SDK I/O,
  // persist with wx, then open the wallet from the saved mnemonic.
  const mnemonic = asMnemonic(generateMnemonic(wordlist));
  if (!mnemonic) {
    fail("Could not create a wallet mnemonic", "wallet");
  }
  secrets.add(mnemonic);

  try {
    await writeFile(file, `${mnemonic}\n`, {
      encoding: "utf8",
      flag: "wx",
      mode: 0o600,
    });
  } catch (err) {
    if (err?.code === "EEXIST") {
      fail("Seed file already exists; refusing to overwrite", "file");
    }
    fail("Could not write --file", "file");
  }

  let wallet;
  try {
    ({ wallet } = await SparkWallet.initialize({
      mnemonicOrSeed: mnemonic,
      options: { network },
    }));
  } catch {
    fail("Could not create a wallet", "wallet");
  }

  const address = await wallet.getSparkAddress();
  emit({ ok: true, mode: "new", sparkAddress: address });
}

if (to && amountRaw == null && unitsRaw == null) {
  fail("Transfer requires --amount (human USDB) or --units (smallest units)", "usage");
}

if (amountRaw != null && unitsRaw != null) {
  fail("pass either --amount (human) or --units (smallest), not both", "amount");
}

// --amount assumes USDB's 6 decimals. An invoice carries its own asset, so the
// same 0.25 would mean 0.25 USDB or 250000 sats depending on the invoice. Refuse
// to guess: plain --invoice (the documented form) and --invoice --units are exact.
if (invoice && amountRaw != null) {
  fail(
    "--invoice does not take --amount: the invoice decides the asset, so decimals are unknown. Use --invoice alone, or --units for exact smallest units.",
    "amount",
  );
}

if (to && !/^(spark|sparkt|sparkrt|sparks|sparkl|sp|spt|sprt|sps|spl)1[023456789acdefghjklmnpqrstuvwxyz]{10,300}$/.test(to)) {
  fail("--to is not a Spark address", "recipient");
}

let raw;
try {
  raw = await readFile(file, "utf8");
} catch {
  if (isOpen) {
    fail("Could not read --file", "file", {
      next: "new",
      nextCli: `node sign.mjs --file ${file} --new`,
    });
  }
  fail("Could not read --file", "file");
}

const mnemonic = mnemonicFrom(raw);
raw = null;
if (!mnemonic) {
  fail("No 12/24-word mnemonic in that file", "mnemonic");
}
secrets.add(mnemonic);

let wallet;
try {
  ({ wallet } = await SparkWallet.initialize({
    mnemonicOrSeed: mnemonic,
    options: { network },
  }));
} catch {
  // Deliberately not the SDK's message: on a bad mnemonic it reports on the
  // characters and length of the material it was handed.
  fail("Could not open the wallet from that mnemonic", "wallet");
}

const address = await wallet.getSparkAddress();
if (expect && address !== expect) {
  fail("Wrong wallet", "expect", { sparkAddress: address, expect }, 2);
}

if (check) {
  const { balance, tokenBalances } = await wallet.getBalance();
  const balances = collectBalances(tokenBalances);
  const usdbMatches = balances.filter((b) => b.asset === "USDB");
  emit({
    ok: true,
    mode: "check",
    sparkAddress: address,
    btcSats: typeof balance === "bigint" ? balance.toString() : String(balance ?? 0),
    usdb: usdbMatches.length === 1 ? usdbMatches[0] : null,
    // More than one token can claim the USDB ticker, so say so instead of
    // silently reporting the first one as "the" balance.
    usdbAmbiguous: usdbMatches.length > 1 ? usdbMatches : undefined,
    balances,
  });
}

if (isOpen) {
  const sourceChain = arg("sourceChain", "base") || "base";
  const sourceAsset = arg("sourceAsset", "USDC") || "USDC";
  const ref = arg("ref");
  if (!/^[a-z0-9-]+$/i.test(sourceChain) || !/^[A-Za-z0-9]+$/.test(sourceAsset)) {
    fail("Bad --sourceChain or --sourceAsset", "usage");
  }
  if (ref && !/^[a-zA-Z0-9_-]{1,32}$/.test(ref)) {
    fail("Bad --ref", "usage");
  }

  // next=spend when USDB already landed; otherwise fund the Orchestra address.
  let next = "fund";
  try {
    const { tokenBalances } = await wallet.getBalance();
    const balances = collectBalances(tokenBalances);
    const usdbMatches = balances.filter((b) => b.asset === "USDB");
    const usdb = usdbMatches.length === 1 ? usdbMatches[0] : null;
    const usdbAmount = usdb?.amount != null ? String(usdb.amount) : "0";
    if (usdb && usdbAmount !== "0" && usdbAmount !== "0.0") next = "spend";
  } catch {
    // Balance is best-effort; open still looks up the pot.
  }

  const openUrl = new URL("deposit", `${zappiOrigin}/`);
  openUrl.searchParams.set("sparkAddress", address);
  openUrl.searchParams.set("sourceChain", sourceChain);
  openUrl.searchParams.set("sourceAsset", sourceAsset);
  if (ref) openUrl.searchParams.set("ref", ref);
  const open = openUrl.toString();

  let res;
  try {
    res = await fetch(open);
  } catch (err) {
    fail(err?.message || "Could not open pot", "open", {
      sparkAddress: address,
      open,
      next: "retry",
    });
  }

  const http = res.status;
  let body = {};
  try {
    body = await res.json();
  } catch {
    body = {};
  }

  if (http === 200) {
    const depositAddress =
      body.depositAddress ||
      body.pot?.depositAddress ||
      body.howToFund?.depositAddress ||
      null;
    const potPublic = body.pot && typeof body.pot === "object" ? body.pot : null;
    const pot = potPublic
      ? {
          id: potPublic.id ?? null,
          sparkAddress: potPublic.sparkAddress ?? address,
          depositAddress: potPublic.depositAddress ?? depositAddress,
          sourceChain: potPublic.sourceChain ?? sourceChain,
          sourceAsset: potPublic.sourceAsset ?? sourceAsset,
          destinationAsset: potPublic.destinationAsset ?? "USDB",
        }
      : null;
    // Never copy mnemonic / seed fields from the server body onto stdout.
    emit({
      ok: true,
      mode: "open",
      http,
      sparkAddress: address,
      depositAddress,
      pot,
      potId: pot?.id ?? null,
      howToFund: body.howToFund
        ? {
            chain: body.howToFund.chain ?? sourceChain,
            asset: body.howToFund.asset ?? sourceAsset,
            depositAddress: body.howToFund.depositAddress ?? depositAddress,
            destinationAsset: body.howToFund.destinationAsset ?? "USDB",
            sparkAddress: body.howToFund.sparkAddress ?? address,
          }
        : null,
      sourceChain,
      sourceAsset,
      ref: ref || null,
      open,
      next,
      nextCli:
        next === "spend"
          ? `node sign.mjs --file ${file} --to spark1... --amount 0.25`
          : `node sign.mjs --file ${file} --check`,
    });
  }

  if (http === 400) {
    fail((body && body.error) || "Bad input", "bad-input", {
      http,
      sparkAddress: address,
      open,
    });
  }
  if (http === 402) {
    // Skill path with sparkAddress must stay free; 402 means bare /deposit.
    fail(
      "Deposit open returned 402. Retry --open (includes sparkAddress). Do not hit bare /deposit. Never POST the seed.",
      "pay",
      {
        http,
        sparkAddress: address,
        open,
        next: "fund",
        fundDirect: true,
      },
    );
  }
  fail((body && body.error) || `Open failed (${http})`, "open", {
    http,
    sparkAddress: address,
    open,
  });
}

if (invoice) {
  let resolved = null;
  try {
    resolved = resolveTokenAmount({ amountRaw: null, unitsRaw });
  } catch (err) {
    fail(err.message, "amount");
  }
  const payload = { invoice };
  if (resolved) payload.amount = resolved.units;
  let result;
  try {
    result = await wallet.fulfillSparkInvoice([payload]);
  } catch (err) {
    fail(err?.message || "fulfillSparkInvoice failed", "invoice", {
      mode: "invoice",
      sparkAddress: address,
      invoice,
    });
  }
  const summary = summarizeInvoiceResult(result);
  const ok = invoiceSucceeded(summary);
  emit(
    {
      ok,
      mode: "invoice",
      sparkAddress: address,
      invoice,
      amount: resolved?.amount ?? null,
      units: resolved ? resolved.units.toString() : null,
      result: summary,
    },
    ok ? 0 : 4,
  );
}

let resolved;
try {
  resolved = resolveTokenAmount({ amountRaw, unitsRaw });
} catch (err) {
  fail(err.message, "amount");
}

const { tokenBalances } = await wallet.getBalance();
const selection = selectToken(collectBalances(tokenBalances), asset, token);
if (selection.error) {
  fail(selection.error, selection.code, {
    mode: "transfer",
    sparkAddress: address,
    asset,
    candidates: selection.candidates,
  });
}
const { tokenIdentifier, units: available, decimals } = selection.token;

// Re-resolve with asset decimals when using human --amount
if (resolved.source === "amount" && decimals !== USDB_DECIMALS) {
  try {
    resolved = resolveTokenAmount({ amountRaw, unitsRaw: null, decimals });
  } catch (err) {
    fail(err.message, "amount");
  }
}

if (safeBigInt(available) < resolved.units) {
  fail("not enough balance", "balance", {
    mode: "transfer",
    sparkAddress: address,
    asset,
    available,
    availableAmount: unitsToHuman(safeBigInt(available), decimals),
    amount: resolved.amount,
    units: resolved.units.toString(),
  }, 3);
}

let tx;
try {
  tx = await wallet.transferTokens({
    tokenIdentifier,
    tokenAmount: resolved.units,
    receiverSparkAddress: to,
  });
} catch (err) {
  fail(err?.message || "transferTokens failed", "transfer", {
    mode: "transfer",
    sparkAddress: address,
    to,
    asset,
    amount: resolved.amount,
    units: resolved.units.toString(),
  });
}

const hash = typeof tx === "string" ? tx : tx?.id || tx?.hash || null;
emit({
  ok: true,
  mode: "transfer",
  tx: hash,
  from: address,
  to,
  amount: resolved.amount,
  units: resolved.units.toString(),
  asset,
  tokenIdentifier,
  issuer: selection.token.issuer ?? null,
});
