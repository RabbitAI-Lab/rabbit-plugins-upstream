## Description:

Operate noCRM.io through OOMOL's oo CLI connector for reading, creating, updating, and deleting leads, plus listing teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators with an OOMOL-connected noCRM.io account use this skill to manage lead workflows through schema-checked connector actions. It supports lead creation, assignment, tagging, duplication, status changes, deletion, description updates, and team listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions use remote installer commands that may be unsafe if the source is not verified.

Mitigation: Review setup instructions before installation and prefer a verified, version-pinned, signed, or checksum-validated oo CLI source.

Risk: Write and destructive noCRM.io actions can change or delete CRM data.

Mitigation: Confirm the exact target, payload, and intended effect with the user before write actions, and require explicit approval before destructive deletion.

## Reference(s):

- [noCRM.io homepage](https://www.nocrm.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nocrm-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands, connector schema guidance, action payload guidance, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
