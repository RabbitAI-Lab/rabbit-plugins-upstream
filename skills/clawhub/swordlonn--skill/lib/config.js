import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const SKILL_DIR = path.resolve(__dirname, "..");
const CONFIG_PATH = path.join(SKILL_DIR, "config.json");

const DEFAULT_CONFIG = {
  domain: "watchitai.net",
  bridgePort: 8765,
  mode: "server",
};

let cachedConfig = null;

export function loadConfig() {
  if (cachedConfig) return cachedConfig;

  let config = { ...DEFAULT_CONFIG };

  try {
    if (fs.existsSync(CONFIG_PATH)) {
      const raw = fs.readFileSync(CONFIG_PATH, "utf-8");
      const userConfig = JSON.parse(raw);
      config = { ...config, ...userConfig };
    }
  } catch (e) {
    console.warn("[config] Failed to load config, using defaults:", e.message);
  }

  if (process.env.WATCHITAI_DOMAIN) {
    config.domain = process.env.WATCHITAI_DOMAIN;
  }
  if (process.env.WATCHITAI_BRIDGE_PORT) {
    config.bridgePort = parseInt(process.env.WATCHITAI_BRIDGE_PORT) || 8765;
  }
  if (process.env.WATCHITAI_MODE) {
    config.mode = process.env.WATCHITAI_MODE;
  }

  cachedConfig = config;
  return config;
}

export function getDomain() {
  return loadConfig().domain;
}

export function getBridgePort() {
  return loadConfig().bridgePort;
}

export function getMode() {
  return loadConfig().mode;
}

export function getHostUrl() {
  const { domain } = loadConfig();
  return `https://${domain}/host`;
}

export function getLocalHostUrl() {
  const { bridgePort } = loadConfig();
  return `http://localhost:${bridgePort}/`;
}

export function getApiBase() {
  const { domain } = loadConfig();
  return `https://${domain}/api`;
}

export function isServerMode() {
  return loadConfig().mode === "server";
}

export default {
  loadConfig,
  getDomain,
  getBridgePort,
  getMode,
  getHostUrl,
  getLocalHostUrl,
  getApiBase,
  isServerMode,
};
