/**
 * Enumerate the WhatsApp groups this account participates in, and the phone
 * numbers of their members.
 *
 * THIS IS A PRIVACY-SENSITIVE OPERATION. It reads your WhatsApp session
 * credentials, contacts WhatsApp's servers as your account, and assembles a
 * dataset about OTHER PEOPLE who never consented to being exported.
 * It therefore does nothing at all unless you pass --yes.
 *
 * Defaults are the conservative ones:
 *   - nothing is written to disk unless you pass --save
 *   - phone numbers are masked to the last 4 digits unless you pass --resolve-lids
 *
 * Run with: npx tsx scripts/wa-fetch-contacts.ts --yes [--save[=PATH]] [--resolve-lids]
 */

import {
  makeWASocket,
  useMultiFileAuthState,
  makeCacheableSignalKeyStore,
  fetchLatestBaileysVersion,
} from "@whiskeysockets/baileys";
import pino from "pino";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";

const argv = process.argv.slice(2);
const has = (flag: string) => argv.includes(flag);
const valueOf = (flag: string): string | undefined => {
  const hit = argv.find((a) => a.startsWith(`${flag}=`));
  return hit ? hit.slice(flag.length + 1) : undefined;
};

const CONSENTED = has("--yes");
const SAVE = has("--save") || argv.some((a) => a.startsWith("--save="));
const RESOLVE_LIDS = has("--resolve-lids");

const AUTH_DIR =
  valueOf("--auth-dir") ||
  process.env.WA_AUTH_DIR ||
  path.join(os.homedir(), ".openclaw/credentials/whatsapp/default");

const OUTPUT_PATH =
  valueOf("--save") ||
  path.join(os.homedir(), ".openclaw/workspace/bank/whatsapp-contacts-full.json");

function disclose() {
  console.log("");
  console.log("⚠️  whatsapp-ultimate — group/contact enumeration");
  console.log("");
  console.log("   This will:");
  console.log(`     • READ your WhatsApp session credentials from: ${AUTH_DIR}`);
  console.log("     • CONNECT to WhatsApp servers as your account (a linked-device session)");
  console.log("     • ENUMERATE every group you are in and every member of those groups");
  console.log(
    `     • ${RESOLVE_LIDS ? "RESOLVE opaque LIDs to real phone numbers (--resolve-lids)" : "MASK phone numbers to the last 4 digits (pass --resolve-lids for full numbers)"}`,
  );
  console.log(
    `     • ${SAVE ? `WRITE the dataset to ${OUTPUT_PATH} (mode 0600)` : "keep everything IN MEMORY — nothing is written to disk (pass --save to persist)"}`,
  );
  console.log("");
  console.log("   The people in those groups did not agree to this. Only run it on groups");
  console.log("   you have a legitimate reason to inventory, and delete the output when done.");
  console.log("");
}

// Load LID reverse mappings — ONLY when the user explicitly opted in.
function loadLidMappings(): Map<string, string> {
  const mappings = new Map<string, string>();
  if (!RESOLVE_LIDS) return mappings;

  const files = fs.readdirSync(AUTH_DIR);
  for (const file of files) {
    if (file.startsWith("lid-mapping-") && file.endsWith("_reverse.json")) {
      try {
        const lid = file.replace("lid-mapping-", "").replace("_reverse.json", "");
        const content = fs.readFileSync(path.join(AUTH_DIR, file), "utf-8");
        const phone = JSON.parse(content);
        if (typeof phone === "string") {
          mappings.set(lid, phone);
        }
      } catch {
        // Skip invalid files
      }
    }
  }

  console.log(`📋 Loaded ${mappings.size} LID mappings (--resolve-lids)`);
  return mappings;
}

// Last-4 masking. Not reversible from the output alone.
function maskPhone(phone: string): string {
  if (RESOLVE_LIDS) return phone;
  if (phone.startsWith("LID:")) return `LID:…${phone.slice(-4)}`;
  return `+•••••${phone.slice(-4)}`;
}

async function main() {
  disclose();

  if (!CONSENTED) {
    console.error("❌ Refusing to run without explicit consent.");
    console.error("   Re-run with --yes if the above is what you want:");
    console.error("     npx tsx scripts/wa-fetch-contacts.ts --yes");
    process.exit(1);
  }

  console.log("🔌 Connecting to WhatsApp...");

  const lidMappings = loadLidMappings();

  const logger = pino({ level: "silent" });
  const { state } = await useMultiFileAuthState(AUTH_DIR);
  const { version } = await fetchLatestBaileysVersion();

  const sock = makeWASocket({
    auth: {
      creds: state.creds,
      keys: makeCacheableSignalKeyStore(state.keys, logger),
    },
    version,
    logger,
    printQRInTerminal: false,
    browser: ["OpenClaw Contact Sync", "Chrome", "1.0.0"],
    markOnlineOnConnect: false,
  });

  // Wait for connection
  await new Promise<void>((resolve, reject) => {
    sock.ev.on("connection.update", (update) => {
      if (update.connection === "open") {
        resolve();
      }
      if (update.connection === "close") {
        reject(new Error("Connection closed"));
      }
    });
    setTimeout(() => reject(new Error("Connection timeout")), 30000);
  });

  console.log("✅ Connected! Fetching all groups...");

  try {
    const groups = await sock.groupFetchAllParticipating();

    const contacts: Record<string, {
      phone: string;
      lid?: string;
      groups: Array<{ id: string; name: string; isAdmin: boolean }>;
      isAdmin: boolean
    }> = {};
    const groupList: Array<{ id: string; subject: string; participantCount: number }> = [];
    let unresolvedLids = 0;

    console.log(`📊 Found ${Object.keys(groups).length} groups`);

    for (const [jid, meta] of Object.entries(groups)) {
      groupList.push({
        id: jid,
        subject: meta.subject,
        participantCount: meta.participants?.length || 0,
      });

      for (const participant of meta.participants || []) {
        let rawId = participant.id?.split("@")[0];
        if (!rawId || rawId.includes(":")) continue;

        // Check if this is a LID that needs resolution
        let phone: string;
        let lid: string | undefined;

        if (lidMappings.has(rawId)) {
          // This is a LID, resolve to phone (only reachable with --resolve-lids)
          phone = `+${lidMappings.get(rawId)}`;
          lid = rawId;
        } else if (rawId.length > 15) {
          // Likely an unresolved LID
          unresolvedLids++;
          phone = `LID:${rawId}`;
          lid = rawId;
        } else {
          // Real phone number
          phone = `+${rawId}`;
        }

        const key = maskPhone(phone);

        if (!contacts[key]) {
          contacts[key] = {
            phone: key,
            lid: RESOLVE_LIDS ? lid : undefined,
            groups: [],
            isAdmin: false,
          };
        }

        contacts[key].groups.push({
          id: jid,
          name: meta.subject,
          isAdmin: participant.admin ? true : false,
        });

        if (participant.admin) {
          contacts[key].isAdmin = true;
        }
      }
    }

    // Sort contacts by number of groups
    const sortedContacts = Object.values(contacts).sort(
      (a, b) => b.groups.length - a.groups.length
    );

    // Separate resolved and unresolved
    const resolved = sortedContacts.filter(c => !c.phone.startsWith("LID:"));
    const unresolved = sortedContacts.filter(c => c.phone.startsWith("LID:"));

    const output = {
      extracted: new Date().toISOString(),
      source: "whatsapp-groups",
      redacted: !RESOLVE_LIDS,
      selfId: RESOLVE_LIDS ? sock.user?.id : undefined,
      stats: {
        totalGroups: groupList.length,
        totalContacts: sortedContacts.length,
        resolvedContacts: resolved.length,
        unresolvedLids: unresolved.length,
      },
      groups: groupList.sort((a, b) => b.participantCount - a.participantCount),
      contacts: resolved,
      unresolvedContacts: unresolved.length > 0 ? unresolved : undefined,
    };

    console.log(`\n📱 Found ${resolved.length} contacts across ${groupList.length} groups`);
    if (unresolved.length > 0) {
      console.log(`⚠️  ${unresolved.length} contacts have unresolved LIDs`);
    }

    if (SAVE) {
      fs.mkdirSync(path.dirname(OUTPUT_PATH), { recursive: true });
      fs.writeFileSync(OUTPUT_PATH, JSON.stringify(output, null, 2), { mode: 0o600 });
      // writeFileSync's mode only applies on creation — tighten an existing file too.
      fs.chmodSync(OUTPUT_PATH, 0o600);
      console.log(`💾 Saved to: ${OUTPUT_PATH} (mode 0600${output.redacted ? ", phone numbers masked" : ", FULL phone numbers"})`);
      console.log(`   Delete it when you are done:  rm ${OUTPUT_PATH}`);
    } else {
      console.log("💨 Nothing written to disk (pass --save to persist this dataset).");
    }

    // Print top contacts by group membership
    console.log("\n🔝 Top contacts by group membership:");
    for (const contact of resolved.slice(0, 15)) {
      const admin = contact.isAdmin ? " (admin)" : "";
      console.log(`  ${contact.phone}: ${contact.groups.length} groups${admin}`);
    }

  } catch (err: unknown) {
    const error = err as Error;
    console.error("❌ Error:", error.message);
    throw err;
  } finally {
    sock.ws?.close();
    process.exit(0);
  }
}

main().catch((err) => {
  console.error("Fatal error:", err);
  process.exit(1);
});
