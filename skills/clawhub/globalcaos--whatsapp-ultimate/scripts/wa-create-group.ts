/**
 * Create a WhatsApp group using Baileys directly.
 *
 * THIS TAKES A REAL, VISIBLE ACTION ON YOUR ACCOUNT. It reads your WhatsApp
 * session credentials, connects as you, and creates a group that every listed
 * participant will see appear on their phone. It is not undoable from here.
 * It therefore does nothing at all unless you pass --yes.
 *
 * Usage: npx tsx scripts/wa-create-group.ts --yes "Group Name" "+phone1" "+phone2" ...
 * Options: --auth-dir=PATH   (or WA_AUTH_DIR env) use a different session directory
 */

import {
  makeWASocket,
  useMultiFileAuthState,
  makeCacheableSignalKeyStore,
  fetchLatestBaileysVersion,
} from "@whiskeysockets/baileys";
import pino from "pino";
import path from "node:path";
import os from "node:os";

const argv = process.argv.slice(2);
const CONSENTED = argv.includes("--yes");
const authDirFlag = argv.find((a) => a.startsWith("--auth-dir="));

const AUTH_DIR =
  (authDirFlag ? authDirFlag.slice("--auth-dir=".length) : undefined) ||
  process.env.WA_AUTH_DIR ||
  path.join(os.homedir(), ".openclaw/credentials/whatsapp/default");

async function main() {
  const args = argv.filter((a) => a !== "--yes" && !a.startsWith("--auth-dir="));

  if (args.length < 2) {
    console.error('Usage: npx tsx scripts/wa-create-group.ts --yes "Group Name" "+phone1" "+phone2" ...');
    process.exit(1);
  }

  const [name, ...rawParticipants] = args;

  // Convert phone numbers to WhatsApp JIDs
  const participants = rawParticipants.map(p => {
    const cleaned = p.replace(/[^0-9]/g, "");
    return `${cleaned}@s.whatsapp.net`;
  });

  console.log("");
  console.log("⚠️  whatsapp-ultimate — group creation");
  console.log("");
  console.log("   This will:");
  console.log(`     • READ your WhatsApp session credentials from: ${AUTH_DIR}`);
  console.log("     • CONNECT to WhatsApp servers as your account (a linked-device session)");
  console.log(`     • CREATE the group "${name}" with ${participants.length} participant(s)`);
  console.log("     • NOTIFY every one of them — the group appears on their phone immediately");
  console.log("");
  console.log("   Participants:");
  for (const p of rawParticipants) console.log(`     - ${p}`);
  console.log("");
  console.log("   Only the group name and those phone numbers are sent to WhatsApp.");
  console.log("");

  if (!CONSENTED) {
    console.error("❌ Refusing to create a group without explicit consent.");
    console.error("   Re-run with --yes if the above is what you want.");
    process.exit(1);
  }

  console.log(`🔌 Connecting to WhatsApp...`);

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
    browser: ["OpenClaw Group Creator", "Chrome", "1.0.0"],
    markOnlineOnConnect: false,
  });

  await new Promise<void>((resolve, reject) => {
    sock.ev.on("connection.update", (update) => {
      if (update.connection === "open") resolve();
      if (update.connection === "close") reject(new Error("Connection closed"));
    });
    setTimeout(() => reject(new Error("Connection timeout")), 30000);
  });

  console.log(`✅ Connected!`);
  console.log(`📱 Creating group "${name}" with ${participants.length} participants...`);

  try {
    const result = await sock.groupCreate(name, participants);
    console.log(`\n✅ Group created!`);
    console.log(`   ID: ${result.id}`);
    console.log(`   Name: ${result.subject}`);
    if (result.creation) {
      console.log(`   Created: ${new Date(result.creation * 1000).toISOString()}`);
    }
  } catch (err) {
    console.error(`\n❌ Failed to create group:`, (err as Error).message);
    throw err;
  } finally {
    sock.ws?.close();
    process.exit(0);
  }
}

main().catch(err => {
  console.error("Fatal:", err);
  process.exit(1);
});
