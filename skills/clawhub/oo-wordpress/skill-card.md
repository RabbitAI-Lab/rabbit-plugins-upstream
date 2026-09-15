## Description:

Enables agents to read, create, update, and delete WordPress content through an OOMOL-connected WordPress account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate WordPress accounts via OOMOL, including listing content and creating, updating, or deleting posts, pages, comments, categories, and tags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions tell users to execute unverified remote installer scripts for the oo CLI.

Mitigation: Review the installer source before running it, prefer a verified or package-manager installation path, and connect only WordPress accounts where create, update, and delete authority through OOMOL is acceptable.

## Reference(s):

- [ClawHub WordPress Skill](https://clawhub.ai/oomol/skills/oo-wordpress)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [WordPress](https://wordpress.org)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
