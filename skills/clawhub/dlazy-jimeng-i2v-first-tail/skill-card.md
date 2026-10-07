## Description:

Guides agents in generating a transition video from first and last frame images using Jimeng through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate a transition video between supplied first and last frame images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted service, and generated outputs are hosted there.

Mitigation: Submit only content approved for third-party processing and review the service terms before use.

Risk: Authentication may save an API key locally, and a global CLI installation can persist.

Mitigation: Use a per-invocation API key or the pinned npx command when persistence is undesirable; protect and rotate keys as needed.

Risk: Command examples in the skill documentation use options that differ from its option list.

Mitigation: Check the CLI help and run a dry run before submitting a generation request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked service returns a hosted generated-video URL; results can optionally be saved locally.]

## Skill Version(s):

1.3.25 (source: server release; supplied skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
