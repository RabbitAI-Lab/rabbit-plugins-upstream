---
name: skill-batch-ops
slug: skill-batch-ops
displayName: Skill Batch Operations
version: "1.0.1"
description: "Batch operations across many skills (3+): inventory, batch patching, multi-platform publish, version alignment, and per-item verification. Use for stale-skill sweeps, fleet-wide version bumps, or bulk ClawHub / SkillHub / GitHub sync. Trigger keywords: 批量更新 skill, batch publish, 批量补丁, 批量发布, multi-skill sync, version phantom occupation, 版本空占, 429 rate limit, 两周未更新, stale skill sweep, skill 盘点, 批量同步, align versions, bulk publish verify. Companion to skill-audit-publish which handles single-skill governance; includes the platform restriction checklist."
description_zh: "多 skill 批量运维：盘点 → 批量补丁 → 多平台发布 → 逐项验证。包含平台限制清单（版本空占、skillhub 严格校验、60s 限流、显式传参）。适用于陈旧 skill 盘点、批量版本对齐、三平台批量同步。单 skill 治理走 skill-audit-publish，本 skill 只做批量手术。"
read_when: "Operating on 3 or more skills at once: stale-skill sweeps, batch frontmatter patches, fleet-wide version alignment, or bulk platform sync."
not_for:
  - Single-skill audit / publish / sanitize (use skill-audit-publish)
  - Designing a new skill (use skill-design-guide)
  - Patching non-agent-created skills (use skill-local-overlay)
agent_created: true
---

# Skill Batch Operations

Purpose: run the same operation across N skills without repeating known platform traps N times. Division of labor: skill-audit-publish owns single-skill governance; this skill owns repetition, ordering, and rate-limit choreography.

## Workflow

1. [Deterministic] **Inventory**: build the target list first (slug, local path, local version, platform latest per platform). Never publish blind from memory — always query platform latest before choosing version numbers.
2. [Deterministic] **Version decision**: unified version across all platforms = max(existing platform latests) + 0.0.1. Check ClawHub with `inspect <slug> --versions` (platform Latest can lead the version field inside the file — phantom occupation). Check SkillHub via its API. Check GitHub via the repo frontmatter.
3. [Deterministic] **Batch patch**: apply file changes via scripts written with the file-write tool. NEVER pass multi-line content through shell heredocs or `python -c` string arguments — newlines get corrupted into literal `/n`. Each patched skill gets frontmatter validated: leading `---`, slug, displayName, version, and quoting on the version value.
4. [Deterministic] **Publish ClawHub** per skill with explicit parameters: `--slug`, `--name`, `--version`, `--changelog`, using `C:/` style paths. Remove any platform-generated files (e.g. skill-card.md) from the source directory first. "Version already exists" = phantom occupation → bump and retry.
5. [Deterministic] **Publish SkillHub** per skill, ≥60s between publishes (429 rate limit). Frontmatter must be complete: leading `---`, slug, displayName, version. Downloaded-from-ClawHub files usually need these backfilled.
6. [Deterministic] **Sync GitHub** from the FINAL published source directory (the one with final version numbers), never from install/download directories which may hold stale content. Contents API upserts only — it never deletes removed files.
7. [Deterministic] **Verify**: install each skill back from the platform; diff installed SKILL.md against the published source; confirm version fields match. Record per-item status.

## Platform Restriction Checklist

| Platform | Trap | Countermeasure |
|---|---|---|
| ClawHub | version phantom occupation | `inspect --versions`, target Latest + 0.0.1 |
| ClawHub | platform-generated files in install dirs | delete before publish |
| ClawHub | unquoted version rejected | quote in frontmatter + explicit `--version` |
| SkillHub | strict frontmatter validation | leading `---`, slug, displayName, version |
| SkillHub | 429 on consecutive publishes | ≥60s interval |
| GitHub | connector cannot create personal repos | PAT from credential file, REST API |
| GitHub | contents API never deletes | full re-push from pub source; note stale files |
| All | `\n` corruption in shell args | multi-line content only via written script files |

## Hard Rules

- Per-item verification is never skipped, even when the batch is large.
- Explicit publish parameters always; no reliance on frontmatter defaults for version-critical fields.
- One failure is logged and the batch continues; systemic failure (auth, network) halts the batch immediately.
- GitHub sync source = final published directory, never an install/download directory.

## Failure Handling

- Item fails on one platform: log with the platform error text, continue the rest, include in the final failure table.
- Same item fails twice on the same platform: stop touching that item, mark MANUAL, move on.
- Auth errors: verify the credential source file was actually read and the value actually exported to the subprocess before suspecting the credential itself.

## Output Format

Final batch table: skill | ClawHub version + result | SkillHub version + result | GitHub result | verify status. Followed by a failure list (empty = clean run) and the unified version number used.
