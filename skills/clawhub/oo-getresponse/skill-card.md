## Description:

GetResponse lets agents read, create, update, and delete GetResponse account data through an OOMOL-connected workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate GetResponse accounts, including campaign, contact, newsletter, custom-field, tag, and statistics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance directs users to run an internet installer directly in a shell.

Mitigation: Prefer a signed or checksum-verified installer path, inspect installer content before execution, and avoid running setup from an elevated shell.

Risk: Write and destructive actions can modify or delete GetResponse campaigns and contacts.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running state-changing or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-getresponse)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [GetResponse Homepage](https://www.getresponse.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, an authenticated OOMOL account, and a connected GetResponse account.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
