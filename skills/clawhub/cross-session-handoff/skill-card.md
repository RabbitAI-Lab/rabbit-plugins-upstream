## Description:

Produce a structured handoff document so another session or agent can resume work without re-deriving state, decisions, blockers, or next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tooled-app](https://clawhub.ai/user/tooled-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and operators use this skill when pausing, transferring, or resuming work across sessions. It helps the next worker understand current state, completed work, blockers, decisions, dependencies, and ordered next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated handoffs can expose sensitive project context if shared beyond the intended team.

Mitigation: Review each handoff before sharing and reference secret names only; do not include secret values.

Risk: A stale handoff can cause a later agent to act on outdated state, blockers, or next steps.

Mitigation: Use the required expiry date and mark completed handoffs resolved after work resumes.

## Reference(s):

- [OpenClaw](https://openclaw.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown handoff document with a YAML machine-readable block]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires writing a handoff file; generated handoffs should reference secret names only, not secret values.]

## Skill Version(s):

1.1.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
