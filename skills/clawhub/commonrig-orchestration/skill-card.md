## Description:

Delegate coding work to subagents safely - bounded briefs with exact files and acceptance checks, disjoint ownership for parallel writers, no git writes in briefs, and verification before claiming done. The free orchestration protocol from CommonRig, an agent operating kit for Claude Code and Codex.

This skill is ready for commercial/non-commercial use.

## Publisher:

[commonrig](https://clawhub.ai/user/commonrig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using coding agents can delegate well-bounded implementation tasks with clear file ownership and acceptance checks, then review and verify the returned work while retaining scope and integration responsibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated agents may exceed the intended scope or take external actions if their permissions are unclear.

Mitigation: Define each agent's file access, runtime, cost, and external-action permissions before delegation; verify returned work before claiming completion.

## Reference(s):

- [CommonRig Orchestration on ClawHub](https://clawhub.ai/commonrig/skills/commonrig-orchestration)
- [CommonRig](https://commonrig.com)
- [CommonRig orchestration protocol sample](https://commonrig.com/v1/sample)
- [CommonRig sample repository](https://github.com/commonrig/commonrig-sample)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Concise written guidance and delegation brief templates in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plain guidance; no scripts, network calls, or credentials.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
