## Description:

Instantly.ai connector skill for reading, creating, and updating Instantly.ai data through OOMOL's oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Instantly.ai connector schemas and run campaign or lead actions through an OOMOL-connected account. It supports listing campaigns and leads, retrieving campaigns, and creating leads after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands without checksum or pinned release verification.

Mitigation: Prefer a verified package, pinned release, checksum, or manual install guide before installing the OOMOL CLI.

Risk: The create_lead action can change Instantly.ai data.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-instantly-ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Instantly.ai homepage](https://instantly.ai)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use live connector schemas and return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
