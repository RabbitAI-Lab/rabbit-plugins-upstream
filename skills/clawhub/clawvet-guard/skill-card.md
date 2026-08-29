## Description:

Use before installing, enabling, or running any third-party OpenClaw skill, and when the user says "install this skill", "is this skill safe", "scan/vet/check this skill", or "should I trust this".

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security-conscious users use this skill before installing, enabling, or running third-party OpenClaw or ClawHub skills. It guides an agent to run ClawVet scans and report risk grades, scores, and high-severity findings before proceeding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses npx-based scanner commands, which may fetch scanner code at runtime.

Mitigation: Pin or preinstall a trusted ClawVet version in environments that require stricter supply-chain control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mohibshaikh/skills/clawvet-guard)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown]

**Output Format:** [Markdown with inline shell commands and JSON result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scanner output may include risk grades, scores, finding counts, and finding details from ClawVet.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
