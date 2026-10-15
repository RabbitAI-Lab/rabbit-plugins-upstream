## Description:

Helps agents scan third-party OpenClaw skills with ClawVet and review findings before installation or use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users vet third-party skills before installing, enabling, or running them, and review installed skills for concerning findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an untrusted or unexpected scanner version may expose local skill folders to unwanted behavior.

Mitigation: Use an installed ClawVet CLI obtained from a trusted source; review updates before installing them.

Risk: Incomplete scans or overlooked warnings could lead to installing an unsafe skill.

Mitigation: Require complete local coverage and review the scanner's warnings and recommendation before installation.

## Reference(s):

- [clawvet-guard on ClawHub](https://clawhub.ai/mohibshaikh/skills/clawvet-guard)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Text with scan commands and finding summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scan coverage, recommendation, and high-severity findings before installation decisions.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
