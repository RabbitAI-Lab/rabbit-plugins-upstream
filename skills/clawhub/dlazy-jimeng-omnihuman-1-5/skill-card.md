## Description:

Generate realistic digital human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy CLI for generating digital human broadcast videos from portrait images plus audio or text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy cloud endpoints for generation.

Mitigation: Invoke the skill only with media and prompts appropriate for dLazy's hosted service, and review inputs before execution.

Risk: Authentication can save an API key in the local dLazy CLI configuration.

Mitigation: Use account key rotation or revocation when needed, and prefer per-invocation credentials if persistent local configuration is not desired.

Risk: A global CLI install persists a third-party executable on the system.

Mitigation: Use the pinned npx invocation when a temporary, explicit CLI run is preferred.

Risk: Cloud generation may consume paid credits or trigger uploads unintentionally if invoked casually.

Mitigation: Run the tool explicitly, use dry-run behavior where appropriate, and confirm parameters before submitting generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands; the dLazy CLI returns JSON with hosted output URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are hosted by dLazy and may be downloaded locally with the CLI save option; async runs return a generation ID for polling.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
