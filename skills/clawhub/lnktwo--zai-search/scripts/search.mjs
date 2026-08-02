#!/usr/bin/env node

// Z.AI Web Search — GLM-4.5-Flash with built-in web_search tool
// Free model + free live web search. No balance needed.
// Works with Z.AI Coding Plan API keys.

function usage() {
  console.error(`Usage: search.mjs "query" [-n 10] [--domain example.com] [--raw]`);
  console.error(`  -n N        Max results (default: 10, max: 20)`);
  console.error(`  --domain D  Filter to specific domain`);
  console.error(`  --raw       Skip GLM summarization`);
  process.exit(2);
}

const args = process.argv.slice(2);
if (args.length === 0 || args[0] === "-h" || args[0] === "--help") usage();

const query = args[0];
let n = 10;
let domainFilter = null;
let rawMode = false;

for (let i = 1; i < args.length; i++) {
  const a = args[i];
  if (a === "-n") {
    n = Math.max(1, Math.min(20, Number.parseInt(args[++i] ?? "10", 10)));
    continue;
  }
  if (a === "--domain") {
    domainFilter = args[++i] ?? null;
    continue;
  }
  if (a === "--raw") {
    rawMode = true;
    continue;
  }
  if (a === "--recency" || a === "--days") { ++i; continue; } // accepted but ignored
  console.error(`Unknown arg: ${a}`);
  usage();
}

const apiKey = (process.env.ZAI_API_KEY ?? process.env.Z_AI_API_KEY ?? "").trim();
if (!apiKey) {
  console.error("Missing ZAI_API_KEY (get one at https://chat.z.ai)");
  process.exit(1);
}

const baseUrl = process.env.ZAI_BASE_URL ?? "https://api.z.ai/api/coding/paas/v4";
const model = "glm-4.5-flash";

// ─── Build request ─────────────────────────────────────────────
const searchPrompt = rawMode
  ? `Search the web for: "${query}"${domainFilter ? ` (site:${domainFilter})` : ""}\n\nList up to ${n} results. For each: title, URL, and a one-line summary. Use this format:\n\n- **[Title]** URL\n  Summary\n\nRespond in the query's language.`
  : `Search the web for: "${query}"${domainFilter ? ` (site:${domainFilter})` : ""}\n\nProvide up to ${n} relevant results in this format:\n\n## Sources\n\n- **[Title]** URL\n  Brief factual summary (max 2 sentences)\n\nThen add a concise summary section.\n\nRules:\n- Only real URLs from search results — no fabrication\n- If nothing relevant found, say so honestly\n- Respond in the query's language`;

const body = {
  model,
  messages: [{ role: "user", content: searchPrompt }],
  tools: [{ type: "web_search", web_search: { enable: true, search_result: true } }],
  max_tokens: 2048,
  temperature: 0.1,
};

// ─── Execute ───────────────────────────────────────────────────
try {
  const resp = await fetch(`${baseUrl}/chat/completions`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${apiKey}`,
    },
    body: JSON.stringify(body),
  });

  if (!resp.ok) {
    const text = await resp.text().catch(() => "");
    throw new Error(`Z.AI search failed (${resp.status}): ${text}`);
  }

  const data = await resp.json();
  const choice = data.choices?.[0];
  const message = choice?.message ?? {};

  const content = (message.content ?? "").trim();
  if (content) {
    console.log(content);
  } else {
    console.log("## No results found\n");
  }

  // Extract reference URLs from web_search tool calls if present
  const toolCalls = message.tool_calls ?? [];
  const refs = [];
  for (const tc of toolCalls) {
    const results = tc.web_search ?? tc.search_result ?? [];
    if (Array.isArray(results)) {
      for (const r of results) {
        const link = r.link ?? r.url ?? r.href ?? "";
        const title = r.title ?? r.name ?? "";
        if (link) refs.push({ title, link });
      }
    }
  }

  if (refs.length > 0) {
    console.log("\n---\n## References\n");
    for (const r of refs.slice(0, n)) {
      console.log(`- [${r.title || r.link}](${r.link})`);
    }
  }
} catch (err) {
  console.error(`Search error: ${err.message}`);
  process.exit(1);
}
