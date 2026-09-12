## Description:

Audit and repair an AI agent's memory corpus for consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thomaszhou22](https://clawhub.ai/user/thomaszhou22)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to audit long-term agent memory files for stale numbers, contradictory facts, dangling file references, stale daily entries, and orphan files before the agent relies on them. The workflow guides the agent to run the local audit script, verify findings with the user or live evidence, apply approved repairs, rerun the audit, and report results in the user's language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local audit script reads workspace memory files and also checks root agent-state files such as AGENTS.md and HEARTBEAT.md.

Mitigation: Run it only on workspaces you intend to audit, and install it only if that local file-reading scope is acceptable.

Risk: Heuristic stale-number and consistency findings may be candidates rather than confirmed facts.

Mitigation: Review findings before allowing edits, and confirm current facts with the user or live evidence before updating memory.

## Reference(s):

- [Source repository](https://github.com/Thomaszhou22/memory-checkup)
- [ClawHub skill page](https://clawhub.ai/thomaszhou22/skills/memory-checkup)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON audit output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled audit script can emit human-readable text or machine-readable JSON; the skill instructs the agent to verify findings before editing memory files.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
