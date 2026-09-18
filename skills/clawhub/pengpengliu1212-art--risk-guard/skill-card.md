## Description:

Risk Guard helps OpenClaw users diagnose common false failures and require confirmation before high-risk or irreversible operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pengpengliu1212-art](https://clawhub.ai/user/pengpengliu1212-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators using OpenClaw use this skill to run local diagnostics, classify operational risk, and request confirmation before risky actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The diagnostic script may delete older workspace .lock and .tmp files even though the skill presents cleanup as requiring explicit confirmation.

Mitigation: Review before installing, run diagnostics with --dry-run first, and avoid running cleanup in workspaces where older .lock or .tmp files may still be important.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pengpengliu1212-art/skills/risk-guard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, json, guidance]

**Output Format:** [Markdown guidance with command examples and JSON diagnostic reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-only diagnostics; dry-run mode is available before cleanup.]

## Skill Version(s):

1.0.1 (source: release evidence and skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
