## Description:

Latchshot lets agents capture public web pages as PNG, JPEG, or PDF artifacts and read Latchshot usage details through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Latchshot from an agent session, capture public web pages in common artifact formats, and check plan usage and quota status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute unverified remote installer scripts on the user's machine.

Mitigation: Review setup before installation and prefer a verified, versioned, signed, or checksum-validated oo CLI source.

Risk: Page capture fetches a public URL, consumes render quota, and stores a generated artifact.

Mitigation: Confirm the target URL and output format before capture, and check usage or quota status when cost or rate limits matter.

## Reference(s):

- [Latchshot homepage](https://latchshot.fly.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-latchshot)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce PNG, JPEG, or PDF capture artifacts; action responses include JSON metadata.]

## Skill Version(s):

1.0.2 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
