## Description:

Loomio (loomio.com). Use this skill for ANY Loomio request: searching and reading poll data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Loomio poll information from an OOMOL-connected Loomio account. It supports reading a specific poll and listing polls for a group with schema-first command guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a remotely downloaded installer without verification.

Mitigation: Review the oo CLI installation source before use and prefer a signed package, pinned version, checksum, or signature verification with explicit user approval.

Risk: Connected Loomio accounts may expose private Loomio content through OOMOL even though the listed actions are read-only.

Mitigation: Use an account with appropriate access scope and confirm that requested poll or group data may be shared before returning sensitive results.

## Reference(s):

- [ClawHub Loomio Skill Page](https://clawhub.ai/oomol/skills/oo-loomio)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Loomio Homepage](https://www.loomio.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Markdown, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs read-only Loomio connector actions through the oo CLI after inspecting the live action schema.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
