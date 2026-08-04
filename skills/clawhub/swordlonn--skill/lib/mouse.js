import * as path from "path";
import { fileURLToPath } from "url";
import { IS_WINDOWS, IS_MACOS, IS_LINUX } from "./platform.js";
import { execCmd, sanitizeNumber, wrapWithPermissionCheck } from "./utils.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let nutMouse = null;

async function getNutMouse() {
  if (nutMouse !== null) return nutMouse;
  try {
    const nut = await import("@nut-tree/nut-js");
    nutMouse = nut.mouse;
    console.log("[watchitai] Using nut.js for mouse control");
    return nutMouse;
  } catch (e) {
    nutMouse = false;
    console.log("[watchitai] nut.js not available, using platform fallback");
    return null;
  }
}

export async function moveMouse(x, y) {
  x = sanitizeNumber(x, 0, 10000);
  y = sanitizeNumber(y, 0, 10000);

  const mouse = await getNutMouse();
  if (mouse) {
    await mouse.setPosition({ x, y });
    return;
  }

  if (IS_MACOS) {
    await execCmd(
      `osascript -e 'tell application "System Events" to set mouse location to {${x}, ${y}}'`,
    );
  } else if (IS_WINDOWS) {
    const script = `
      Add-Type -AssemblyName System.Windows.Forms
      [System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point(${x}, ${y})
    `;
    await execCmd(`powershell -Command "${script.replace(/"/g, '\\"')}"`);
  } else if (IS_LINUX) {
    await execCmd(`xdotool mousemove ${x} ${y}`);
  }
}

export async function mouseDown(button = "left") {
  const validButtons = ["left", "right", "middle"];
  if (!validButtons.includes(button)) button = "left";

  const mouse = await getNutMouse();
  if (mouse) {
    const { Button } = await import("@nut-tree/nut-js");
    const btnMap = { left: Button.LEFT, right: Button.RIGHT, middle: Button.MIDDLE };
    await mouse.pressButton(btnMap[button] || Button.LEFT);
    return;
  }

  if (IS_MACOS) {
    const btnNum = button === "right" ? 2 : button === "middle" ? 3 : 1;
    await execCmd(`osascript -e 'tell application "System Events" to click mouse button ${btnNum}'`);
  } else if (IS_WINDOWS) {
    const script = `
      Add-Type -AssemblyName System.Windows.Forms
      $signature = @"
      [DllImport("user32.dll", CharSet=CharSet.Auto, CallingConvention=CallingConvention.StdCall)]
      public static extern void mouse_event(long dwFlags, long dx, long dy, long cButtons, long dwExtraInfo);
      "@
      $MouseEvent = Add-Type -memberDefinition $signature -name "MouseEvent" -namespace Win32Functions -passThru
      $MouseEvent::mouse_event(0x0002, 0, 0, 0, 0)
    `;
    await execCmd(`powershell -Command "${script.replace(/"/g, '\\"')}"`);
  } else if (IS_LINUX) {
    const btnNum = button === "right" ? 3 : button === "middle" ? 2 : 1;
    await execCmd(`xdotool mousedown ${btnNum}`);
  }
}

export async function mouseUp(button = "left") {
  const validButtons = ["left", "right", "middle"];
  if (!validButtons.includes(button)) button = "left";

  const mouse = await getNutMouse();
  if (mouse) {
    const { Button } = await import("@nut-tree/nut-js");
    const btnMap = { left: Button.LEFT, right: Button.RIGHT, middle: Button.MIDDLE };
    await mouse.releaseButton(btnMap[button] || Button.LEFT);
    return;
  }

  if (IS_MACOS) {
    try {
      await execCmd(`cliclick ku:${button === "right" ? "right" : button === "middle" ? "middle" : "left"}`);
    } catch {
      console.warn("[watchitai] mouseUp not fully supported on macOS without cliclick");
    }
  } else if (IS_WINDOWS) {
    const script = `
      Add-Type -AssemblyName System.Windows.Forms
      $signature = @"
      [DllImport("user32.dll", CharSet=CharSet.Auto, CallingConvention=CallingConvention.StdCall)]
      public static extern void mouse_event(long dwFlags, long dx, long dy, long cButtons, long dwExtraInfo);
      "@
      $MouseEvent = Add-Type -memberDefinition $signature -name "MouseEvent" -namespace Win32Functions -passThru
      $MouseEvent::mouse_event(0x0004, 0, 0, 0, 0)
    `;
    await execCmd(`powershell -Command "${script.replace(/"/g, '\\"')}"`);
  } else if (IS_LINUX) {
    const btnNum = button === "right" ? 3 : button === "middle" ? 2 : 1;
    await execCmd(`xdotool mouseup ${btnNum}`);
  }
}

export async function clickMouse(button = "left") {
  const validButtons = ["left", "right", "middle"];
  if (!validButtons.includes(button)) button = "left";

  const mouse = await getNutMouse();
  if (mouse) {
    const { Button } = await import("@nut-tree/nut-js");
    const btnMap = { left: Button.LEFT, right: Button.RIGHT, middle: Button.MIDDLE };
    await mouse.click(btnMap[button] || Button.LEFT);
    return;
  }

  if (IS_MACOS) {
    const btnNum = button === "right" ? 2 : button === "middle" ? 3 : 1;
    await execCmd(
      `osascript -e 'tell application "System Events" to click mouse button ${btnNum}'`,
    );
  } else if (IS_WINDOWS) {
    await mouseDown(button);
    await new Promise((r) => setTimeout(r, 50));
    await mouseUp(button);
  } else if (IS_LINUX) {
    const btnNum = button === "right" ? 3 : button === "middle" ? 2 : 1;
    await execCmd(`xdotool click ${btnNum}`);
  }
}

export async function getMousePosition() {
  const mouse = await getNutMouse();
  if (mouse) {
    const pos = await mouse.getPosition();
    return { x: pos.x, y: pos.y };
  }

  if (IS_MACOS) {
    const { stdout } = await execCmd(
      `osascript -e 'tell application "System Events" to get mouse location'`,
    );
    const parts = stdout.trim().split(", ").map(Number);
    return { x: parts[0], y: parts[1] };
  } else if (IS_WINDOWS) {
    const script = `
      Add-Type -AssemblyName System.Windows.Forms
      [System.Windows.Forms.Cursor]::Position.X.ToString() + "," + [System.Windows.Forms.Cursor]::Position.Y.ToString()
    `;
    const { stdout } = await execCmd(
      `powershell -Command "${script.replace(/"/g, '\\"')}"`,
    );
    const parts = stdout.trim().split(",").map(Number);
    return { x: parts[0], y: parts[1] };
  } else if (IS_LINUX) {
    const { stdout } = await execCmd(`xdotool getmouselocation`);
    const match = stdout.match(/x:(\d+).*y:(\d+)/);
    return match ? { x: Number(match[1]), y: Number(match[2]) } : { x: 0, y: 0 };
  }
  return { x: 0, y: 0 };
}

export async function scrollMouse(deltaX = 0, deltaY = 0) {
  deltaX = sanitizeNumber(deltaX, -1000, 1000);
  deltaY = sanitizeNumber(deltaY, -1000, 1000);

  const mouse = await getNutMouse();
  if (mouse) {
    try {
      const { ScrollDirection } = await import("@nut-tree/nut-js");
      if (deltaY !== 0) {
        const direction = deltaY > 0 ? ScrollDirection.DOWN : ScrollDirection.UP;
        await mouse.scroll(Math.abs(deltaY), direction);
      }
      return;
    } catch (e) {
      console.warn("[watchitai] nut.js scroll failed, falling back:", e.message);
    }
  }

  if (IS_MACOS) {
    try {
      await execCmd(`cliclick sc:${-deltaY}`);
    } catch {
      console.warn("[watchitai] scroll not supported on macOS without cliclick");
    }
  } else if (IS_WINDOWS) {
    const script = `
      $signature = @"
      [DllImport("user32.dll", CharSet=CharSet.Auto, CallingConvention=CallingConvention.StdCall)]
      public static extern void mouse_event(long dwFlags, long dx, long dy, long cButtons, long dwExtraInfo);
      "@
      $MouseEvent = Add-Type -memberDefinition $signature -name "MouseEvent" -namespace Win32Functions -passThru
      $MouseEvent::mouse_event(0x0800, 0, 0, ${deltaY * 120}, 0)
    `;
    await execCmd(`powershell -Command "${script.replace(/"/g, '\\"')}"`);
  } else if (IS_LINUX) {
    const steps = Math.abs(Math.round(deltaY / 100));
    const btn = deltaY > 0 ? 5 : 4;
    for (let i = 0; i < Math.max(1, steps); i++) {
      await execCmd(`xdotool click ${btn}`);
    }
  }
}

export default {
  moveMouse: wrapWithPermissionCheck(moveMouse, "moveMouse"),
  mouseDown: wrapWithPermissionCheck(mouseDown, "mouseDown"),
  mouseUp: wrapWithPermissionCheck(mouseUp, "mouseUp"),
  clickMouse: wrapWithPermissionCheck(clickMouse, "clickMouse"),
  getMousePosition: wrapWithPermissionCheck(getMousePosition, "getMousePosition"),
  scrollMouse: wrapWithPermissionCheck(scrollMouse, "scrollMouse"),
};
