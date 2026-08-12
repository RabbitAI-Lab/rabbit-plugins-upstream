## Description:

Kadoa (kadoa.com). Use this skill for ANY Kadoa request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Kadoa through an OOMOL-connected account, including listing workflows, reading workflow status, retrieving extracted records, and creating temporary export links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Kadoa workflow data and create temporary export links through the user's OOMOL-connected account.

Mitigation: Install and use it only when the agent is allowed to access that Kadoa account data; for general Kadoa discussion, instruct the agent not to operate the connector.

Risk: Expired credentials, missing scopes, missing app connections, or billing stops can prevent connector actions from running.

Mitigation: Follow the skill's setup and recovery guidance only after a command fails with the matching authentication, connection, scope, or billing error.

## Reference(s):

- [Kadoa homepage](https://www.kadoa.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kadoa)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON data, execution metadata, or temporary signed export URLs depending on the selected Kadoa action.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
