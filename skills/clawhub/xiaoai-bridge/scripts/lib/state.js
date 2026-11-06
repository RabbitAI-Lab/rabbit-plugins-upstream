/**
 * 会话缓存目录与凭据文件的强制校验。
 *
 * 背景：上游 `@mi-gpt/miot@1.2.2` 在登录成功后把包含 passToken / serviceToken /
 * ssecurity 的会话写入 `process.cwd()/.mi.json`（相对路径、固定文件名、默认权限
 * 受 umask 影响）。ClawHub 审计 T09 指出：旧实现接受任意 `XIAOAI_STATE_DIR`
 * （包括共享临时目录里被其他用户预先创建的目录），并且在 chmod 失败时静默继续，
 * 导致凭据可能落进攻击者可读的目录。
 *
 * 本模块的处理口径：
 * 1. 默认目录改为当前用户的私有状态目录，不再默认使用 `os.tmpdir()`；
 * 2. 目录必须是真实目录（拒绝符号链接）、属主必须是当前用户（POSIX），
 *    权限必须收紧到 0700 并复验；
 * 3. 缓存文件在登录前以 0600 独占预创建，登录后复验类型/属主/权限/硬链接；
 * 4. 任何校验失败一律抛 ConfigError 中止，不再忽略错误；
 * 5. 只有“权限无法强制 / ACL 无法验证”这一类情况允许用
 *    `XIAOAI_ALLOW_INSECURE_STATE_DIR=true` 显式确认后继续。
 */

import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import { ConfigError } from "./errors.js";

/** 状态目录名（各平台固定使用）。 */
export const STATE_DIR_NAME = "xiaoai-bridge";
/** 上游 MIoT/MiNA 写死的会话缓存文件名。 */
export const CACHE_FILE_NAME = ".mi.json";
export const STATE_DIR_ENV_VAR = "XIAOAI_STATE_DIR";
export const ALLOW_INSECURE_ENV_VAR = "XIAOAI_ALLOW_INSECURE_STATE_DIR";
/** 超过这个大小的“缓存文件”一定不是上游写的，直接视为异常。 */
export const MAX_CACHE_FILE_BYTES = 1024 * 1024;

const INSECURE_HINT =
  "如确需在无法强制权限的位置运行（例如单用户机器或不受支持的文件系统），" +
  `${ALLOW_INSECURE_ENV_VAR}=true 后重试，并自行确认该目录只有当前用户可以读写。`;

const TRUE_VALUES = new Set(["1", "true", "yes", "on"]);

function noop() {}

function isTrue(value) {
  return TRUE_VALUES.has(String(value ?? "").trim().toLowerCase());
}

function currentUid() {
  return typeof process.getuid === "function" ? process.getuid() : null;
}

/** 把 mode 格式化成 0o700 这样的字符串，便于日志阅读。 */
function formatMode(mode) {
  return `0${(mode & 0o777).toString(8).padStart(3, "0")}`;
}

function pathImpl(platform) {
  return platform === "win32" ? path.win32 : path.posix;
}

function isPathInside(parent, child, platform) {
  const impl = pathImpl(platform);
  const relative = impl.relative(impl.resolve(parent), impl.resolve(child));
  return relative === "" || (!relative.startsWith("..") && !impl.isAbsolute(relative));
}

function lstatOrNull(fsImpl, file) {
  try {
    return fsImpl.lstatSync(file);
  } catch (error) {
    if (error?.code === "ENOENT") {
      return null;
    }
    throw new ConfigError(`无法访问 ${file}：${error.message}`);
  }
}

/**
 * 解析默认状态目录：当前用户的私有目录。
 *
 * - Windows：`%LOCALAPPDATA%\xiaoai-bridge`
 * - macOS：`~/Library/Application Support/xiaoai-bridge`
 * - 其它：`$XDG_STATE_HOME/xiaoai-bridge`（需为绝对路径），否则 `~/.local/state/xiaoai-bridge`
 *
 * 无法确定用户主目录时直接报错，绝不回落到 `os.tmpdir()`。
 *
 * @param {{ platform?: string, env?: Record<string, string | undefined>, homedir?: string }} [options]
 * @returns {string}
 */
export function resolveDefaultStateDir(options = {}) {
  const platform = options.platform ?? process.platform;
  const env = options.env ?? process.env;
  const homedir = String(options.homedir ?? os.homedir() ?? "").trim();
  const impl = pathImpl(platform);

  if (platform === "win32") {
    const localAppData = String(env.LOCALAPPDATA ?? "").trim();
    if (localAppData && impl.isAbsolute(localAppData)) {
      return impl.join(localAppData, STATE_DIR_NAME);
    }
    if (homedir) {
      return impl.join(homedir, "AppData", "Local", STATE_DIR_NAME);
    }
    throw new ConfigError(
      `无法确定用户 AppData 目录，请显式设置 ${STATE_DIR_ENV_VAR} 指向当前用户的私有目录`,
    );
  }

  if (platform === "darwin" && homedir) {
    return impl.join(homedir, "Library", "Application Support", STATE_DIR_NAME);
  }

  const xdgStateHome = String(env.XDG_STATE_HOME ?? "").trim();
  if (xdgStateHome && impl.isAbsolute(xdgStateHome)) {
    return impl.join(xdgStateHome, STATE_DIR_NAME);
  }
  if (homedir) {
    return impl.join(homedir, ".local", "state", STATE_DIR_NAME);
  }

  throw new ConfigError(
    `无法确定用户主目录，请显式设置 ${STATE_DIR_ENV_VAR} 指向当前用户的私有目录`,
  );
}

/**
 * 解析实际使用的状态目录（环境变量优先）。
 *
 * @param {Record<string, string | undefined>} [env]
 * @param {{ platform?: string, homedir?: string }} [options]
 * @returns {{ dir: string, source: "env" | "default", allowInsecure: boolean }}
 */
export function resolveStateDir(env = process.env, options = {}) {
  const raw = String(env[STATE_DIR_ENV_VAR] ?? "").trim();
  const allowInsecure = isTrue(env[ALLOW_INSECURE_ENV_VAR]);
  if (raw) {
    return { dir: path.resolve(raw), source: "env", allowInsecure };
  }
  const dir = resolveDefaultStateDir({ ...options, env });
  return { dir: path.resolve(dir), source: "default", allowInsecure };
}

/**
 * 判断目录是否满足“只有当前用户可以读写”。
 *
 * 纯函数，便于离线测试（stats 可以是真实 fs.Stats 或等价对象）。
 *
 * @param {fs.Stats | { isSymbolicLink: () => boolean, isDirectory: () => boolean, mode: number, uid?: number }} stats
 * @param {{ platform?: string, uid?: number | null, dir?: string, env?: Record<string, string | undefined>, homedir?: string }} [ctx]
 * @returns {{ ok: boolean, code: string, message: string, overridable: boolean }}
 */
export function evaluateDirSecurity(stats, ctx = {}) {
  const platform = ctx.platform ?? process.platform;
  const dir = ctx.dir ?? "";

  if (!stats) {
    return { ok: false, code: "MISSING", message: `会话缓存目录不存在：${dir}`, overridable: false };
  }
  if (typeof stats.isSymbolicLink === "function" && stats.isSymbolicLink()) {
    return {
      ok: false,
      code: "SYMLINK",
      message: `会话缓存目录不能是符号链接：${dir}。请改用真实目录，或通过 ${STATE_DIR_ENV_VAR} 指定其他私有目录。`,
      overridable: false,
    };
  }
  if (typeof stats.isDirectory === "function" && !stats.isDirectory()) {
    return {
      ok: false,
      code: "NOT_DIRECTORY",
      message: `会话缓存路径已存在但不是目录：${dir}。请删除该路径或改用其他目录。`,
      overridable: false,
    };
  }

  if (platform === "win32") {
    if (isWindowsSharedPath(dir, ctx)) {
      return {
        ok: false,
        code: "FOREIGN_LOCATION",
        message:
          `会话缓存目录位于公共目录或其他用户的配置目录内：${dir}。` +
          `该位置无法保证只有当前用户可以访问，拒绝写入凭据；请改用当前用户目录内的路径。`,
        overridable: false,
      };
    }
    if (!isWindowsUserPath(dir, ctx)) {
      return {
        ok: false,
        code: "ACL_UNVERIFIABLE",
        message:
          `会话缓存目录不在当前用户目录内，无法验证访问控制：${dir}。` +
          `请把 ${STATE_DIR_ENV_VAR} 指向用户目录内的路径。${INSECURE_HINT}`,
        overridable: true,
      };
    }
    return { ok: true, code: "OK", message: "", overridable: false };
  }

  const uid = ctx.uid ?? null;
  if (uid !== null && typeof stats.uid === "number" && stats.uid !== uid) {
    return {
      ok: false,
      code: "FOREIGN_OWNER",
      message:
        `会话缓存目录属于其他用户（uid=${stats.uid}，当前 uid=${uid}）：${dir}。` +
        `拒绝把凭据写入该目录；请改用私有目录，或执行 chown -R ${uid} "${dir}" 修正属主。`,
      overridable: false,
    };
  }
  if ((stats.mode & 0o077) !== 0) {
    return {
      ok: false,
      code: "MODE_TOO_OPEN",
      message: `会话缓存目录权限过宽（${formatMode(stats.mode)}）：${dir}，同组或其他用户可读写。`,
      overridable: true,
    };
  }
  if ((stats.mode & 0o700) !== 0o700) {
    return {
      ok: false,
      code: "MODE_TOO_OPEN",
      message: `会话缓存目录缺少属主读写执行权限（${formatMode(stats.mode)}）：${dir}。`,
      overridable: true,
    };
  }
  return { ok: true, code: "OK", message: "", overridable: false };
}

/**
 * 判断缓存文件是否安全（普通文件、属主正确、0600、非硬链接、大小合理）。
 *
 * @param {fs.Stats} stats
 * @param {{ platform?: string, uid?: number | null, file?: string }} [ctx]
 * @returns {{ ok: boolean, code: string, message: string, overridable: boolean }}
 */
export function evaluateFileSecurity(stats, ctx = {}) {
  const platform = ctx.platform ?? process.platform;
  const file = ctx.file ?? "";

  if (!stats) {
    return {
      ok: false,
      code: "MISSING",
      message: `会话缓存文件不存在：${file}。请确认目录可写（${STATE_DIR_ENV_VAR}）。`,
      overridable: false,
    };
  }
  if (typeof stats.isSymbolicLink === "function" && stats.isSymbolicLink()) {
    return {
      ok: false,
      code: "SYMLINK",
      message: `会话缓存不能是符号链接：${file}。`,
      overridable: false,
    };
  }
  if (typeof stats.isFile === "function" && !stats.isFile()) {
    return {
      ok: false,
      code: "NOT_FILE",
      message: `会话缓存不是普通文件：${file}。`,
      overridable: false,
    };
  }
  if (typeof stats.size === "number" && stats.size > MAX_CACHE_FILE_BYTES) {
    return {
      ok: false,
      code: "TOO_LARGE",
      message: `会话缓存文件异常过大（${stats.size} 字节）：${file}。`,
      overridable: false,
    };
  }
  if (typeof stats.nlink === "number" && stats.nlink > 1) {
    return {
      ok: false,
      code: "HARDLINK",
      message: `会话缓存存在多余硬链接（nlink=${stats.nlink}）：${file}。`,
      overridable: false,
    };
  }
  if (platform === "win32") {
    return { ok: true, code: "OK", message: "", overridable: false };
  }

  const uid = ctx.uid ?? null;
  if (uid !== null && typeof stats.uid === "number" && stats.uid !== uid) {
    return {
      ok: false,
      code: "FOREIGN_OWNER",
      message: `会话缓存属于其他用户（uid=${stats.uid}）：${file}。`,
      overridable: false,
    };
  }
  if ((stats.mode & 0o077) !== 0) {
    return {
      ok: false,
      code: "MODE_TOO_OPEN",
      message: `会话缓存权限过宽（${formatMode(stats.mode)}）：${file}，凭据可被其他用户读取。`,
      overridable: true,
    };
  }
  if ((stats.mode & 0o600) !== 0o600) {
    return {
      ok: false,
      code: "MODE_TOO_OPEN",
      message: `会话缓存缺少属主读写权限（${formatMode(stats.mode)}）：${file}。`,
      overridable: true,
    };
  }
  return { ok: true, code: "OK", message: "", overridable: false };
}

function isWindowsSharedPath(dir, ctx) {
  const env = ctx.env ?? process.env;
  const homedir = String(ctx.homedir ?? os.homedir() ?? "").trim();
  const target = path.win32.resolve(String(dir));

  const sharedRoots = [
    env.ProgramData,
    env.PUBLIC,
    env.SystemRoot ? path.win32.join(env.SystemRoot, "Temp") : null,
    env.SystemRoot,
    env.windir,
  ]
    .map((value) => String(value ?? "").trim())
    .filter((value) => value && path.win32.isAbsolute(value));

  if (sharedRoots.some((root) => isPathInside(root, target, "win32"))) {
    return true;
  }

  // C:\Users\<name>：只允许当前用户自己的 profile，其它 profile 与 Users 根目录一律拒绝。
  const usersRoot = homedir ? path.win32.dirname(homedir) : "";
  if (usersRoot && isPathInside(usersRoot, target, "win32")) {
    const relative = path.win32.relative(usersRoot, target);
    const firstSegment = relative.split("\\")[0] ?? "";
    if (relative === "" || firstSegment.toLowerCase() !== path.win32.basename(homedir).toLowerCase()) {
      return true;
    }
  }
  return false;
}

function isWindowsUserPath(dir, ctx) {
  const env = ctx.env ?? process.env;
  const homedir = String(ctx.homedir ?? os.homedir() ?? "").trim();
  const roots = [homedir, env.LOCALAPPDATA, env.APPDATA, env.USERPROFILE]
    .map((value) => String(value ?? "").trim())
    .filter((value) => value && path.win32.isAbsolute(value));
  if (roots.length === 0) {
    return false;
  }
  return roots.some((root) => isPathInside(root, dir, "win32"));
}

/**
 * 目录是否“专用”：为空或只含 `.mi.json`。
 * 只有专用目录才允许自动收紧权限，避免把 $HOME 等项目/共享目录改坏。
 */
function isDedicatedStateDir(fsImpl, dir) {
  try {
    return fsImpl.readdirSync(dir).every((name) => name === CACHE_FILE_NAME);
  } catch {
    return false;
  }
}

function normalizeOptions(options) {
  return {
    fs: options.fs ?? fs,
    platform: options.platform ?? process.platform,
    uid: options.uid !== undefined ? options.uid : currentUid(),
    env: options.env ?? process.env,
    homedir: options.homedir ?? os.homedir(),
    allowInsecure: options.allowInsecure === true,
    warn: options.warn ?? noop,
  };
}

/**
 * 创建并校验私有状态目录（0700，属主为当前用户）。
 *
 * @param {string} dir
 * @param {{ fs?: typeof fs, platform?: string, uid?: number | null, allowInsecure?: boolean, env?: Record<string, string | undefined>, homedir?: string, warn?: (line: string) => void }} [options]
 * @returns {{ dir: string, tightened: boolean, insecureAck: boolean, warnings: string[], mode: string }}
 */
export function ensureStateDir(dir, options = {}) {
  const { fs: fsImpl, platform, uid, env, homedir, allowInsecure, warn } = normalizeOptions(options);
  const warnings = [];
  const target = path.resolve(String(dir));
  const ctx = { platform, uid, dir: target, env, homedir };

  let stats = lstatOrNull(fsImpl, target);
  if (!stats) {
    try {
      fsImpl.mkdirSync(target, { recursive: true, mode: 0o700 });
    } catch (error) {
      throw new ConfigError(
        `无法创建会话缓存目录 ${target}：${error.message}。可通过 ${STATE_DIR_ENV_VAR} 指定其他目录。`,
      );
    }
    stats = lstatOrNull(fsImpl, target);
    if (!stats) {
      throw new ConfigError(`会话缓存目录创建后仍不可访问：${target}`);
    }
  }

  let tightened = false;
  let chmodFailure = null;
  let assessment = evaluateDirSecurity(stats, ctx);

  if (platform === "win32" && assessment.code !== "SYMLINK" && assessment.code !== "NOT_DIRECTORY") {
    // Windows 无法读取 ACL，只能按“用户目录内”放行；这里再对真实路径做一次
    // 检查，防止用户目录里的 junction/symlink 父级把目录指到别处。
    let realTarget;
    try {
      realTarget = fsImpl.realpathSync(target);
    } catch (error) {
      throw new ConfigError(`无法解析会话缓存目录的真实路径 ${target}：${error.message}`);
    }
    ctx.dir = realTarget;
    stats = lstatOrNull(fsImpl, realTarget);
    if (!stats) {
      throw new ConfigError(`会话缓存目录真实路径不可访问：${realTarget}`);
    }
    assessment = evaluateDirSecurity(stats, ctx);
  }

  if (assessment.code === "MODE_TOO_OPEN") {
    if (!isDedicatedStateDir(fsImpl, target)) {
      // 目录里还有别的文件（例如用户把 XIAOAI_STATE_DIR 指向 $HOME），
      // 自动 chmod 会影响其它程序，必须由用户自行处理。
      if (!allowInsecure) {
        throw new ConfigError(
          `会话缓存目录权限过宽（${formatMode(stats.mode)}）且包含其他文件，拒绝自动修改目录权限：${target}。` +
            `请把 ${STATE_DIR_ENV_VAR} 指向一个专用目录，或手动执行 chmod 700 "${target}"。`,
        );
      }
      chmodFailure = new Error("目录包含其他文件，未自动收紧权限");
    } else {
      try {
        fsImpl.chmodSync(target, 0o700);
        tightened = true;
      } catch (error) {
        chmodFailure = error;
        if (!allowInsecure) {
          throw new ConfigError(
            `无法把会话缓存目录权限收紧到 0700：${target}（${error.message}）。凭据写入已中止。${INSECURE_HINT}`,
          );
        }
      }
      stats = lstatOrNull(fsImpl, target);
      if (!stats) {
        throw new ConfigError(`会话缓存目录在收紧权限后消失：${target}`);
      }
      assessment = evaluateDirSecurity(stats, ctx);
    }
  }

  if (!assessment.ok) {
    if (assessment.overridable && allowInsecure) {
      const detail = chmodFailure
        ? `无法收紧目录权限：${chmodFailure.message}`
        : assessment.message;
      warnings.push(`⚠️  安全告警：${detail}（已按 ${ALLOW_INSECURE_ENV_VAR}=true 继续）`);
      warn(warnings[warnings.length - 1]);
      return {
        dir: target,
        tightened,
        insecureAck: true,
        warnings,
        mode: formatMode(stats.mode),
      };
    }
    throw new ConfigError(assessment.message);
  }

  return {
    dir: target,
    tightened,
    insecureAck: false,
    warnings,
    mode: formatMode(stats.mode),
  };
}

function verifyActiveDirectory(dir, options) {
  const { fs: fsImpl, platform, uid, env, homedir, allowInsecure } = normalizeOptions(options);
  const target = path.resolve(String(dir));

  let realDir;
  let realCwd;
  try {
    realDir = fsImpl.realpathSync(target);
    realCwd = fsImpl.realpathSync(process.cwd());
  } catch (error) {
    throw new ConfigError(`无法解析工作目录：${error.message}。凭据写入已中止。`);
  }
  if (realDir !== realCwd) {
    throw new ConfigError(
      `未能切换到会话缓存目录：期望 ${realDir}，实际 ${realCwd}。凭据写入已中止。`,
    );
  }

  let stats;
  try {
    stats = fsImpl.statSync(realCwd);
  } catch (error) {
    throw new ConfigError(`无法检查当前工作目录：${error.message}`);
  }
  const assessment = evaluateDirSecurity(stats, {
    platform,
    uid,
    dir: realCwd,
    env,
    homedir,
  });
  if (!assessment.ok && !(allowInsecure && assessment.overridable)) {
    throw new ConfigError(`当前工作目录不是私有目录：${assessment.message}`);
  }
  return { dir: realCwd, mode: formatMode(stats.mode) };
}

function removeCacheFile(fsImpl, file, warn) {
  try {
    fsImpl.rmSync(file, { force: true });
    return true;
  } catch (error) {
    warn(`⚠️  无法删除不安全的会话缓存 ${file}：${error.message}，请手动删除后再运行。`);
    return false;
  }
}

/** 已知的上游会话服务键；缓存里只保留这些顶层键。 */
const ALLOWED_STORE_KEYS = new Set(["micoapi", "mina", "miot"]);

function parseJsonObject(raw) {
  let parsed;
  try {
    parsed = JSON.parse(
      raw,
      (key, value) =>
        key === "__proto__" || key === "constructor" || key === "prototype" ? undefined : value,
    );
  } catch {
    return null;
  }
  if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) {
    return null;
  }
  return parsed;
}

function writeCacheContent(fsImpl, file, content) {
  const constants = fsImpl.constants ?? fs.constants ?? {};
  const noFollow =
    process.platform !== "win32" &&
    typeof constants.O_NOFOLLOW === "number" &&
    constants.O_NOFOLLOW > 0;
  const flags = noFollow
    ? constants.O_WRONLY | constants.O_CREAT | constants.O_TRUNC | constants.O_NOFOLLOW
    : "w";
  let fd = null;
  try {
    fd = fsImpl.openSync(file, flags, 0o600);
    fsImpl.writeFileSync(fd, content, { encoding: "utf8" });
  } catch (error) {
    if (error?.code === "ELOOP") {
      throw new ConfigError(`会话缓存文件在写入前被替换为符号链接：${file}`);
    }
    throw new ConfigError(`无法写入会话缓存文件 ${file}：${error.message}`);
  } finally {
    if (fd !== null) {
      try {
        fsImpl.closeSync(fd);
      } catch {
        // close 失败不影响后续复验，忽略。
      }
    }
  }
}

function sanitizeCacheContent(fsImpl, file) {
  let raw;
  try {
    raw = fsImpl.readFileSync(file, "utf8");
  } catch (error) {
    throw new ConfigError(`无法读取会话缓存文件 ${file}：${error.message}`);
  }

  const parsed = parseJsonObject(raw);
  if (!parsed) {
    writeCacheContent(fsImpl, file, "{}\n");
    return { changed: true, reset: true };
  }

  const store = {};
  let dropped = false;
  for (const [key, value] of Object.entries(parsed)) {
    if (ALLOWED_STORE_KEYS.has(key)) {
      store[key] = value;
    } else {
      dropped = true;
    }
  }
  if (!dropped) {
    return { changed: false, reset: false };
  }
  writeCacheContent(fsImpl, file, `${JSON.stringify(store)}\n`);
  return { changed: true, reset: Object.keys(store).length === 0 };
}

function statCacheFile(fsImpl, file) {
  try {
    return fsImpl.statSync(file);
  } catch (error) {
    throw new ConfigError(`无法确认会话缓存文件状态 ${file}：${error.message}`);
  }
}

function readCacheIdentity(fsImpl, file) {
  let stats;
  try {
    stats = fsImpl.lstatSync(file, { bigint: true });
  } catch {
    try {
      stats = fsImpl.lstatSync(file);
    } catch {
      return null;
    }
  }
  return { dev: String(stats.dev), ino: String(stats.ino) };
}

function createCacheFile(fsImpl, file) {
  let fd = null;
  try {
    fd = fsImpl.openSync(file, "wx", 0o600);
    fsImpl.writeFileSync(fd, "{}\n", { encoding: "utf8" });
    return true;
  } catch (error) {
    if (error?.code === "EEXIST") {
      // 并发下已被创建：交给调用方复验类型、权限与硬链接。
      return false;
    }
    throw new ConfigError(`无法创建会话缓存文件 ${file}：${error.message}`);
  } finally {
    if (fd !== null) {
      try {
        fsImpl.closeSync(fd);
      } catch {
        // close 失败不影响后续复验，忽略。
      }
    }
  }
}

/**
 * 登录前预创建/复验 `.mi.json`，保证上游写入时落在 0600 的 inode 上。
 *
 * @param {string} dir
 * @param {object} [options]
 * @returns {{ file: string, mode: string, action: "created" | "kept" | "replaced" | "reset" | "sanitized", warnings: string[] }}
 */
export function prepareCacheFile(dir, options = {}) {
  const { fs: fsImpl, platform, uid, allowInsecure, warn } = normalizeOptions(options);
  const warnings = [];
  const target = path.resolve(String(dir));
  const file = path.join(target, CACHE_FILE_NAME);
  const ctx = { platform, uid, file };

  let action = "kept";
  let stats = null;

  for (let attempt = 0; attempt < 3; attempt += 1) {
    stats = lstatOrNull(fsImpl, file);
    if (!stats) {
      const created = createCacheFile(fsImpl, file);
      stats = lstatOrNull(fsImpl, file);
      if (!stats) {
        throw new ConfigError(`无法创建会话缓存文件：${file}`);
      }
      if (created && action !== "replaced") {
        action = "created";
      }
    }

    const assessment = evaluateFileSecurity(stats, ctx);
    if (assessment.ok || assessment.overridable) {
      break;
    }
    if (!removeCacheFile(fsImpl, file, warn)) {
      throw new ConfigError(`${assessment.message} 无法自动移除该文件，请手动删除后重试。`);
    }
    warnings.push(`⚠️  已移除不安全的会话缓存（${assessment.code}）：${file}`);
    stats = null;
    action = "replaced";
  }

  if (!stats) {
    throw new ConfigError(`无法准备会话缓存文件：${file}`);
  }

  let assessment = evaluateFileSecurity(stats, ctx);
  let chmodFailure = null;
  if (assessment.code === "MODE_TOO_OPEN") {
    try {
      fsImpl.chmodSync(file, 0o600);
    } catch (error) {
      chmodFailure = error;
      if (!allowInsecure) {
        const removed = removeCacheFile(fsImpl, file, warn);
        throw new ConfigError(
          `无法收紧会话缓存文件权限（${file}）：${error.message}。凭据写入已中止。` +
            `${removed ? "已删除该缓存文件。" : "无法自动删除，请手动删除后重试。"}`,
        );
      }
    }
    stats = lstatOrNull(fsImpl, file);
    if (!stats) {
      throw new ConfigError(`会话缓存文件在收紧权限后消失：${file}`);
    }
    assessment = evaluateFileSecurity(stats, ctx);
  }
  if (!assessment.ok && !(allowInsecure && assessment.overridable)) {
    const removed = removeCacheFile(fsImpl, file, warn);
    throw new ConfigError(
      `${assessment.message}${
        removed ? " 已删除该缓存文件。" : " 无法自动删除，请手动删除后重试。"
      }`,
    );
  }
  if (!assessment.ok) {
    const detail = chmodFailure
      ? `无法收紧文件权限：${chmodFailure.message}`
      : assessment.message;
    warnings.push(`⚠️  安全告警：${detail}（已按 ${ALLOW_INSECURE_ENV_VAR}=true 继续）`);
  }

  // 上游会把已有内容当 store 合并；损坏/非对象/未知字段一律清理，避免注入。
  const sanitized = sanitizeCacheContent(fsImpl, file);
  if (sanitized.changed) {
    if (action === "kept") {
      action = sanitized.reset ? "reset" : "sanitized";
    }
    warnings.push(`⚠️  已清理会话缓存中无法识别或损坏的内容：${file}`);
  }

  const finalStats = statCacheFile(fsImpl, file);
  return { file, mode: formatMode(finalStats.mode), action, warnings };
}

/**
 * 登录后复验 `.mi.json`：目录仍安全、文件仍是预创建的那个、权限正确、内容非空。
 *
 * @param {string} dir
 * @param {{ expected?: { dev?: number, ino?: number }, allowInsecure?: boolean }} [options]
 * @returns {{ file: string, mode: string, warnings: string[], identity: { dev?: number, ino?: number } }}
 */
export function verifyCacheFile(dir, options = {}) {
  const { fs: fsImpl, platform, uid, env, homedir, allowInsecure, warn } = normalizeOptions(options);
  const warnings = [];
  const target = path.resolve(String(dir));
  const file = path.join(target, CACHE_FILE_NAME);
  const ctx = { platform, uid, file };

  // 登录期间目录可能被改名/替换，先复验目录本身。
  const dirStats = lstatOrNull(fsImpl, target);
  const dirAssessment = evaluateDirSecurity(dirStats, {
    platform,
    uid,
    dir: target,
    env,
    homedir,
  });
  if (!dirAssessment.ok && !(allowInsecure && dirAssessment.overridable)) {
    throw new ConfigError(`登录后会话缓存目录不再安全：${dirAssessment.message}`);
  }

  let stats = lstatOrNull(fsImpl, file);
  if (!stats) {
    throw new ConfigError(
      `登录后未找到会话缓存：${file}。请确认目录可写（${STATE_DIR_ENV_VAR}）。`,
    );
  }

  const expected = options.expected;
  const identity = readCacheIdentity(fsImpl, file);
  if (expected && identity) {
    const devChanged = expected.dev !== undefined && String(expected.dev) !== identity.dev;
    const inoChanged =
      expected.ino !== undefined && identity.ino !== "0" && String(expected.ino) !== identity.ino;
    if (devChanged || inoChanged) {
      removeCacheFile(fsImpl, file, warn);
      throw new ConfigError(
        `登录后会话缓存文件已被替换（dev/ino 变化）：${file}。已删除该文件，请运行 clean 后重新登录。`,
      );
    }
  }

  let assessment = evaluateFileSecurity(stats, ctx);
  let chmodFailure = null;
  if (assessment.code === "MODE_TOO_OPEN") {
    try {
      fsImpl.chmodSync(file, 0o600);
    } catch (error) {
      chmodFailure = error;
    }
    stats = lstatOrNull(fsImpl, file);
    if (!stats) {
      throw new ConfigError(`会话缓存文件在收紧权限后消失：${file}`);
    }
    assessment = evaluateFileSecurity(stats, ctx);
  }

  if (!assessment.ok) {
    if (allowInsecure && assessment.overridable) {
      const detail = chmodFailure
        ? `无法收紧文件权限：${chmodFailure.message}`
        : assessment.message;
      warnings.push(`⚠️  安全告警：${detail}（已按 ${ALLOW_INSECURE_ENV_VAR}=true 继续）`);
    } else {
      const removed = removeCacheFile(fsImpl, file, warn);
      throw new ConfigError(
        `${assessment.message}${removed ? " 已删除该缓存文件。" : ""} ` +
          `请运行 clean 后重新登录，并检查 ${STATE_DIR_ENV_VAR} 的属主与权限。`,
      );
    }
  }

  // 预创建的 {} 不能作为“登录成功已写入”的证据。
  let raw;
  try {
    raw = fsImpl.readFileSync(file, "utf8");
  } catch (error) {
    throw new ConfigError(`无法读取会话缓存文件 ${file}：${error.message}`);
  }
  const store = parseJsonObject(raw);
  if (!store || Object.keys(store).length === 0) {
    throw new ConfigError(
      `登录后会话缓存仍为空或无法解析：${file}。可能未成功写入（只读文件/目录或上游失败），` +
        `请运行 clean 后重新登录。`,
    );
  }

  const finalStats = statCacheFile(fsImpl, file);
  return {
    file,
    mode: formatMode(finalStats.mode),
    warnings,
    identity: readCacheIdentity(fsImpl, file) ?? { dev: finalStats.dev, ino: finalStats.ino },
  };
}

/**
 * 准备一次登录所需的私有工作目录：校验目录 → chdir → 复验 cwd → 预创建缓存。
 *
 * @param {{ stateDir: string, stateDirSource?: string, allowInsecureStateDir?: boolean }} config
 * @param {object} [options]
 * @returns {{ dir: string, cacheFile: string, mode: string, action: string, warnings: string[] }}
 */
export function prepareSessionState(config, options = {}) {
  const allowInsecure =
    config.allowInsecureStateDir !== undefined
      ? config.allowInsecureStateDir === true
      : options.allowInsecure === true;
  const opts = { ...options, allowInsecure };
  const fsImpl = opts.fs ?? fs;
  const ensured = ensureStateDir(config.stateDir, opts);
  const warnings = [...ensured.warnings];

  try {
    process.chdir(ensured.dir);
  } catch (error) {
    throw new ConfigError(`无法切换到会话缓存目录 ${ensured.dir}：${error.message}`);
  }

  verifyActiveDirectory(ensured.dir, opts);
  const cache = prepareCacheFile(ensured.dir, opts);
  warnings.push(...cache.warnings);

  return {
    dir: ensured.dir,
    dirMode: ensured.mode,
    cacheFile: cache.file,
    mode: cache.mode,
    action: cache.action,
    identity: readCacheIdentity(fsImpl, cache.file),
    warnings,
  };
}

/**
 * 环境变量文件（含 passToken）的权限检查与尽力收紧。
 *
 * @param {string} file
 * @param {{ fs?: typeof fs, platform?: string, uid?: number | null, warn?: (line: string) => void }} [options]
 * @returns {{ existed: boolean, tightened: boolean }}
 */
export function inspectEnvFile(file, options = {}) {
  const { fs: fsImpl, platform, uid, warn } = normalizeOptions(options);
  const target = path.resolve(String(file));

  let stats;
  try {
    stats = fsImpl.lstatSync(target);
  } catch (error) {
    if (error?.code === "ENOENT") {
      return { existed: false, tightened: false };
    }
    throw new ConfigError(`无法检查环境变量文件 ${target}：${error.message}`);
  }

  if (stats.isSymbolicLink()) {
    warn(
      `⚠️  环境变量文件是符号链接：${target}。请确认链接目标仅当前用户可读（chmod 600），否则 passToken 可能泄露。`,
    );
    return { existed: true, tightened: false };
  }
  if (!stats.isFile()) {
    throw new ConfigError(`环境变量路径不是普通文件：${target}`);
  }
  if (platform === "win32") {
    return { existed: true, tightened: false };
  }

  if (uid !== null && typeof stats.uid === "number" && stats.uid !== uid) {
    warn(`⚠️  环境变量文件属于其他用户（uid=${stats.uid}）：${target}，请确认其来源可信。`);
  }
  // 可被同组/其他用户修改 = 凭据可被注入或替换，直接拒绝。
  if ((stats.mode & 0o022) !== 0) {
    throw new ConfigError(
      `环境变量文件可被同组或其他用户修改（${formatMode(stats.mode)}）：${target}。` +
        `请执行 chmod 600 "${target}" 后重试。`,
    );
  }
  if ((stats.mode & 0o077) === 0) {
    return { existed: true, tightened: false };
  }

  warn(
    `⚠️  环境变量文件权限过宽（${formatMode(stats.mode)}）：${target}，passToken 可被同组或其他用户读取。正在收紧为 0600。`,
  );
  try {
    fsImpl.chmodSync(target, 0o600);
  } catch (error) {
    throw new ConfigError(
      `无法收紧环境变量文件权限（${target}）：${error.message}。请手动执行 chmod 600 后重试。`,
    );
  }
  let after;
  try {
    after = fsImpl.statSync(target);
  } catch (error) {
    throw new ConfigError(`无法确认环境变量文件权限 ${target}：${error.message}`);
  }
  if ((after.mode & 0o077) !== 0) {
    throw new ConfigError(
      `自动收紧环境变量文件权限未生效（${formatMode(after.mode)}）：${target}。请手动执行 chmod 600 后重试。`,
    );
  }
  warn(`    ✅ 已收紧为 0600。`);
  return { existed: true, tightened: true };
}

/**
 * 旧版本可能留下的会话缓存位置（只做检测/告警，不再复用）。
 *
 * @param {{ fs?: typeof fs, cwd?: string, scriptDir?: string, skillRoot?: string, tmpdir?: string, excludeDirs?: string[] }} [options]
 * @returns {string[]}
 */
export function findLegacyCachePaths(options = {}) {
  const fsImpl = options.fs ?? fs;
  const tmpdir = options.tmpdir ?? os.tmpdir();
  const cwd = options.cwd ?? process.cwd();
  const excluded = new Set(
    (Array.isArray(options.excludeDirs) ? options.excludeDirs : []).map((dir) =>
      path.resolve(String(dir)),
    ),
  );
  const candidates = [];

  if (options.scriptDir) {
    candidates.push(path.join(options.scriptDir, CACHE_FILE_NAME));
  }
  if (options.skillRoot) {
    candidates.push(path.join(options.skillRoot, CACHE_FILE_NAME));
  }
  candidates.push(path.join(cwd, CACHE_FILE_NAME));
  candidates.push(path.join(tmpdir, STATE_DIR_NAME, CACHE_FILE_NAME));

  const seen = new Set();
  const found = [];
  for (const candidate of candidates) {
    const absolute = path.resolve(candidate);
    if (seen.has(absolute)) {
      continue;
    }
    seen.add(absolute);
    if (excluded.has(path.dirname(absolute))) {
      continue;
    }
    try {
      fsImpl.lstatSync(absolute);
      found.push(absolute);
    } catch {
      // 不存在或无法访问都不报告，避免把 EACCES/ENOTDIR 误报成“遗留缓存”。
    }
  }
  return found;
}

/** 判断文件内容是否像小米会话缓存（用于 legacy 清理时避免误删同名文件）。 */
function looksLikeXiaoaiCache(fsImpl, file) {
  let stats;
  try {
    stats = fsImpl.lstatSync(file);
  } catch {
    return false;
  }
  if (stats.isSymbolicLink()) {
    return true;
  }
  if (!stats.isFile() || stats.size > MAX_CACHE_FILE_BYTES) {
    return false;
  }
  let raw;
  try {
    raw = fsImpl.readFileSync(file, "utf8");
  } catch {
    return false;
  }
  if (/"(passToken|serviceToken|ssecurity)"/.test(raw)) {
    return true;
  }
  const parsed = parseJsonObject(raw);
  return parsed !== null && Object.keys(parsed).some((key) => ALLOWED_STORE_KEYS.has(key));
}

/**
 * 安全清理某个目录下的 `.mi.json`（不跟随目录符号链接）。
 *
 * 默认只删缓存文件、不删目录；`removeEmptyDir` 仅由调用方对“当前状态目录”开启，
 * 避免把 cwd/技能目录/旧临时目录等非专用目录删掉。
 * `requireCacheSignature` 用于 legacy 位置：内容不像小米会话缓存时只提示、不删除。
 *
 * @param {string} dir
 * @param {{ fs?: typeof fs, removeEmptyDir?: boolean, requireCacheSignature?: boolean }} [options]
 * @returns {{ dir: string, removedFile: boolean, dirRemoved: boolean, notes: string[] }}
 */
export function cleanStateDir(dir, options = {}) {
  const fsImpl = options.fs ?? fs;
  const target = path.resolve(String(dir));
  const removeEmptyDir = options.removeEmptyDir === true;
  const requireCacheSignature = options.requireCacheSignature === true;
  const notes = [];

  let stats;
  try {
    stats = fsImpl.lstatSync(target);
  } catch (error) {
    if (error?.code === "ENOENT") {
      return { dir: target, removedFile: false, dirRemoved: false, notes };
    }
    throw new ConfigError(`无法访问会话缓存目录 ${target}：${error.message}`);
  }

  if (stats.isSymbolicLink()) {
    throw new ConfigError(
      `会话缓存目录是符号链接，拒绝清理：${target}。请确认 ${STATE_DIR_ENV_VAR} 指向真实目录。`,
    );
  }
  if (!stats.isDirectory()) {
    throw new ConfigError(`会话缓存路径不是目录，拒绝清理：${target}`);
  }

  const file = path.join(target, CACHE_FILE_NAME);
  let fileStats = null;
  try {
    fileStats = fsImpl.lstatSync(file);
  } catch (error) {
    if (error?.code !== "ENOENT") {
      throw new ConfigError(`无法访问会话缓存文件 ${file}：${error.message}`);
    }
  }

  let removedFile = false;
  if (fileStats) {
    if (fileStats.isDirectory()) {
      try {
        fsImpl.rmdirSync(file);
        notes.push(`ℹ️  已删除空目录 ${file}（该路径本应是缓存文件）。`);
      } catch {
        notes.push(
          `⚠️  ${file} 是非空目录，clean 不会递归删除；请确认内容后手动删除并重新登录。`,
        );
      }
    } else if (requireCacheSignature && !looksLikeXiaoaiCache(fsImpl, file)) {
      notes.push(`ℹ️  ${file} 内容不像小米会话缓存，已跳过；如确认无用请手动删除。`);
    } else {
      fsImpl.rmSync(file, { force: true });
      removedFile = true;
      if (fileStats.isSymbolicLink()) {
        notes.push(`ℹ️  ${file} 是符号链接，只删除了链接本身。`);
      }
    }
  }

  let dirRemoved = false;
  if (removeEmptyDir) {
    let empty = false;
    try {
      empty = fsImpl.readdirSync(target).length === 0;
    } catch (error) {
      throw new ConfigError(`无法读取会话缓存目录 ${target}：${error.message}`);
    }
    if (empty) {
      try {
        fsImpl.rmdirSync(target);
        dirRemoved = true;
      } catch (error) {
        throw new ConfigError(`无法删除空缓存目录 ${target}：${error.message}`);
      }
    }
  }

  return { dir: target, removedFile, dirRemoved, notes };
}

/**
 * `check` 命令的实现：只做本地状态检查，不读取凭据、不发起网络请求。
 *
 * @param {Record<string, string | undefined>} [env]
 * @param {{ fs?: typeof fs, platform?: string, uid?: number | null, env?: Record<string, string | undefined>, homedir?: string, cwd?: string, scriptDir?: string, skillRoot?: string, tmpdir?: string, warn?: (line: string) => void }} [options]
 * @returns {{ ok: boolean, lines: string[], exitCode: number }}
 */
export function runSecurityCheck(env = process.env, options = {}) {
  const { fs: fsImpl, platform, uid, homedir } = normalizeOptions(options);
  const resolved = resolveStateDir(env, { platform, homedir });
  const lines = [];
  let ok = true;

  lines.push(
    `状态目录：${resolved.dir}（来源：${resolved.source === "env" ? STATE_DIR_ENV_VAR : "默认"}）`,
  );

  let existedBefore = false;
  try {
    fsImpl.lstatSync(resolved.dir);
    existedBefore = true;
  } catch (error) {
    if (error?.code !== "ENOENT") {
      lines.push(`目录探测：${error.message}`);
    }
  }

  try {
    const ensured = ensureStateDir(resolved.dir, {
      ...options,
      platform,
      uid,
      env,
      homedir,
      allowInsecure: resolved.allowInsecure,
      warn: (line) => lines.push(line),
    });
    for (const warning of ensured.warnings) {
      if (!lines.includes(warning)) {
        lines.push(warning);
      }
    }
    if (!existedBefore) {
      lines.push("说明：该目录此前不存在，已按 0700 创建（不含凭据）。");
    }
    if (ensured.insecureAck) {
      ok = false;
      lines.push(
        `目录校验：已按 ${ALLOW_INSECURE_ENV_VAR}=true 放行，但目录不满足安全要求（不安全，建议修复）`,
      );
    } else if (platform === "win32") {
      lines.push(`目录校验：通过（用户目录路径策略；模式 ${ensured.mode} 仅供参考）`);
    } else {
      lines.push(`目录校验：通过（${ensured.mode}，属主=当前用户）`);
    }
    if (ensured.tightened) {
      lines.push("目录校验：已把权限收紧到 0700");
    }
  } catch (error) {
    ok = false;
    lines.push(`目录校验：失败 — ${error.message}`);
  }

  const cacheFile = path.join(resolved.dir, CACHE_FILE_NAME);
  try {
    const stats = fsImpl.lstatSync(cacheFile);
    const assessment = evaluateFileSecurity(stats, { platform, uid, file: cacheFile });
    if (assessment.ok) {
      lines.push(`缓存文件：存在（${formatMode(stats.mode)}，普通文件）`);
    } else if (resolved.allowInsecure && assessment.overridable) {
      ok = false;
      lines.push(`缓存文件：存在但权限不满足要求（${assessment.message}）；运行时会收紧或告警放行`);
    } else {
      ok = false;
      lines.push(`缓存文件：需要处理 — ${assessment.message}`);
    }
  } catch (error) {
    if (error?.code === "ENOENT") {
      lines.push("缓存文件：不存在（首次运行会以 0600 创建）");
    } else {
      ok = false;
      lines.push(`缓存文件：无法检查 — ${error.message}`);
    }
  }

  const legacy = findLegacyCachePaths({
    fs: fsImpl,
    cwd: options.cwd,
    scriptDir: options.scriptDir,
    skillRoot: options.skillRoot,
    tmpdir: options.tmpdir,
  });
  if (legacy.length > 0) {
    lines.push(`旧版缓存：发现 ${legacy.length} 处（运行 clean 清理）`);
    for (const file of legacy) {
      lines.push(`  - ${file}`);
    }
  } else {
    lines.push("旧版缓存：无");
  }

  return { ok, lines, exitCode: ok ? 0 : 2 };
}
