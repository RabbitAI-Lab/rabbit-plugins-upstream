## Description:

Evenium lets an agent operate Evenium through an OOMOL-connected account to read, create, and update event and guest data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use this skill to look up Evenium events and guests, inspect live action schemas, and run supported Evenium connector actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer execution for the oo CLI.

Mitigation: Prefer a verified package or inspect and verify the oo CLI installer before running it; use setup only when the CLI is missing.

Risk: One Evenium action has unclear read/write semantics and may change state.

Mitigation: Require explicit confirmation before actions marked write or any action whose live schema shows state-changing behavior.

## Reference(s):

- [Evenium homepage](https://corp.evenium.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-evenium)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before action payloads; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
