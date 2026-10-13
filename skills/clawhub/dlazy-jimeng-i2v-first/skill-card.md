## Description:

Generates dynamic video from a single first-frame image and a text prompt using Jimeng through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to request short videos from a first-frame image and prompt, then retrieve the generated result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local images may be sent to dLazy, and generated results are hosted by dLazy.

Mitigation: Avoid private media unless the service terms and handling meet your needs.

Risk: Login may store an API key in the local user configuration.

Mitigation: Protect the local account and rotate or revoke the key if exposed.

Risk: Documentation examples and version labels differ from the documented command options and release version.

Mitigation: Check the installed CLI help and confirm option names before submitting a request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI repository (declared in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to request video generation; completed tasks provide a hosted result URL, while asynchronous tasks provide an ID for status checks.]

## Skill Version(s):

1.3.28 (source: server-resolved ClawHub release; skill documents say 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
