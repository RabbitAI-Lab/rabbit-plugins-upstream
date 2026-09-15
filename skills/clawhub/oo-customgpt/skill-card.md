## Description:

CustomGPT.ai enables agents to operate a user's CustomGPT.ai account through OOMOL, including listing agents, conversations, messages, and documents, creating conversations, and sending non-streaming prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and other CustomGPT.ai users can use this skill to inspect account resources, create conversations, and send prompts to CustomGPT agents through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup fallback documents pipe-to-shell installation for the oo CLI.

Mitigation: Install the oo CLI through a verified package or download and inspect the installer before execution.

Risk: Write actions can create conversations and send prompts through a connected CustomGPT.ai account.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

Risk: The skill depends on OOMOL as the CustomGPT.ai connector and on server-side credentials.

Mitigation: Use it only when that connector relationship is acceptable and reconnect or refresh credentials only after an auth or connection failure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-customgpt)
- [CustomGPT.ai homepage](https://customgpt.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schema inspection before constructing CustomGPT.ai connector payloads.]

## Skill Version(s):

1.0.3 (source: evidence.release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
