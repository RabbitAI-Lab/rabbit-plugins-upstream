## Description:

Bilingual local scanner that helps developers red-team agents or prompts before launch by detecting jailbreak and dangerous-capability patterns, assigning risk tiers, and returning hardening guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and security reviewers use this skill to run local pre-release checks on agent prompts or prompt files for jailbreak, instruction override, data exfiltration, privilege escalation, and related dangerous-request patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented blocking gate fails open, so the scanner exit code may not reliably stop unsafe releases.

Mitigation: Review scan results manually and do not use the exit code as the sole release-blocking control until the gate behavior is fixed and verified.

Risk: The install path includes an unpinned global npx command.

Mitigation: Use a pinned, reviewed package or install from a trusted, versioned artifact before running in shared or production environments.

Risk: Prompt scans may include secrets, proprietary prompts, or other sensitive content.

Mitigation: Run scans locally on sanitized inputs when possible and avoid sharing scan logs that contain sensitive prompt text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-redteam-kit)
- [LGD Hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and plain-text scanner output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local scanner output with matched patterns, risk tiers, and hardening recommendations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
