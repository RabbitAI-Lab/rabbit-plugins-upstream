## Description:

Generate matching scene sound effects from text descriptions or video frames using Kling SFX through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request short sound effects or background audio prompts for scenes, either from text or from one reference video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media passed to the CLI may be sent to dLazy's hosted API and file service.

Mitigation: Use the skill only when the user is comfortable with hosted processing and avoid submitting sensitive media unless approved.

Risk: The skill requires a dLazy API key that may be stored locally or supplied through the environment.

Mitigation: Use `dlazy login`, `dlazy auth set`, or `DLAZY_API_KEY` intentionally, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Broad trigger wording such as generic dubbing requests could invoke the skill when a user did not intend a Kling or dLazy sound-effect workflow.

Mitigation: Prefer explicit requests for Kling or dLazy SFX generation before using the CLI.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-keling-sfx)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON result references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs or an asynchronous generateId for later polling.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
