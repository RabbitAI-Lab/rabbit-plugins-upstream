/**
 * Cross-platform screen capture module.
 *
 * Priority:
 *   1. Platform helper scripts (take_screenshot.py / .ps1)
 *   2. screenshot-desktop npm module
 *   3. Platform command fallbacks (screencapture, scrot, PowerShell)
 *
 * Includes permission detection and helpful error messages.
 */

import { exec, spawn } from "child_process";
import * as fs from "fs";
import * as os from "os";
import * as path from "path";
import { fileURLToPath } from "url";
import { IS_WINDOWS, IS_MACOS, IS_LINUX, getPlatformName } from "./platform.js";
import { warn, info, error } from "./utils.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const SCRIPTS_DIR = path.resolve(__dirname, "../scripts");

let screenshotDesktop = null;
let permissionWarned = { screenRecording: false };

async function getScreenshotModule() {
  if (screenshotDesktop !== null) return screenshotDesktop;
  try {
    if (IS_LINUX && !process.env.DISPLAY) {
      warn("[watchitai] No DISPLAY env, skipping screenshot-desktop (headless)");
      screenshotDesktop = false;
      return null;
    }
    const mod = await import("screenshot-desktop");
    const ss = mod.default || mod;
    screenshotDesktop = ss;
    info("[watchitai] Using screenshot-desktop for screen capture");
    return screenshotDesktop;
  } catch (e) {
    screenshotDesktop = false;
    return null;
  }
}

function execCmd(cmd, options = {}) {
  return new Promise((resolve, reject) => {
    const timeout = options.timeout || 10000;
    const child = exec(cmd, {
      ...options,
      timeout,
      killSignal: "SIGTERM",
    }, (err, stdout, stderr) => {
      if (err) reject(err);
      else resolve({ stdout, stderr });
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

function getTempFile(suffix = ".png") {
  return path.join(os.tmpdir(), `watchitai_${Date.now()}${suffix}`);
}

// ============================================================
// Permission error detection
// ============================================================
function isPermissionError(error) {
  const msg = (error.message || String(error)).toLowerCase();
  if (IS_MACOS) {
    return (
      msg.includes("could not create image") ||
      msg.includes("screen recording") ||
      msg.includes("operation not permitted") ||
      msg.includes("permission denied")
    );
  }
  if (IS_LINUX) {
    return msg.includes("permission denied");
  }
  return false;
}

function getPermissionHint() {
  if (IS_MACOS) {
    return [
      "",
      "💡 HINT: Screen Recording permission may be missing.",
      "   Go to System Settings → Privacy & Security → Screen Recording",
      "   and enable permission for your terminal / Trae.",
      "",
      "   Or run the preflight script:",
      `   bash ${path.join(SCRIPTS_DIR, "ensure_macos_permissions.sh")}`,
    ].join("\n");
  }
  if (IS_LINUX) {
    return [
      "",
      "💡 HINT: Make sure you have a screenshot tool installed:",
      "   sudo apt install scrot           (Debian/Ubuntu)",
      "   sudo dnf install scrot           (Fedora)",
      "   sudo pacman -S scrot             (Arch)",
    ].join("\n");
  }
  return "";
}

function warnPermissionOnce() {
  if (!permissionWarned.screenRecording) {
    permissionWarned.screenRecording = true;
    warn(getPermissionHint());
  }
}

// ============================================================
// Helper script based capture (preferred)
// ============================================================
async function captureWithHelper(mode = "temp", outPath = null) {
  const scriptPath = IS_WINDOWS
    ? path.join(SCRIPTS_DIR, "take_screenshot.ps1")
    : path.join(SCRIPTS_DIR, "take_screenshot.py");

  if (!fs.existsSync(scriptPath)) {
    return null;
  }

  let cmd;
  let timeout = 8000;

  if (IS_WINDOWS) {
    let args = `-ExecutionPolicy Bypass -File "${scriptPath}"`;
    if (outPath) args += ` -Path "${outPath}"`;
    else args += ` -Mode ${mode}`;
    cmd = `powershell ${args}`;
    timeout = 10000;
  } else {
    let args = `"${scriptPath}"`;
    if (outPath) args += ` --path "${outPath}"`;
    else args += ` --mode ${mode}`;
    cmd = `python3 ${args}`;
    timeout = 5000;
  }

  try {
    const { stdout } = await execCmdWithCleanup(cmd, { timeout });
    const savedPath = stdout.trim().split("\n")[0].trim();
    if (savedPath && fs.existsSync(savedPath)) {
      const buffer = fs.readFileSync(savedPath);
      if (mode === "temp" || outPath === null) {
        fs.unlink(savedPath, () => {});
      }
      return buffer;
    }
  } catch (e) {
    warn("[watchitai] helper script failed:", e.message);
  }
  return null;
}

const ACTIVE_CHILD_PROCESSES = new Set();
let screenshotServer = null;
let screenshotServerQueue = [];
let screenshotServerReady = false;

function cleanupChildProcess(child) {
  ACTIVE_CHILD_PROCESSES.delete(child);
}

function killChildProcess(child) {
  try {
    if (!child.killed) {
      child.kill("SIGTERM");
      setTimeout(() => {
        if (!child.killed) {
          child.kill("SIGKILL");
        }
      }, 2000);
    }
  } catch (e) {
    // ignore
  }
  cleanupChildProcess(child);
}

function execCmdWithCleanup(cmd, options = {}) {
  return new Promise((resolve, reject) => {
    const timeout = options.timeout || 10000;
    const child = exec(cmd, {
      ...options,
      maxBuffer: 50 * 1024 * 1024, // 50MB for screenshot data
      timeout,
      killSignal: "SIGTERM",
    }, (err, stdout, stderr) => {
      cleanupChildProcess(child);
      if (err) reject(err);
      else resolve({ stdout, stderr });
    });

    ACTIVE_CHILD_PROCESSES.add(child);

    child.on("error", (err) => {
      cleanupChildProcess(child);
      reject(err);
    });

    child.on("exit", (code, signal) => {
      if (signal === "SIGTERM" || signal === "SIGKILL") {
        cleanupChildProcess(child);
      }
    });
  });
}

async function startScreenshotServer() {
  if (screenshotServer) {
    return screenshotServer;
  }

  return new Promise((resolve, reject) => {
    const scriptPath = path.join(SCRIPTS_DIR, "take_screenshot.py");
    if (!fs.existsSync(scriptPath)) {
      reject(new Error("Screenshot script not found"));
      return;
    }

    const child = spawn("python3", [scriptPath, "--server"], {
      stdio: ["pipe", "pipe", "pipe"],
    });

    ACTIVE_CHILD_PROCESSES.add(child);

    let pendingResolve = null;
    let buffer = Buffer.alloc(0);
    let expectedLength = 0;

    child.stdout.on("data", (data) => {
      // 确保 data 是 Buffer 类型
      let chunk = Buffer.isBuffer(data) ? data : Buffer.from(data);

      // Process all complete messages in this chunk
      while (chunk.length > 0) {
        if (expectedLength > 0) {
          // We're reading binary image data
          const needed = expectedLength - buffer.length;
          const piece = chunk.slice(0, needed);
          buffer = Buffer.concat([buffer, piece]);
          chunk = chunk.slice(piece.length);

          if (buffer.length >= expectedLength) {
            const result = buffer.slice(0, expectedLength);
            buffer = Buffer.alloc(0);
            expectedLength = 0;

            const queued = screenshotServerQueue.shift();
            if (queued) {
              queued.resolve(result);
            }
            processServerQueue();
          }
        } else {
          // We're reading a text header line (OK <len>\n or ERROR <msg>\n)
          const nlIdx = chunk.indexOf(0x0a); // \n
          if (nlIdx === -1) {
            // No newline yet, buffer partial header
            buffer = Buffer.concat([buffer, chunk]);
            chunk = Buffer.alloc(0);
          } else {
            // Combine buffered partial header with new chunk up to newline
            const lineBytes = Buffer.concat([buffer, chunk.slice(0, nlIdx)]);
            chunk = chunk.slice(nlIdx + 1);
            buffer = Buffer.alloc(0);
            const line = lineBytes.toString("utf-8").trim();

            if (line.startsWith("OK ")) {
              expectedLength = parseInt(line.slice(3));
              if (isNaN(expectedLength)) {
                expectedLength = 0;
                const queued = screenshotServerQueue.shift();
                if (queued) queued.reject(new Error("Invalid response"));
                processServerQueue();
              } else {
                buffer = Buffer.alloc(0);
              }
            } else if (line.startsWith("ERROR ")) {
              expectedLength = 0;
              const queued = screenshotServerQueue.shift();
              if (queued) queued.reject(new Error(line.slice(7)));
              processServerQueue();
            }
          }
        }
      }
    });

    child.stderr.on("data", (data) => {
      warn("[watchitai] screenshot-server stderr:", data.toString().trim());
    });

    child.on("error", (err) => {
      cleanupChildProcess(child);
      screenshotServer = null;
      screenshotServerReady = false;
      reject(err);
    });

    child.on("exit", (code, signal) => {
      cleanupChildProcess(child);
      screenshotServer = null;
      screenshotServerReady = false;
      
      while (screenshotServerQueue.length > 0) {
        const queued = screenshotServerQueue.shift();
        queued.reject(new Error("Server exited"));
      }
    });

    setTimeout(() => {
      if (!screenshotServerReady) {
        screenshotServerReady = true;
        screenshotServer = child;
        resolve(child);
      }
    }, 1000);

    setTimeout(() => {
      if (!screenshotServerReady) {
        killChildProcess(child);
        reject(new Error("Server startup timeout"));
      }
    }, 5000);
  });
}

async function captureViaServer(options = {}) {
  if (!IS_MACOS && !IS_LINUX) {
    return null;
  }

  try {
    await startScreenshotServer();

    return new Promise((resolve, reject) => {
      const timeout = setTimeout(() => {
        const idx = screenshotServerQueue.findIndex(q => q === queued);
        if (idx !== -1) {
          screenshotServerQueue.splice(idx, 1);
        }
        reject(new Error("Capture timeout"));
      }, options.timeout || 15000);

      const queued = {
        resolve: (data) => {
          clearTimeout(timeout);
          resolve(data);
        },
        reject: (err) => {
          clearTimeout(timeout);
          reject(err);
        },
        sent: false,
        options,
      };

      screenshotServerQueue.push(queued);
      processServerQueue();
    });
  } catch (e) {
    warn("[watchitai] Server capture failed:", e.message);
    return null;
  }
}

function processServerQueue() {
  if (!screenshotServerReady || screenshotServerQueue.length === 0) {
    return;
  }

  const queued = screenshotServerQueue[0];
  if (queued && !queued.sent) {
    queued.sent = true;
    const cmd = JSON.stringify({
      action: "capture",
      quality: queued.options.quality,
      maxWidth: queued.options.maxWidth,
    }) + "\n";
    if (!screenshotServer || !screenshotServer.stdin || screenshotServer.stdin.destroyed) {
      warn("[watchitai] screenshotServer stdin not available");
      queued.reject(new Error("Server stdin not available"));
      screenshotServerQueue.shift();
      processServerQueue();
      return;
    }
    try {
      screenshotServer.stdin.write(cmd);
    } catch (e) {
      warn("[watchitai] Failed to write to server stdin:", e.message);
      queued.reject(e);
      screenshotServerQueue.shift();
      processServerQueue();
    }
  }
}

function stopScreenshotServer() {
  if (screenshotServer) {
    try {
      screenshotServer.stdin.write("QUIT\n");
    } catch (e) {
      // ignore
    }
    setTimeout(() => {
      killChildProcess(screenshotServer);
      screenshotServer = null;
      screenshotServerReady = false;
    }, 1000);
  }
}

export function killAllChildProcesses() {
  stopScreenshotServer();
  for (const child of ACTIVE_CHILD_PROCESSES) {
    killChildProcess(child);
  }
  ACTIVE_CHILD_PROCESSES.clear();
}

// ============================================================
// Main capture function
// ============================================================
export async function captureScreen(displayId = null, options = {}) {
  let lastError = null;

  const { quality = 85, maxWidth = null } = options;

  if (IS_LINUX && !process.env.DISPLAY) {
    const err = new Error("Cannot capture screen: no DISPLAY environment variable (headless environment)");
    warn("[watchitai] Skipping screen capture: headless environment (no DISPLAY)");
    throw err;
  }

  // 1. Try persistent server mode first (avoids process spawning)
  try {
    const serverResult = await captureViaServer({ quality, maxWidth });
    if (serverResult) {
      return serverResult;
    }
  } catch (e) {
    lastError = e;
    warn("[watchitai] server capture failed:", e.message);
  }

  // 2. Try helper script
  try {
    const helperResult = await captureWithHelper("temp");
    if (helperResult) {
      return helperResult;
    }
  } catch (e) {
    lastError = e;
    warn("[watchitai] helper script failed:", e.message);
  }

  // 3. Try screenshot-desktop
  try {
    const ss = await getScreenshotModule();
    if (ss) {
      const img = await Promise.race([
        ss(),
        new Promise((_, reject) => setTimeout(() => reject(new Error("screenshot-desktop timeout")), 10000)),
      ]);
      return img;
    }
  } catch (e) {
    lastError = e;
    if (isPermissionError(e)) {
      warnPermissionOnce();
    } else {
      warn("[watchitai] screenshot-desktop failed, falling back:", e.message);
    }
  }

  // 4. Fallback to platform commands
  const tmpFile = getTempFile();

  try {
    if (IS_MACOS) {
      let cmd = "screencapture -x ";
      if (displayId) cmd += `-D ${displayId} `;
      cmd += tmpFile;
      await execCmdWithCleanup(cmd, { timeout: 5000 });
    } else if (IS_WINDOWS) {
      const script = `
        Add-Type -AssemblyName System.Drawing
        Add-Type -AssemblyName System.Windows.Forms
        $bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
        $bitmap = New-Object System.Drawing.Bitmap($bounds.Width, $bounds.Height)
        $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
        $graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)
        $bitmap.Save("${tmpFile.replace(/\\/g, "\\\\")}", [System.Drawing.Imaging.ImageFormat]::Png)
        $graphics.Dispose()
        $bitmap.Dispose()
      `;
      await execCmdWithCleanup(`powershell -Command "${script.replace(/"/g, '\\"')}"`, { timeout: 8000 });
    } else if (IS_LINUX) {
      let cmd = "";
      try {
        await execCmdWithCleanup("which scrot");
        cmd = `scrot -o ${tmpFile}`;
      } catch {
        try {
          await execCmdWithCleanup("which gnome-screenshot");
          cmd = `gnome-screenshot -f ${tmpFile}`;
        } catch {
          cmd = `import -window root ${tmpFile}`;
        }
      }
      await execCmdWithCleanup(cmd, { timeout: 5000 });
    }

    if (fs.existsSync(tmpFile)) {
      const buffer = fs.readFileSync(tmpFile);
      fs.unlink(tmpFile, () => {});
      return buffer;
    } else {
      throw new Error("Screenshot file not created");
    }
  } catch (e) {
    if (isPermissionError(e)) {
      warnPermissionOnce();
    }
    error("[watchitai] Screen capture failed:", e.message);
    throw e;
  } finally {
    if (fs.existsSync(tmpFile)) {
      try {
        fs.unlinkSync(tmpFile);
      } catch {
        // ignore
      }
    }
  }
}

export async function getScreenSources() {
  const ss = await getScreenshotModule();
  if (ss && ss.listDisplays) {
    try {
      const displays = await ss.listDisplays();
      return displays.map((d, i) => ({
        id: d.id || String(i),
        name: d.name || `Display ${i + 1}`,
        width: d.width || 0,
        height: d.height || 0,
      }));
    } catch (e) {
      warn("[watchitai] listDisplays failed:", e.message);
    }
  }

  return [{ id: "0", name: "Primary Display", width: 0, height: 0 }];
}

export async function getScreenSize() {
  try {
    if (IS_MACOS) {
      const { stdout } = await execCmd(
        "system_profiler SPDisplaysDataType | grep Resolution",
      );
      const match = stdout.match(/(\d+)\s*x\s*(\d+)/);
      if (match) return { width: Number(match[1]), height: Number(match[2]) };
    } else if (IS_WINDOWS) {
      const script = `
        Add-Type -AssemblyName System.Windows.Forms
        $s = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
        $s.Width.ToString() + "," + $s.Height.ToString()
      `;
      const { stdout } = await execCmd(
        `powershell -Command "${script.replace(/"/g, '\\"')}"`,
      );
      const parts = stdout.trim().split(",").map(Number);
      return { width: parts[0], height: parts[1] };
    } else if (IS_LINUX) {
      if (!process.env.DISPLAY) {
        warn("[watchitai] No DISPLAY env, returning default screen size (headless)");
        return { width: 1920, height: 1080 };
      }
      try {
        const { stdout } = await execCmd("xrandr | grep '\\*'");
        const match = stdout.match(/(\d+)\s*x\s*(\d+)/);
        if (match) return { width: Number(match[1]), height: Number(match[2]) };
      } catch {
        // fall through
      }
    }
  } catch (e) {
    warn("[watchitai] getScreenSize failed:", e.message);
  }
  return { width: 1920, height: 1080 };
}

export async function saveScreenshotToFile(outputPath, displayId = null) {
  const buffer = await captureScreen(displayId);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, buffer);
  return outputPath;
}

export default {
  captureScreen,
  getScreenSources,
  getScreenSize,
  saveScreenshotToFile,
};
