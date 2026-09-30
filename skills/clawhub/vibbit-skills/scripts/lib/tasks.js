'use strict'

const fs = require('node:fs/promises')
const path = require('node:path')
const crypto = require('node:crypto')
const { VibbitError } = require('./client')
const { normalize } = require('./results')
const { commands } = require('./registry')
const { stringifyJson } = require('./json')
const { wireIntegers } = require('./translation')

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms))
function wireBody(spec, input) {
  if (spec.defaults) input = { ...spec.defaults, ...input }
  if (spec.operation) return wireIntegers(input)
  if (spec.wire === 'native_object') return { task_type: spec.task_type, input_info: { input: wireIntegers(input) } }
  const encoded = JSON.stringify(input)
  // Legacy JSON text is accepted inside input_info.input; the InputInfo envelope must stay an object.
  return { task_type: spec.task_type, input_info: { input: encoded } }
}

async function save(file, record, exclusive = false) {
  await fs.mkdir(path.dirname(file), { recursive: true, mode: 0o700 })
  const text = JSON.stringify(record, null, 2) + '\n'
  if (exclusive) return fs.writeFile(file, text, { flag: 'wx', mode: 0o600 })
  const temporary = `${file}.${crypto.randomUUID()}.tmp`
  await fs.writeFile(temporary, text, { flag: 'wx', mode: 0o600 })
  await fs.rename(temporary, file)
}

function taskPath(taskId) {
  if (typeof taskId !== 'string' || !/^task-[A-Za-z0-9_-]{1,160}$/.test(taskId)) throw new VibbitError('input', 'Expected a complete task-... ID returned by Vibbit')
  return `/tasks/${encodeURIComponent(taskId)}`
}

function requestSpec(spec, input, taskId) {
  if (spec.operation && (typeof taskId !== 'string' || !/^task-\d+$/.test(taskId))) throw new VibbitError('input', 'Translation actions require the complete numeric task-... parent ID')
  return { method: spec.method || 'POST', route: spec.operation ? taskPath(taskId) + spec.suffix : '/tasks', body: wireBody(spec, input) }
}

async function submit(client, name, input, { stateFile, stateDir, taskId, onProgress = () => {} } = {}) {
  const spec = commands[name]
  const file = path.resolve(stateFile || path.join(stateDir || process.env.VIBBIT_STATE_DIR || '.vibbit/tasks', `${crypto.randomUUID()}.json`))
  const { method, route, body } = requestSpec(spec, input, taskId)
  const record = {
    version: 1, command: name, task_type: spec.task_type, base_url: client.base,
    input_sha256: crypto.createHash('sha256').update(stringifyJson(body)).digest('hex'),
    ...(spec.operation ? { task_id: taskId, operation: spec.operation } : {}),
    ...(name === 'translate_video' ? { expected_targets: input.items.map(v => ({ source_sha256: crypto.createHash('sha256').update(v.source_video.url).digest('hex'), languages: v.target_languages || [input.target_language || 'zh-CN'] })) } : {}),
    ...(spec.result_kind === 'translation' ? { review_mode: name === 'translate_video' ? !input.auto_translate : name === 'update_translation' || input.sub_task_id !== undefined } : {}),
    phase: 'SUBMITTING', created_at: new Date().toISOString(),
  }
  await save(file, record, true)
  onProgress({ phase: record.phase, state_file: file })
  let data
  try {
    data = await client.request(method, route, body)
    if (spec.operation && data.task_id && data.task_id !== taskId) throw new VibbitError('protocol', 'Action response has a different task_id', { task_id: taskId, ambiguous: true })
  } catch (error) {
    record.task_id = taskId || error.task_id
    record.request_id = error.request_id
    if (spec.operation) record.mutation_outcome = error.ambiguous === false ? 'rejected' : 'unknown'
    record.phase = spec.operation ? (error.ambiguous === false ? 'REJECTED' : 'MUTATION_UNKNOWN') : error.task_id ? 'ACKNOWLEDGED' : error.ambiguous === false ? 'REJECTED' : 'SUBMIT_UNKNOWN'
    record.updated_at = new Date().toISOString()
    await save(file, record)
    error.state_file = file
    throw error
  }
  // Record the server ID before decoding results, so a schema error can still be recovered by GET.
  if (spec.operation) data = { ...data, task_id: taskId }
  record.task_id = data.task_id
  record.request_id = data.request_id
  if (spec.operation) record.mutation_outcome = 'acknowledged'
  // Synchronous handlers intentionally return no task_id; their result is the
  // terminal response, so the journal must not label a successful call unknown.
  record.phase = data.task_id ? 'ACKNOWLEDGED' : spec.mode === 'sync' ? 'COMPLETED' : 'SUBMIT_UNKNOWN'
  await save(file, record)
  onProgress({ phase: record.phase, task_id: data.task_id, state_file: file })
  try {
    const output = normalize(data, { ...spec, expected_targets: record.expected_targets })
    if (output.status !== 'COMPLETED' && !output.task_id) throw new VibbitError('protocol', 'Pending submission is missing task_id; do not resubmit', { request_id: data.request_id, ambiguous: true })
    record.phase = output.status
    record.updated_at = new Date().toISOString()
    // Results and temporary upload credentials deliberately stay out of the journal.
    await save(file, record)
    return {
      ...output,
      state_file: file,
      command: name,
      ...(record.mutation_outcome ? { mutation_outcome: record.mutation_outcome } : {}),
      ...(record.review_mode && ['PENDING', 'RUNNING'].includes(output.status)
        ? { review_context_required: true, review_visibility: output.review_visibility || 'unavailable' }
        : {}),
    }
  } catch (error) {
    if (error.kind === 'task_failed') {
      record.phase = error.status || 'FAILED'; record.updated_at = new Date().toISOString()
      await save(file, record)
    }
    error.state_file = file
    throw error
  }
}

async function status(client, taskId, spec = {}, budgetMs) {
  const data = await client.request('GET', taskPath(taskId), undefined, budgetMs)
  if (data.task_id && data.task_id !== taskId) throw new VibbitError('protocol', 'Returned task_id differs from the requested task_id', { task_id: taskId })
  const taskSpec = commands[Object.keys(commands).find(key => commands[key].task_type === data.task_info?.task_type)] || spec
  return normalize({ ...data, task_id: taskId }, { ...taskSpec, expected_targets: spec.expected_targets })
}

async function wait(client, taskId, { spec = {}, timeoutMs = 50000, intervalMs = 5000, stateFile, onProgress = () => {}, now = Date.now, delay = sleep } = {}) {
  if (intervalMs < 5000) throw new VibbitError('input', 'Polling interval must be at least 5 seconds')
  if (!(timeoutMs > 0 && timeoutMs <= 3600000)) throw new VibbitError('input', 'Wait timeout must be between 1 ms and one hour')
  const initialRecord = stateFile ? await loadState(stateFile, client.base) : undefined
  if (initialRecord?.expected_targets) spec = { ...spec, expected_targets: initialRecord.expected_targets }
  const deadline = now() + timeoutMs
  let last
  let minimumInterval = spec.min_poll_ms || 10000
  while (now() < deadline) {
    try {
      last = await status(client, taskId, spec, deadline - now())
      if (initialRecord?.mutation_outcome) last.mutation_outcome = initialRecord.mutation_outcome
      if (initialRecord?.mutation_outcome === 'unknown') last.warnings = [...(last.warnings || []), 'The write outcome remains unknown; GET does not prove that the edit or confirmation was applied.']
      const known = Object.values(commands).find(s => s.task_type === last.task_type)
      if (known) minimumInterval = known.min_poll_ms
      if (stateFile) {
        const record = await loadState(stateFile, client.base)
        record.phase = last.status
        record.updated_at = new Date().toISOString()
        await save(stateFile, record)
      }
      onProgress({ task_id: taskId, status: last.status, ...(last.progress_percent !== undefined ? { progress_percent: last.progress_percent } : {}) })
      if (initialRecord?.review_mode && ['PENDING', 'RUNNING'].includes(last.status)) return {
        ...last,
        state_file: path.resolve(stateFile),
        review_context_required: true,
        review_visibility: last.review_visibility || 'unavailable',
      }
      if (['COMPLETED', 'FAILED', 'INSUFFICIENT_POINTS'].includes(last.status)) return { ...last, ...(stateFile ? { state_file: path.resolve(stateFile) } : {}) }
    } catch (error) {
      error.task_id ||= taskId
      if (stateFile) error.state_file = path.resolve(stateFile)
      if (error.kind === 'task_failed' && stateFile) {
        const record = await loadState(stateFile, client.base)
        record.phase = error.status || 'FAILED'; record.updated_at = new Date().toISOString()
        await save(stateFile, record)
      }
      const retryableRead = error.kind === 'transport' || error.http_status === 429 || error.http_status >= 500 || [1006, 500].includes(error.code)
      if (!retryableRead) throw error
      onProgress({ task_id: taskId, status: 'QUERY_RETRY', code: error.code })
      const backoff = Math.max(intervalMs, minimumInterval, (error.retry_after_seconds || 0) * 1000)
      await delay(Math.min(backoff, Math.max(0, deadline - now())))
      continue
    }
    await delay(Math.min(Math.max(intervalMs, minimumInterval), Math.max(0, deadline - now())))
  }
  return { ok: true, task_id: taskId, status: last?.status || 'UNKNOWN', wait_timed_out: true, ...(initialRecord?.mutation_outcome ? { mutation_outcome: initialRecord.mutation_outcome } : {}), ...(stateFile ? { state_file: path.resolve(stateFile) } : {}) }
}

async function loadState(file, base) {
  const record = JSON.parse(await fs.readFile(file, 'utf8'))
  if (record.version !== 1 || !commands[record.command]) throw new VibbitError('input', 'Unrecognized task journal')
  if (record.base_url !== base) throw new VibbitError('configuration', 'Journal belongs to a different API environment; use its original VIBBIT_BASE_URL')
  return record
}

async function resume(client, file, options = {}) {
  const record = await loadState(file, client.base)
  if (!record.task_id) throw new VibbitError('cannot_resume', 'Journal has no server task ID. Do not resubmit automatically; resolve the original submission with Vibbit first.', { state_file: path.resolve(file), phase: record.phase, request_id: record.request_id })
  return wait(client, record.task_id, { ...options, spec: commands[record.command], stateFile: file })
}

module.exports = { wireBody, requestSpec, submit, status, wait, resume, loadState }
