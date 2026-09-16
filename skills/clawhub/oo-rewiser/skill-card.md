## Description:

Rewiser (rewiser.io). Use this skill for ANY Rewiser request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Rewiser through an OOMOL-connected account, including listing folders, retrieving recent transactions, and creating multiple transactions after confirming write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes one-line remote installer commands that could execute unverified code.

Mitigation: Install the oo CLI through a trusted, reviewable, verified method before allowing the agent to run Rewiser actions.

Risk: The create_multiple_transactions action changes Rewiser data.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Rewiser homepage](https://rewiser.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema lookup before connector actions; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
