## Description:

Guides an agent to generate videos with Seedance 2.0 from text prompts, reference media, or first and last frames using dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to request short videos from text, reference images, videos, or audio, and first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy's hosted service, and generated files are hosted there.

Mitigation: Confirm you trust the service before sending sensitive prompts or media.

Risk: Logging in can save an API key locally.

Mitigation: Use DLAZY_API_KEY for per-invocation authentication if you prefer less local persistence.

Risk: Installing the CLI adds third-party software to the execution environment.

Mitigation: Review the package before installation; consider the pinned npx invocation instead of a global install.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a hosted result URL or an asynchronous task ID.]

## Skill Version(s):

1.3.27 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
