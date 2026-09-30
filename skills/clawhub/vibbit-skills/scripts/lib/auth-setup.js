'use strict'

const http = require('node:http')
const crypto = require('node:crypto')
const { execFile } = require('node:child_process')
const { promisify } = require('node:util')
const { createClient, normalizeBase, VibbitError } = require('./client')
const { saveCredential, environmentKey, validKey } = require('./auth-store')
const { setupPage } = require('./auth-page')
const profile = require('./account-profile')

async function requestBody(req) {
  let size = 0
  const chunks = []
  for await (const chunk of req) {
    size += chunk.length
    if (size > 8192) throw new Error('limit')
    chunks.push(chunk)
  }
  return JSON.parse(Buffer.concat(chunks).toString('utf8'))
}

async function startSetup({ env = process.env, timeoutMs = 600000,
  verify = key => createClient({ base: profile.apiBase, key }).request('GET', '/health'),
  save = key => saveCredential(key, { env }),
} = {}) {
  if (environmentKey(env)) throw new VibbitError('configuration', 'An environment key already takes precedence. Use auth_status --check and update it through the host credential settings; a local file will not override it.')
  if (normalizeBase(env.VIBBIT_BASE_URL) !== profile.apiBase) throw new VibbitError('configuration', 'Local setup is bound to this package region. Use the matching regional package or host credential settings for the selected API environment.')
  if (process.platform === 'win32') throw new VibbitError('configuration', 'Use the host credential settings on Windows; this local helper requires POSIX private-file permissions.')
  if (!profile.webBase) throw new VibbitError('configuration', 'The account website is not configured for this package')
  const prefix = '/' + crypto.randomBytes(32).toString('base64url') + '/'
  const nonce = crypto.randomBytes(24).toString('base64url')
  const html = setupPage(nonce)
  let origin, timer, finished = false, busy = false, complete
  const done = new Promise(resolve => { complete = resolve })
  const finish = result => {
    if (finished) return
    finished = true
    clearTimeout(timer)
    server.close()
    server.closeIdleConnections?.()
    complete(result)
  }
  const server = http.createServer(async (req, res) => {
    res.setHeader('Cache-Control', 'no-store')
    res.setHeader('Referrer-Policy', 'no-referrer')
    res.setHeader('X-Content-Type-Options', 'nosniff')
    res.setHeader('X-Frame-Options', 'DENY')
    res.setHeader('Connection', 'close')
    res.setHeader('Content-Security-Policy', `default-src 'none'; script-src 'nonce-${nonce}'; style-src 'nonce-${nonce}'; connect-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'`)
    const send = (code, body) => { res.writeHead(code, { 'Content-Type': 'application/json' }); res.end(JSON.stringify(body)) }
    const reject = () => { req.resume(); send(403, { ok: false, reason: 'expired' }) }
    if (finished || req.headers.host !== new URL(origin).host || !req.url.startsWith(prefix)) return reject()
    if (req.method === 'GET' && req.url === prefix) {
      if (req.headers['sec-fetch-dest'] === 'iframe') return reject()
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' }); res.end(html); return
    }
    if (req.method !== 'POST' || req.headers.origin !== origin ||
      req.headers['content-type'] !== 'application/json' ||
      ![undefined, 'same-origin'].includes(req.headers['sec-fetch-site']) ||
      ![prefix + 'verify', prefix + 'cancel'].includes(req.url)) return reject()
    if (busy) { req.resume(); return send(409, { ok: false, reason: 'pending' }) }
    if (req.url === prefix + 'cancel') {
      req.resume(); send(200, { ok: true }); finish({ ok: false, cancelled: true }); return
    }
    busy = true
    let key
    try {
      if (Number(req.headers['content-length']) > 8192) { req.resume(); send(413, { ok: false, reason: 'invalid' }); return }
      const input = await requestBody(req)
      key = typeof input.key === 'string' ? input.key.trim() : ''
      if (!validKey(key) || Object.keys(input).some(field => field !== 'key')) { send(400, { ok: false, reason: 'invalid' }); return }
      try { await verify(key) } catch (error) {
        const reason = error.http_status === 403 || error.code === 403 ? 'forbidden'
          : error.kind === 'authentication' ? 'authentication' : 'transport'
        send(400, { ok: false, reason }); return
      }
      if (finished) { send(410, { ok: false, reason: 'expired' }); return }
      // After verification, commit locally before reporting success. No key or API payload is echoed.
      clearTimeout(timer)
      try { await save(key) } catch {
        send(500, { ok: false, reason: 'saveFailed' }); finish({ ok: false, saved: false }); return
      }
      send(200, { ok: true })
      finish({ ok: true, configured: true, verified: true, source: 'private_file', region: profile.region, base: profile.apiBase })
    } catch { if (!res.writableEnded) send(400, { ok: false, reason: 'invalid' }) }
    finally { key = undefined; busy = false }
  })
  server.requestTimeout = 15000
  server.headersTimeout = 10000
  server.setTimeout(45000, socket => socket.destroy())
  await new Promise((resolve, reject) => {
    server.once('error', reject)
    server.listen(0, '127.0.0.1', resolve)
  })
  origin = 'http://127.0.0.1:' + server.address().port
  timer = setTimeout(() => {
    finish({ ok: false, expired: true, next: 'Open a new local setup page or use host credential settings.' })
    server.closeAllConnections?.()
  }, timeoutMs)
  return { url: origin + prefix, done, close: () => finish({ ok: false, cancelled: true }) }
}

async function openBrowser(url) {
  const program = process.platform === 'darwin' ? 'open' : 'xdg-open'
  try { await promisify(execFile)(program, [url], { timeout: 5000 }); return true } catch { return false }
}

module.exports = { startSetup, openBrowser }
