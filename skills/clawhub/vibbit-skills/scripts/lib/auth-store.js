'use strict'

const fs = require('node:fs/promises')
const { constants } = require('node:fs')
const path = require('node:path')
const os = require('node:os')
const crypto = require('node:crypto')
const { normalizeBase, VibbitError } = require('./client')
const profile = require('./account-profile')

const configError = () => new VibbitError('configuration', 'Credential storage must be a private, owned directory and regular file. Use host credential settings if private file storage is unavailable.')
function validKey(key) {
  return typeof key === 'string' && /^[\x21-\x7e]{1,4096}$/.test(key)
}
function environmentKey(env = process.env) {
  return (env.VIBBIT_API_KEY || env.VIBBIT_OPENAPI_KEY || '').trim()
}
function storageDirectory(env = process.env) {
  if (env.VIBBIT_CONFIG_DIR && !path.isAbsolute(env.VIBBIT_CONFIG_DIR)) throw configError()
  return env.VIBBIT_CONFIG_DIR || path.join(os.homedir(), '.vibbit', 'credentials')
}
function checkPrivate(stat, directory = false) {
  if (process.platform === 'win32' || stat.uid !== process.getuid?.() || (stat.mode & 0o077) !== 0 ||
    (directory ? !stat.isDirectory() : !stat.isFile() || stat.nlink !== 1 || stat.size > 16384)) throw configError()
}
async function privateDirectory(dir, create) {
  if (process.platform === 'win32') throw configError()
  if (create) await fs.mkdir(dir, { recursive: true, mode: 0o700 })
  checkPrivate(await fs.lstat(dir), true)
}
async function readStored({ env = process.env, base = normalizeBase(env.VIBBIT_BASE_URL) } = {}) {
  // A saved key never follows a changed API destination, including another region.
  if (base !== profile.apiBase || process.platform === 'win32') return undefined
  const dir = storageDirectory(env)
  let handle
  try {
    await privateDirectory(dir, false)
    handle = await fs.open(path.join(dir, profile.region + '.json'), constants.O_RDONLY | constants.O_NOFOLLOW)
    checkPrivate(await handle.stat())
    const data = JSON.parse(await handle.readFile('utf8'))
    if (data.version !== 1 || data.base !== base || !validKey(data.key)) throw configError()
    return { key: data.key, base, source: 'private_file' }
  } catch (error) {
    if (error.code === 'ENOENT') return undefined
    throw configError()
  } finally { await handle?.close() }
}
async function resolveCredential({ env = process.env } = {}) {
  const base = normalizeBase(env.VIBBIT_BASE_URL)
  const key = environmentKey(env)
  if (key) {
    if (!validKey(key)) throw new VibbitError('configuration', 'The configured API key has an invalid format')
    return { base, key, source: 'environment' }
  }
  return await readStored({ env, base }) || { base, source: 'missing' }
}
async function saveCredential(key, { env = process.env } = {}) {
  key = typeof key === 'string' ? key.trim() : key
  if (!validKey(key)) throw new VibbitError('input', 'Invalid API key format')
  const dir = storageDirectory(env)
  const file = path.join(dir, profile.region + '.json')
  let temporary
  try {
    await privateDirectory(dir, true)
    try { checkPrivate(await fs.lstat(file)) } catch (error) { if (error.code !== 'ENOENT') throw error }
    temporary = path.join(dir, crypto.randomUUID() + '.tmp')
    const handle = await fs.open(temporary, 'wx', 0o600)
    try {
      await handle.writeFile(JSON.stringify({ version: 1, base: profile.apiBase, key }) + '\n')
      await handle.sync()
    } finally { await handle.close() }
    await fs.rename(temporary, file)
  } catch { throw configError() }
  finally { if (temporary) await fs.rm(temporary, { force: true }).catch(() => {}) }
  return { saved: true, source: 'private_file', base: profile.apiBase }
}
async function clearCredential({ env = process.env } = {}) {
  const dir = storageDirectory(env)
  try {
    await privateDirectory(dir, false)
    const file = path.join(dir, profile.region + '.json')
    checkPrivate(await fs.lstat(file))
    await fs.unlink(file)
  } catch (error) { if (error.code !== 'ENOENT') throw configError() }
  return { ok: true, cleared: 'private_file', region: profile.region, environment_still_configured: !!environmentKey(env), server_key_revoked: false }
}

module.exports = { resolveCredential, readStored, saveCredential, clearCredential, environmentKey, storageDirectory, validKey }
