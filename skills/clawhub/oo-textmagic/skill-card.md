## Description:

Textmagic (textmagic.com). Use this skill for reading, creating, and updating Textmagic data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Textmagic account data, contacts, lists, templates, and current user details, and to create lists or send plain-text SMS messages through the OOMOL oo CLI after confirming state-changing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute changing code on a user machine.

Mitigation: Install the oo CLI only through a trusted, reviewed method; do not allow an agent to run the remote installer automatically.

Risk: SMS sending and list creation can change the connected Textmagic account or incur usage costs.

Mitigation: Confirm the exact action, recipients, payload, and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-textmagic)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Textmagic homepage](https://www.textmagic.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI connector commands and JSON request payloads; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
