## Description:

Kuaimai ERP lets an agent read and update Kuaimai ERP data through OOMOL's oo CLI and a connected Kuaimai account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to inspect Kuaimai ERP schemas, list or retrieve ERP records, and run supported Kuaimai connector actions from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad access to Kuaimai ERP through the user's connected OOMOL account.

Mitigation: Install only when the user trusts OOMOL and wants agent access to Kuaimai ERP; review the live connector schema before running actions.

Risk: The setup path includes remote CLI install scripts.

Mitigation: Prefer installing the oo CLI directly from verified official instructions before using the skill.

Risk: Write actions, including session refresh, can change ERP state or extend access.

Mitigation: Require explicit user confirmation for the exact payload and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kuaimai)
- [Kuaimai ERP homepage](https://www.kuaimai.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; responses are JSON when --json is used.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
