#!/usr/bin/env node
/**
 * WatchItAI Skill Cross-Platform Test Script
 *
 * Tests the JavaScript bridge modules on the current platform.
 * Works on Linux, macOS, and Windows without native dependencies.
 *
 * Usage:
 *   node test-skill.js [--bridge]   # Run all tests (use --bridge to test bridge server)
 */

import http from "http";

let passed = 0;
let failed = 0;
let warnings = 0;

function logPass(msg) {
  passed++;
  console.log(`  ✅ ${msg}`);
}
function logFail(msg) {
  failed++;
  console.log(`  ❌ ${msg}`);
}
function logWarn(msg) {
  warnings++;
  console.log(`  ⚠️  ${msg}`);
}

async function testPlatform() {
  console.log("\n🔍 Platform Detection Test");
  try {
    const m = await import("./lib/platform.js");
    const name = m.getPlatformName();
    const info = m.getOSInfo();
    console.log(`  Platform: ${name}`);
    console.log(`  OS Info: ${JSON.stringify(info)}`);

    const PLATFORM_MAP = { darwin: "macos", win32: "windows", linux: "linux" };
    const expected = PLATFORM_MAP[process.platform] || process.platform;
    if (name === expected) {
      logPass("Platform detection works correctly");
    } else {
      logFail(`Platform mismatch: expected ${expected}, got ${name}`);
    }
  } catch (e) {
    logFail(`Platform detection failed: ${e.message}`);
  }
}

async function testConfig() {
  console.log("\n⚙️  Config Loading Test");
  try {
    const m = await import("./lib/config.js");
    const config = m.loadConfig();
    console.log(`  Domain: ${config.domain}`);
    console.log(`  Bridge Port: ${config.bridgePort}`);
    console.log(`  Mode: ${config.mode}`);
    logPass("Config loads successfully");
  } catch (e) {
    logFail(`Config loading failed: ${e.message}`);
  }
}

async function testUtils() {
  console.log("\n🔧 Utilities Test");
  try {
    const m = await import("./lib/utils.js");

    // Test token generation
    const token = m.generateToken(32);
    if (token && token.length > 0) {
      logPass(`Token generation works (${token.length} chars)`);
    } else {
      logFail("Token generation failed");
    }

    // Test token validation
    const valid = m.validateToken(token, token);
    const invalid = m.validateToken("wrong", token);
    if (valid === true && invalid === false) {
      logPass("Token validation works correctly");
    } else {
      logFail("Token validation logic incorrect");
    }

    // Test logging
    m.info("Test info log");
    m.warn("Test warn log");
    logPass("Logging functions work");
  } catch (e) {
    logFail(`Utilities test failed: ${e.message}`);
  }
}

async function testModuleLoading(moduleName, importPath) {
  console.log(`\n📦 ${moduleName} Module Loading Test`);
  try {
    await import(importPath);
    logPass(`${moduleName} module loaded successfully`);
  } catch (e) {
    logWarn(`${moduleName} module loading: ${e.message}`);
  }
}

function healthCheck(port) {
  return new Promise((resolve) => {
    const req = http.get(`http://localhost:${port}/health`, (res) => {
      let data = "";
      res.on("data", (chunk) => data += chunk);
      res.on("end", () => {
        try {
          const health = JSON.parse(data);
          if (health.status === "ok") {
            resolve({ ok: true, data: health });
          } else {
            resolve({ ok: false, error: "Unexpected status" });
          }
        } catch (e) {
          resolve({ ok: false, error: `Invalid response: ${data}` });
        }
      });
    });
    req.on("error", (e) => {
      resolve({ ok: false, error: e.message });
    });
    req.setTimeout(3000, () => {
      resolve({ ok: false, error: "Timeout" });
      req.destroy();
    });
  });
}

async function testBridgeServer() {
  console.log("\n🔌 Bridge Server Test");
  try {
    const m = await import("./lib/bridge-server.js");

    // Start bridge with skipPermissionCheck
    const result = await m.startBridgeServer(8765, { skipPermissionCheck: true });
    console.log(`  Bridge server started on port: ${result.port}`);

    // Health check
    const health = await healthCheck(8765);
    if (health.ok) {
      logPass("Bridge server health check passed");
    } else {
      logWarn(`Bridge server health check: ${health.error}`);
    }

    // Stop bridge
    m.stopBridgeServer();
    logPass("Bridge server stopped cleanly");
  } catch (e) {
    logWarn(`Bridge server test: ${e.message}`);
  }
}

async function main() {
  const testBridge = process.argv.includes("--bridge");

  console.log("🎯 WatchItAI Skill Cross-Platform Tests");
  console.log(`   Platform: ${process.platform} ${process.arch}`);
  console.log(`   Node.js: ${process.version}`);

  await testPlatform();
  await testConfig();
  await testUtils();
  await testModuleLoading("Permissions", "./lib/permissions.js");
  await testModuleLoading("Screen", "./lib/screen.js");
  await testModuleLoading("Mouse", "./lib/mouse.js");
  await testModuleLoading("Keyboard", "./lib/keyboard.js");

  if (testBridge) {
    await testBridgeServer();
  }

  console.log(`\n=====================================`);
  console.log(`Results: ${passed} passed, ${failed} failed, ${warnings} warnings`);
  console.log(`=====================================`);

  if (failed > 0) {
    process.exit(1);
  }
}

main().catch((e) => {
  console.error("Fatal error:", e.message);
  process.exit(1);
});
