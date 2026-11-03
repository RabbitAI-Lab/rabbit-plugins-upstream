const MCP_URL = 'https://ai.ihaola.com.cn/api/mcp/haola-pe'
const PROTOCOL_VERSION = '2025-06-18'
const CLIENT_VERSION = '1.0.0'
const ALLOWED_TOOLS = new Set([
  'plan_quotation',
  'vendor_brands',
  'vendor_list',
  'knowledge_get',
  'faq',
  'corp_inquiry',
  'corp_contact',
  'help',
  'progress_report',
])

class MCPError extends Error {
  constructor(message, status) {
    super(message)
    this.name = 'MCPError'
    this.status = status
  }
}

let sessionId = ''
let nextId = 0
let initialized = false
let protocolVersion = ''

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
  const headers = {
    Accept: 'application/json, text/event-stream',
    'Content-Type': 'application/json',
  }
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
  if (response.status === 401) throw new MCPError('需要先登录', 401)
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
      name: '好啦体检 · 企业团检报价',
      version: CLIENT_VERSION,
    },
  })
  protocolVersion = result?.protocolVersion || PROTOCOL_VERSION
  await rpc('notifications/initialized', undefined, true)
  initialized = true
}

async function listTools() {
  await ensureReady()
  const result = await rpc('tools/list', {})
  return (result?.tools || []).filter(tool => ALLOWED_TOOLS.has(tool.name))
}

async function callTool(name, argumentsValue) {
  if (!ALLOWED_TOOLS.has(name)) throw new MCPError(`工具 ${name} 不在本 Skill 的调用范围内`)
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
  process.stdout.write([
    '用法：node scripts/haola.mjs <命令>',
    '',
    '命令：',
    '  ping',
    '  tools',
    '  call <工具名> \'<json>\'',
  ].join('\n') + '\n')
  process.exitCode = 1
}

main().catch(error => {
  process.stderr.write(`${error.message || error}\n`)
  process.exitCode = 1
})
