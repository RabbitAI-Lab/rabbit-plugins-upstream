#!/usr/bin/env node

// src/lib/file.ts
import { closeSync, constants, existsSync, openSync, readFileSync, writeFileSync } from "node:fs";

// src/lib/errors.ts
var TIME_FILE = "time.md";
var MISSING_TIME_FILE_ERROR = "Error: time.md not found. Run 'time init' first.";
var MISSING_SCRATCH_FILE_ERROR = "Error: No scratch pad found. Run 'time scratch' first.";

class CliError extends Error {
  constructor(message) {
    super(message);
    this.name = "CliError";
  }
}
function fail(message) {
  throw new CliError(message);
}
function isCliError(error) {
  return error instanceof CliError;
}

// src/lib/time.ts
function isValidTimezone(value) {
  try {
    new Intl.DateTimeFormat("en-US", { timeZone: value });
    return true;
  } catch {
    return false;
  }
}
function detectTimezone(preferred) {
  const candidates = [preferred, process.env.TZ, Intl.DateTimeFormat().resolvedOptions().timeZone, "UTC"];
  for (const candidate of candidates) {
    if (candidate && isValidTimezone(candidate)) {
      return candidate;
    }
  }
  return "UTC";
}
function getWeekday(date, timezone) {
  return new Intl.DateTimeFormat("en-US", { weekday: "long", timeZone: timezone }).format(date);
}
function isoWeekNumber(date) {
  const utcDate = new Date(Date.UTC(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDate()));
  const day = utcDate.getUTCDay() || 7;
  utcDate.setUTCDate(utcDate.getUTCDate() + 4 - day);
  const yearStart = new Date(Date.UTC(utcDate.getUTCFullYear(), 0, 1));
  return Math.ceil(((utcDate.getTime() - yearStart.getTime()) / 86400000 + 1) / 7);
}
function isoWeeksInYear(year) {
  return isoWeekNumber(new Date(Date.UTC(year, 11, 28)));
}
function quarterForDate(date) {
  const month = date.getUTCMonth();
  const quarter = Math.floor(month / 3) + 1;
  return `Q${quarter} ${date.getUTCFullYear()}`;
}
function buildNow(date = new Date, timezone) {
  const resolvedTimezone = detectTimezone(timezone);
  const year = date.getUTCFullYear();
  return {
    timestamp: date.toISOString(),
    weekday: getWeekday(date, resolvedTimezone),
    week: `${isoWeekNumber(date)} of ${isoWeeksInYear(year)}`,
    quarter: quarterForDate(date),
    timezone: resolvedTimezone
  };
}

// src/lib/parser.ts
function splitRow(row) {
  const cols = row.split("|").map((part) => part.trim());
  return cols.slice(1, -1);
}
function sectionBounds(lines, heading) {
  const startHeadingIndex = lines.findIndex((line) => line.trim() === heading);
  if (startHeadingIndex === -1) {
    return null;
  }
  let end = lines.length;
  for (let i = startHeadingIndex + 1;i < lines.length; i += 1) {
    const line = lines[i] ?? "";
    if (line.trim().startsWith("## ")) {
      end = i;
      break;
    }
  }
  return [startHeadingIndex + 1, end];
}
function subsectionBounds(lines, heading) {
  const startHeadingIndex = lines.findIndex((line) => line.trim() === heading);
  if (startHeadingIndex === -1) {
    return null;
  }
  let end = lines.length;
  for (let i = startHeadingIndex + 1;i < lines.length; i += 1) {
    const trimmed = (lines[i] ?? "").trim();
    if (trimmed.startsWith("### ") || trimmed.startsWith("## ")) {
      end = i;
      break;
    }
  }
  return [startHeadingIndex + 1, end];
}
function parseEventTable(rows, warn, label) {
  const tableRows = rows.filter((line) => line.trim().startsWith("|"));
  if (tableRows.length < 2) {
    return [];
  }
  const events = [];
  for (const row of tableRows.slice(2)) {
    const cols = splitRow(row);
    if (cols.length < 5) {
      warn(`Skipping malformed ${label} row: ${row}`);
      continue;
    }
    const [distance, name, type, notes, iso] = cols;
    if (!name) {
      warn(`Skipping ${label} row with empty event name.`);
      continue;
    }
    events.push({
      distance: distance ?? "",
      name,
      type: type || undefined,
      notes: notes || undefined,
      iso: iso ?? ""
    });
  }
  return events;
}
function parseSequences(lines, bounds, warn) {
  if (!bounds) {
    return [];
  }
  const [start, end] = bounds;
  const sequences = [];
  for (let i = start;i < end; i += 1) {
    const trimmed = (lines[i] ?? "").trim();
    if (!trimmed.startsWith("### ")) {
      continue;
    }
    const name = trimmed.slice(4).trim();
    let chainLine = "";
    for (let j = i + 1;j < end; j += 1) {
      const candidate = (lines[j] ?? "").trim();
      if (!candidate) {
        continue;
      }
      if (candidate.startsWith("### ") || candidate.startsWith("## ")) {
        break;
      }
      chainLine = candidate;
      i = j;
      break;
    }
    if (!chainLine) {
      warn(`Sequence '${name}' is missing a chain line.`);
      continue;
    }
    const events = chainLine.split(/→|->/).map((token) => token.trim()).filter((token) => token && token !== "[NOW]");
    sequences.push({ name, events });
  }
  return sequences;
}
function parseSpans(lines, bounds, warn) {
  if (!bounds) {
    return [];
  }
  const [start, end] = bounds;
  const tableRows = lines.slice(start, end).filter((line) => line.trim().startsWith("|"));
  if (tableRows.length < 2) {
    return [];
  }
  const spans = [];
  for (const row of tableRows.slice(2)) {
    const cols = splitRow(row);
    if (cols.length < 4) {
      warn(`Skipping malformed span row: ${row}`);
      continue;
    }
    const [name, from, to, length] = cols;
    if (!name) {
      continue;
    }
    spans.push({
      name,
      from: from ?? "",
      to: to ?? "",
      length: length ?? ""
    });
  }
  return spans;
}
function parseTimeContext(markdown, options = {}) {
  const warn = options.warn ?? (() => {});
  const lines = markdown.split(/\r?\n/);
  const fallbackNow = buildNow(new Date, "UTC");
  const context = {
    now: fallbackNow,
    behindEvents: [],
    aheadEvents: [],
    sequences: [],
    spans: []
  };
  const nowBounds = sectionBounds(lines, "## Now");
  if (nowBounds) {
    const [start, end] = nowBounds;
    const fields = new Map;
    for (const line of lines.slice(start, end)) {
      const match = line.trim().match(/^-\s+\*\*([^*]+)\*\*:\s*(.*)$/);
      if (!match) {
        continue;
      }
      const key = match[1];
      const value = match[2];
      if (!key || value === undefined) {
        continue;
      }
      fields.set(key.toLowerCase(), value);
    }
    context.now = {
      timestamp: fields.get("timestamp") || fallbackNow.timestamp,
      weekday: fields.get("weekday") || fallbackNow.weekday,
      week: fields.get("week") || fallbackNow.week,
      quarter: fields.get("quarter") || fallbackNow.quarter,
      timezone: fields.get("timezone") || fallbackNow.timezone
    };
  } else {
    warn("Missing ## Now section. Using fallback NOW values.");
  }
  const behindBounds = subsectionBounds(lines, "### Behind (Past)");
  if (behindBounds) {
    const [start, end] = behindBounds;
    context.behindEvents = parseEventTable(lines.slice(start, end), warn, "behind");
  } else {
    warn("Missing ### Behind (Past) section.");
  }
  const aheadBounds = subsectionBounds(lines, "### Ahead (Future)");
  if (aheadBounds) {
    const [start, end] = aheadBounds;
    context.aheadEvents = parseEventTable(lines.slice(start, end), warn, "ahead");
  } else {
    warn("Missing ### Ahead (Future) section.");
  }
  context.sequences = parseSequences(lines, sectionBounds(lines, "## Sequences"), warn);
  context.spans = parseSpans(lines, sectionBounds(lines, "## Durations"), warn);
  return context;
}

// src/lib/distance.ts
var MINUTE = 60 * 1000;
var HOUR = 60 * MINUTE;
var DAY = 24 * HOUR;
var WEEK = 7 * DAY;
var MONTH = 30 * DAY;
function pluralize(value, unit) {
  return `${value} ${unit}${value === 1 ? "" : "s"}`;
}
function unitForMs(ms) {
  if (ms < HOUR) {
    return { value: Math.round(ms / MINUTE), unit: "minute" };
  }
  if (ms < DAY) {
    return { value: Math.round(ms / HOUR), unit: "hour" };
  }
  if (ms < 14 * DAY) {
    return { value: Math.round(ms / DAY), unit: "day" };
  }
  if (ms < 8 * WEEK) {
    return { value: Math.round(ms / WEEK), unit: "week" };
  }
  return { value: Math.round(ms / MONTH), unit: "month" };
}
function formatDistance(target, now) {
  const diff = target.getTime() - now.getTime();
  const abs = Math.abs(diff);
  const { value, unit } = unitForMs(abs);
  const amount = Math.max(0, value);
  const direction = diff >= 0 ? "ahead" : "behind";
  return `${pluralize(amount, unit)} ${direction}`;
}
function formatLength(ms) {
  const abs = Math.abs(ms);
  const { value, unit } = unitForMs(abs);
  return pluralize(Math.max(0, value), unit);
}
function classifyPosition(target, now) {
  return target.getTime() < now.getTime() ? "behind" : "ahead";
}
function sortTimelineEvents(events) {
  return [...events].sort((a, b) => new Date(a.iso).getTime() - new Date(b.iso).getTime());
}

// src/lib/renderer.ts
function escapeCell(value) {
  return value.replace(/\|/g, "\\|").replace(/\r?\n/g, " ");
}
function renderEventTable(events) {
  const rows = [
    "| distance | event | type | notes | iso |",
    "|----------|-------|------|-------|-----|"
  ];
  for (const event of events) {
    rows.push(`| ${escapeCell(event.distance)} | ${escapeCell(event.name)} | ${escapeCell(event.type || "")} | ${escapeCell(event.notes || "")} | ${escapeCell(event.iso)} |`);
  }
  return rows;
}
function renderNowSection(context) {
  return [
    "## Now",
    `- **timestamp**: ${context.now.timestamp}`,
    `- **weekday**: ${context.now.weekday}`,
    `- **week**: ${context.now.week}`,
    `- **quarter**: ${context.now.quarter}`,
    `- **timezone**: ${context.now.timezone}`
  ];
}
function sequenceWithNow(sequence, context) {
  const allEvents = [...context.behindEvents, ...context.aheadEvents];
  const byName = new Map(allEvents.map((event) => [event.name.toLowerCase(), event]));
  const nowMs = new Date(context.now.timestamp).getTime();
  let insertAt = sequence.events.length;
  for (let i = 0;i < sequence.events.length; i += 1) {
    const eventName = sequence.events[i];
    if (!eventName) {
      continue;
    }
    const event = byName.get(eventName.toLowerCase());
    if (!event) {
      insertAt = i;
      break;
    }
    const eventMs = new Date(event.iso).getTime();
    if (eventMs >= nowMs) {
      insertAt = i;
      break;
    }
  }
  const tokens = [...sequence.events];
  tokens.splice(insertAt, 0, "[NOW]");
  return tokens.join(" → ");
}
function renderTimeContext(context, options = {}) {
  const view = options.view ?? "full";
  const includeMetaSections = options.includeMetaSections ?? true;
  const lines = ["# Time Context", "", ...renderNowSection(context), "", "## Timeline", ""];
  if (view === "full" || view === "past") {
    lines.push("### Behind (Past)", "", ...renderEventTable(sortTimelineEvents(context.behindEvents)), "");
  }
  if (view === "full" || view === "ahead") {
    lines.push("### Ahead (Future)", "", ...renderEventTable(sortTimelineEvents(context.aheadEvents)), "");
  }
  if (view === "full" && includeMetaSections) {
    lines.push("## Sequences", "");
    for (const sequence of context.sequences) {
      lines.push(`### ${sequence.name}`);
      lines.push(sequenceWithNow(sequence, context));
      lines.push("");
    }
    lines.push("## Durations", "", "| span | from | to | length |", "|------|------|----|--------|");
    for (const span of context.spans) {
      lines.push(`| ${escapeCell(span.name)} | ${escapeCell(span.from)} | ${escapeCell(span.to)} | ${escapeCell(span.length)} |`);
    }
    lines.push("");
  }
  return `${lines.join(`
`).trimEnd()}
`;
}

// src/lib/scratch.ts
var SCRATCH_DIR = "/tmp";
var SCRATCH_BASENAME = "time-scratch";
function sanitizeLabel(input) {
  const sanitized = input.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/-+/g, "-").replace(/^-|-$/g, "");
  if (!sanitized) {
    fail(`Error: Label '${input}' contains no valid characters.`);
  }
  return sanitized;
}
function scratchFilePath(label) {
  if (label === undefined) {
    return `${SCRATCH_DIR}/${SCRATCH_BASENAME}.md`;
  }
  return `${SCRATCH_DIR}/${SCRATCH_BASENAME}-${sanitizeLabel(label)}.md`;
}

// src/lib/file.ts
function readMarkdownFile(path, missingMessage) {
  if (!existsSync(path)) {
    throw new CliError(missingMessage);
  }
  return readFileSync(path, "utf8");
}
function readTimeFile() {
  return readMarkdownFile(TIME_FILE, MISSING_TIME_FILE_ERROR);
}
function writeTimeFile(content) {
  writeFileSync(TIME_FILE, content, "utf8");
}
function loadContext(warn) {
  const content = readTimeFile();
  return parseTimeContext(content, { warn });
}
function saveContext(context) {
  const rendered = renderTimeContext(context);
  writeTimeFile(rendered);
  return rendered;
}
function noFollowFlag() {
  return typeof constants.O_NOFOLLOW === "number" ? constants.O_NOFOLLOW : 0;
}
function readScratchFile(path) {
  let fd;
  try {
    fd = openSync(path, constants.O_RDONLY | noFollowFlag());
  } catch (error) {
    const code = error.code;
    if (code === "ENOENT") {
      throw new CliError(MISSING_SCRATCH_FILE_ERROR);
    }
    if (code === "ELOOP") {
      throw new CliError(`Error: Refusing to follow symlink at '${path}'.`);
    }
    throw error;
  }
  try {
    return readFileSync(fd, "utf8");
  } finally {
    closeSync(fd);
  }
}
function writeScratchFile(path, content) {
  let fd;
  try {
    fd = openSync(path, constants.O_WRONLY | constants.O_CREAT | constants.O_TRUNC | noFollowFlag(), 384);
  } catch (error) {
    const code = error.code;
    if (code === "ELOOP") {
      throw new CliError(`Error: Refusing to follow symlink at '${path}'.`);
    }
    throw error;
  }
  try {
    writeFileSync(fd, content, "utf8");
  } finally {
    closeSync(fd);
  }
}
function loadScratchContext(label) {
  const content = readScratchFile(scratchFilePath(label));
  return parseTimeContext(content);
}
function saveScratchContext(context, label) {
  const rendered = renderTimeContext(context, { includeMetaSections: false });
  writeScratchFile(scratchFilePath(label), rendered);
  return rendered;
}

// src/commands/ahead.ts
function aheadCommand() {
  const context = loadContext((message) => process.stderr.write(`Warning: ${message}
`));
  process.stdout.write(renderTimeContext(context, { view: "ahead" }));
}

// src/lib/cli.ts
import { parseArgs } from "node:util";
var USAGE = `Usage: time <command> [options]

Commands:
  init [--timezone <iana_tz>] [--force]
  now [--timezone <iana_tz>]
  add <event> (--in <duration> | --on <date> | --at <datetime>) [--type <type>] [--notes <text>]
  refresh
  show
  past
  ahead
  remove <event>
  seq <name> <event1> <event2> [event3...]
  span <name> --from <when> --to <when>
  scratch [label]
  scratch create [label]
  scratch add <event> (--in <duration> | --on <date> | --at <datetime>) [--scratch <label>]
  scratch show [--scratch <label>]
  scratch clear [--scratch <label>]
`;
function commandError(message) {
  throw new CliError(message);
}
function parseCommandArgs(args, options) {
  return parseArgs({
    args,
    options,
    allowPositionals: true,
    strict: true
  });
}
function runWithErrors(action) {
  try {
    action();
    return 0;
  } catch (error) {
    if (isCliError(error)) {
      process.stderr.write(`${error.message}
`);
      return 1;
    }
    const message = error instanceof Error ? error.message : "Unknown error";
    process.stderr.write(`Error: ${message}
`);
    return 1;
  }
}

// src/lib/context.ts
function emptyContext(timezone) {
  return {
    now: buildNow(new Date, timezone),
    behindEvents: [],
    aheadEvents: [],
    sequences: [],
    spans: []
  };
}
function allEvents(context) {
  return [...context.behindEvents, ...context.aheadEvents];
}
function hasEventName(context, name) {
  const target = name.toLowerCase();
  return allEvents(context).some((event) => event.name.toLowerCase() === target);
}
function upsertEvent(context, event) {
  const now = new Date(context.now.timestamp);
  const when = new Date(event.iso);
  event.distance = formatDistance(when, now);
  if (classifyPosition(when, now) === "behind") {
    context.behindEvents = sortTimelineEvents([...context.behindEvents, event]);
  } else {
    context.aheadEvents = sortTimelineEvents([...context.aheadEvents, event]);
  }
}
function rebuildEventPositions(context) {
  const now = new Date(context.now.timestamp);
  const merged = allEvents(context);
  const behind = [];
  const ahead = [];
  for (const event of merged) {
    const eventDate = new Date(event.iso);
    const next = {
      ...event,
      distance: formatDistance(eventDate, now)
    };
    if (classifyPosition(eventDate, now) === "behind") {
      behind.push(next);
    } else {
      ahead.push(next);
    }
  }
  context.behindEvents = sortTimelineEvents(behind);
  context.aheadEvents = sortTimelineEvents(ahead);
}

// src/lib/duration.ts
var UNIT_MS = {
  minute: 60 * 1000,
  hour: 60 * 60 * 1000,
  day: 24 * 60 * 60 * 1000,
  week: 7 * 24 * 60 * 60 * 1000,
  month: 30 * 24 * 60 * 60 * 1000
};
function normalizeUnit(raw) {
  return raw.toLowerCase().replace(/s$/, "");
}
function parseDuration(input) {
  let text = input.trim().toLowerCase();
  if (!text) {
    throw new Error("Duration cannot be empty. Expected formats like '3 days' or '2 hours ago'.");
  }
  let direction = "future";
  if (text.startsWith("in ")) {
    text = text.slice(3).trim();
    direction = "future";
  }
  if (text.endsWith(" ago")) {
    text = text.slice(0, -4).trim();
    direction = "past";
  } else if (text.endsWith(" from now")) {
    text = text.slice(0, -9).trim();
    direction = "future";
  }
  const match = text.match(/^(-?\d+(?:\.\d+)?)\s*(minutes?|hours?|days?|weeks?|months?)$/i);
  if (!match) {
    throw new Error("Invalid duration. Use forms like '3 days', 'in 2 hours', or '5 days ago'.");
  }
  let value = Number(match[1]);
  if (!Number.isFinite(value)) {
    throw new Error("Invalid duration value.");
  }
  const rawUnit = match[2];
  if (!rawUnit) {
    throw new Error("Invalid duration unit.");
  }
  const unit = normalizeUnit(rawUnit);
  const unitMs = UNIT_MS[unit];
  if (!unitMs) {
    throw new Error(`Unsupported duration unit '${rawUnit}'.`);
  }
  if (value < 0) {
    value = Math.abs(value);
    direction = "past";
  }
  return {
    ms: value * unitMs,
    direction
  };
}

// src/lib/date-parse.ts
var WEEKDAY = {
  sunday: 0,
  monday: 1,
  tuesday: 2,
  wednesday: 3,
  thursday: 4,
  friday: 5,
  saturday: 6
};
function addMs(date, ms) {
  return new Date(date.getTime() + ms);
}
function parseRelativeKeyword(value, base) {
  if (value === "today") {
    return new Date(base);
  }
  if (value === "tomorrow") {
    return addMs(base, 24 * 60 * 60 * 1000);
  }
  if (value === "yesterday") {
    return addMs(base, -24 * 60 * 60 * 1000);
  }
  const nextMatch = value.match(/^next\s+(monday|tuesday|wednesday|thursday|friday|saturday|sunday)$/);
  if (!nextMatch) {
    return null;
  }
  const weekday = nextMatch[1];
  if (!weekday) {
    return null;
  }
  const target = WEEKDAY[weekday];
  if (target === undefined) {
    return null;
  }
  const current = base.getDay();
  let delta = (target - current + 7) % 7;
  if (delta === 0) {
    delta = 7;
  }
  return addMs(base, delta * 24 * 60 * 60 * 1000);
}
function parseDateInput(input, base = new Date) {
  const trimmed = input.trim();
  if (!trimmed) {
    throw new Error("Date input cannot be empty.");
  }
  const lower = trimmed.toLowerCase();
  const relative = parseRelativeKeyword(lower, base);
  if (relative) {
    return relative;
  }
  try {
    const duration = parseDuration(trimmed);
    return addMs(base, duration.direction === "future" ? duration.ms : -duration.ms);
  } catch {}
  const parsed = new Date(trimmed);
  if (!Number.isNaN(parsed.getTime())) {
    return parsed;
  }
  throw new Error("Could not parse date. Use ISO (2026-02-20), named date (Feb 20 2026), or relative forms (tomorrow, next Monday).");
}

// src/lib/event-date.ts
function parseEventDate(inValue, onValue, atValue, now) {
  const count = Number(Boolean(inValue)) + Number(Boolean(onValue)) + Number(Boolean(atValue));
  if (count !== 1) {
    commandError("Error: Provide exactly one of --in, --on, or --at.");
  }
  if (inValue) {
    const parsed = parseDuration(inValue);
    return new Date(now.getTime() + (parsed.direction === "future" ? parsed.ms : -parsed.ms));
  }
  if (onValue) {
    return parseDateInput(onValue, now);
  }
  const atDate = new Date(atValue);
  if (Number.isNaN(atDate.getTime())) {
    commandError("Error: Could not parse --at datetime. Use an ISO datetime like 2026-02-20T14:00:00Z.");
  }
  return atDate;
}

// src/commands/add.ts
function addCommand(args) {
  const parsed = parseCommandArgs(args, {
    in: { type: "string" },
    on: { type: "string" },
    at: { type: "string" },
    type: { type: "string" },
    notes: { type: "string" }
  });
  const eventName = parsed.positionals[0];
  if (!eventName) {
    commandError("Error: Missing event name. Usage: time add <event> (--in|--on|--at ...)");
  }
  const context = loadContext((message) => process.stderr.write(`Warning: ${message}
`));
  if (hasEventName(context, eventName)) {
    commandError(`Error: Event '${eventName}' already exists. Use a distinct name.`);
  }
  const now = new Date(context.now.timestamp);
  const eventDate = parseEventDate(parsed.values.in, parsed.values.on, parsed.values.at, now);
  upsertEvent(context, {
    name: eventName,
    iso: eventDate.toISOString(),
    distance: "",
    type: parsed.values.type,
    notes: parsed.values.notes
  });
  process.stdout.write(saveContext(context));
}

// src/commands/init.ts
import { existsSync as existsSync2, readdirSync } from "node:fs";
function initCommand(args) {
  const parsed = parseCommandArgs(args, {
    timezone: { type: "string" },
    force: { type: "boolean" }
  });
  if (existsSync2(TIME_FILE) && !parsed.values.force) {
    commandError("Error: time.md already exists. Use --force to overwrite.");
  }
  try {
    const scratchFiles = readdirSync(process.cwd()).filter((name) => /^time-scratch.*\.md$/i.test(name));
    if (scratchFiles.length > 0) {
      process.stderr.write(`Warning: Scratch pad files found in this directory. If you need an ephemeral
` + `timeline, use 'time scratch' instead. 'time init' creates a persistent
` + `project timeline.
`);
    }
  } catch {}
  const context = emptyContext(parsed.values.timezone);
  const rendered = saveContext(context);
  process.stdout.write(rendered);
}

// src/commands/now.ts
function nowCommand(args) {
  const parsed = parseCommandArgs(args, {
    timezone: { type: "string" }
  });
  const context = loadContext((message) => process.stderr.write(`Warning: ${message}
`));
  const timezone = parsed.values.timezone || context.now.timezone;
  context.now = buildNow(new Date, timezone);
  process.stdout.write(saveContext(context));
}

// src/commands/past.ts
function pastCommand() {
  const context = loadContext((message) => process.stderr.write(`Warning: ${message}
`));
  process.stdout.write(renderTimeContext(context, { view: "past" }));
}

// src/commands/refresh.ts
function refreshCommand() {
  const context = loadContext((message) => process.stderr.write(`Warning: ${message}
`));
  context.now = buildNow(new Date, context.now.timezone);
  rebuildEventPositions(context);
  process.stdout.write(saveContext(context));
}

// src/commands/remove.ts
function removeCommand(args) {
  const target = args[0];
  if (!target) {
    commandError("Error: Missing event name. Usage: time remove <event>");
  }
  const context = loadContext((message) => process.stderr.write(`Warning: ${message}
`));
  const key = target.toLowerCase();
  const beforeCount = context.behindEvents.length + context.aheadEvents.length;
  context.behindEvents = context.behindEvents.filter((event) => event.name.toLowerCase() !== key);
  context.aheadEvents = context.aheadEvents.filter((event) => event.name.toLowerCase() !== key);
  for (const sequence of context.sequences) {
    sequence.events = sequence.events.filter((eventName) => eventName.toLowerCase() !== key);
  }
  const afterCount = context.behindEvents.length + context.aheadEvents.length;
  if (afterCount === beforeCount) {
    const available = allEvents(context).map((event) => event.name).sort((a, b) => a.localeCompare(b));
    commandError(`Error: Event '${target}' not found. Available events: ${available.join(", ") || "none"}`);
  }
  process.stdout.write(saveContext(context));
}

// src/commands/scratch.ts
import { existsSync as existsSync3, unlinkSync } from "node:fs";
function scratchCreate(label) {
  const context = emptyContext();
  process.stdout.write(saveScratchContext(context, label));
}
function scratchAdd(args) {
  const parsed = parseCommandArgs(args, {
    in: { type: "string" },
    on: { type: "string" },
    at: { type: "string" },
    scratch: { type: "string" }
  });
  const eventName = parsed.positionals[0];
  if (!eventName) {
    commandError("Error: Missing event name. Usage: time scratch add <event> (--in|--on|--at ...)");
  }
  const label = parsed.values.scratch;
  const context = loadScratchContext(label);
  if (hasEventName(context, eventName)) {
    commandError(`Error: Event '${eventName}' already exists in the scratch pad.`);
  }
  const now = new Date(context.now.timestamp);
  const eventDate = parseEventDate(parsed.values.in, parsed.values.on, parsed.values.at, now);
  upsertEvent(context, {
    name: eventName,
    iso: eventDate.toISOString(),
    distance: "",
    type: undefined,
    notes: undefined
  });
  process.stdout.write(saveScratchContext(context, label));
}
function scratchShow(args) {
  const parsed = parseCommandArgs(args, {
    scratch: { type: "string" }
  });
  if (parsed.positionals.length > 0) {
    commandError("Error: Usage: time scratch show [--scratch <label>]");
  }
  const context = loadScratchContext(parsed.values.scratch);
  process.stdout.write(renderTimeContext(context, { includeMetaSections: false }));
}
function scratchClear(args) {
  const parsed = parseCommandArgs(args, {
    scratch: { type: "string" }
  });
  if (parsed.positionals.length > 0) {
    commandError("Error: Usage: time scratch clear [--scratch <label>]");
  }
  const path = scratchFilePath(parsed.values.scratch);
  if (!existsSync3(path)) {
    process.stderr.write(`Warning: No scratch pad found at ${path}. Nothing to clear.
`);
    return;
  }
  unlinkSync(path);
}
function scratchCommand(args) {
  const mode = args[0];
  if (mode === "create") {
    const label = args[1];
    if (args.length > 2) {
      commandError("Error: Usage: time scratch create [label]");
    }
    scratchCreate(label);
    return;
  }
  if (mode === "add") {
    scratchAdd(args.slice(1));
    return;
  }
  if (mode === "show") {
    scratchShow(args.slice(1));
    return;
  }
  if (mode === "clear") {
    scratchClear(args.slice(1));
    return;
  }
  if (args.length > 1) {
    commandError("Error: Usage: time scratch [label]");
  }
  scratchCreate(mode);
}

// src/commands/seq.ts
function seqCommand(args) {
  const name = args[0];
  const events = args.slice(1);
  if (!name) {
    commandError("Error: Missing sequence name. Usage: time seq <name> <event1> <event2> [...]");
  }
  if (events.length < 2) {
    commandError("Error: Sequence requires at least 2 events.");
  }
  const context = loadContext((message) => process.stderr.write(`Warning: ${message}
`));
  const known = new Set(allEvents(context).map((event) => event.name.toLowerCase()));
  const unknown = events.filter((eventName) => !known.has(eventName.toLowerCase()));
  if (unknown.length > 0) {
    process.stderr.write(`Warning: Unknown events in sequence '${name}': ${unknown.join(", ")}
`);
  }
  const index = context.sequences.findIndex((sequence) => sequence.name.toLowerCase() === name.toLowerCase());
  if (index >= 0) {
    context.sequences[index] = { name, events };
  } else {
    context.sequences.push({ name, events });
  }
  process.stdout.write(saveContext(context));
}

// src/commands/show.ts
function showCommand() {
  const context = loadContext((message) => process.stderr.write(`Warning: ${message}
`));
  process.stdout.write(renderTimeContext(context));
}

// src/commands/span.ts
function spanCommand(args) {
  const parsed = parseCommandArgs(args, {
    from: { type: "string" },
    to: { type: "string" }
  });
  const name = parsed.positionals[0];
  if (!name) {
    commandError("Error: Missing span name. Usage: time span <name> --from <when> --to <when>");
  }
  const fromInput = parsed.values.from;
  const toInput = parsed.values.to;
  if (!fromInput || !toInput) {
    commandError("Error: span requires both --from and --to.");
  }
  const context = loadContext((message) => process.stderr.write(`Warning: ${message}
`));
  const now = new Date(context.now.timestamp);
  const fromDate = parseDateInput(fromInput, now);
  const toDate = parseDateInput(toInput, now);
  if (fromDate.getTime() > toDate.getTime()) {
    commandError("Error: --from must be before --to.");
  }
  const span = {
    name,
    from: formatDistance(fromDate, now),
    to: formatDistance(toDate, now),
    length: formatLength(toDate.getTime() - fromDate.getTime())
  };
  const index = context.spans.findIndex((item) => item.name.toLowerCase() === name.toLowerCase());
  if (index >= 0) {
    context.spans[index] = span;
  } else {
    context.spans.push(span);
  }
  process.stdout.write(saveContext(context));
}

// src/index.ts
var commands = {
  init: initCommand,
  add: addCommand,
  now: nowCommand,
  refresh: refreshCommand,
  show: () => showCommand(),
  past: () => pastCommand(),
  ahead: () => aheadCommand(),
  remove: removeCommand,
  scratch: scratchCommand,
  seq: seqCommand,
  span: spanCommand
};
function printUsageToStderr() {
  process.stderr.write(USAGE);
}
var argv = process.argv.slice(2);
var command = argv[0];
if (!command) {
  printUsageToStderr();
  process.exit(1);
}
if (command === "--help" || command === "-h" || command === "help") {
  printUsageToStderr();
  process.exit(0);
}
var handler = commands[command];
if (!handler) {
  process.stderr.write(`Error: Unknown command '${command}'.
`);
  printUsageToStderr();
  process.exit(1);
}
var code = runWithErrors(() => handler(argv.slice(1)));
process.exit(code);
