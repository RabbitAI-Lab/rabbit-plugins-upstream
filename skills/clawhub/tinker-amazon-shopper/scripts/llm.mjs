// llm.mjs — LLM client wrapper. Three modes: mock (for tests), openclaw gateway, subprocess.
//
// Env vars:
//   MOCK_LLM_RESPONSE_FILE  — path to JSON file mapping call_site → response. Forces mock mode.
//   AMAZON_SHOPPER_LLM_CMD  — override the subprocess CLI. Default: "oracle".

import { readFile } from "node:fs/promises";
import { spawn } from "node:child_process";
import { basename } from "node:path";

// SAFETY: AMAZON_SHOPPER_LLM_CMD names a program this skill will execute. Left
// unchecked, an env var anyone can set turns the skill into a generic process
// launcher, so the basename must be one of the LLM CLIs it is actually for.
// Escape hatch for a genuinely different CLI: AMAZON_SHOPPER_ALLOW_ANY_LLM_CMD=1.
const ALLOWED_LLM_CMDS = new Set(["claude", "oracle", "gemini", "openclaw", "llm", "ollama"]);

function resolveLlmCmd() {
  const rawCmd = process.env.AMAZON_SHOPPER_LLM_CMD || "claude --print";
  const parts = rawCmd.trim().split(/\s+/);
  const cmd = parts[0];
  if (process.env.AMAZON_SHOPPER_ALLOW_ANY_LLM_CMD !== "1" && !ALLOWED_LLM_CMDS.has(basename(cmd))) {
    throw new Error(
      `refusing to run '${cmd}' as an LLM CLI: not one of ${[...ALLOWED_LLM_CMDS].join(", ")}. ` +
      "Set AMAZON_SHOPPER_ALLOW_ANY_LLM_CMD=1 if you really mean it.",
    );
  }
  return { cmd, args: parts.slice(1) };
}

async function mockLLM(call_site) {
  const f = process.env.MOCK_LLM_RESPONSE_FILE;
  const raw = await readFile(f, "utf8");
  const map = JSON.parse(raw);
  if (!(call_site in map)) {
    throw new Error(`mock has no entry for call_site '${call_site}' (mock file: ${f})`);
  }
  return map[call_site];
}

function runCmd(cmd, args, stdinPayload) {
  return new Promise((resolve, reject) => {
    const child = spawn(cmd, args, { stdio: ["pipe", "pipe", "pipe"] });
    let out = "", err = "";
    child.stdout.on("data", d => out += d.toString());
    child.stderr.on("data", d => err += d.toString());
    child.on("error", reject);
    child.on("close", code => {
      if (code === 0) resolve(out);
      else reject(new Error(`${cmd} exited ${code}: ${err.slice(0, 500)}`));
    });
    if (stdinPayload) child.stdin.write(stdinPayload);
    child.stdin.end();
  });
}

async function gatewayLLM({ call_site, system, user }) {
  const params = JSON.stringify({
    system, user, response_format: "json", task_weight: "small",
    label: `amazon-shopper:${call_site}`,
  });
  const raw = await runCmd("openclaw", ["gateway", "call", "llm.completion", "--params", params]);
  const m = raw.match(/(\{[\s\S]*\})\s*$/);
  if (!m) throw new Error(`gateway llm.completion returned no JSON: ${raw.slice(0, 200)}`);
  const obj = JSON.parse(m[1]);
  const text = obj.content ?? obj.text ?? obj.response ?? obj.completion;
  if (!text) throw new Error(`gateway llm.completion: missing text field`);
  return JSON.parse(text);
}

async function subprocessLLM({ call_site, system, user }) {
  // AMAZON_SHOPPER_LLM_CMD may include args (split on whitespace).
  // Default: `claude --print` — works with stdin, returns clean JSON,
  // uses local Claude auth. To override: AMAZON_SHOPPER_LLM_CMD="oracle"
  // or AMAZON_SHOPPER_LLM_CMD="gemini -p".
  const { cmd, args } = resolveLlmCmd();
  const payload = `SYSTEM:\n${system}\n\nUSER:\n${user}\n\nReturn ONLY a single JSON object. No prose.`;
  const out = await runCmd(cmd, args, payload);
  const m = out.match(/\{[\s\S]*\}/);
  if (!m) throw new Error(`${cmd} returned no JSON: ${out.slice(0, 200)}`);
  return JSON.parse(m[0]);
}

export async function callLLM({ call_site, system, user, schema }) {
  if (process.env.MOCK_LLM_RESPONSE_FILE) {
    return await mockLLM(call_site);
  }
  try {
    return await gatewayLLM({ call_site, system, user });
  } catch (e) {
    process.stderr.write(`[llm] gateway failed (${e.message.slice(0, 100)}), falling back to subprocess\n`);
    return await subprocessLLM({ call_site, system, user });
  }
}

// callLLMVision — read structured data off a local image file. Uses the
// claude CLI's inline image-path support (verified 2026-05-29: `claude --print`
// with a "Path: /tmp/x.jpg" reference returns vision-derived JSON). Falls back
// to the same mock layer as callLLM for tests.
export async function callLLMVision({ call_site, prompt, imagePath }) {
  if (process.env.MOCK_LLM_RESPONSE_FILE) {
    return await mockLLM(call_site);
  }
  const { cmd, args } = resolveLlmCmd();
  const payload = `${prompt}\n\nImage file path: ${imagePath}\n\nReturn ONLY a single JSON object. No prose.`;
  const out = await runCmd(cmd, args, payload);
  const m = out.match(/\{[\s\S]*\}/);
  if (!m) throw new Error(`${cmd} (vision) returned no JSON: ${out.slice(0, 200)}`);
  return JSON.parse(m[0]);
}
