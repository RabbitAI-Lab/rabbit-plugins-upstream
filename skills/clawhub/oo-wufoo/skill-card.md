## Description:

Operates Wufoo through an OOMOL-connected account with the oo CLI for reading forms, fields, and entries and submitting new entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business operators use this skill to inspect Wufoo forms, fields, and entries or submit new form entries through an OOMOL-connected Wufoo account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes internet installer commands that execute downloaded shell or PowerShell code.

Mitigation: Review the setup path before installing, prefer a signed or version-pinned oo CLI installation method, and avoid running curl|bash or irm|iex blindly.

Risk: The submit_entry action can create new Wufoo entries.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub Wufoo skill page](https://clawhub.ai/oomol/skills/oo-wufoo)
- [Wufoo homepage](https://www.wufoo.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId when actions run.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
