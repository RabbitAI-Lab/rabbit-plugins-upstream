#!/usr/bin/env node
/**
 * 调试工具：读取最近几条小爱音箱对话记录。
 *
 * 隐私默认值：不打印语音转写原文，只输出条数与时间。
 * 需要排查识别问题时，显式设置 PRINT_TRANSCRIPTS=true。
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import dotenv from "dotenv";
import { getMiNA } from "@mi-gpt/miot";

import {
  ConfigError,
  ensureStateDir,
  parseConfig,
  restrictFilePermissions,
  withLogsToStderr,
} from "./lib/core.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SKILL_ROOT = path.resolve(__dirname, "..");

function loadEnvironment() {
  const explicit = String(process.env.XIAOAI_ENV_FILE ?? "").trim();
  const candidates = explicit
    ? [path.resolve(explicit)]
    : [path.join(__dirname, ".env"), path.join(SKILL_ROOT, ".env")];

  for (const file of candidates) {
    dotenv.config({ path: file, quiet: true });
  }
}

async function main() {
  loadEnvironment();
  const config = parseConfig(process.env);

  const stateDir = ensureStateDir(config.stateDir);
  process.chdir(stateDir);

  const mina = await withLogsToStderr(() =>
    getMiNA({
      userId: config.userId,
      passToken: config.passToken || undefined,
      password: config.password || undefined,
      did: config.did,
      debug: config.debug,
    }),
  );

  if (!mina) {
    throw new Error("登录失败：请检查 MI_USER_ID、passToken/密码与 MI_DEVICE_ID");
  }

  const cacheFile = path.join(stateDir, ".mi.json");
  if (fs.existsSync(cacheFile)) {
    restrictFilePermissions(cacheFile);
  }

  const conversations = await mina.getConversations({ limit: 5 });
  const records = conversations?.records ?? [];

  console.log(`共 ${records.length} 条记录`);

  if (String(process.env.PRINT_TRANSCRIPTS ?? "").toLowerCase() === "true") {
    for (const record of records) {
      console.log(`时间: ${new Date(record.time).toLocaleString()}`);
      console.log(`内容: ${record.query}`);
      console.log("---");
    }
  } else {
    console.log("默认不打印语音转写内容；如需查看原文，请设置 PRINT_TRANSCRIPTS=true");
  }
}

try {
  await main();
} catch (error) {
  if (error instanceof ConfigError) {
    console.error(`❌ 配置错误：${error.message}`);
    process.exitCode = 2;
  } else {
    console.error(`❌ ${error.message}`);
    process.exitCode = 1;
  }
}
