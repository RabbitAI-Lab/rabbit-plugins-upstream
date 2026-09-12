/**
 * ChatGPT Conversation Exporter — browser-relay path (recommended)
 *
 * Fetches conversations from ChatGPT's internal API through an attached browser relay,
 * using the session your browser already holds. It reads no token, no cookie jar and no
 * credential file: every request runs inside the page with `credentials: 'include'`.
 *
 * WRITES TO DISK: index.json, summary.md, and (unless indexOnly) one .json and one .md per
 * conversation containing full message text. The output directory is created mode 0700 and
 * every file mode 0600. Nothing is uploaded anywhere.
 *
 * CONSENT: exportChatGPTConversations() refuses to run unless the caller passes
 * `confirmed: true`. An agent must ask the user first — this is the gate that stops a
 * skill install from turning into an unattended dump of someone's chat history.
 *
 * OFF SWITCH: set CHATGPT_EXPORT_DISABLE=1 or create ~/.openclaw/chatgpt-export.disabled
 * and the function throws before any fetch or write.
 *
 * Usage: called from agent context. See SKILL.md.
 */

import { writeFileSync, mkdirSync, existsSync, realpathSync, chmodSync, lstatSync } from "fs";
import { join, resolve, sep, dirname } from "path";
import { homedir } from "os";

// Configuration
const CHATGPT_BASE = "https://chatgpt.com";
const API_BASE = `${CHATGPT_BASE}/backend-api`;
const DELAY_MS = 500; // Delay between requests to avoid rate limiting

/**
 * A dedicated private directory, deliberately NOT ~/chatgpt-export: sync clients and backup
 * tools tend to watch the top of the home directory, and an export is a plaintext copy of
 * everything the user has ever typed into ChatGPT.
 */
const EXPORT_ROOT = join(homedir(), ".local", "share", "chatgpt-export");

/**
 * The ownership marker. scripts/export.sh --purge deletes nothing that does not carry this
 * file, so the relay writes it too — otherwise exports made here could not be cleaned up by
 * the supported delete path.
 */
const MANIFEST_NAME = ".chatgpt-export-manifest.json";
const MANIFEST_FORMAT = "chatgpt-export-manifest/1";

/**
 * Best-effort redaction of the fixed-shape credentials people paste into chats. This is a
 * safety net, not a guarantee: it cannot recognise a secret that has no recognisable shape.
 */
const REDACTIONS: Array<[RegExp, string]> = [
  [/sk-[A-Za-z0-9_-]{16,}/g, "[REDACTED:openai-key]"],
  [/gh[pousr]_[A-Za-z0-9]{16,}/g, "[REDACTED:github-token]"],
  [/AKIA[0-9A-Z]{16}/g, "[REDACTED:aws-key-id]"],
  [/AIza[0-9A-Za-z_-]{30,}/g, "[REDACTED:google-key]"],
  [/xox[baprs]-[A-Za-z0-9-]{10,}/g, "[REDACTED:slack-token]"],
  [/eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{5,}/g, "[REDACTED:jwt]"],
  [/-----BEGIN [A-Z ]*PRIVATE KEY-----/g, "[REDACTED:private-key-header]"],
  [/(Bearer |bearer )[A-Za-z0-9._-]{20,}/g, "$1[REDACTED:bearer]"],
];

export function redact(text: string, enabled: boolean): string {
  if (!enabled) return text;
  let out = text;
  for (const [pattern, replacement] of REDACTIONS) out = out.replace(pattern, replacement);
  return out;
}

/**
 * Destination allowlisting. Writing an export into a folder a sync client is watching hands a
 * plaintext copy of the user's whole history to a cloud they were not thinking about, so a
 * destination that looks synced, sits inside a git repo, or leaves the home directory is
 * refused unless the caller explicitly overrides it.
 */
const SYNC_MARKERS = [
  "Dropbox",
  "Google Drive",
  "GoogleDrive",
  "OneDrive",
  "iCloud",
  "Mobile Documents",
  "Nextcloud",
  "ownCloud",
  "Syncthing",
  "pCloud",
  "MEGA",
  "Yandex.Disk",
];

/**
 * Write a file that is readable only by this user.
 *
 * writeFileSync's `mode` is applied ONLY when the file is created. Writing over a file that
 * already exists — a re-run into the same export directory is the ordinary case — kept whatever
 * mode the old file had, so a 0644 leftover stayed world-readable while holding conversation
 * text. chmod after the write makes 0600 true on every path, not just the first one.
 */
function writePrivate(path: string, contents: string): void {
  writeFileSync(path, contents, { mode: 0o600 });
  chmodSync(path, 0o600);
}

export function destinationObjection(dir: string): string | null {
  const abs = resolve(dir);

  // CANONICALIZE FIRST, THEN JUDGE (fixed 1.9.1). The sync-marker test used to run against the
  // path as written, which meant ~/notsynced passed while being a symlink to ~/Dropbox: the
  // string carries no marker, so the export went to a cloud folder anyway. Every test below now
  // runs on the resolved path. The destination usually does not exist yet, so resolve the
  // deepest ancestor that DOES exist and re-attach the tail — the symlink is always in the part
  // that exists.
  let existing = abs;
  while (!existsSync(existing) && dirname(existing) !== existing) existing = dirname(existing);
  let canonical: string;
  try {
    canonical =
      abs === existing ? realpathSync(abs) : join(realpathSync(existing), abs.slice(existing.length + 1));
  } catch {
    return "its path could not be resolved";
  }
  let home: string;
  try {
    home = realpathSync(homedir());
  } catch {
    return "your home directory could not be resolved";
  }

  for (const marker of SYNC_MARKERS) {
    if (canonical.includes(marker) || abs.includes(marker)) {
      return `it resolves to what looks like a synced folder (${marker})`;
    }
  }
  if (canonical === home) {
    return "it resolves to your home directory itself";
  }
  if (!canonical.startsWith(home + sep)) {
    return `it resolves to a location outside your home directory (${canonical})`;
  }
  let probe = canonical;
  while (probe.startsWith(home + sep)) {
    if (existsSync(join(probe, ".git"))) {
      return `it resolves to a path inside a git repository (${probe})`;
    }
    probe = dirname(probe);
  }
  return null;
}

interface ConversationItem {
  id: string;
  title: string;
  create_time: number;
  update_time: number;
}

interface ConversationResponse {
  items: ConversationItem[];
  total: number;
  limit: number;
  offset: number;
}

interface MessageContent {
  content_type: string;
  parts?: string[];
}

interface Message {
  id: string;
  author: { role: string };
  content: MessageContent;
  create_time?: number;
}

interface MappingNode {
  id: string;
  message?: Message;
  parent?: string;
  children?: string[];
}

interface FullConversation {
  id: string;
  title: string;
  create_time: number;
  update_time: number;
  mapping: Record<string, MappingNode>;
  current_node: string;
}

// JavaScript to execute in browser context
const FETCH_CONVERSATIONS_JS = `
(async () => {
  const results = [];
  let offset = 0;
  const limit = 100;
  
  while (true) {
    const response = await fetch(
      'https://chatgpt.com/backend-api/conversations?offset=' + offset + '&limit=' + limit,
      { credentials: 'include' }
    );
    
    if (!response.ok) {
      throw new Error('Failed to fetch: ' + response.status);
    }
    
    const data = await response.json();
    results.push(...data.items);
    
    if (data.items.length < limit) {
      break;
    }
    offset += limit;
    
    // Small delay to be nice
    await new Promise(r => setTimeout(r, 200));
  }
  
  return JSON.stringify({ items: results, total: results.length });
})()
`;

function assertConversationId(id: string): string {
  if (typeof id !== "string" || !id) throw new Error("Missing conversation id");
  if (id.length > 128) throw new Error("Conversation id too long");
  if (!/^[A-Za-z0-9_-]+$/.test(id)) throw new Error("Conversation id contains disallowed characters");
  return id;
}

const createFetchConversationJS = (id: string) => {
  const safeId = assertConversationId(id);
  return `
(async () => {
  const response = await fetch(
    'https://chatgpt.com/backend-api/conversation/${safeId}',
    { credentials: 'include' }
  );
  
  if (!response.ok) {
    throw new Error('Failed to fetch conversation: ' + response.status);
  }
  
  return JSON.stringify(await response.json());
})()
`;
};

function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "")
    .slice(0, 50);
}

function extractMessages(
  conversation: FullConversation,
): Array<{ role: string; content: string; timestamp?: number }> {
  const messages: Array<{ role: string; content: string; timestamp?: number }> = [];
  const mapping = conversation.mapping;

  // Find root node (no parent)
  let currentId = Object.keys(mapping).find((id) => !mapping[id].parent);
  if (!currentId) return messages;

  // Walk the tree following children
  const visited = new Set<string>();
  const queue = [currentId];

  while (queue.length > 0) {
    const nodeId = queue.shift()!;
    if (visited.has(nodeId)) continue;
    visited.add(nodeId);

    const node = mapping[nodeId];
    if (node?.message?.content?.parts && node.message.author.role !== "system") {
      const content = node.message.content.parts.join("\n");
      if (content.trim()) {
        messages.push({
          role: node.message.author.role,
          content,
          timestamp: node.message.create_time,
        });
      }
    }

    // Add children to queue
    if (node?.children) {
      queue.push(...node.children);
    }
  }

  return messages;
}

function conversationToMarkdown(conversation: FullConversation): string {
  const messages = extractMessages(conversation);
  const date = new Date(conversation.create_time * 1000).toISOString().split("T")[0];

  let md = `# ${conversation.title || "Untitled Conversation"}\n\n`;
  md += `**Date:** ${date}\n`;
  md += `**ID:** ${conversation.id}\n\n`;
  md += `---\n\n`;

  for (const msg of messages) {
    const roleLabel = msg.role === "user" ? "**You:**" : "**ChatGPT:**";
    md += `${roleLabel}\n\n${msg.content}\n\n---\n\n`;
  }

  return md;
}

// Main export function - designed to be called from agent context
export async function exportChatGPTConversations(options: {
  browserEvaluate: (js: string) => Promise<string>;
  /** Explicit user consent. Without `true` this function refuses to run. */
  confirmed?: boolean;
  outputDir?: string;
  format?: "json" | "md" | "both";
  limit?: number;
  /** Write only the conversation index — no message bodies are fetched or saved. */
  indexOnly?: boolean;
  /** Best-effort scrub of common secret formats before anything is written. */
  redact?: boolean;
  /** Days until this export is considered expired by `export.sh --purge-expired`. */
  expireDays?: number;
  onProgress?: (current: number, total: number, title: string) => void;
}): Promise<{ exported: number; outputDir: string; errors: string[] }> {
  const {
    browserEvaluate,
    confirmed = false,
    outputDir = join(EXPORT_ROOT, new Date().toISOString().split("T")[0]),
    format = "both",
    limit,
    indexOnly = true,
    redact: redactSecrets = false,
    expireDays = 30,
    onProgress,
  } = options;

  // Off switch — checked before any network call or file write.
  if (
    process.env.CHATGPT_EXPORT_DISABLE === "1" ||
    existsSync(join(homedir(), ".openclaw", "chatgpt-export.disabled"))
  ) {
    throw new Error(
      "ChatGPT export is disabled on this machine " +
        "(CHATGPT_EXPORT_DISABLE=1 or ~/.openclaw/chatgpt-export.disabled). Nothing was fetched.",
    );
  }

  // Consent gate — the caller must have asked the user, and say so. The message is structured
  // on purpose: an agent that relays it has already told the user the destination and the exact
  // scope, which is the confirmation step this skill is required to perform before any fetch.
  if (!confirmed) {
    throw new Error(
      "Refusing to export without explicit consent. Show the user these exact terms and get a " +
        "yes, then call again with { confirmed: true }:\n" +
        `  Destination : ${outputDir} (created mode 0700, files 0600)\n` +
        `  Scope       : ${indexOnly ? "INDEX ONLY — titles, ids, timestamps. No message text is fetched." : "FULL CONTENT — the complete text of every message, both sides."}\n` +
        `  Cap         : ${limit ? `the ${limit} most recent conversations` : "none — every conversation in the account"}\n` +
        `  Redaction   : ${redactSecrets ? "on (best-effort)" : "off"}\n` +
        "  Network     : chatgpt.com only. No upload, no telemetry, no third party.\n" +
        "  Sensitivity : the export may contain credentials, health, legal, financial or " +
        "work-confidential material.\n" +
        "Use { indexOnly: true } to export titles and timestamps only.",
    );
  }

  // Destination allowlisting, before anything is fetched or written. This is unconditional:
  // the allowUnsafeDest override was removed in 1.9.1. An escape hatch that lets a plaintext
  // copy of an entire chat history be written into a synced folder or a git repo is not a
  // guardrail, and documenting it did not make it one.
  const objection = destinationObjection(outputDir);
  if (objection) {
    throw new Error(
      `Refusing to export to ${outputDir} — ${objection}. Pick a local, non-synced ` +
        "directory inside your home and outside any git repository.",
    );
  }

  const errors: string[] = [];

  // Create output directories, readable only by this user.
  //
  // mkdirSync's `mode` applies ONLY when the directory is actually created; reusing a directory
  // that already exists at 0755 silently kept it world-readable while the caller had been told
  // 0700. chmod after the fact so the mode is enforced on reuse as well as on creation. The
  // same applies to writeFileSync's mode, which is why every write below is followed by chmod.
  mkdirSync(outputDir, { recursive: true, mode: 0o700 });
  chmodSync(outputDir, 0o700);

  // Re-verify AFTER creation. Between the check above and this point the path could have been
  // swapped for a symlink; resolving it again and re-running the objection closes that window,
  // and refusing a symlinked leaf means we never write through one.
  if (lstatSync(outputDir).isSymbolicLink()) {
    throw new Error(
      `Refusing to export to ${outputDir} — the destination itself is a symbolic link.`,
    );
  }
  const settledDir = realpathSync(outputDir);
  const settledObjection = destinationObjection(settledDir);
  if (settledObjection) {
    throw new Error(
      `Refusing to export to ${outputDir} — after creation it resolves to ${settledDir}, ` +
        `which is unacceptable: ${settledObjection}.`,
    );
  }

  mkdirSync(join(outputDir, "conversations"), { recursive: true, mode: 0o700 });
  chmodSync(join(outputDir, "conversations"), 0o700);

  // Ownership marker + expiry, so `export.sh --purge` / `--purge-expired` will accept this
  // directory later. Without it the delete path refuses to touch these files, by design.
  const nowEpoch = Math.floor(Date.now() / 1000);
  writePrivate(
    join(outputDir, MANIFEST_NAME),
    JSON.stringify(
      {
        format: MANIFEST_FORMAT,
        tool: "chatgpt-exporter-ultimate",
        created_at_epoch: nowEpoch,
        expires_at_epoch: nowEpoch + expireDays * 86400,
        expire_days: expireDays,
        index_only: indexOnly,
        redacted: redactSecrets,
      },
      null,
      2,
    ),
  );

  // Fetch conversation list
  console.log("Fetching conversation list...");
  const listResult = await browserEvaluate(FETCH_CONVERSATIONS_JS);
  const { items } = JSON.parse(listResult) as { items: ConversationItem[] };

  console.log(`Found ${items.length} conversations`);

  // Save index
  writePrivate(
    join(outputDir, "index.json"),
    redact(JSON.stringify(items, null, 2), redactSecrets),
  );

  if (indexOnly) {
    console.log("indexOnly: skipping message bodies. Only index.json was written.");
    console.log(`Delete it when done:  ./scripts/export.sh --purge -o "${outputDir}"`);
    return { exported: 0, outputDir, errors };
  }

  // Fetch each conversation
  const toFetch = limit ? items.slice(0, limit) : items;
  let exported = 0;

  for (let i = 0; i < toFetch.length; i++) {
    const item = toFetch[i];
    const slug = slugify(item.title || "untitled");

    onProgress?.(i + 1, toFetch.length, item.title || "Untitled");

    try {
      const convResult = await browserEvaluate(createFetchConversationJS(item.id));
      const conversation = JSON.parse(convResult) as FullConversation;

      // Save JSON
      if (format === "json" || format === "both") {
        writePrivate(
          join(outputDir, "conversations", `${item.id}.json`),
          redact(JSON.stringify(conversation, null, 2), redactSecrets),
        );
      }

      // Save Markdown
      if (format === "md" || format === "both") {
        const md = redact(conversationToMarkdown(conversation), redactSecrets);
        writePrivate(join(outputDir, "conversations", `${item.id}_${slug}.md`), md);
      }

      exported++;

      // Rate limiting delay
      if (i < toFetch.length - 1) {
        await new Promise((r) => setTimeout(r, DELAY_MS));
      }
    } catch (err) {
      const errMsg = `Failed to export ${item.id} (${item.title}): ${err}`;
      console.error(errMsg);
      errors.push(errMsg);
    }
  }

  // Create summary.
  //
  // Conversation TITLES are conversation content: people paste keys, client names and medical
  // detail into the first message, and ChatGPT titles the thread from it. Redaction used to be
  // applied to index.json and to the per-conversation files but NOT here, so a run with
  // { redact: true } produced a "redacted" export whose summary still listed every title in
  // clear. The whole rendered summary now goes through the same filter as everything else.
  const summary = redact(
    `# ChatGPT Export Summary

**Date:** ${new Date().toISOString()}
**Total Conversations:** ${items.length}
**Exported:** ${exported}
**Errors:** ${errors.length}

## Conversations

${items.map((i) => `- [${i.title || "Untitled"}](conversations/${i.id}_${slugify(i.title || "untitled")}.md)`).join("\n")}
`,
    redactSecrets,
  );

  writePrivate(join(outputDir, "summary.md"), summary);

  return { exported, outputDir, errors };
}

// CLI entry point
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log("This script should be run from the OpenClaw agent context.");
  console.log("The agent will use the browser tool to execute the export.");
  console.log('\nInvoke it by name, so ordinary conversation about ChatGPT cannot trigger it:');
  console.log('  "chatgpt-exporter-ultimate: export my conversations"');
  console.log("");
  console.log("It writes plaintext copies of your conversations to");
  console.log("~/.local/share/chatgpt-export/<date> (mode 0700), index-only unless you ask for");
  console.log("full content, and will not run until you have confirmed the destination and scope.");
  console.log("Delete an export:  ./scripts/export.sh --purge -o <dir>");
  console.log("Off switch: CHATGPT_EXPORT_DISABLE=1 or touch ~/.openclaw/chatgpt-export.disabled");
}
