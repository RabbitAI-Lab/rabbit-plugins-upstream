/**
 * Platform detection and utilities for cross-platform support.
 * Supports Windows, macOS, and Linux.
 * 
 * For testing, set PLATFORM_OVERRIDE environment variable to:
 *   - win32 (Windows)
 *   - darwin (macOS)
 *   - linux (Linux)
 */

export const PLATFORM = process.env.PLATFORM_OVERRIDE || process.platform;
export const IS_WINDOWS = PLATFORM === "win32";
export const IS_MACOS = PLATFORM === "darwin";
export const IS_LINUX = PLATFORM === "linux";

export function getPlatformName() {
  if (IS_WINDOWS) return "windows";
  if (IS_MACOS) return "macos";
  if (IS_LINUX) return "linux";
  return PLATFORM;
}

export function getOSInfo() {
  return {
    platform: getPlatformName(),
    arch: process.arch,
    release: process.getSystemVersion ? process.getSystemVersion() : "unknown",
  };
}

export default {
  PLATFORM,
  IS_WINDOWS,
  IS_MACOS,
  IS_LINUX,
  getPlatformName,
  getOSInfo,
};
