#!/usr/bin/env node
/**
 * MoA Executor - Calls multiple reference models in parallel.
 *
 * Input  schema (version 1):  { version: "1", preset: {...}, conversation: "...", task_type?: "general" }
 * Output schema (version 1):  { version: "1", references: [...], quality_stats: {...}, elapsed_ms: N, usage: {...}, cost_usd: N|null }
 *
 * API keys are read from environment variables.
 */

const https = require("https");
const http = require("http");
const fs = require("fs");
const path = require("path");

// ── Concurrency limit ──────────────────────────────────────────────────────
const MAX_CONCURRENT_REFERENCES = 8;

// ── Token budget for reference model input ─────────────────────────────────
const REFERENCE_SAFETY_MARGIN_TOKENS = 4096;

// ── Per-provider context windows ───────────────────────────────────────────
const PROVIDER_CONTEXT_WINDOWS = {
  sensenova: {
    "deepseek-v4-flash": 1000000,
    "sensenova-6.7-flash-lite": 256000,
    "*": 256000,
  },
  nvidia: {
    "stepfun-ai/step-3.5-flash": 256000,
    "stepfun-ai/step-3.7-flash": 250000,
    "nvidia/nemotron-3-ultra-550b-a55b": 195000,
    "nvidia/llama-3.3-nemotron-super-49b-v1": 195000,
    "nvidia/nemotron-3-super-120b-a12b": 256000,
    "nvidia/z-ai/glm-5.1": 198000,
    "*": 128000,
  },
};

function getContextWindow(provider, model) {
  const pCfg = PROVIDER_CONTEXT_WINDOWS[provider];
  if (!pCfg) return 128000;
  return pCfg[model] || pCfg["*"] || 128000;
}

// ── Rough token counter ────────────────────────────────────────────────────
function estimateTokens(text) {
  let tokens = 0;
  for (let i = 0; i < text.length; i++) {
    const code = text.charCodeAt(i);
    if (code > 127) tokens += 1.5;
    else tokens += 0.3;
  }
  return Math.ceil(tokens);
}

function truncateConversation(conversation, provider, model, maxTokens, advisoryPrompt = ADVISORY_PROMPT) {
  const ctxWindow = getContextWindow(provider, model);
  const advisorPromptTokens = estimateTokens(advisoryPrompt);
  const availableForConversation = ctxWindow - advisorPromptTokens - REFERENCE_SAFETY_MARGIN_TOKENS - (maxTokens || 600);
  if (availableForConversation <= 0) return "";
  const convTokens = estimateTokens(conversation);
  if (convTokens <= availableForConversation) return conversation;
  const charBudget = Math.floor(availableForConversation * 3);
  const halfBudget = Math.floor(charBudget / 2);
  let prefixEnd = halfBudget;
  if (halfBudget > 20) {
    const nlPos = conversation.lastIndexOf('\n\n', halfBudget);
    if (nlPos > halfBudget * 0.5) prefixEnd = nlPos;
    else { const dotPos = conversation.lastIndexOf('. ', halfBudget); if (dotPos > halfBudget * 0.5) prefixEnd = dotPos + 1; }
  }
  let suffixStart = conversation.length - halfBudget;
  if (suffixStart > 20 && suffixStart < conversation.length) {
    const nlPos = conversation.indexOf('\n\n', suffixStart);
    if (nlPos > 0 && nlPos < conversation.length - 10) suffixStart = nlPos;
    else { const dotPos = conversation.indexOf('. ', suffixStart); if (dotPos > 0 && dotPos < conversation.length - 10) suffixStart = dotPos + 1; }
  }
  const prefix = conversation.slice(0, prefixEnd);
  const suffix = conversation.slice(suffixStart);
  return `${prefix}\n\n[... ${Math.floor((convTokens - availableForConversation))} tokens truncated ...]\n\n${suffix}`;
}

// ── Semaphore for concurrency control ──────────────────────────────────────
class Semaphore {
  constructor(max) { this.max = max; this.current = 0; this.queue = []; }
  async acquire() { if (this.current < this.max) { this.current++; return; } await new Promise((resolve) => this.queue.push(resolve)); this.current++; }
  release() { this.current--; if (this.queue.length > 0) { const next = this.queue.shift(); next(); } }
  async run(fn) { await this.acquire(); try { return await fn(); } finally { this.release(); } }
}
const refSemaphore = new Semaphore(MAX_CONCURRENT_REFERENCES);

// =============================================================================
// ===== MODEL PRICING =====
// =============================================================================

const MODEL_PRICING = {
  "gpt-5.5": { input: 0.015, output: 0.06, cacheRead: 0.0075 },
  "gpt-5.4-mini": { input: 0.003, output: 0.012, cacheRead: 0.0015 },
  "gpt-5.3-codex-spark": { input: 0.002, output: 0.008, cacheRead: 0.001 },
  "claude-opus-4-6": { input: 0.015, output: 0.075, cacheRead: 0.0015 },
  "claude-opus-4-8": { input: 0.015, output: 0.075, cacheRead: 0.0015 },
  "claude-sonnet-4": { input: 0.003, output: 0.015, cacheRead: 0.0003 },
  "claude-haiku-3-5": { input: 0.001, output: 0.005, cacheRead: 0.0001 },
  "gemini-3-pro-preview": { input: 0.005, output: 0.02, cacheRead: 0.0025 },
  "gemini-3-flash-preview": { input: 0.0005, output: 0.002, cacheRead: 0.00025 },
  "deepseek/deepseek-v4-pro": { input: 0.002, output: 0.008, cacheRead: 0.001 },
  "deepseek/deepseek-v4-flash": { input: 0.0005, output: 0.002, cacheRead: 0.00025 },
  "deepseek-v4-flash": { input: 0.0005, output: 0.002, cacheRead: 0.00025 },
  "sensenova/deepseek-v4-flash": { input: 0.0005, output: 0.002, cacheRead: 0.00025 },
  "sensenova/sensenova-6.7-flash-lite": { input: 0.0003, output: 0.001, cacheRead: 0.00015 },
  "openrouter/auto": { input: 0.002, output: 0.008, cacheRead: 0.001 },
  "nvidia/stepfun-ai/step-3.5-flash": { input: 0, output: 0, cacheRead: 0 },
  "nvidia/stepfun-ai/step-3.7-flash": { input: 0, output: 0, cacheRead: 0 },
  "nvidia/llama-3.3-nemotron-super-49b-v1": { input: 0, output: 0, cacheRead: 0 },
  "nvidia/nemotron-3-ultra-550b-a55b": { input: 0, output: 0, cacheRead: 0 },
  "grok-4": { input: 0.005, output: 0.02, cacheRead: 0.0025 },
  "grok-3": { input: 0.003, output: 0.015, cacheRead: 0.0015 },
  "together/meta-llama/Llama-3.3-70B-Instruct-Turbo": { input: 0.0009, output: 0.0009, cacheRead: 0 },
  "kimi-k2.6": { input: 0.002, output: 0.008, cacheRead: 0.001 },
  "kimi-k2.5": { input: 0.001, output: 0.004, cacheRead: 0.0005 },
  "agnes-2.0-flash": { input: 0.0005, output: 0.002, cacheRead: 0.00025 },
};

function estimateCost(model, usage) {
  const pricing = MODEL_PRICING[model];
  if (!pricing) return { cost_usd: null, source: "unknown" };
  const inputCost = (usage.input_tokens || 0) / 1000 * pricing.input;
  const outputCost = (usage.output_tokens || 0) / 1000 * pricing.output;
  const cacheReadCost = (usage.cache_read_tokens || 0) / 1000 * pricing.cacheRead;
  return { cost_usd: parseFloat((inputCost + outputCost - cacheReadCost).toFixed(6)), breakdown: { input: parseFloat(inputCost.toFixed(6)), output: parseFloat(outputCost.toFixed(6)), cache_saved: parseFloat(cacheReadCost.toFixed(6)) }, source: "pricing_table" };
}

// =============================================================================
// ===== PROVIDER ADAPTERS =====
// =============================================================================

const API_ENDPOINTS = {
  openai: { url: "https://api.openai.com/v1/chat/completions", envKey: "OPENAI_API_KEY", apiKeyInHeader: true, defaultTimeout: 30000, buildBody: (model, messages, maxTokens, temp) => ({ model, messages, max_tokens: maxTokens, temperature: temp }), parseResponse: (json) => { const m = json.choices?.[0]?.message; return m?.content || m?.reasoning || ""; }, parseUsage: (json) => { const u = json.usage; if (!u) return null; return { input_tokens: u.prompt_tokens||0, output_tokens: u.completion_tokens||0, total_tokens: u.total_tokens||0, cache_read_tokens: u.prompt_tokens_details?.cached_tokens||0, reasoning_tokens: u.completion_tokens_details?.reasoning_tokens||0 }; }, },
  anthropic: { url: "https://api.anthropic.com/v1/messages", envKey: "ANTHROPIC_API_KEY", apiKeyInHeader: true, defaultTimeout: 60000, headers: { "anthropic-version": "2023-06-01" }, buildBody: (model, messages, maxTokens, temp) => ({ model, max_tokens: maxTokens||1024, temperature: temp??0.7, messages: messages.filter(m=>m.role!=="system"), system: messages.find(m=>m.role==="system")?.content }), parseResponse: (json) => json.content?.map(c=>c.text).join("") || "", parseUsage: (json) => { const u=json.usage; if(!u)return null; return { input_tokens: u.input_tokens||0, output_tokens: u.output_tokens||0, total_tokens: (u.input_tokens||0)+(u.output_tokens||0), cache_read_tokens: u.cache_read_input_tokens||0, reasoning_tokens:0 }; }, },
  openrouter: { url: "https://openrouter.ai/api/v1/chat/completions", envKey: "OPENROUTER_API_KEY", apiKeyInHeader: true, defaultTimeout: 60000, headers: { "HTTP-Referer": "https://openclaw.ai", "X-Title": "OpenClaw MoA" }, buildBody: (model, messages, maxTokens, temp) => ({ model, messages, max_tokens: maxTokens, temperature: temp }), parseResponse: (json) => { const m=json.choices?.[0]?.message; return m?.content||m?.reasoning||""; }, parseUsage: (json) => { const u=json.usage; if(!u)return null; return { input_tokens: u.prompt_tokens||0, output_tokens: u.completion_tokens||0, total_tokens: u.total_tokens||0, cache_read_tokens: u.prompt_tokens_details?.cached_tokens||0, reasoning_tokens: u.completion_tokens_details?.reasoning_tokens||0 }; }, },
  deepseek: { url: "https://api.deepseek.com/v1/chat/completions", envKey: "DEEPSEEK_API_KEY", apiKeyInHeader: true, defaultTimeout: 30000, buildBody: (model, messages, maxTokens, temp) => ({ model, messages, max_tokens: maxTokens, temperature: temp }), parseResponse: (json) => { const m=json.choices?.[0]?.message; return m?.content||m?.reasoning||""; }, parseUsage: (json) => { const u=json.usage; if(!u)return null; return { input_tokens: u.prompt_tokens||0, output_tokens: u.completion_tokens||0, total_tokens: u.total_tokens||0, cache_read_tokens: u.prompt_tokens_details?.cached_tokens||0, reasoning_tokens: u.completion_tokens_details?.reasoning_tokens||0 }; }, },
  together: { url: "https://api.together.xyz/v1/chat/completions", envKey: "TOGETHER_API_KEY", apiKeyInHeader: true, defaultTimeout: 30000, buildBody: (model, messages, maxTokens, temp) => ({ model, messages, max_tokens: maxTokens, temperature: temp }), parseResponse: (json) => { const m=json.choices?.[0]?.message; return m?.content||m?.reasoning||""; }, parseUsage: (json) => { const u=json.usage; if(!u)return null; return { input_tokens: u.prompt_tokens||0, output_tokens: u.completion_tokens||0, total_tokens: u.total_tokens||0, cache_read_tokens: u.prompt_tokens_details?.cached_tokens||0, reasoning_tokens: u.completion_tokens_details?.reasoning_tokens||0 }; }, },
  xai: { url: "https://api.x.ai/v1/chat/completions", envKey: "XAI_API_KEY", apiKeyInHeader: true, defaultTimeout: 30000, buildBody: (model, messages, maxTokens, temp) => ({ model, messages, max_tokens: maxTokens, temperature: temp }), parseResponse: (json) => { const m=json.choices?.[0]?.message; return m?.content||m?.reasoning||""; }, parseUsage: (json) => { const u=json.usage; if(!u)return null; return { input_tokens: u.prompt_tokens||0, output_tokens: u.completion_tokens||0, total_tokens: u.total_tokens||0, cache_read_tokens: u.prompt_tokens_details?.cached_tokens||0, reasoning_tokens: u.completion_tokens_details?.reasoning_tokens||0 }; }, },
  google: { url: (model) => `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, envKey: "GEMINI_API_KEY", apiKeyInHeader: false, defaultTimeout: 30000, buildBody: (model, messages, maxTokens, temp) => { const contents = messages.filter(m=>m.role!=="system").map(m=>({role: m.role==="assistant"?"model":"user", parts:[{text:m.content}]})); const sm = messages.find(m=>m.role==="system"); const body={contents}; if(sm) body.system_instruction={parts:[{text:sm.content}]}; const gc={}; if(maxTokens) gc.maxOutputTokens=maxTokens; if(temp!==undefined) gc.temperature=temp; if(Object.keys(gc).length) body.generationConfig=gc; return body; }, parseResponse: (json) => json.candidates?.[0]?.content?.parts?.map(p=>p.text).join("")||"", parseUsage: (json) => { const u=json.usageMetadata; if(!u)return null; return { input_tokens: u.promptTokenCount||0, output_tokens: u.candidatesTokenCount||0, total_tokens: u.totalTokenCount||0, cache_read_tokens:0, reasoning_tokens:0 }; }, },
  moonshot: { url: "https://api.moonshot.cn/v1/chat/completions", envKey: "MOONSHOT_API_KEY", apiKeyInHeader: true, defaultTimeout: 30000, buildBody: (model, messages, maxTokens, temp) => ({ model, messages, max_tokens: maxTokens, temperature: temp }), parseResponse: (json) => { const m=json.choices?.[0]?.message; return m?.content||m?.reasoning||""; }, parseUsage: (json) => { const u=json.usage; if(!u)return null; return { input_tokens: u.prompt_tokens||0, output_tokens: u.completion_tokens||0, total_tokens: u.total_tokens||0, cache_read_tokens: u.prompt_tokens_details?.cached_tokens||0, reasoning_tokens: u.completion_tokens_details?.reasoning_tokens||0 }; }, },
  nvidia: { url: "https://integrate.api.nvidia.com/v1/chat/completions", envKey: "NVIDIA_API_KEY", apiKeyInHeader: true, defaultTimeout: 60000, buildBody: (model, messages, maxTokens, temp) => ({ model, messages, max_tokens: maxTokens, temperature: temp }), parseResponse: (json) => { const m=json.choices?.[0]?.message; return m?.content||m?.reasoning||""; }, parseUsage: (json) => { const u=json.usage; if(!u)return null; return { input_tokens: u.prompt_tokens||0, output_tokens: u.completion_tokens||0, total_tokens: u.total_tokens||0, cache_read_tokens:0, reasoning_tokens:0 }; }, },
  sensenova: { url: "https://token.sensenova.cn/v1/chat/completions", envKey: "SENSENOVA_API_KEY", apiKeyInHeader: true, defaultTimeout: 30000, buildBody: (model, messages, maxTokens, temp) => ({ model, messages, max_tokens: maxTokens, temperature: temp }), parseResponse: (json) => { const m=json.choices?.[0]?.message; return m?.content||m?.reasoning||""; }, parseUsage: (json) => { const u=json.usage; if(!u)return null; return { input_tokens: u.prompt_tokens||0, output_tokens: u.completion_tokens||0, total_tokens: u.total_tokens||0, cache_read_tokens:0, reasoning_tokens:0 }; }, },
  agnes: { url: "https://apihub.agnes-ai.com/v1/chat/completions", envKey: "AGNES_API_KEY", apiKeyInHeader: true, defaultTimeout: 30000, buildBody: (model, messages, maxTokens, temp) => ({ model, messages, max_tokens: maxTokens, temperature: temp }), parseResponse: (json) => { const m=json.choices?.[0]?.message; return m?.content||m?.reasoning||""; }, parseUsage: (json) => { const u=json.usage; if(!u)return null; return { input_tokens: u.prompt_tokens||0, output_tokens: u.completion_tokens||0, total_tokens: u.total_tokens||0, cache_read_tokens:0, reasoning_tokens:0 }; }, },
};

// =============================================================================
// ===== PROMPT MANAGEMENT =====
// =============================================================================

const ADVISORY_PROMPT = `You are a reference advisor in a Mixture of Agents (MoA) process. You are NOT the acting agent and you do NOT execute anything: you cannot call tools, run commands, browse, or access files, repositories, or URLs. A separate aggregator/orchestrator model holds those capabilities and will take the actual actions.

The conversation below is the current state of a task handled by that acting agent. Your job is to give your most intelligent analysis of that state: understand the goal, reason about the problem, and advise on what to do next. Surface the best approach, concrete next steps, likely pitfalls and risks, and anything the acting agent may have missed or gotten wrong.

Respond with your advice directly — no preamble, no disclaimers about tools or access. Your response is private guidance handed to the aggregator, not an answer shown to the user.`;

const TASK_PROMPTS = {
  coding: `You are a code reviewer in a Mixture of Agents process. You focus ONLY on finding bugs, issues, and problems in the code. Do NOT explain how the code works, do NOT suggest architectural improvements unless they cause bugs. Output format: list each issue with severity (critical/major/minor) and a concrete patch or fix. If no bugs are found, say "No issues found."`,
  architecture: `You are an architecture reviewer in a Mixture of Agents process. Focus on: scalability, boundary definitions, complexity, coupling, and maintainability. Identify concrete risks and tradeoffs. If the design is sound, confirm and explain why.`,
  writing: `You are an editor in a Mixture of Agents process. Focus on: clarity, logical flow, readability, and structure. Identify contradictions, missing logic, unclear phrasing. Suggest concrete rewrites for problematic sections.`,
};

function loadPrompt(taskType) {
  const p = path.join(__dirname, 'prompts', `${taskType}.md`);
  try { return fs.readFileSync(p, "utf8").trim(); } catch { return TASK_PROMPTS[taskType] || ADVISORY_PROMPT; }
}

// =============================================================================
// ===== QUALITY GATE // P1: Enhanced — catches refusals + low-quality signals =====
// =============================================================================

const QUALITY_REJECT_PATTERNS = [
  { pattern: /^\s*$/, reason: "empty_response" },
  { pattern: /^\s*\(empty response\)\s*$/i, reason: "empty_placeholder" },
  // English refusals
  { pattern: /i['']?m (sorry|unable|cannot|can['']?t|not able)/i, reason: "refusal" },
  { pattern: /(i|cannot|can['']?t) (assist|help with|answer|respond)/i, reason: "refusal" },
  { pattern: /sorry[,:] (i am|i'm|but i)/i, reason: "apology_refusal" },
  { pattern: /as an ai (assistant|language model)/i, reason: "generic_disclaimer" },
  { pattern: /i am an ai/i, reason: "generic_disclaimer" },
  { pattern: /i (do not|don't|cannot|can't) (have|access|see|view)/i, reason: "refusal" },
  { pattern: /unfortunately[,:]? i/i, reason: "apology_refusal" },
  // Chinese refusals
  { pattern: /抱[歉歉]/i, reason: "cn_apology" },
  { pattern: /[对很]不[起住]/i, reason: "cn_apology" },
  { pattern: /无法[回解]答/i, reason: "cn_refusal" },
  { pattern: /不能[回解]答/i, reason: "cn_refusal" },
  { pattern: /[无没]法完成/i, reason: "cn_refusal" },
  { pattern: /我不[知清]道/i, reason: "cn_refusal" },
  { pattern: /作为(一个)?(ai|人工智能)/i, reason: "cn_disclaimer" },
  { pattern: /我只是一个(ai|人工智能)/i, reason: "cn_disclaimer" },
  { pattern: /不在我的知识[范围库]/i, reason: "cn_unknowledge" },
  { pattern: /[暂目]无法[提处]供/i, reason: "cn_refusal" },
  { pattern: /(不好意思|很抱歉|非常抱歉)/i, reason: "cn_apology" },
  // API / system errors
  { pattern: /rate limit/i, reason: "rate_limit" },
  { pattern: /api (error|key|limit|timeout)/i, reason: "api_error" },
  { pattern: /too many requests/i, reason: "rate_limit" },
];

// P1: Low-quality signal detection
function detectRepetition(text) {
  const norm = text.toLowerCase().trim();
  const paragraphs = norm.split(/\n+/).filter(p => p.trim().length > 20);
  if (paragraphs.length < 2) return false;
  const seen = new Set(); let repeats = 0;
  for (const p of paragraphs) {
    const key = p.trim().substring(0, 40);
    if (seen.has(key)) repeats++; else seen.add(key);
    if (repeats >= 2) return true;
  }
  return false;
}

function detectHedgingDensity(text) {
  const hedgingWords = ['maybe', 'perhaps', 'probably', 'possibly', 'might', 'could', 'somewhat', 'i think', 'i believe', 'i guess', 'not sure', '不一定', '可能', '也许', '大概', '或许', '不确定', '不好说', '不太确定', '差不多'];
  let count = 0; const lower = text.toLowerCase();
  for (const hw of hedgingWords) {
    const regex = new RegExp(hw.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
    const matches = lower.match(regex);
    if (matches) count += matches.length;
  }
  const words = text.split(/\s+/).length;
  if (words < 20) return false;
  return count / words > 0.15;
}

// ── Unified decision function ───────────────────────────────────────────────

function shouldKeepReference(ref, context = {}) {
  if (ref.error) {
    return { keep: false, quality_class: "bad", reference_rank: 0, reason: "error", diagnostics: { error: true, error_message: (ref.error || "").substring(0, 200) } };
  }

  const output = (ref.output || "").trim();

  // 2. Hard reject: quality gate
  if (output.length < 50) {
    return { keep: false, quality_class: "bad", reference_rank: 0, reason: "too_short", diagnostics: { length: output.length, refusal: false, api_error: false, truncated: !!ref.truncated } };
  }
  for (const qr of QUALITY_REJECT_PATTERNS) {
    if (qr.pattern.test(output)) {
      return { keep: false, quality_class: "bad", reference_rank: 0, reason: qr.reason, diagnostics: { length: output.length, refusal: true, refusal_pattern: qr.reason, api_error: qr.reason.startsWith("api_") || qr.reason === "rate_limit", truncated: !!ref.truncated } };
    }
  }

  // P1: Low quality signals (not hard reject, but lower rank/class)
  let lowQualityPenalty = 0;
  if (detectRepetition(output)) lowQualityPenalty += 20;
  if (detectHedgingDensity(output)) lowQualityPenalty += 15;

  // 3. Quality classification
  let quality_class = "ok";
  let goodSignals = 0;
  if (output.length > 300) goodSignals++;
  if (ref.usage && ref.usage.output_tokens !== undefined && ref.usage.output_tokens > 100) goodSignals++;
  if (ref.latency_ms !== undefined && ref.latency_ms < 10000) goodSignals++;
  if (!ref.truncated) goodSignals++;
  if (lowQualityPenalty > 20) goodSignals = Math.max(0, goodSignals - 1);
  if (goodSignals >= 3) quality_class = "good";
  else if (lowQualityPenalty > 20) quality_class = "ok";  // penalized but not bad

  // 4. Reference rank
  let reference_rank = 50;
  reference_rank += Math.min(30, Math.floor(output.length / 20));
  if (ref.truncated) reference_rank -= 15;
  if (ref.usage && ref.usage.output_tokens !== undefined && ref.usage.output_tokens < 20) reference_rank -= 20;
  if (ref.usage && ref.usage.output_tokens !== undefined && ref.usage.output_tokens > 100) reference_rank += 10;
  if (ref.latency_ms !== undefined && ref.latency_ms < 5000) reference_rank += 5;
  reference_rank = Math.max(0, Math.min(100, reference_rank - lowQualityPenalty));

  return { keep: true, quality_class, reference_rank, reason: "ok", diagnostics: { length: output.length, refusal: false, api_error: false, truncated: !!ref.truncated, lowQualityPenalty } };
}

// =============================================================================
// ===== HTTP LAYER =====
// =============================================================================

function httpRequest(url, options, body) {
  return new Promise((resolve, reject) => {
    const mod = new URL(url).protocol === "https:" ? https : http;
    const req = mod.request(url, {
      method: "POST",
      headers: { "Content-Type": "application/json", ...options.headers, ...(options.apiKey && options.apiKeyInHeader !== false ? { Authorization: `Bearer ${options.apiKey}` } : {}) },
      timeout: options.timeout || 30000,
    }, (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => {
        try {
          if (res.statusCode >= 200 && res.statusCode < 300) {
            const parsed = JSON.parse(data);
            const usage = options.parseUsage ? options.parseUsage(parsed) : null;
            resolve({ data: parsed, usage });
          } else {
            reject({ statusCode: res.statusCode, statusText: res.statusMessage, body: data.slice(0, 500), retryable: res.statusCode === 429 || (res.statusCode >= 500 && res.statusCode < 600) });
          }
        } catch (e) { reject({ statusCode: -1, statusText: "ParseError", body: e.message, retryable: false }); }
      });
    });
    req.on("error", (err) => reject({ statusCode: -1, statusText: err.code, body: err.message, retryable: true }));
    req.on("timeout", () => { req.destroy(); reject({ statusCode: -1, statusText: "Timeout", body: "Request timed out", retryable: true }); });
    if (body) req.write(JSON.stringify(body));
    req.end();
  });
}

// =============================================================================
// ===== REFERENCE EXECUTION =====
// =============================================================================

async function callReference(provider, model, conversation, maxTokens, temperature, timeoutSeconds, advisoryPrompt = ADVISORY_PROMPT) {
  const endpoint = API_ENDPOINTS[provider];
  if (!endpoint) return { provider, model, error: `Unknown provider: ${provider}` };

  const apiKey = process.env[endpoint.envKey];
  if (!apiKey) return { provider, model, error: `Missing ${endpoint.envKey} environment variable` };

  const truncatedConv = truncateConversation(conversation, provider, model, maxTokens, advisoryPrompt);
  const messages = [{ role: "system", content: advisoryPrompt }, { role: "user", content: truncatedConv }];
  const body = endpoint.buildBody(model, messages, maxTokens || 600, temperature ?? 0.7);
  const baseUrl = typeof endpoint.url === "function" ? endpoint.url(model) : endpoint.url;
  let url = baseUrl;
  let bearerToken = apiKey;
  if (!endpoint.apiKeyInHeader) { url = `${baseUrl}?key=***)}`; bearerToken = null; }

  const timeoutMs = (timeoutSeconds || 0) * 1000 || endpoint.defaultTimeout || 30000;
  let lastError = null;
  const maxRetries = 2;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const { data, usage } = await httpRequest(url, { headers: endpoint.headers, apiKey: bearerToken, apiKeyInHeader: endpoint.apiKeyInHeader, parseUsage: endpoint.parseUsage, timeout: timeoutMs }, body);
      const output = endpoint.parseResponse(data) || "(empty response)";
      const cost = usage ? estimateCost(model, usage) : { cost_usd: null, source: "no_usage" };
      return { provider, model, output, usage, cost, truncated: truncatedConv !== conversation };
    } catch (err) {
      lastError = err;
      if (err.retryable && attempt < maxRetries) await new Promise((r) => setTimeout(r, attempt * 1000));
    }
  }
  return { provider, model, error: `After ${maxRetries} attempts: ${lastError.statusText} (${lastError.statusCode}) — ${lastError.body}` };
}

// =============================================================================
// ===== HEALTH CHECK =====
// =============================================================================

async function runHealthCheck(input) {
  const results = { version: "1", mode: "health", timestamp: new Date().toISOString(), checks: [], summary: { passed: 0, failed: 0, total: 0 } };
  const providers = [
    { name: "SenseNova", envKey: "SENSENOVA_API_KEY", endpoint: "https://token.sensenova.cn/v1/chat/completions" },
    { name: "NVIDIA", envKey: "NVIDIA_API_KEY", endpoint: "https://integrate.api.nvidia.com/v1/chat/completions" },
    { name: "DeepSeek", envKey: "DEEPSEEK_API_KEY", endpoint: "https://api.deepseek.com/v1/chat/completions" },
    { name: "Agnes", envKey: "AGNES_API_KEY", endpoint: "https://apihub.agnes-ai.com/v1/chat/completions" },
    { name: "OpenAI", envKey: "OPENAI_API_KEY", endpoint: "https://api.openai.com/v1/models" },
    { name: "Anthropic", envKey: "ANTHROPIC_API_KEY", endpoint: "https://api.anthropic.com/v1/messages" },
    { name: "Google Gemini", envKey: "GEMINI_API_KEY", endpoint: "https://generativelanguage.googleapis.com/v1beta/models" },
    { name: "xAI", envKey: "XAI_API_KEY", endpoint: "https://api.x.ai/v1/chat/completions" },
    { name: "OpenRouter", envKey: "OPENROUTER_API_KEY", endpoint: "https://openrouter.ai/api/v1/chat/completions" },
    { name: "Together", envKey: "TOGETHER_API_KEY", endpoint: "https://api.together.xyz/v1/chat/completions" },
    { name: "Moonshot", envKey: "MOONSHOT_API_KEY", endpoint: "https://api.moonshot.cn/v1/chat/completions" },
  ];

  for (const p of providers) {
    const key = process.env[p.envKey];
    const check = { provider: p.name, envKey: p.envKey, keyPresent: !!key, keyLength: key ? key.length : 0, endpointReachable: false, endpointLatencyMs: null, error: null };
    if (key) {
      const start = Date.now();
      try {
        await new Promise((resolve, reject) => {
          const mod = p.endpoint.startsWith('https') ? https : http;
          const req = mod.get(p.endpoint, { timeout: 5000 }, (res) => resolve());
          req.on('error', (err) => reject(err));
          req.on('timeout', () => { req.destroy(); reject(new Error('timeout')); });
        });
        check.endpointReachable = true;
        check.endpointLatencyMs = Date.now() - start;
      } catch (err) { check.endpointReachable = false; check.error = err.message || 'unknown'; check.endpointLatencyMs = Date.now() - start; }
    }
    check.status = check.keyPresent && check.endpointReachable ? 'passed' : 'failed';
    results.checks.push(check);
    if (check.status === 'passed') results.summary.passed++; else results.summary.failed++;
    results.summary.total++;
  }

  const promptTypes = ['general', 'coding', 'architecture', 'writing'];
  for (const pt of promptTypes) {
    const fpath = path.join(__dirname, 'prompts', `${pt}.md`);
    try { const content = fs.readFileSync(fpath, 'utf8'); results.checks.push({ provider: 'prompts', file: `prompts/${pt}.md`, status: 'passed', size: content.length }); results.summary.passed++; results.summary.total++; }
    catch (err) { results.checks.push({ provider: 'prompts', file: `prompts/${pt}.md`, status: 'failed', error: err.message }); results.summary.failed++; results.summary.total++; }
  }

  try {
    const presetPath = path.join(__dirname, 'presets.default.yaml');
    const content = fs.readFileSync(presetPath, 'utf8');
    results.checks.push({ provider: 'config', file: 'presets.default.yaml', status: 'passed', size: content.length });
    results.summary.passed++; results.summary.total++;
  } catch (err) { results.checks.push({ provider: 'config', file: 'presets.default.yaml', status: 'failed', error: err.message }); results.summary.failed++; results.summary.total++; }

  return results;
}

// =============================================================================
// ===== MAIN PIPELINE =====
// =============================================================================

function sentenceDedup(references, threshold) {
  if (references.length < 2) return references;
  function normalizeText(t) { return t.toLowerCase().replace(/[^\w\u4e00-\u9fff]/g, ' ').replace(/\s+/g, ' ').trim(); }
  function overlap(a, b) {
    const normA = normalizeText(a.output || ''); const normB = normalizeText(b.output || '');
    if (normA.length < 50 || normB.length < 50) return 0;
    const sentsA = new Set(normA.split(/[。\n]+/).filter(s => s.trim().length > 10).map(s => s.trim()));
    const sentsB = new Set(normB.split(/[。\n]+/).filter(s => s.trim().length > 10).map(s => s.trim()));
    if (sentsB.size === 0) return 0;
    let ov = 0; for (const s of sentsB) { if (sentsA.has(s)) ov++; }
    return ov / sentsB.size;
  }
  const deduped = [references[0]];
  for (let i = 1; i < references.length; i++) {
    let isDup = false;
    for (const kept of deduped) { if (overlap(kept, references[i]) > threshold) { isDup = true; break; } }
    if (!isDup) deduped.push(references[i]);
  }
  return deduped.length >= 2 ? deduped : references;
}

// P4: Custom presets — merge env var + input JSON overrides into default preset
function resolvePresets(inputPreset, inputPresetName) {
  let finalPreset = JSON.parse(JSON.stringify(inputPreset)); // deep clone

  // P4: Try env var custom presets
  try {
    const envPresets = process.env.MOA_CUSTOM_PRESETS;
    if (envPresets) {
      const parsed = JSON.parse(envPresets);
      if (inputPresetName && parsed[inputPresetName]) {
        // Merge custom preset into the current preset
        const custom = parsed[inputPresetName];
        if (custom.reference_models) finalPreset.reference_models = custom.reference_models;
        if (custom.reference_max_tokens) finalPreset.reference_max_tokens = custom.reference_max_tokens;
        // Merge aggregation config
        if (custom.aggregation) {
          finalPreset.aggregation = { ...(finalPreset.aggregation || {}), ...custom.aggregation };
        }
      }
    }
  } catch {}

  // P4: Also try input-level custom_presets
  return finalPreset;
}

async function main() {
  const chunks = [];
  for await (const chunk of process.stdin) chunks.push(chunk);
  const input = JSON.parse(chunks.join(""));

  if (input.mode === 'health') {
    const results = await runHealthCheck(input);
    process.stdout.write(JSON.stringify(results, null, 2));
    return;
  }

  const { preset: rawPreset, conversation, presetName, max_tokens, custom_presets } = input;
  if (!rawPreset || !conversation) {
    console.error(JSON.stringify({ error: "Missing preset or conversation in input" }));
    process.exit(1);
  }

  // P4: Merge custom presets from input
  const preset = resolvePresets(rawPreset, presetName);
  if (custom_presets && presetName && custom_presets[presetName]) {
    const cp = custom_presets[presetName];
    if (cp.reference_models) preset.reference_models = cp.reference_models;
    if (cp.reference_max_tokens) preset.reference_max_tokens = cp.reference_max_tokens;
    if (cp.aggregation) preset.aggregation = { ...(preset.aggregation || {}), ...cp.aggregation };
  }

  const refs = preset.reference_models || [];
  if (refs.length === 0) {
    console.error(JSON.stringify({ error: "No reference models configured" }));
    process.exit(1);
  }

  let maxTokens = preset.reference_max_tokens;
  if (max_tokens && typeof max_tokens === 'number') maxTokens = max_tokens;

  const temperature = preset.reference_temperature;
  const timeoutSeconds = preset.timeout_seconds;
  const totalTimeoutMs = (preset.total_timeout_seconds || 120) * 1000;
  const taskType = preset.task_type || "general";
  const advisoryPrompt = TASK_PROMPTS[taskType] || ADVISORY_PROMPT;

  // P2: Read aggregation config from preset
  const aggConfig = preset.aggregation || {};
  const dedupEnabled = aggConfig.dedup_enabled !== false;
  const dedupThreshold = typeof aggConfig.dedup_threshold === 'number' ? aggConfig.dedup_threshold : 0.6;

  // P3: Resolve model names (env overrides)
  let resolvedRefs;
  try {
    const modelMap = process.env.MOA_MODEL_MAP ? JSON.parse(process.env.MOA_MODEL_MAP) : {};
    resolvedRefs = refs.map((ref, idx) => {
      const presetKey = (presetName || '').toUpperCase().replace(/[^A-Z0-9_]/g, '_');
      const envOverride = process.env[`MOA_MODEL_${presetKey}_${idx}`];
      if (envOverride) return { ...ref, model: envOverride };
      const fullKey = `${ref.provider}/${ref.model}`;
      if (modelMap[fullKey]) return { ...ref, model: modelMap[fullKey] };
      if (modelMap[ref.model]) return { ...ref, model: modelMap[ref.model] };
      return ref;
    });
  } catch { resolvedRefs = refs; }

  // Call all reference models in parallel
  const start = Date.now();
  const rawResults = await Promise.race([
    Promise.all(resolvedRefs.map((ref) =>
      refSemaphore.run(async () => {
        const refStart = Date.now();
        const result = await callReference(ref.provider, ref.model, conversation, maxTokens, temperature, ref.timeout_seconds || timeoutSeconds, advisoryPrompt);
        result.latency_ms = Date.now() - refStart;
        return result;
      })
    )),
    new Promise((_, reject) => setTimeout(() => reject({ statusCode: -1, statusText: "TotalTimeout", body: `Exceeded total timeout of ${totalTimeoutMs}ms` }), totalTimeoutMs)),
  ]);
  const elapsed = Date.now() - start;

  // P3: Error isolation — separate successful and failed references
  const succeededRefs = [];
  const failedRefs = [];
  let qualityStats = { passed: 0, rejected: 0, rejections: {} };
  const context = { taskType, preset };

  for (const ref of rawResults) {
    if (ref.error) {
      // P3: Don't discard — track as failed but don't crash
      ref.reference_rank = 0;
      ref.quality_class = "bad";
      ref.quality_gate = { passed: false, reason: "error", diagnostics: { error: true, error_message: ref.error.substring(0, 200) } };
      failedRefs.push(ref);
      qualityStats.rejected++;
      qualityStats.rejections["error"] = (qualityStats.rejections["error"] || 0) + 1;
      continue;
    }
    const decision = shouldKeepReference(ref, context);
    ref.reference_rank = decision.reference_rank;
    ref.quality_class = decision.quality_class;
    ref.quality_gate = { passed: decision.keep, reason: decision.reason, diagnostics: decision.diagnostics };
    if (decision.keep) {
      succeededRefs.push(ref);
      qualityStats.passed++;
    } else {
      failedRefs.push(ref);
      qualityStats.rejected++;
      qualityStats.rejections[decision.reason] = (qualityStats.rejections[decision.reason] || 0) + 1;
    }
  }

  // If ALL quality gate rejected, fall back
  let keptResults = succeededRefs;
  if (keptResults.length === 0 && rawResults.length > 0) {
    // Use failed refs that have output (not errors)
    keptResults = rawResults.filter(r => !r.error).map(ref => { ref.reference_rank = 50; ref.quality_class = "ok"; ref.quality_gate = { passed: true, reason: "fallback_all_rejected" }; return ref; });
    if (keptResults.length === 0) {
      // If even those are empty, use raw results as-is
      keptResults = rawResults.map(ref => { ref.reference_rank = 50; ref.quality_class = "ok"; ref.quality_gate = { passed: true, reason: "fallback_all_rejected" }; return ref; });
    }
  }

  // Sort by reference_rank descending
  keptResults.sort((a, b) => (b.reference_rank || 0) - (a.reference_rank || 0));
  const keepCount = preset.keep_top_k || keptResults.length;
  let finalReferences = keptResults.slice(0, keepCount);

  // P3: Apply dedup (configurable via aggregation config)
  if (dedupEnabled && finalReferences.length >= 3) {
    finalReferences = sentenceDedup(finalReferences, dedupThreshold);
  }

  // Aggregate usage and cost
  const totalUsage = { input_tokens: 0, output_tokens: 0, total_tokens: 0, cache_read_tokens: 0, reasoning_tokens: 0 };
  let totalCost = null;
  for (const ref of finalReferences) {
    if (!ref.error && ref.usage) {
      totalUsage.input_tokens += ref.usage.input_tokens || 0;
      totalUsage.output_tokens += ref.usage.output_tokens || 0;
      totalUsage.total_tokens += ref.usage.total_tokens || 0;
      totalUsage.cache_read_tokens += ref.usage.cache_read_tokens || 0;
      totalUsage.reasoning_tokens += ref.usage.reasoning_tokens || 0;
    }
    if (ref.cost && ref.cost.cost_usd !== null) { if (totalCost === null) totalCost = 0; totalCost += ref.cost.cost_usd; }
  }

  const output = {
    version: "1",
    references: finalReferences,
    failed_references: failedRefs.length > 0 ? failedRefs.length : undefined,
    quality_stats: qualityStats,
    elapsed_ms: elapsed,
    usage: totalUsage,
    cost_usd: totalCost !== null ? parseFloat(totalCost.toFixed(6)) : null,
  };
  process.stdout.write(JSON.stringify(output));
}

main().catch((err) => {
  console.error(JSON.stringify({ error: err.message }));
  process.exit(1);
});