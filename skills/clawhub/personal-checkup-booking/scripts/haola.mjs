import { createHash, randomBytes } from 'node:crypto'
import { chmod, lstat, mkdir, readFile, rename, rm, writeFile } from 'node:fs/promises'
import { createServer } from 'node:http'
import { homedir, userInfo } from 'node:os'
import { join } from 'node:path'
import { spawn, spawnSync } from 'node:child_process'

const MCP_URL = 'https://ai.ihaola.com.cn/api/mcp/haola-pe'
const PROTOCOL_VERSION = '2025-06-18'
const CLIENT_VERSION = '1.0.0'
const CLIENT_NAME = '好啦体检 · 个人体检定制和预约'
const TOKEN_DIR = join(homedir(), '.haola')
const TOKEN_PATH = join(TOKEN_DIR, 'token.json')
const ANONYMOUS_TOOLS = new Set([
  'vendor_list',
  'vendor_brands',
  'knowledge_get',
  'faq',
  'help',
  'progress_report',
])
const ALLOWED_TOOLS = new Set([
  ...ANONYMOUS_TOOLS,
  'plan_recommend',
  'order_list',
  'order_detail',
  'welfare_list',
  'welfare_detail',
  'cautions',
  'contact_list',
  'contact_get',
  'contact_create',
  'contact_update',
  'contact_profile_get',
  'contact_profile_save',
  'reservation_book',
  'reservation_cancel',
  'reservation_modify',
  'card_list',
])

class MCPError extends Error {
  constructor(message, status) {
    super(message)
    this.name = 'MCPError'
    this.status = status
  }
}

class LoginRequired extends MCPError {
  constructor(message = '需要先登录') {
    super(message, 401)
    this.name = 'LoginRequired'
  }
}

let sessionId = ''
let nextId = 0
let initialized = false
let protocolVersion = ''

async function readToken() {
  try {
    const file = await lstat(TOKEN_PATH)
    if (!file.isFile()) return null
    if (process.platform === 'win32') {
      restrictWindowsAcl(TOKEN_PATH)
    } else {
      await chmod(TOKEN_PATH, 0o600)
    }
    const token = JSON.parse(await readFile(TOKEN_PATH, 'utf8'))
    if (token.expires_at && Date.now() / 1000 > Number(token.expires_at) - 30) return null
    return token
  } catch {
    return null
  }
}

function parsePayload(text, contentType) {
  const trimmed = text.trim()
  if (!trimmed) return null
  if (contentType.includes('text/event-stream') || trimmed.startsWith('data:')) {
    const events = trimmed
      .split(/\r?\n\r?\n/)
      .map(event => event
        .split(/\r?\n/)
        .filter(line => line.startsWith('data:'))
        .map(line => line.slice(5).trimStart())
        .join('\n'))
      .filter(Boolean)
    for (let index = events.length - 1; index >= 0; index--) {
      try {
        return JSON.parse(events[index])
      } catch {
        continue
      }
    }
  }
  return JSON.parse(trimmed)
}

async function rpc(method, params, notification = false) {
  const token = await readToken()
  const headers = {
    Accept: 'application/json, text/event-stream',
    'Content-Type': 'application/json',
  }
  if (token?.access_token) headers.Authorization = `Bearer ${token.access_token}`
  if (sessionId) headers['mcp-session-id'] = sessionId
  if (protocolVersion) headers['MCP-Protocol-Version'] = protocolVersion

  const payload = {
    jsonrpc: '2.0',
    method,
  }
  if (!notification) payload.id = ++nextId
  if (params !== undefined) payload.params = params

  const response = await fetch(MCP_URL, {
    method: 'POST',
    headers,
    body: JSON.stringify(payload),
    redirect: 'error',
    signal: AbortSignal.timeout(180000),
  })
  const responseSession = response.headers.get('mcp-session-id')
  if (responseSession) sessionId = responseSession
  if (response.status === 401) throw new LoginRequired()
  const text = await response.text()
  if (!response.ok) throw new MCPError(`HTTP ${response.status}: ${text}`, response.status)
  if (notification) return null

  const body = parsePayload(text, response.headers.get('content-type') || '')
  if (body?.error) throw new MCPError(body.error.message || JSON.stringify(body.error))
  return body?.result
}

async function ensureReady() {
  if (initialized) return
  const result = await rpc('initialize', {
    protocolVersion: PROTOCOL_VERSION,
    capabilities: {},
    clientInfo: {
      name: '好啦体检 · 个人体检定制和预约',
      version: CLIENT_VERSION,
    },
  })
  protocolVersion = result?.protocolVersion || PROTOCOL_VERSION
  await rpc('notifications/initialized', undefined, true)
  initialized = true
}

async function listTools() {
  await ensureReady()
  const token = await readToken()
  const result = await rpc('tools/list', {})
  return (result?.tools || []).filter(tool => (
    ALLOWED_TOOLS.has(tool.name)
    && (token || ANONYMOUS_TOOLS.has(tool.name))
  ))
}

async function callTool(name, argumentsValue) {
  if (!ALLOWED_TOOLS.has(name)) throw new MCPError(`工具 ${name} 不在本 Skill 的调用范围内`)
  if (!ANONYMOUS_TOOLS.has(name) && !await readToken()) throw new LoginRequired()
  await ensureReady()
  const result = await rpc('tools/call', {
    name,
    arguments: argumentsValue,
  })
  const text = (result?.content || [])
    .filter(item => item.type === 'text')
    .map(item => item.text)
    .join('')
  let payload = null
  if (text) {
    try {
      payload = JSON.parse(text)
    } catch {
      payload = { raw: text }
    }
  }
  if (result?.isError) throw new MCPError(payload?.message || text || `${name} 调用失败`)
  if (payload && payload.code !== undefined && payload.code !== 0 && payload.code !== 200) {
    throw new MCPError(payload.message || '业务错误', payload.code)
  }
  return payload || { raw: text }
}

function printJson(value) {
  process.stdout.write(`${JSON.stringify(value, null, 2)}\n`)
}

function buildPkce() {
  const verifier = randomBytes(32).toString('base64url')
  const challenge = createHash('sha256')
    .update(verifier)
    .digest('base64url')
  return {
    verifier,
    challenge,
  }
}

async function postForm(url, body) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams(body),
    redirect: 'error',
    signal: AbortSignal.timeout(30000),
  })
  const text = await response.text()
  const payload = text ? JSON.parse(text) : {}
  if (!response.ok) throw new MCPError(`HTTP ${response.status}: ${text}`, response.status)
  return payload
}

async function postJson(url, body) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
    redirect: 'error',
    signal: AbortSignal.timeout(30000),
  })
  const text = await response.text()
  const payload = text ? JSON.parse(text) : {}
  if (!response.ok) throw new MCPError(`HTTP ${response.status}: ${text}`, response.status)
  return payload
}

function openBrowser(url) {
  const command = process.platform === 'darwin'
    ? ['open', [url]]
    : process.platform === 'win32'
      ? ['cmd', ['/c', 'start', '', url]]
      : ['xdg-open', [url]]
  const child = spawn(command[0], command[1], {
    detached: true,
    stdio: 'ignore',
  })
  child.on('error', () => {
    process.stderr.write(`请打开授权地址：${url}\n`)
  })
  child.unref()
}

function restrictWindowsAcl(path, directory = false) {
  const permissions = directory ? '(OI)(CI)F' : 'F'
  const result = spawnSync(
    'icacls',
    [path, '/inheritance:r', '/grant:r', `${userInfo().username}:${permissions}`],
    {
      encoding: 'utf8',
      windowsHide: true,
    },
  )
  if (result.status !== 0) {
    throw new MCPError(`设置凭据权限失败：${result.stderr || result.stdout || 'icacls 失败'}`)
  }
}

async function saveToken(token) {
  await mkdir(TOKEN_DIR, {
    recursive: true,
    mode: 0o700,
  })
  if (process.platform === 'win32') {
    restrictWindowsAcl(TOKEN_DIR, true)
  } else {
    await chmod(TOKEN_DIR, 0o700)
  }

  const temporaryPath = `${TOKEN_PATH}.${process.pid}.${randomBytes(6).toString('hex')}.tmp`
  try {
    await writeFile(temporaryPath, `${JSON.stringify(token, null, 2)}\n`, {
      flag: 'wx',
      mode: 0o600,
    })
    if (process.platform === 'win32') {
      restrictWindowsAcl(temporaryPath)
    } else {
      await chmod(temporaryPath, 0o600)
    }
    await rename(temporaryPath, TOKEN_PATH)
    if (process.platform === 'win32') restrictWindowsAcl(TOKEN_PATH)
  } catch (error) {
    await rm(temporaryPath, { force: true })
    throw error
  }
}

async function login() {
  const issuer = 'https://ai.ihaola.com.cn'
  const callback = {
    code: '',
    error: '',
    state: '',
  }
  let resolveCallback
  let rejectCallback
  const callbackPromise = new Promise((resolve, reject) => {
    resolveCallback = resolve
    rejectCallback = reject
  })
  const server = createServer((request, response) => {
    const url = new URL(request.url || '/', issuer)
    if (url.pathname !== '/callback') {
      response.writeHead(404)
      response.end('Not Found')
      return
    }
    callback.code = url.searchParams.get('code') || ''
    callback.error = url.searchParams.get('error') || ''
    callback.state = url.searchParams.get('state') || ''
    response.writeHead(callback.code ? 200 : 400, {
      'Content-Type': 'text/html; charset=utf-8',
    })
    response.end(callback.code
      ? '<h2>登录成功</h2><p>可以关闭这个页面，回到对话继续。</p>'
      : '<h2>登录失败</h2><p>没有拿到授权码。</p>')
    if (callback.code || callback.error) resolveCallback(callback)
  })

  await new Promise((resolve, reject) => {
    server.once('error', reject)
    server.listen(0, '127.0.0.1', resolve)
  })

  try {
    const port = server.address().port
    const redirectUri = `http://127.0.0.1:${port}/callback`
    const registration = await postJson(
      `${issuer}/api/auth/oauth/register`,
      {
        client_name: CLIENT_NAME,
        redirect_uris: [redirectUri],
        grant_types: ['authorization_code', 'refresh_token'],
        response_types: ['code'],
        token_endpoint_auth_method: 'none',
      },
    )
    const pkce = buildPkce()
    const state = randomBytes(16).toString('base64url')
    const authorizeUrl = new URL(`${issuer}/api/auth/oauth/authorize`)
    authorizeUrl.search = new URLSearchParams({
      response_type: 'code',
      client_id: registration.client_id,
      redirect_uri: redirectUri,
      scope: 'haola-pe',
      state,
      code_challenge: pkce.challenge,
      code_challenge_method: 'S256',
      resource: MCP_URL,
    }).toString()

    process.stdout.write(`请在浏览器完成登录：${authorizeUrl}\n`)
    openBrowser(authorizeUrl.toString())
    const timeout = setTimeout(() => {
      rejectCallback(new MCPError('登录超时'))
    }, 300000)
    const result = await callbackPromise.finally(() => clearTimeout(timeout))
    if (result.error) throw new MCPError(result.error)
    if (result.state !== state) throw new MCPError('state 不匹配')

    const token = await postForm(
      `${issuer}/api/auth/oauth/token`,
      {
        grant_type: 'authorization_code',
        code: result.code,
        redirect_uri: redirectUri,
        client_id: registration.client_id,
        code_verifier: pkce.verifier,
        resource: MCP_URL,
      },
    )
    const saved = {
      access_token: token.access_token,
      refresh_token: token.refresh_token,
      token_type: token.token_type || 'Bearer',
      expires_at: token.expires_in
        ? Math.floor(Date.now() / 1000) + Number(token.expires_in)
        : null,
      client_id: registration.client_id,
      obtained_at: Math.floor(Date.now() / 1000),
    }
    await saveToken(saved)
    process.stdout.write(`登录成功，凭据已保存到 ${TOKEN_PATH}\n`)
  } finally {
    server.close()
  }
}

async function main() {
  const [command, ...args] = process.argv.slice(2)
  if (command === 'ping') {
    await ensureReady()
    process.stdout.write(`连接成功：${MCP_URL}\n`)
    return
  }
  if (command === 'tools') {
    const tools = await listTools()
    process.stdout.write(`当前可调用 ${tools.length} 个工具\n`)
    for (const tool of tools) {
      process.stdout.write(`  ${tool.name.padEnd(24)}${(tool.description || '').split('\n')[0]}\n`)
    }
    return
  }
  if (command === 'call') {
    if (!args[0]) throw new MCPError('用法：node scripts/haola.mjs call <工具名> \'<json>\'')
    const argumentsValue = JSON.parse(args[1] || '{}')
    if (!argumentsValue || Array.isArray(argumentsValue) || typeof argumentsValue !== 'object') {
      throw new MCPError('工具参数必须是 JSON 对象')
    }
    printJson(await callTool(args[0], argumentsValue))
    return
  }
  if (command === 'login') {
    await login()
    return
  }
  if (command === 'whoami') {
    const token = await readToken()
    process.stdout.write(token ? `已登录：${TOKEN_PATH}\n` : '未登录\n')
    if (!token) process.exitCode = 1
    return
  }
  if (command === 'logout') {
    await rm(TOKEN_PATH, { force: true })
    process.stdout.write('已清除本地凭据\n')
    return
  }
  process.stdout.write([
    '用法：node scripts/haola.mjs <命令>',
    '',
    '命令：',
    '  ping',
    '  tools',
    '  call <工具名> \'<json>\'',
    '  login',
    '  whoami',
    '  logout',
  ].join('\n') + '\n')
  process.exitCode = 1
}

main().catch(error => {
  process.stderr.write(`${error.message || error}\n`)
  process.exitCode = 1
})
