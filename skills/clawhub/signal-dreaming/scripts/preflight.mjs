#!/usr/bin/env node
import fs from "node:fs/promises";
import { pathToFileURL } from "node:url";
import {
  canonicalRoot,
  fail,
  safePath,
} from "./common.mjs";

export const MIN_OPENCLAW = "2026.7.1-2";
export const MIN_NODE = "22.23.1";

function tuple(value, label) {
  const match = String(value).match(/(\d+)\.(\d+)\.(\d+)(?:-(\d+))?/);
  if (!match) throw fail("VERSION_INVALID", `cannot parse ${label} version: ${value}`);
  return match.slice(1).map((item) => Number(item ?? 0));
}

function atLeast(actual, minimum, label) {
  const left = tuple(actual, label);
  const right = tuple(minimum, label);
  for (let index = 0; index < right.length; index += 1) {
    if (left[index] > right[index]) return true;
    if (left[index] < right[index]) return false;
  }
  return true;
}

export async function readEvidenceFiles(versionFile, dreamingFile, cronFile) {
  let openclawVersion;
  let nativeDreamingEnabled;
  let cronEnvelope;
  try {
    openclawVersion = (await fs.readFile(versionFile, "utf8")).trim();
    nativeDreamingEnabled = JSON.parse(await fs.readFile(dreamingFile, "utf8"));
    cronEnvelope = JSON.parse(await fs.readFile(cronFile, "utf8"));
  } catch (error) {
    throw fail("CLI_SCHEMA", `preflight evidence is missing or invalid: ${error.message}`);
  }
  if (!cronEnvelope || !Array.isArray(cronEnvelope.jobs)) {
    throw fail("CLI_SCHEMA", "openclaw cron list JSON is missing jobs[]");
  }
  return {
    openclawVersion,
    nodeVersion: process.versions.node,
    nativeDreamingEnabled,
    cronJobs: cronEnvelope.jobs,
  };
}

function isSignalWriter(job) {
  if (!job.enabled) return false;
  const name = typeof job.name === "string" ? job.name : "";
  const message = typeof job.payload?.message === "string" ? job.payload.message : "";
  return /(signal-dreaming|dream-protocol\.md|memory dream consolidation|run a dream consolidation)/i.test(`${name}\n${message}`);
}

export async function preflight(workspaceInput, evidence, options = {}) {
  const root = await canonicalRoot(workspaceInput);
  const errors = [];
  const warnings = [];
  const addError = (code, message) => errors.push({ code, message });

  if (!evidence || typeof evidence !== "object") addError("EVIDENCE_MISSING", "preflight evidence is missing");
  if (typeof evidence?.openclawVersion !== "string") addError("CLI_SCHEMA", "openclawVersion must be a string");
  else if (!atLeast(evidence.openclawVersion, MIN_OPENCLAW, "OpenClaw")) {
    addError("OPENCLAW_TOO_OLD", `OpenClaw ${MIN_OPENCLAW}+ is required`);
  }
  if (typeof evidence?.nodeVersion !== "string") addError("CLI_SCHEMA", "nodeVersion must be a string");
  else if (!atLeast(evidence.nodeVersion, MIN_NODE, "Node.js")) {
    addError("NODE_TOO_OLD", `Node.js ${MIN_NODE}+ is required`);
  }
  if (typeof evidence?.nativeDreamingEnabled !== "boolean") {
    addError("CLI_SCHEMA", "nativeDreamingEnabled must be boolean");
  } else if (evidence.nativeDreamingEnabled && !options.readOnly) {
    addError("NATIVE_DREAMING_ENABLED", "built-in OpenClaw Dreaming must be disabled before signal-dreaming writes");
  } else if (evidence.nativeDreamingEnabled) {
    warnings.push({ code: "READ_ONLY_ONLY", message: "native Dreaming is enabled; write mode is unavailable" });
  }
  if (!Array.isArray(evidence?.cronJobs)) addError("CLI_SCHEMA", "cronJobs must be an array");

  const jobs = Array.isArray(evidence?.cronJobs) ? evidence.cronJobs : [];
  for (const job of jobs) {
    if (!job || typeof job !== "object" || typeof job.id !== "string" || typeof job.name !== "string"
      || typeof job.enabled !== "boolean" || !job.payload || typeof job.payload !== "object") {
      addError("CLI_SCHEMA", "cron job fields are missing or have changed");
      break;
    }
  }
  const writers = jobs.filter(isSignalWriter).map((job) => ({ id: job.id, name: job.name }));
  if (writers.length > 1) addError("MULTIPLE_WRITERS", "more than one enabled signal-dreaming writer was found; disable all but one before write mode");
  if (writers.length === 0 && options.scheduled && !options.readOnly) {
    addError("NO_SCHEDULED_WRITER", "scheduled write mode requires exactly one enabled signal-dreaming writer");
  } else if (writers.length === 0) {
    warnings.push({ code: "NO_SCHEDULED_WRITER", message: "no enabled scheduled signal-dreaming writer was found; only an explicit manual run may write" });
  }

  const required = [
    ["MEMORY.md", "file"],
    ["memory", "directory"],
    ["memory/dream-log.md", "file"],
  ];
  for (const [relative, kind] of required) {
    try {
      await safePath(root, relative, { mustExist: true, kind, rejectSymlink: kind === "file" });
    } catch (error) {
      addError(error.code ?? "PATH_ERROR", error.message);
    }
  }
  for (const relative of ["logs/signal-dreaming/state.json", ".backup/memory-dreams/probe/manifest.json"]) {
    try {
      await safePath(root, relative);
    } catch (error) {
      addError(error.code ?? "PATH_ERROR", error.message);
    }
  }

  return {
    schema: "signal-dreaming.preflight.v3",
    ok: errors.length === 0,
    readOnly: Boolean(options.readOnly),
    scheduled: Boolean(options.scheduled),
    writeAllowed: errors.length === 0 && !evidence?.nativeDreamingEnabled,
    root,
    compatibility: {
      minimumOpenClaw: MIN_OPENCLAW,
      testedOpenClaw: ["2026.7.1-2"],
      minimumNode: MIN_NODE,
      testedNode: ["22.23.1"],
    },
    writers,
    errors,
    warnings,
  };
}

function parseArgs(argv) {
  const args = [...argv];
  const workspace = args.shift();
  if (!workspace) throw fail("USAGE", "usage: preflight.mjs <workspace-root> [--evidence file] [--read-only] [--scheduled]");
  let evidenceFile;
  let versionFile;
  let dreamingFile;
  let cronFile;
  let readOnly = false;
  let scheduled = false;
  while (args.length) {
    const arg = args.shift();
    if (arg === "--read-only") readOnly = true;
    else if (arg === "--scheduled") scheduled = true;
    else if (arg === "--evidence") evidenceFile = args.shift();
    else if (arg === "--version-file") versionFile = args.shift();
    else if (arg === "--dreaming-file") dreamingFile = args.shift();
    else if (arg === "--cron-file") cronFile = args.shift();
    else throw fail("USAGE", `unknown argument: ${arg}`);
  }
  if (!evidenceFile && (!versionFile || !dreamingFile || !cronFile)) {
    throw fail("USAGE", "provide --evidence or all of --version-file, --dreaming-file, and --cron-file");
  }
  return { workspace, evidenceFile, versionFile, dreamingFile, cronFile, readOnly, scheduled };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const evidence = args.evidenceFile
    ? JSON.parse(await fs.readFile(args.evidenceFile, "utf8"))
    : await readEvidenceFiles(args.versionFile, args.dreamingFile, args.cronFile);
  const result = await preflight(args.workspace, evidence, { readOnly: args.readOnly, scheduled: args.scheduled });
  process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
  if (!result.ok) process.exitCode = 2;
}

if (import.meta.url === pathToFileURL(process.argv[1] ?? "").href) {
  main().catch((error) => {
    process.stderr.write(`${JSON.stringify({ ok: false, code: error.code ?? "ERROR", message: error.message })}\n`);
    process.exitCode = 2;
  });
}
