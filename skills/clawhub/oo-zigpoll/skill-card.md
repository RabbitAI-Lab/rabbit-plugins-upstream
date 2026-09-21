## Description:

Use this skill for Zigpoll requests, including reading, creating, and updating data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Zigpoll through an OOMOL-connected account, including reading users, accounts, polls, slides, participants, and responses. It can also generate trackable survey links after confirming the write action payload and effect with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include running a remotely fetched oo CLI installer script.

Mitigation: Review the installer before execution and prefer an official package manager or verified installer when available.

Risk: The connector can read Zigpoll account data and generate survey links through the connected account.

Mitigation: Connect only an account whose data may be accessed by the OOMOL connector, and confirm generated survey-link write payloads before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-zigpoll)
- [Zigpoll Homepage](https://www.zigpoll.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
