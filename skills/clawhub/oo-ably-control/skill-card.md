## Description:

Ably Control lets agents manage Ably Control resources through the OOMOL-connected oo CLI, including reading, creating, updating, and deleting apps, API keys, queues, account details, and statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer Ably Control resources from an agent session through an OOMOL-connected account. It supports resource inspection, account and app statistics, API key and queue management, and guarded write or destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ably API tokens or API key material may be returned by connector actions.

Mitigation: Treat returned credentials as sensitive, avoid exposing them unnecessarily, and only use this skill with Ably and OOMOL accounts the user trusts the agent to manage.

Risk: Write and destructive actions can change or remove Ably apps, API keys, and queues.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running actions tagged as write or destructive.

Risk: First-time setup includes remote installer commands.

Mitigation: Run installer commands only after independently verifying the installer source and integrity.

## Reference(s):

- [Ably Control homepage](https://ably.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ably-control)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to fetch live action schemas before building JSON payloads and to return oo CLI connector results as JSON when running actions.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
