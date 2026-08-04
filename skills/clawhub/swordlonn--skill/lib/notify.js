/**
 * Cross-platform system notification module.
 * Uses node-notifier as primary backend, falls back to platform tools.
 * Supports Windows, macOS, and Linux.
 */

import { exec } from "child_process";
import { IS_WINDOWS, IS_MACOS, IS_LINUX } from "./platform.js";

let notifier = null;

async function getNotifier() {
  if (notifier !== null) return notifier;
  try {
    const mod = await import("node-notifier");
    notifier = mod.default || mod;
    console.log("[watchitai] Using node-notifier for system notifications");
    return notifier;
  } catch (e) {
    notifier = false;
    console.log("[watchitai] node-notifier not available, using platform fallback");
    return null;
  }
}

function execCmd(cmd) {
  return new Promise((resolve, reject) => {
    exec(cmd, (err, stdout, stderr) => {
      if (err) reject(err);
      else resolve({ stdout, stderr });
    });
  });
}

export async function showNotification(title, message = "", options = {}) {
  const n = await getNotifier();
  if (n) {
    try {
      n.notify({
        title,
        message,
        ...options,
      });
      return;
    } catch (e) {
      console.warn("[watchitai] node-notifier failed, falling back:", e.message);
    }
  }

  try {
    if (IS_MACOS) {
      await execCmd(
        `osascript -e 'display notification "${message.replace(/'/g, "''")}" with title "${title.replace(/'/g, "''")}"'`,
      );
    } else if (IS_WINDOWS) {
      const script = `
        Add-Type -AssemblyName System.Windows.Forms
        $n = New-Object System.Windows.Forms.NotifyIcon
        $n.Icon = [System.Drawing.SystemIcons]::Information
        $n.BalloonTipTitle = "${title.replace(/"/g, '\\"')}"
        $n.BalloonTipText = "${message.replace(/"/g, '\\"')}"
        $n.Visible = $true
        $n.ShowBalloonTip(5000)
      `;
      await execCmd(`powershell -Command "${script.replace(/"/g, '\\"')}"`);
    } else if (IS_LINUX) {
      try {
        await execCmd(
          `notify-send "${title.replace(/"/g, '\\"')}" "${message.replace(/"/g, '\\"')}"`,
        );
      } catch {
        console.log(`[watchitai] ${title}: ${message}`);
      }
    }
  } catch (e) {
    console.warn("[watchitai] Notification failed:", e.message);
  }
}

export async function showAlert(title, message = "") {
  try {
    if (IS_MACOS) {
      await execCmd(
        `osascript -e 'display dialog "${message.replace(/"/g, '\\"')}" with title "${title.replace(/"/g, '\\"')}" buttons {"OK"} default button 1'`,
      );
    } else if (IS_WINDOWS) {
      const script = `
        Add-Type -AssemblyName System.Windows.Forms
        [System.Windows.Forms.MessageBox]::Show("${message.replace(/"/g, '\\"')}", "${title.replace(/"/g, '\\"')}", [System.Windows.Forms.MessageBoxButtons]::OK)
      `;
      await execCmd(`powershell -Command "${script.replace(/"/g, '\\"')}"`);
    } else if (IS_LINUX) {
      try {
        await execCmd(
          `zenity --info --title="${title.replace(/"/g, '\\"')}" --text="${message.replace(/"/g, '\\"')}"`,
        );
      } catch {
        console.log(`[watchitai] ALERT - ${title}: ${message}`);
      }
    }
  } catch (e) {
    console.warn("[watchitai] Alert failed:", e.message);
  }
}

export default {
  showNotification,
  showAlert,
};
