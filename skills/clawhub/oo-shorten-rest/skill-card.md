## Description:

Shorten.REST (shorten.rest). Use this skill for ANY Shorten.REST request: reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Shorten.REST URL aliases through an OOMOL-connected account. It supports creating, retrieving, updating, listing, and deleting aliases, plus listing click records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Review setup before installation, use verified official packages or pinned releases, and do not allow an agent to run remote installer scripts automatically.

Risk: Alias creation, update, and deletion can change or remove Shorten.REST data.

Mitigation: Confirm exact payloads and targets with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shorten-rest)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Shorten.REST Homepage](https://shorten.rest)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
