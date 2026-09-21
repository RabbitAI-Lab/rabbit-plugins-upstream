## Description:

Feishu (feishu.cn) skill for reading, creating, updating, and deleting Feishu data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Feishu through an OOMOL-connected account, including Drive, Docs, Wiki, Base/Bitable, Sheets, Slides, mail, chat, calendar, tasks, approvals, OKRs, Minutes, and video meeting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute third-party code.

Mitigation: Manually install the oo CLI from vetted documentation and do not let an agent run curl|bash or iex installer commands without review.

Risk: Tagged write and destructive actions can change, overwrite, or remove Feishu data.

Mitigation: Require explicit confirmation of the target, payload, and expected effect before running tagged actions, and inspect the live action schema first.

Risk: The skill operates through OOMOL and the oo CLI using a connected Feishu account.

Mitigation: Install only if OOMOL and the oo CLI are trusted, and review the Feishu connection scopes before use.

## Reference(s):

- [Feishu homepage](https://www.feishu.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown instructions with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the OOMOL oo CLI Feishu connector; live action schemas should be inspected before building payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
