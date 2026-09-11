## Description:

Diagnose and safely repair one local Codex Desktop task selected by its UI title or thread ID when recent turns are missing, truncated, merged into an interrupted turn, or hidden by damaged rollout ordering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to diagnose one damaged local Codex Desktop conversation and, when the supported corruption pattern is detected, guide a guarded offline repair and verification workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generated .command launcher may be affected by command injection according to the security scan.

Mitigation: Inspect the resolved thread ID before running the launcher, or wait until the publisher fixes the launcher escaping and validation issue.

Risk: The documented npx installation path is unpinned and third-party.

Mitigation: Install from ClawHub or from a pinned, reviewed commit.

Risk: The skill can modify local Codex conversation files.

Mitigation: Use it only for the specific supported repair case and keep backups until the repaired UI state is confirmed.

## Reference(s):

- [Supported and unsupported repair patterns](references/repair-patterns.md)
- [Codex Thread Repair README](README.md)
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/codex-thread-repair)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and local diagnostic output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prepare a local .command launcher, backups, and a repaired JSONL rollout only for the supported repair case.]

## Skill Version(s):

1.0.1 (source: server release metadata and artifact changelog, released 2026-09-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
