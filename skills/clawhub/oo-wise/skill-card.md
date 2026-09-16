## Description:

Wise helps agents retrieve exchange rates, supported transfer currencies, and available personal or business profiles through an OOMOL-connected Wise account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer Wise account and transfer-data questions by fetching exchange rates, transfer currencies, and profile information from an OOMOL-connected Wise account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes broad activation wording for Wise-related requests.

Mitigation: Use it only for explicit Wise connector tasks and confirm the user's intent before retrieving profile or account metadata.

Risk: The first-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Prefer an independently verified official installation path or review the installer before running setup commands.

Risk: Profile and account metadata may be returned from the connected Wise account.

Mitigation: Request only the data needed for the user's task and avoid exposing unnecessary profile details.

## Reference(s):

- [ClawHub Wise skill page](https://clawhub.ai/oomol/skills/oo-wise)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Wise homepage](https://wise.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live Wise connector data returned by the oo CLI when the agent executes read actions.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
