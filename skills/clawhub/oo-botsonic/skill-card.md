## Description:

Botsonic (botsonic.com). Use this skill for ANY Botsonic request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Botsonic connector actions through an OOMOL-connected account, including generating bot responses, reading conversations, listing conversations, and listing FAQs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes installing the oo CLI by piping a remote installer script into a shell.

Mitigation: Review the installer step before use, prefer manually downloading and verifying the installer from OOMOL's official documentation, and install the CLI only when required.

Risk: The skill can run Botsonic actions that generate responses or otherwise change service state.

Mitigation: Only run Botsonic actions the user explicitly requested, and confirm payload and effect before actions tagged as write or destructive.

## Reference(s):

- [Botsonic homepage](https://botsonic.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-botsonic)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces oo CLI schema inspection and connector execution guidance; connector responses are JSON.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
