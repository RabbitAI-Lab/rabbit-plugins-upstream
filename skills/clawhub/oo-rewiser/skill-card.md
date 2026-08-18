## Description:

Rewiser (rewiser.io). Use this skill for ANY Rewiser request - reading, creating, and updating data. Whenever a task involves Rewiser, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Rewiser through an OOMOL-connected account, including listing folders, reading recent transactions, and creating transactions after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read private financial or business records from the connected Rewiser account.

Mitigation: Install and use it only for accounts where agent access to Rewiser records is intended.

Risk: The create_multiple_transactions action changes Rewiser account data.

Mitigation: Confirm the exact transaction payload and expected effect with the user before running any write action.

Risk: Connector access may fail when the oo CLI is missing, the account is not signed in, the Rewiser connection is expired, or billing credit is unavailable.

Mitigation: Use the documented recovery steps only after a matching command failure, then retry the intended action.

## Reference(s):

- [Rewiser homepage](https://rewiser.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-rewiser)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas before actions; write actions require user confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
