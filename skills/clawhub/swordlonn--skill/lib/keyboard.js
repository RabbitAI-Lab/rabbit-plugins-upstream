import * as path from "path";
import { fileURLToPath } from "url";
import { IS_WINDOWS, IS_MACOS, IS_LINUX } from "./platform.js";
import { execCmd, sanitizeString, wrapWithPermissionCheck } from "./utils.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let nutKeyboard = null;

async function getNutKeyboard() {
  if (nutKeyboard !== null) return nutKeyboard;
  try {
    const nut = await import("@nut-tree/nut-js");
    nutKeyboard = nut.keyboard;
    console.log("[watchitai] Using nut.js for keyboard control");
    return nutKeyboard;
  } catch (e) {
    nutKeyboard = false;
    console.log("[watchitai] nut.js not available, using platform fallback");
    return null;
  }
}

const KEY_MAP = {
  Backspace: "backspace",
  Tab: "tab",
  Enter: "enter",
  Shift: "shift",
  Control: "control",
  Alt: "alt",
  Meta: "meta",
  Escape: "escape",
  " ": "space",
  ArrowLeft: "left",
  ArrowUp: "up",
  ArrowRight: "right",
  ArrowDown: "down",
  Delete: "delete",
  Home: "home",
  End: "end",
  PageUp: "pageup",
  PageDown: "pagedown",
  F1: "f1",
  F2: "f2",
  F3: "f3",
  F4: "f4",
  F5: "f5",
  F6: "f6",
  F7: "f7",
  F8: "f8",
  F9: "f9",
  F10: "f10",
  F11: "f11",
  F12: "f12",
};

function mapKey(key) {
  return KEY_MAP[key] || key;
}

function getModifierFlags(modifiers) {
  const flags = [];
  if (modifiers?.ctrl) flags.push("ctrl");
  if (modifiers?.shift) flags.push("shift");
  if (modifiers?.alt) flags.push("alt");
  if (modifiers?.meta) flags.push("cmd");
  return flags;
}

export async function keyDown(key, modifiers = {}) {
  key = sanitizeString(key, 50);

  const keyboard = await getNutKeyboard();
  if (keyboard) {
    const { Key } = await import("@nut-tree/nut-js");
    const nutKey = Key[mapKey(key).toUpperCase().replace(/-/g, "_")] || key;
    if (nutKey) {
      await keyboard.pressKey(nutKey);
      return;
    }
  }

  const mappedKey = mapKey(key);
  const mods = getModifierFlags(modifiers);

  if (IS_MACOS) {
    try {
      let cmd = "";
      if (mods.length > 0) {
        const keyStr = mods.map((m) => `${m === "cmd" ? "command" : m} down`).join(" & ");
        cmd = `osascript -e 'tell application "System Events" to ${keyStr} & key down "${mappedKey}"'`;
      } else {
        cmd = `osascript -e 'tell application "System Events" to key down "${mappedKey}"'`;
      }
      await execCmd(cmd);
    } catch (e) {
      console.warn("[watchitai] keyDown failed:", e.message);
    }
  } else if (IS_WINDOWS) {
    try {
      const script = `
        Add-Type -AssemblyName System.Windows.Forms
        [System.Windows.Forms.SendKeys]::SendWait("${mappedKey === "enter" ? "{ENTER}" : mappedKey}")
      `;
      await execCmd(`powershell -Command "${script.replace(/"/g, '\\"')}"`);
    } catch (e) {
      console.warn("[watchitai] keyDown failed:", e.message);
    }
  } else if (IS_LINUX) {
    try {
      let args = "";
      if (mods.ctrl) args += " --clearmodifiers ctrl+";
      if (mods.shift) args += "shift+";
      if (mods.alt) args += "alt+";
      if (mods.meta) args += "super+";
      args += mappedKey;
      await execCmd(`xdotool keydown ${args}`);
    } catch (e) {
      console.warn("[watchitai] keyDown failed:", e.message);
    }
  }
}

export async function keyUp(key, modifiers = {}) {
  key = sanitizeString(key, 50);

  const keyboard = await getNutKeyboard();
  if (keyboard) {
    const { Key } = await import("@nut-tree/nut-js");
    const nutKey = Key[mapKey(key).toUpperCase().replace(/-/g, "_")] || key;
    if (nutKey) {
      await keyboard.releaseKey(nutKey);
      return;
    }
  }

  const mappedKey = mapKey(key);

  if (IS_MACOS) {
    try {
      await execCmd(
        `osascript -e 'tell application "System Events" to key up "${mappedKey}"'`,
      );
    } catch (e) {
      console.warn("[watchitai] keyUp failed:", e.message);
    }
  } else if (IS_WINDOWS) {
    // SendKeys doesn't have separate up; rely on down+up in keyPress
  } else if (IS_LINUX) {
    try {
      await execCmd(`xdotool keyup ${mappedKey}`);
    } catch (e) {
      console.warn("[watchitai] keyUp failed:", e.message);
    }
  }
}

export async function keyPress(key, modifiers = {}) {
  key = sanitizeString(key, 50);

  const keyboard = await getNutKeyboard();
  if (keyboard) {
    const { Key } = await import("@nut-tree/nut-js");
    const nutKey = Key[mapKey(key).toUpperCase().replace(/-/g, "_")] || key;
    if (nutKey) {
      await keyboard.type(nutKey);
      return;
    }
  }

  await keyDown(key, modifiers);
  await new Promise((r) => setTimeout(r, 20));
  await keyUp(key, modifiers);
}

export async function typeText(text) {
  text = sanitizeString(text, 500);

  const keyboard = await getNutKeyboard();
  if (keyboard) {
    await keyboard.type(text);
    return;
  }

  if (IS_MACOS) {
    try {
      await execCmd(
        `osascript -e 'tell application "System Events" to keystroke "${text.replace(/"/g, '\\"')}"'`,
      );
    } catch (e) {
      console.warn("[watchitai] typeText failed:", e.message);
    }
  } else if (IS_WINDOWS) {
    try {
      const script = `
        Add-Type -AssemblyName System.Windows.Forms
        [System.Windows.Forms.SendKeys]::SendWait("${text.replace(/"/g, '\\"').replace(/\{/g, "{{}").replace(/\}/g, "}}")}")
      `;
      await execCmd(`powershell -Command "${script.replace(/"/g, '\\"')}"`);
    } catch (e) {
      console.warn("[watchitai] typeText failed:", e.message);
    }
  } else if (IS_LINUX) {
    try {
      await execCmd(`xdotool type "${text.replace(/"/g, '\\"')}"`);
    } catch (e) {
      console.warn("[watchitai] typeText failed:", e.message);
    }
  }
}

export default {
  keyDown: wrapWithPermissionCheck(keyDown, "keyDown"),
  keyUp: wrapWithPermissionCheck(keyUp, "keyUp"),
  keyPress: wrapWithPermissionCheck(keyPress, "keyPress"),
  typeText: wrapWithPermissionCheck(typeText, "typeText"),
};
