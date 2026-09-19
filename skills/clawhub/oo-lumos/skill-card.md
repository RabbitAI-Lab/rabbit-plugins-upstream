## Description:

Lumos helps agents search and read Lumos access request and AppStore app data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and operations teams use this skill to retrieve Lumos access requests and AppStore app records without handling raw credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that execute immediately.

Mitigation: Review the installer source and prefer a verified, pinned, or signed oo CLI installation method before use.

Risk: Future connector actions could change Lumos state if write or destructive actions are added.

Mitigation: Keep use focused on the listed read actions and require explicit user confirmation before any tagged write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lumos)
- [Lumos homepage](https://www.lumos.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects returned by the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
