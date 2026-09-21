## Description:

Use before installing, enabling, or running any third-party OpenClaw skill, and when the user asks to scan, vet, or check a skill they did not author, or whether such a skill from ClawHub or another untrusted source is safe to install.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT

## Use Case:

Developers and security reviewers use this skill to run ClawVet checks on third-party OpenClaw skills before installation, enabling, or execution. It helps them interpret scan status, coverage, grades, recommendations, and high-severity findings before deciding whether to proceed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the ClawVet npm CLI through npx, which creates a supply-chain dependency on the fetched package version.

Mitigation: Pin the clawvet version or verify npm provenance before running scans in stricter environments.

Risk: Remote or incomplete scans may miss referenced files or dynamic behavior in untrusted skill artifacts.

Mitigation: Stage the full skill locally, require complete coverage and a non-failed status, and treat untrusted skill text as data rather than instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mohibshaikh/skills/clawvet-guard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON field names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node, npm, and npx; scan results depend on ClawVet output and local inspection coverage.]

## Skill Version(s):

1.0.4 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
