## Description:

Zip Archive API helps agents compress publicly accessible files into ZIP archives and extract publicly accessible archives through an OOMOL-connected Zip Archive API account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to compress publicly accessible files into ZIP archives or extract publicly accessible archives through a connected Zip Archive API account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI from a pinned, verified release or trusted package manager before using the skill.

Risk: The extract_archive action is marked as write-capable and can create transit-hosted extracted files.

Mitigation: Confirm the exact action payload and intended effect with the user before running write actions.

## Reference(s):

- [Zip Archive API homepage](https://archiveapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zip-archive-api)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before constructing payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
