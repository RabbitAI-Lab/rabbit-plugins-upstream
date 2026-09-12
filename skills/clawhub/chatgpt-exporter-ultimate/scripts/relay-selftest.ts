/**
 * Regression tests for the browser-relay exporter's file-safety behaviour.
 *
 * These cover the three relay-side findings from the 1.9.0 scan:
 *   - files and directories got their private mode only at CREATION, so reusing an existing
 *     permissive path left conversation text world-readable;
 *   - redaction was applied to index.json and the per-conversation files but NOT to summary.md,
 *     so a "redacted" export still listed every conversation title in clear;
 *   - allowUnsafeDest let a caller switch the destination guard off.
 *
 * Plus the destination check itself, which must resolve symlinks before judging a path.
 *
 * No network. The relay is driven with a stub browserEvaluate, so nothing contacts chatgpt.com
 * and no real conversation is ever read. Everything happens inside a throwaway HOME.
 *
 * Run:  node --experimental-strip-types scripts/relay-selftest.ts
 */

import { mkdtempSync, mkdirSync, writeFileSync, statSync, readFileSync, rmSync, symlinkSync, realpathSync, chmodSync } from "fs";
import { dirname, join, resolve } from "path";
import { tmpdir } from "os";

import { destinationObjection, exportChatGPTConversations } from "./export-conversations.ts";

let pass = 0;
let fail = 0;

function ok(name: string, condition: boolean, detail = ""): void {
  if (condition) {
    console.log(`✓ PASS: ${name}`);
    pass++;
  } else {
    console.log(`✗ FAIL: ${name}${detail ? ` — ${detail}` : ""}`);
    fail++;
  }
}

// A throwaway HOME. realpath it: on macOS $TMPDIR is under a symlinked /var, which would make
// every path look like the symlink bug under test.
const HOME = realpathSync(mkdtempSync(join(tmpdir(), "cge-relay-")));
const OUTSIDE = realpathSync(mkdtempSync(join(tmpdir(), "cge-outside-")));
process.env.HOME = HOME;
delete process.env.CHATGPT_EXPORT_DISABLE;

const mode = (p: string): string => (statSync(p).mode & 0o777).toString(8);

async function main(): Promise<void> {
  const scriptDir = dirname(resolve(process.argv[1]));

// ---------------------------------------------------------------- destination vetting
mkdirSync(join(HOME, "Dropbox", "exports"), { recursive: true });
mkdirSync(join(HOME, "code", "project", ".git"), { recursive: true });
mkdirSync(join(HOME, "safe"), { recursive: true });

ok("a plain directory under home is accepted",
   destinationObjection(join(HOME, "safe", "2026-01-01")) === null);

ok("a literal path outside home is refused",
   (destinationObjection(join(OUTSIDE, "x")) ?? "").includes("outside your home"));

ok("a literal synced folder is refused",
   (destinationObjection(join(HOME, "Dropbox", "exports")) ?? "").includes("synced"));

ok("a literal git repository is refused",
   (destinationObjection(join(HOME, "code", "project", "exports")) ?? "").includes("git"));

// The 1.9.0 shape: a literal path that looks fine and resolves somewhere it is not.
symlinkSync(OUTSIDE, join(HOME, "escape"));
ok("a symlink under home pointing outside home is refused",
   (destinationObjection(join(HOME, "escape", "exports")) ?? "").includes("outside your home"));

symlinkSync(join(HOME, "Dropbox"), join(HOME, "notsynced"));
ok("a symlink whose name hides a synced target is refused",
   (destinationObjection(join(HOME, "notsynced", "exports")) ?? "").includes("synced"));

symlinkSync(join(HOME, "code", "project"), join(HOME, "plain"));
ok("a symlink into a git repository is refused",
   (destinationObjection(join(HOME, "plain", "exports")) ?? "").includes("git"));

mkdirSync(join(HOME, "a"), { recursive: true });
symlinkSync(OUTSIDE, join(HOME, "a", "link"));
ok("a symlinked ancestor with a not-yet-created tail is refused",
   (destinationObjection(join(HOME, "a", "link", "2026-01-01")) ?? "").includes("outside your home"));

// ---------------------------------------------------------------- relay stub
const TITLE_SECRET = "invoice for sk-abcdefghijklmnopqrstuvwx";
const ITEMS = [
  { id: "c1", title: TITLE_SECRET, create_time: 1, update_time: 2 },
];

const stubEvaluate = async (js: string): Promise<string> => {
  if (js.includes("conversations?offset")) {
    return JSON.stringify({ items: ITEMS, total: 1, limit: 100, offset: 0 });
  }
  return JSON.stringify({
    title: TITLE_SECRET,
    create_time: 1,
    update_time: 2,
    mapping: {
      m1: {
        id: "m1",
        message: {
          id: "m1",
          author: { role: "user" },
          create_time: 1,
          content: { content_type: "text", parts: ["my key is sk-abcdefghijklmnopqrstuvwx"] },
        },
        parent: null,
        children: [],
      },
    },
  });
};

// ---------------------------------------------------------------- reused permissive paths
// The exact failure the scanner named: the directory and the files already exist, wide open,
// from an earlier run or a careless mkdir. mkdir/writeFile `mode` is ignored when the target
// exists, so 1.9.0 left them at 0777/0666 while telling the caller 0700/0600.
const REUSED = join(HOME, "safe", "reused");
mkdirSync(join(REUSED, "conversations"), { recursive: true });
writeFileSync(join(REUSED, "index.json"), "stale");
writeFileSync(join(REUSED, "summary.md"), "stale");
chmodSync(REUSED, 0o777);
chmodSync(join(REUSED, "conversations"), 0o777);
chmodSync(join(REUSED, "index.json"), 0o666);
chmodSync(join(REUSED, "summary.md"), 0o666);

const result = await exportChatGPTConversations({
  browserEvaluate: stubEvaluate,
  confirmed: true,
  outputDir: REUSED,
  indexOnly: false,
  redact: true,
});

ok("export into a reused directory succeeds", result.exported === 1,
   `exported=${result.exported} errors=${result.errors.join("|")}`);

ok("a reused output directory is forced back to 0700", mode(REUSED) === "700",
   `mode is ${mode(REUSED)}`);
ok("a reused conversations directory is forced back to 0700",
   mode(join(REUSED, "conversations")) === "700",
   `mode is ${mode(join(REUSED, "conversations"))}`);
ok("a reused index.json is forced back to 0600", mode(join(REUSED, "index.json")) === "600",
   `mode is ${mode(join(REUSED, "index.json"))}`);
ok("a reused summary.md is forced back to 0600", mode(join(REUSED, "summary.md")) === "600",
   `mode is ${mode(join(REUSED, "summary.md"))}`);
ok("a freshly written conversation file is 0600",
   mode(join(REUSED, "conversations", "c1.json")) === "600",
   `mode is ${mode(join(REUSED, "conversations", "c1.json"))}`);
ok("the manifest is 0600",
   mode(join(REUSED, ".chatgpt-export-manifest.json")) === "600");

// ---------------------------------------------------------------- summary redaction
const summary = readFileSync(join(REUSED, "summary.md"), "utf8");
ok("summary.md is redacted like every other file",
   !summary.includes("sk-abcdefghijklmnopqrstuvwx"),
   "the secret in the conversation title survived into summary.md");
ok("summary.md still lists the conversation", summary.includes("REDACTED"),
   "expected a redaction marker where the title was");

const index = readFileSync(join(REUSED, "index.json"), "utf8");
ok("index.json is still redacted", !index.includes("sk-abcdefghijklmnopqrstuvwx"));

const convMd = readFileSync(
  join(REUSED, "conversations", `c1_${summarySlug()}.md`),
  "utf8",
);
ok("conversation markdown is still redacted", !convMd.includes("sk-abcdefghijklmnopqrstuvwx"));

function summarySlug(): string {
  return TITLE_SECRET.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 50);
}

// ---------------------------------------------------------------- removed override
const source = readFileSync(join(scriptDir, "export-conversations.ts"), "utf8");
// Strip comments before asserting. The header explains that the override was removed, and
// saying so is the point; what must not exist is a live option, destructure or assignment.
const code = source
  .split("\n")
  .filter((l) => !/^\s*(\/\/|\*|\/\*)/.test(l))
  .join("\n");
ok("allowUnsafeDest has no live implementation in the relay",
   !code.includes("allowUnsafeDest"),
   "found it outside a comment");

// It must actually refuse, not merely lack the flag.
let refused = false;
try {
  await exportChatGPTConversations({
    browserEvaluate: stubEvaluate,
    confirmed: true,
    outputDir: join(HOME, "Dropbox", "exports"),
    indexOnly: true,
    // @ts-expect-error: the option no longer exists; passing it must not re-enable anything.
    allowUnsafeDest: true,
  });
} catch (e) {
  refused = String(e).includes("Refusing to export");
}
ok("a synced destination is refused even when allowUnsafeDest is passed", refused);

// The relay must handle no bearer token.
ok("the relay reads no bearer token",
   !/CHATGPT_ACCESS_TOKEN|Authorization:\s*.?Bearer/.test(source));

rmSync(HOME, { recursive: true, force: true });
rmSync(OUTSIDE, { recursive: true, force: true });

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail === 0 ? 0 : 1);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
