## Description:

TextCortex (textcortex.com). Use this skill for TextCortex requests, including reading data, creating non-streaming chat completions, listing models, and retrieving model metadata through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate TextCortex through OOMOL's connector, inspect live action schemas, run model and chat-completion actions, and handle account setup or billing errors when they block execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says first-time setup includes remote installer commands that should not be run blindly.

Mitigation: Review installation before use, prefer an official pinned and inspectable oo CLI installation method, and verify commands before execution.

Risk: The skill can create TextCortex chat completions through a write-tagged action.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub TextCortex skill page](https://clawhub.ai/oomol/skills/oo-textcortex)
- [TextCortex homepage](https://textcortex.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and may return TextCortex model metadata or chat-completion results.]

## Skill Version(s):

1.0.4 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
