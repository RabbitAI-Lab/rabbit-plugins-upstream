## Description:

Enables agents to read, search, create, update, and delete esa content through an OOMOL-connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and teams with OOMOL-connected esa accounts use this skill to browse, search, create, update, archive, and delete esa posts, comments, categories, tags, members, attachments, and statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may encourage execution of unverified remote installer scripts.

Mitigation: Use a verified package or pinned release with checksum or signature validation, and require explicit user approval before running any installer.

Risk: Write and destructive esa actions can modify, overwrite, archive, or permanently delete workspace content.

Mitigation: Confirm the target, exact payload, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-esa)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [esa](https://esa.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include esa connector results, Markdown content, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
