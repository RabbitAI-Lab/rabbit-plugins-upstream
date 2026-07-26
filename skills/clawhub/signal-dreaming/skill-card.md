## Description: <br>
Safe single-owner bounded memory consolidation with guarded backups, recovery, and deterministic audits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lzyling](https://clawhub.ai/user/lzyling) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to consolidate daily memory logs into durable topic files, a compact MEMORY.md index, and a bounded dream diary while preserving backups, ownership checks, and deterministic audits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs local memory file writes in the target workspace. <br>
Mitigation: Install it only in workspaces where it should maintain MEMORY.md and top-level memory topic files, keep built-in OpenClaw Dreaming disabled before writes, and review the generated plan before editing. <br>
Risk: Multiple scheduled memory writers could create ownership ambiguity. <br>
Mitigation: Create at most one scheduled writer yourself when using the cron template, and run scheduled invocations through preflight with --scheduled. <br>
Risk: Memory consolidation can accidentally preserve outdated authority, lifecycle state, contradictions, or unnecessary private detail. <br>
Mitigation: Review touched topic files semantically before finalization and rely on the deterministic audit to report credential categories by file. <br>
Risk: Incomplete runs require human recovery before another write run. <br>
Mitigation: Inspect the manifest and backups, restore or reconcile files manually, then acknowledge only the exact reviewed run id. <br>


## Reference(s): <br>
- [Signal Dreaming on ClawHub](https://clawhub.ai/lzyling/skills/signal-dreaming) <br>
- [Signal Dreaming V3 Protocol](references/dream-protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command blocks; scripts produce JSON plans, manifests, audits, and state files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces bounded local file updates to MEMORY.md, top-level memory topic files, memory/dream-log.md, logs/signal-dreaming/state.json, and .backup/memory-dreams manifests when its guarded write workflow is followed.] <br>

## Skill Version(s): <br>
3.0.0-rc.1 (source: server release metadata and SKILL.md release candidate note) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
