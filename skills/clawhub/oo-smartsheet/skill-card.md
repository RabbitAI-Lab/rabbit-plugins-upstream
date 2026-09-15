## Description:

Operate Smartsheet through an OOMOL-connected account to read, create, update, and delete sheet data with schema inspection and confirmation safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and end users use this skill to operate a connected Smartsheet account: inspect action schemas, list sheets, read sheet data, and add, update, or delete rows through the oo CLI. State-changing actions require confirmation of the exact target, payload, and effect before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute local code.

Mitigation: Review the installer path before installing and use a trusted, verified oo CLI installation method when available.

Risk: Write and destructive Smartsheet actions can modify or delete sheet data.

Mitigation: Require explicit confirmation of the target, payload, and expected effect before running any write or delete action.

Risk: Connector requests depend on account authentication, Smartsheet connection state, and OOMOL billing status.

Mitigation: Run login or connection setup only after matching failures and resolve billing errors before retrying connector actions.

## Reference(s):

- [ClawHub Smartsheet skill page](https://clawhub.ai/oomol/skills/oo-smartsheet)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Smartsheet homepage](https://www.smartsheet.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI and connector responses may return JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
