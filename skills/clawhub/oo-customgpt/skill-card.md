## Description:

CustomGPT.ai access for reading, creating, and updating CustomGPT data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate CustomGPT.ai agents through an OOMOL-connected account, including listing agents, inspecting conversations and documents, creating conversations, and sending non-streaming prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can lead users to execute installer scripts fetched from the internet.

Mitigation: Review the skill before installation and prefer an official package manager or a downloaded installer that can be verified before execution.

Risk: Write actions can create CustomGPT conversations or send prompts that change account state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and inspect the live action schema before constructing the payload.

## Reference(s):

- [CustomGPT.ai homepage](https://customgpt.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-customgpt)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
