## Description:

OneSignal lets an agent inspect action schemas and run OneSignal connector actions to list, retrieve, create, or cancel messages through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to manage OneSignal messaging workflows from an agent, including inspecting live schemas, listing or retrieving messages, creating push notifications, and canceling scheduled messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include direct remote installer execution with curl | bash and PowerShell iex.

Mitigation: Do not allow an agent to run those installer commands automatically; install the oo CLI through a verified channel before using the skill.

Risk: Create and cancel actions can change OneSignal messaging state.

Mitigation: Confirm the exact payload, target message, and expected effect with the user before running write actions.

## Reference(s):

- [OneSignal homepage](https://onesignal.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-onesignal-rest-api)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed and authenticated oo CLI with a connected OneSignal account.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
