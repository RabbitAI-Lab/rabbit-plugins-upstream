#!/usr/bin/env node

import { existsSync, readFileSync } from "node:fs"
import { resolve, join } from "node:path"

const args = process.argv.slice(2)
const valueAfter = (flag, fallback) => {
  const index = args.indexOf(flag)
  return index >= 0 && args[index + 1] ? args[index + 1] : fallback
}

const root = resolve(valueAfter("--workspace", "."))
const jsonOutput = args.includes("--json")
const findings = []

function add(level, code, message, file = "") {
  findings.push({ level, code, message, file })
}

function read(relativePath) {
  const path = join(root, relativePath)
  return existsSync(path) ? readFileSync(path, "utf8") : ""
}

function parseScalar(raw) {
  const value = raw.trim()
  if (
    (value.startsWith('"') && value.endsWith('"')) ||
    (value.startsWith("'") && value.endsWith("'"))
  ) {
    return value.slice(1, -1)
  }
  if (value === "true") return true
  if (value === "false") return false
  if (/^-?\d+$/.test(value)) return Number(value)
  return value
}

function parseFrontmatter(text) {
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/)
  if (!match) return undefined

  const data = {}
  for (const line of match[1].split(/\r?\n/)) {
    if (!line.trim() || line.trimStart().startsWith("#")) continue
    const field = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/)
    if (!field) continue
    data[field[1]] = parseScalar(field[2])
  }
  return data
}

function isHeading(line, heading) {
  const value = line.trim()
  const prefix = `## ${heading}`
  return value === prefix || value.startsWith(`${prefix} /`)
}

function section(text, heading) {
  const lines = text.split(/\r?\n/)
  const start = lines.findIndex((line) => isHeading(line, heading))
  if (start < 0) return ""
  const content = []
  for (let index = start + 1; index < lines.length; index += 1) {
    if (/^##\s+/.test(lines[index])) break
    content.push(lines[index])
  }
  return content.join("\n").trim()
}

function meaningful(value) {
  return value
    .split(/\r?\n/)
    .map((line) => line.trim())
    .some((line) => line && line !== "-" && line !== "- [ ]" && !line.startsWith("<!--"))
}

function validateLegacy() {
  const legacySets = [
    ["Docs/TARGET.md", "Docs/ACCEPTANCE.md", "Docs/LOOP_STATE.md"],
    ["Docs/TARGET.md", "Docs/ACCEPTANCE.md", "Docs/WORK_ORDER.md"],
  ]
  const found = legacySets.some((set) => set.every((file) => existsSync(join(root, file))))
  if (found) {
    add(
      "warning",
      "legacy_state",
      "No ACTIVE_PACKET.md found. Legacy state is readable, but migrate at a natural boundary.",
    )
    return
  }
  add(
    "error",
    "missing_state",
    "Missing Docs/ACTIVE_PACKET.md and no complete supported legacy state set was found.",
  )
}

function validatePacket() {
  const file = "Docs/ACTIVE_PACKET.md"
  const text = read(file)
  if (!text) {
    validateLegacy()
    return
  }

  const metadata = parseFrontmatter(text)
  if (!metadata) {
    add("error", "missing_frontmatter", "Active Packet must start with YAML frontmatter.", file)
    return
  }

  const requiredFields = [
    "contract_version",
    "packet_id",
    "goal_readiness",
    "project_state",
    "execution_state",
    "alignment_state",
    "qa_required",
    "qa_decision",
    "size",
    "governance",
    "stage",
    "max_stages",
    "stage_minutes",
    "updated_at",
  ]
  for (const field of requiredFields) {
    if (metadata[field] === undefined || metadata[field] === "") {
      add("error", "missing_field", `Active Packet is missing frontmatter field: ${field}.`, file)
    }
  }

  const allowed = {
    goal_readiness: [
      "Concept",
      "Direction",
      "Ready for Planning",
      "Ready for Execution",
      "Owner Decision Required",
    ],
    project_state: [
      "Active",
      "Needs Fix",
      "Blocked",
      "Accepted",
      "Accepted With Risk",
      "Invalid State",
    ],
    execution_state: [
      "Ready",
      "In Progress",
      "Ready for Review",
      "Needs Fix",
      "Blocked",
      "Invalid State",
    ],
    alignment_state: [
      "Aligned",
      "At Risk",
      "Locally Compliant, Globally Misaligned",
      "Owner Review Required",
    ],
    qa_decision: [
      "Not Reviewed",
      "Accepted",
      "Accepted With Risk",
      "Failed",
      "Blocked",
      "Not Required",
    ],
    size: ["Small", "Medium", "Large"],
    governance: ["Lite", "Standard", "Full"],
  }

  for (const [field, values] of Object.entries(allowed)) {
    if (metadata[field] !== undefined && !values.includes(metadata[field])) {
      add(
        "error",
        "invalid_value",
        `${field} must be one of: ${values.join(", ")}.`,
        file,
      )
    }
  }

  if (metadata.contract_version !== "2.0") {
    add("error", "unsupported_contract", "contract_version must be \"2.0\".", file)
  }
  if (typeof metadata.qa_required !== "boolean") {
    add("error", "invalid_type", "qa_required must be true or false.", file)
  }
  if (!Number.isInteger(metadata.stage) || metadata.stage < 1 || metadata.stage > 10) {
    add("error", "invalid_stage", "stage must be an integer from 1 to 10.", file)
  }
  if (
    !Number.isInteger(metadata.max_stages) ||
    metadata.max_stages < 1 ||
    metadata.max_stages > 10 ||
    metadata.stage > metadata.max_stages
  ) {
    add("error", "invalid_stage_budget", "max_stages must be 1-10 and not below stage.", file)
  }

  const expectedMinutes = { Small: 30, Medium: 60, Large: 120 }
  if (
    expectedMinutes[metadata.size] &&
    metadata.stage_minutes !== expectedMinutes[metadata.size]
  ) {
    add(
      "warning",
      "nonstandard_stage_minutes",
      `${metadata.size} normally uses ${expectedMinutes[metadata.size]} stage minutes.`,
      file,
    )
  }

  const rank = { Lite: 1, Standard: 2, Full: 3 }
  const minimum = { Small: 1, Medium: 2, Large: 3 }
  if (
    rank[metadata.governance] &&
    minimum[metadata.size] &&
    rank[metadata.governance] < minimum[metadata.size]
  ) {
    add(
      "error",
      "governance_too_light",
      `${metadata.size} work cannot use ${metadata.governance} governance without re-sizing.`,
      file,
    )
  }

  const requiredSections = [
    "Desired Outcome",
    "User And Situation",
    "Current Stage Outcome",
    "Scope",
    "Non-Goals",
    "Acceptance Criteria",
    "Allowed Changes",
    "Protected Boundaries",
    "Evidence Required",
    "Stop Conditions",
    "Assumptions And Decisions",
    "Current Evidence",
    "One Next Action",
  ]
  for (const heading of requiredSections) {
    if (!text.split(/\r?\n/).some((line) => isHeading(line, heading))) {
      add("error", "missing_section", `Active Packet is missing section: ${heading}.`, file)
    }
  }

  for (const heading of [
    "Desired Outcome",
    "Current Stage Outcome",
    "Scope",
    "Non-Goals",
    "Acceptance Criteria",
  ]) {
    if (!meaningful(section(text, heading))) {
      add("error", "empty_section", `${heading} must contain meaningful content.`, file)
    }
  }

  const activeStates = ["Ready", "In Progress", "Needs Fix"]
  if (
    activeStates.includes(metadata.execution_state) &&
    !meaningful(section(text, "One Next Action"))
  ) {
    add("error", "missing_next_action", "Active execution requires exactly one next action.", file)
  }

  if (metadata.execution_state === "Ready for Review") {
    if (!meaningful(section(text, "Current Evidence"))) {
      add("error", "missing_evidence", "Ready for Review requires current evidence.", file)
    }
    if (/^- \[ \]/m.test(section(text, "Acceptance Criteria"))) {
      add(
        "error",
        "unchecked_acceptance",
        "Ready for Review cannot contain unchecked acceptance criteria.",
        file,
      )
    }
  }

  if (metadata.qa_decision === "Failed") {
    if (metadata.execution_state !== "Needs Fix" || metadata.project_state !== "Needs Fix") {
      add(
        "error",
        "failed_state_mismatch",
        "QA Failed requires execution_state and project_state to be Needs Fix.",
        file,
      )
    }
  }

  if (["Accepted", "Accepted With Risk"].includes(metadata.project_state)) {
    const acceptedQa = ["Accepted", "Accepted With Risk", "Not Required"]
    if (!acceptedQa.includes(metadata.qa_decision)) {
      add(
        "error",
        "acceptance_state_mismatch",
        "Accepted project state requires an accepted or not-required QA decision.",
        file,
      )
    }
  }

  if (
    metadata.alignment_state === "Locally Compliant, Globally Misaligned" &&
    ["Ready", "In Progress", "Ready for Review"].includes(metadata.execution_state)
  ) {
    add(
      "error",
      "misalignment_not_stopped",
      "Globally misaligned work must stop active execution for direction review.",
      file,
    )
  }

  if (metadata.qa_required === true && metadata.qa_decision === "Not Required") {
    add("error", "qa_requirement_mismatch", "qa_required true conflicts with Not Required.", file)
  }
}

function validateLoopRuns() {
  const file = "Docs/LOOP_RUNS.jsonl"
  const text = read(file)
  if (!text.trim()) {
    add("warning", "missing_loop_runs", "No loop-run evidence was found.", file)
    return
  }

  const required = [
    "contract_version",
    "timestamp",
    "packet_id",
    "stage",
    "loop",
    "result",
    "summary",
    "evidence",
    "next_action",
  ]

  text.split(/\r?\n/).forEach((line, index) => {
    if (!line.trim()) return
    let record
    try {
      record = JSON.parse(line)
    } catch (error) {
      add("error", "invalid_jsonl", `Line ${index + 1} is not valid JSON.`, file)
      return
    }
    if (!record || typeof record !== "object" || Array.isArray(record)) {
      add("error", "invalid_record", `Line ${index + 1} must be a JSON object.`, file)
      return
    }
    for (const field of required) {
      if (record[field] === undefined) {
        add("warning", "missing_log_field", `Line ${index + 1} is missing ${field}.`, file)
      }
    }
    if (record.contract_version && record.contract_version !== "2.0") {
      add("warning", "old_log_contract", `Line ${index + 1} uses another contract version.`, file)
    }
  })
}

validatePacket()
validateLoopRuns()

const summary = {
  errors: findings.filter((item) => item.level === "error").length,
  warnings: findings.filter((item) => item.level === "warning").length,
}

if (jsonOutput) {
  console.log(JSON.stringify({ workspace: root, findings, summary }, null, 2))
} else {
  console.log("Agent Loop State Validator v2.0")
  console.log(`Workspace: ${root}`)
  for (const finding of findings) {
    const location = finding.file ? ` ${finding.file}` : ""
    console.log(`- ${finding.level.toUpperCase()} [${finding.code}]${location}: ${finding.message}`)
  }
  if (findings.length === 0) console.log("PASS: state contract is consistent.")
  console.log(`Summary: ${summary.errors} error(s), ${summary.warnings} warning(s).`)
}

process.exitCode = summary.errors > 0 ? 1 : 0
