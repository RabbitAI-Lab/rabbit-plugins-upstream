#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { resolveInside, resolveWorkspaceRoot, safeRegularOrMissing } from "./path-guard.mjs";

const minimum = "2026.7.1";
function stop(message, data = {}) {
  console.log(JSON.stringify({ ready: false, mode: "audit-only", contractVersion: 1, minimumOpenClaw: minimum, error: message, ...data }, null, 2));
  process.exit(3);
}
function tuple(text) {
  const match = String(text).match(/(\d{4})\.(\d+)\.(\d+)/);
  return match?.slice(1).map(Number);
}
function current(actual) {
  const required = [2026, 7, 1];
  for (let index = 0; index < required.length; index += 1) {
    if (actual[index] !== required[index]) return actual[index] > required[index];
  }
  return true;
}
function sameWorkspace(value, root) {
  return typeof value === "string" && path.isAbsolute(value) && path.resolve(value) === root;
}
function view(job) {
  return { id: job.id, name: job.name, enabled: Boolean(job.enabled), schedule: job.schedule ?? null };
}

const [rootArg] = process.argv.slice(2);
let root;
try { root = resolveWorkspaceRoot(rootArg); } catch (error) { stop(error.message); }
let input;
try { input = JSON.parse(fs.readFileSync(0, "utf8")); } catch { stop("sanitized preflight JSON required on stdin"); }

const version = tuple(input.openclawVersion);
if (!version || !current(version)) stop(`OpenClaw ${minimum} or newer is required`, { detectedVersion: String(input.openclawVersion ?? "") });
if (input.capabilities?.promoteExplain !== true || input.capabilities?.remHarness !== true) stop("required native read-only commands were not confirmed");
if (!Array.isArray(input.cron?.jobs)) stop("cron schema unsupported");

const statuses = Array.isArray(input.status) ? input.status : [input.status];
const matchedStatus = statuses.filter(entry => sameWorkspace(entry?.status?.workspaceDir, root));
if (matchedStatus.length !== 1) stop("expected one native status for workspace", { matches: matchedStatus.length });
const status = matchedStatus[0];
if (status?.status?.backend !== "builtin") stop("builtin memory backend required");
if (!Array.isArray(status?.dreamingAudit?.issues)) stop("native Dreaming audit schema unsupported");
if (status.dreamingAudit.issues.length) stop("native Dreaming audit has issues", { issues: status.dreamingAudit.issues });

const promotions = Array.isArray(input.promote) ? input.promote : [input.promote];
const matchedPromotion = promotions.filter(entry => sameWorkspace(entry?.workspaceDir, root));
if (matchedPromotion.length !== 1) stop("expected one promotion result for workspace", { matches: matchedPromotion.length });
const promotion = matchedPromotion[0];
if (!Array.isArray(promotion?.audit?.issues) || !Array.isArray(promotion?.candidates)) stop("promotion schema unsupported");
if (promotion.audit.issues.length) stop("native promotion audit has issues", { issues: promotion.audit.issues });

const native = input.cron.jobs.filter(job => job?.payload?.message === "__openclaw_memory_core_short_term_promotion_dream__");
const related = input.cron.jobs.filter(job => {
  const text = `${job?.name ?? ""} ${job?.payload?.message ?? ""}`.toLowerCase();
  return !native.includes(job) && (/daily[-_ ]?dream/.test(text) || text.includes("signal-dreaming") || text.includes("dream-protocol.md") || text.includes("dream consolidation"));
});
const v2 = related.filter(job => /signal-dreaming-v2|curation-gate\.mjs|gate-driven curation/i.test(`${job?.name ?? ""} ${job?.payload?.message ?? ""}`));
const v1 = related.filter(job => !v2.includes(job));

if (native.filter(job => job.enabled).length !== 1) stop("exactly one native Dreaming job must be enabled", { native: native.map(view) });
if (v1.some(job => job.enabled)) stop("enabled v1 cron would double-write memory", { legacy: v1.map(view) });
if (v2.filter(job => job.enabled).length > 1) stop("multiple enabled v2 curators", { curator: v2.map(view) });

const memory = resolveInside(root, "MEMORY.md", { allowMissing: false, label: "MEMORY.md" });
if (safeRegularOrMissing(root, memory) !== "file") stop("MEMORY.md unsafe");
const log = resolveInside(root, "memory/dream-log.md", { allowMissing: true, label: "legacy diary" });
let history = { state: "missing" };
if (fs.existsSync(log)) {
  if (safeRegularOrMissing(root, log) !== "file") stop("legacy diary unsafe");
  history = {
    state: "preserve-read-only",
    bytes: fs.statSync(log).size,
    sha256: crypto.createHash("sha256").update(fs.readFileSync(log)).digest("hex"),
  };
}

console.log(JSON.stringify({
  ready: true,
  mode: "write-preflight-ready",
  contractVersion: 1,
  minimumOpenClaw: minimum,
  detectedVersion: String(input.openclawVersion),
  native: native.map(view),
  legacy: { jobs: v1.map(view), history },
  curator: v2.map(view),
  writesPerformed: false,
}, null, 2));
