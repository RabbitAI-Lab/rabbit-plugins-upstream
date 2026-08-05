#!/usr/bin/env node
/**
 * Platform Simulation Test Script
 * 
 * Run platform-specific code paths without needing actual Linux/Windows machines.
 * Sets PLATFORM_OVERRIDE environment variable to mock platform detection.
 * 
 * Usage:
 *   node test-platform.js linux    # Test Linux code paths
 *   node test-platform.js windows  # Test Windows code paths
 *   node test-platform.js macos    # Test macOS code paths
 */

import { spawn } from "child_process";
import * as path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const VALID_PLATFORMS = ["macos", "linux", "windows"];

function printUsage() {
  console.log("Platform Simulation Test Script");
  console.log("");
  console.log("Usage:");
  console.log("  node test-platform.js <platform> [test]");
  console.log("");
  console.log("Platforms:");
  console.log("  macos    - Test macOS code paths");
  console.log("  linux    - Test Linux code paths");
  console.log("  windows  - Test Windows code paths");
  console.log("");
  console.log("Tests:");
  console.log("  info     - Platform detection");
  console.log("  screen   - Screen capture module loading");
  console.log("  mouse    - Mouse control module loading");
  console.log("  keyboard - Keyboard control module loading");
  console.log("  all      - Run all tests (default)");
  console.log("");
}

function runTest(platform, testName) {
  return new Promise((resolve, reject) => {
    const platformEnv = platform === "windows" ? "win32" : platform === "linux" ? "linux" : "darwin";
    
    const tests = {
      info: ["node", "index.js", "info"],
      screen: ["node", "-e", `import('./lib/screen.js').then(m => { console.log('getScreenSize:', JSON.stringify(m.getScreenSize())); console.log('getScreenSources:', JSON.stringify(m.getScreenSources())); })`],
      mouse: ["node", "-e", `import('./lib/mouse.js').then(m => { console.log('Mouse module loaded'); })`],
      keyboard: ["node", "-e", `import('./lib/keyboard.js').then(m => { console.log('Keyboard module loaded'); })`],
      permissions: ["node", "index.js", "permissions"],
    };
    
    const cmd = tests[testName];
    if (!cmd) {
      reject(new Error(`Unknown test: ${testName}`));
      return;
    }
    
    console.log(`\n=== ${platform.toUpperCase()} - ${testName} ===`);
    
    const child = spawn(cmd[0], cmd.slice(1), {
      cwd: __dirname,
      env: { ...process.env, PLATFORM_OVERRIDE: platformEnv },
      stdio: "inherit",
    });
    
    child.on("exit", (code) => {
      if (code === 0) {
        console.log(`✅ ${platform.toUpperCase()} - ${testName}: PASSED`);
        resolve();
      } else {
        console.log(`❌ ${platform.toUpperCase()} - ${testName}: FAILED (code ${code})`);
        reject(new Error(`Test failed with code ${code}`));
      }
    });
    
    child.on("error", (err) => {
      console.log(`❌ ${platform.toUpperCase()} - ${testName}: ERROR - ${err.message}`);
      reject(err);
    });
  });
}

async function main() {
  const platform = process.argv[2];
  const test = process.argv[3] || "all";
  
  if (!platform || !VALID_PLATFORMS.includes(platform)) {
    printUsage();
    process.exit(1);
  }
  
  console.log(`🎯 Testing platform: ${platform}`);
  console.log("");
  
  const allTests = ["info", "screen", "mouse", "keyboard", "permissions"];
  const testsToRun = test === "all" ? allTests : [test];
  
  let passed = 0;
  let failed = 0;
  
  for (const t of testsToRun) {
    try {
      await runTest(platform, t);
      passed++;
    } catch (e) {
      failed++;
    }
  }
  
  console.log(`\n=====================================`);
  console.log(`Results: ${passed} passed, ${failed} failed`);
  console.log(`=====================================`);
  
  if (failed > 0) {
    process.exit(1);
  }
}

main().catch((e) => {
  console.error(e.message);
  process.exit(1);
});