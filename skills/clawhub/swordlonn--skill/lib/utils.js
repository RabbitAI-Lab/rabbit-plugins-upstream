import { exec } from "child_process";
import * as path from "path";
import { fileURLToPath } from "url";
import { randomBytes, timingSafeEqual } from "crypto";
import { IS_WINDOWS, IS_MACOS, IS_LINUX } from "./platform.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const SCRIPTS_DIR = path.resolve(__dirname, "../scripts");

const LOG_LEVELS = {
  DEBUG: 0,
  INFO: 1,
  WARN: 2,
  ERROR: 3,
};

let currentLogLevel = LOG_LEVELS.INFO;

export function setLogLevel(level) {
  currentLogLevel = level;
}

export function getLogLevel() {
  return currentLogLevel;
}

function formatMessage(level, message, ...args) {
  const timestamp = new Date().toISOString();
  const levelStr = Object.entries(LOG_LEVELS).find(([, v]) => v === level)?.[0] || "INFO";
  let formatted = `[${timestamp}] [${levelStr}] ${message}`;
  if (args.length > 0) {
    formatted += " " + JSON.stringify(args);
  }
  return formatted;
}

export function debug(message, ...args) {
  if (currentLogLevel <= LOG_LEVELS.DEBUG) {
    console.debug(formatMessage(LOG_LEVELS.DEBUG, message, ...args));
  }
}

export function info(message, ...args) {
  if (currentLogLevel <= LOG_LEVELS.INFO) {
    console.log(formatMessage(LOG_LEVELS.INFO, message, ...args));
  }
}

export function warn(message, ...args) {
  if (currentLogLevel <= LOG_LEVELS.WARN) {
    console.warn(formatMessage(LOG_LEVELS.WARN, message, ...args));
  }
}

export function error(message, ...args) {
  if (currentLogLevel <= LOG_LEVELS.ERROR) {
    console.error(formatMessage(LOG_LEVELS.ERROR, message, ...args));
  }
}

export function execCmd(cmd, options = {}) {
  return new Promise((resolve, reject) => {
    const timeout = options.timeout || 10000;
    const child = exec(cmd, {
      ...options,
      timeout,
      killSignal: "SIGTERM",
    }, (err, stdout, stderr) => {
      if (err) {
        err.stdout = stdout;
        err.stderr = stderr;
        reject(err);
      } else {
        resolve({ stdout, stderr });
      }
    });

    child.on("error", (err) => {
      reject(err);
    });

    child.on("exit", (code, signal) => {
      if (signal === "SIGTERM" || signal === "SIGKILL") {
        reject(new Error(`Command timed out or was killed: ${cmd}`));
      }
    });
  });
}

export function sanitizeNumber(value, min = 0, max = 10000) {
  const num = parseInt(value, 10);
  if (isNaN(num)) return min;
  return Math.max(min, Math.min(max, num));
}

export function sanitizeString(value, maxLength = 100) {
  if (!value || typeof value !== "string") return "";
  const sanitized = value.replace(/[^\w\s\-]/g, "");
  return sanitized.substring(0, maxLength);
}

function isAccessibilityError(error) {
  const msg = (error.message || String(error)).toLowerCase();
  if (IS_MACOS) {
    return (
      msg.includes("not authorized") ||
      msg.includes("-10004") ||
      msg.includes("not allowed") ||
      msg.includes("assistive") ||
      msg.includes("accessibility") ||
      msg.includes("system events")
    );
  }
  if (IS_LINUX) {
    return msg.includes("xdotool") && msg.includes("not found");
  }
  return false;
}

function warnAccessibilityOnce() {
  const warnedKey = "watchitai_accessibility_warned";
  if (global[warnedKey]) return;
  global[warnedKey] = true;

  if (IS_MACOS) {
    warn(`
💡 HINT: Accessibility / Input Monitoring permission may be missing.
   Go to System Settings → Privacy & Security → Accessibility
   and enable permission for your terminal / Trae.

   Or run the preflight script:
   bash ${path.join(SCRIPTS_DIR, "ensure_macos_permissions.sh")}
`);
  } else if (IS_LINUX) {
    warn(`
💡 HINT: xdotool is required for mouse/keyboard control on Linux.
   Install it: sudo apt install xdotool (Debian/Ubuntu)
               sudo dnf install xdotool (Fedora)
`);
  }
}

export function wrapWithPermissionCheck(fn, actionName) {
  return async (...args) => {
    try {
      return await fn(...args);
    } catch (e) {
      if (isAccessibilityError(e)) {
        warnAccessibilityOnce();
      }
      error(`${actionName} failed:`, e.message);
      throw e;
    }
  };
}

export function generateToken(length = 32) {
  const bytes = randomBytes(length);
  const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  let token = "";
  for (let i = 0; i < length; i++) {
    token += chars[bytes[i] % chars.length];
  }
  return token;
}

export function validateToken(token, expected) {
  if (!token || !expected) return false;
  if (token.length !== expected.length) return false;
  // Constant-time comparison to prevent timing attacks
  try {
    return timingSafeEqual(Buffer.from(token), Buffer.from(expected));
  } catch {
    return false;
  }
}

export default {
  setLogLevel,
  getLogLevel,
  debug,
  info,
  warn,
  error,
  execCmd,
  sanitizeNumber,
  sanitizeString,
  wrapWithPermissionCheck,
  generateToken,
  validateToken,
};
