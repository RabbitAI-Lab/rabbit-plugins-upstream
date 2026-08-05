/**
 * Permission detection and guidance for cross-platform control/capture.
 *
 * Detects required permissions and provides helpful guidance
 * when permissions are missing. Integrates with the macOS preflight
 * script for one-stop permission checking.
 */

import { exec, execSync } from "child_process";
import * as path from "path";
import { fileURLToPath } from "url";
import { IS_WINDOWS, IS_MACOS, IS_LINUX, getPlatformName } from "./platform.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const SCRIPTS_DIR = path.resolve(__dirname, "../scripts");

function execCmd(cmd, options = {}) {
  return new Promise((resolve, reject) => {
    exec(cmd, options, (err, stdout, stderr) => {
      if (err) reject(err);
      else resolve({ stdout, stderr });
    });
  });
}

// ============================================================
// Permission types
// ============================================================
export const PERMISSION_TYPES = {
  SCREEN_RECORDING: "screen-recording",
  ACCESSIBILITY: "accessibility",
  INPUT_MONITORING: "input-monitoring",
  NOTIFICATIONS: "notifications",
};

// ============================================================
// macOS permission checks
// ============================================================
async function macosCheckScreenRecording() {
  try {
    const testFile = path.join("/tmp", `watchitai_sr_test_${Date.now()}.png`);
    const result = await execCmd(`screencapture -x -R0,0,1,1 "${testFile}" 2>&1`);
    
    try {
      const fs = await import("fs");
      const stat = fs.statSync(testFile);
      if (stat.size > 0) {
        fs.unlinkSync(testFile);
        return { granted: true, name: PERMISSION_TYPES.SCREEN_RECORDING };
      }
      fs.unlinkSync(testFile);
    } catch {
      // file doesn't exist
    }

    if (result.stderr && result.stderr.includes("could not create image from display")) {
      const isAsleep = await isDisplayAsleep();
      if (isAsleep) {
        // 先尝试自动唤醒
        const wakeResult = await wakeDisplay();
        if (wakeResult.success) {
          // 唤醒成功，重新检测权限
          return macosCheckScreenRecording();
        }
        return {
          granted: null,
          name: PERMISSION_TYPES.SCREEN_RECORDING,
          hint: "Display is asleep. " + (wakeResult.hint || "Wake up your screen to enable screen sharing."),
          reason: "display-asleep",
        };
      }
    }

    return {
      granted: false,
      name: PERMISSION_TYPES.SCREEN_RECORDING,
      hint: "Go to System Settings → Privacy & Security → Screen Recording and enable permission for your terminal / Trae.",
    };
  } catch {
    return {
      granted: false,
      name: PERMISSION_TYPES.SCREEN_RECORDING,
      hint: "Go to System Settings → Privacy & Security → Screen Recording and enable permission for your terminal / Trae.",
    };
  }
}

async function isDisplayAsleep() {
  try {
    const result = await execCmd(
      `system_profiler SPDisplaysDataType 2>/dev/null | grep -i "Display Asleep"`
    );
    return result.stdout && result.stdout.includes("Yes");
  } catch {
    try {
      const result = await execCmd(
        `ioreg -n IODisplayWrangler | grep -i IOPowerManagement`
      );
      return result.stdout && result.stdout.includes('"CurrentPowerState"=0');
    } catch {
      return false;
    }
  }
}

export async function wakeDisplay() {
  if (!IS_MACOS) return { success: false, reason: "not-macos" };

  try {
    // 方案1: caffeinate 临时阻止休眠并尝试唤醒
    await execCmd("caffeinate -u -t 2");
    await new Promise((r) => setTimeout(r, 800));

    // 方案2: 模拟空格键（需要辅助功能权限）
    try {
      await execCmd(
        `osascript -e 'tell application "System Events" to key code 49'`
      );
    } catch {
      // 辅助功能权限可能未授权，忽略
    }

    await new Promise((r) => setTimeout(r, 500));

    // 验证是否唤醒成功
    const stillAsleep = await isDisplayAsleep();
    if (!stillAsleep) {
      return { success: true, method: "auto" };
    }

    return {
      success: false,
      reason: "still-asleep",
      hint: "Auto wake failed. Please wake up your screen manually.",
    };
  } catch (err) {
    return {
      success: false,
      reason: "error",
      hint: `Wake failed: ${err.message}`,
    };
  }
}

async function macosCheckAccessibility() {
  try {
    const { stdout } = await execCmd(
      `osascript -e 'tell application "System Events" to get name of first process' 2>&1`,
    );
    // If we get a real process name (not an error message), permission is granted
    if (stdout && stdout.trim() && !stdout.includes("Error") && !stdout.includes("error")) {
      return { granted: true, name: PERMISSION_TYPES.ACCESSIBILITY };
    }
    return {
      granted: false,
      name: PERMISSION_TYPES.ACCESSIBILITY,
      hint: "Go to System Settings → Privacy & Security → Accessibility and enable permission for your terminal / Trae.",
    };
  } catch (err) {
    return {
      granted: false,
      name: PERMISSION_TYPES.ACCESSIBILITY,
      hint: "Go to System Settings → Privacy & Security → Accessibility and enable permission for your terminal / Trae.",
    };
  }
}

function macosCheckInputMonitoring() {
  return {
    granted: null, // cannot auto-check
    name: PERMISSION_TYPES.INPUT_MONITORING,
    hint: "If keyboard control doesn't work, go to System Settings → Privacy & Security → Input Monitoring.",
  };
}

// ============================================================
// Linux permission checks
// ============================================================
async function linuxCheckXdotool() {
  try {
    await execCmd("which xdotool");
    return {
      granted: true,
      name: "xdotool-available",
      hint: "",
    };
  } catch {
    return {
      granted: false,
      name: "xdotool-available",
      hint: "Install xdotool: sudo apt install xdotool (Debian/Ubuntu) or sudo dnf install xdotool (Fedora)",
    };
  }
}

async function linuxCheckScrot() {
  try {
    await execCmd("which scrot");
    return { granted: true, name: "scrot-available", hint: "" };
  } catch {
    // check for gnome-screenshot as alternative
    try {
      await execCmd("which gnome-screenshot");
      return { granted: true, name: "gnome-screenshot-available", hint: "" };
    } catch {
      return {
        granted: false,
        name: "screenshot-tool",
        hint: "Install a screenshot tool: sudo apt install scrot or sudo apt install gnome-screenshot",
      };
    }
  }
}

// ============================================================
// Windows permission checks
// ============================================================
function windowsCheck() {
  return {
    granted: true,
    name: "windows-permissions",
    hint: "Windows usually doesn't require special permissions for screen capture and input simulation.",
  };
}

// ============================================================
// Main permission check
// ============================================================
export async function checkAllPermissions() {
  // 启动速度优化：所有权限检查并行执行
  if (IS_MACOS) {
    const [screenRec, accessibility, inputMon] = await Promise.all([
      macosCheckScreenRecording(),
      macosCheckAccessibility(),
      Promise.resolve(macosCheckInputMonitoring()),
    ]);
    return [screenRec, accessibility, inputMon];
  } else if (IS_LINUX) {
    const [xdotool, scrot] = await Promise.all([
      linuxCheckXdotool(),
      linuxCheckScrot(),
    ]);
    return [xdotool, scrot];
  } else if (IS_WINDOWS) {
    return [windowsCheck()];
  }
  return [];
}

export async function hasScreenRecordingPermission() {
  const perms = await checkAllPermissions();
  const sr = perms.find((p) => p.name === PERMISSION_TYPES.SCREEN_RECORDING);
  if (sr && sr.reason === "display-asleep") {
    return { granted: null, reason: "display-asleep" };
  }
  return sr ? sr.granted : null;
}

export async function hasAccessibilityPermission() {
  const perms = await checkAllPermissions();
  const acc = perms.find((p) => p.name === PERMISSION_TYPES.ACCESSIBILITY);
  return acc ? acc.granted : null;
}

// ============================================================
// Run macOS preflight script
// ============================================================
export async function runMacOSPreflight() {
  if (!IS_MACOS) {
    console.log("[watchitai] Preflight only needed on macOS");
    return { success: true, platform: getPlatformName() };
  }

  // 先尝试唤醒屏幕，避免因屏幕休眠导致的误判
  const asleep = await isDisplayAsleep();
  if (asleep) {
    console.log("[watchitai] Display appears asleep, attempting to wake...");
    const wakeResult = await wakeDisplay();
    if (wakeResult.success) {
      console.log("[watchitai] Display woke successfully");
    } else {
      console.log("[watchitai] Could not auto-wake display, proceeding with check anyway");
    }
  }

  // 使用 JavaScript 权限检查替代 shell 脚本
  const perms = await checkAllPermissions();
  console.log(formatPermissions(perms));

  const missing = perms.filter((p) => p.granted === false);
  if (missing.length > 0) {
    console.log(`\n⚠️  ${missing.length} permission(s) missing!`);
    console.log("   Some features (screen capture / remote control) may not work.");
    console.log("\n💡 Go to System Settings → Privacy & Security to grant permissions.");
    return { success: false, error: "permissions-missing" };
  }

  const asleepPerm = perms.find((p) => p.reason === "display-asleep");
  if (asleepPerm) {
    console.log(`\n💤 Display is asleep.`);
    console.log("   Wake up your screen to enable screen sharing.");
    return { success: false, error: "display-asleep" };
  }

  return { success: true };
}

// ============================================================
// Format permissions for display
// ============================================================
export function formatPermissions(perms) {
  const lines = [];
  lines.push(`📋 Permissions Check (${getPlatformName()})`);
  lines.push("");
  for (const p of perms) {
    let status;
    if (p.granted === true) {
      status = "✅ Granted";
    } else if (p.granted === false) {
      status = "❌ Missing";
    } else if (p.reason === "display-asleep") {
      status = "💤 Display asleep";
    } else {
      status = "ℹ️  Cannot verify";
    }
    lines.push(`   ${status}  ${p.name}`);
    if (p.hint) {
      lines.push(`         ${p.hint}`);
    }
  }
  return lines.join("\n");
}

export default {
  PERMISSION_TYPES,
  checkAllPermissions,
  hasScreenRecordingPermission,
  hasAccessibilityPermission,
  runMacOSPreflight,
  formatPermissions,
};
