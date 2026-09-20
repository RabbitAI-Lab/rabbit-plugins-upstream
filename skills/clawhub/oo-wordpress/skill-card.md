## Description:

Helps agents operate WordPress through OOMOL's oo CLI, including reading, creating, updating, and deleting WordPress content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage WordPress posts, pages, comments, categories, and tags through an OOMOL-connected account. It is intended for WordPress workflows that need live action schemas before constructing JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can execute a remote oo CLI installer before use.

Mitigation: Review the installer source and run it only if OOMOL's installer is trusted; avoid setup steps unless an oo CLI command fails.

Risk: Write and destructive WordPress actions can change or delete site content.

Mitigation: Confirm the exact action, target, and JSON payload with the user before running write or destructive actions.

## Reference(s):

- [ClawHub WordPress Skill Page](https://clawhub.ai/oomol/skills/oo-wordpress)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [WordPress](https://wordpress.org)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed, oo connector actions return JSON responses that include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
