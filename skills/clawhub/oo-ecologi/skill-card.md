## Description:

Ecologi helps agents inspect live Ecologi connector schemas, read impact totals, and run confirmed purchase actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Ecologi carbon, habitat, tree, and total impact information, and to initiate Ecologi purchase actions after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Purchase actions can create financial or account-affecting Ecologi transactions through the connected account.

Mitigation: Require explicit confirmation of quantity, unit, region, test or live mode, attribution, notification settings, idempotency, and expected cost before running any purchase action.

Risk: The skill documentation includes remote installer pipe commands for first-time setup.

Mitigation: Prefer a verified and pinned installer, or manually inspect and verify the installer before execution.

Risk: The server security verdict is suspicious because purchase actions are under-disclosed and installer commands require review.

Mitigation: Review the skill carefully before installation and apply the server security guidance before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ecologi)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Ecologi homepage](https://ecologi.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Ecologi read or purchase actions through the oo CLI when installed, authenticated, connected, and confirmed for state-changing actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
