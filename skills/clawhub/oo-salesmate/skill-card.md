## Description:

Salesmate (salesmate.io). Use this skill for Salesmate requests to read, create, update, and delete CRM data through the OOMOL oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Salesmate CRM through an OOMOL-connected account, including company, product, user, and module workflows. It guides the agent to inspect live action schemas before running commands and to confirm write or destructive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct remote installer commands for the oo CLI.

Mitigation: Review the setup path before installing, use a verified release or package manager, and do not let an agent run curl-to-bash or irm-to-iex automatically.

Risk: The skill can create or delete Salesmate CRM records.

Mitigation: Require explicit confirmation of the payload, target record, and expected effect before running write or destructive actions.

## Reference(s):

- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Salesmate homepage](https://www.salesmate.io)
- [ClawHub Salesmate skill page](https://clawhub.ai/oomol/skills/oo-salesmate)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before action execution; CRM write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
