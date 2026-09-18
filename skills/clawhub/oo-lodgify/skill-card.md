## Description:

Lodgify (lodgify.com). Use this skill for ANY Lodgify request - searching and reading data. Whenever a task involves Lodgify, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Lodgify schemas and retrieve booking, property, room, availability, and quote information through an OOMOL-connected Lodgify account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes remote installer commands that run downloaded scripts directly in a shell.

Mitigation: Review installer instructions before use and prefer a verified, pinned, or package-managed oo CLI installation source.

Risk: Complex or user-supplied JSON payloads can be malformed or interpreted differently than intended.

Mitigation: Inspect the live action schema before constructing payloads and use file-based JSON payloads for complex input.

Risk: Future connector actions could add write or destructive behavior beyond the current read-oriented release.

Mitigation: Require explicit user confirmation before adding or running any write or destructive Lodgify connector action.

## Reference(s):

- [ClawHub Lodgify skill listing](https://clawhub.ai/oomol/skills/oo-lodgify)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Lodgify homepage](https://www.lodgify.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI connector commands and summarize JSON responses from read-oriented Lodgify actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
