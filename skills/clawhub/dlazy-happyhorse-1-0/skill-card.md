## Description:

Happy Horse 1.0 supports text-to-video, first-frame-to-video, reference-to-video, and video editing, routing each selected mode to its matching sub-model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to send prompts, reference images, or source video to dLazy's Happy Horse 1.0 service and request generated or edited video content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete and the external CLI package's behavior was not verified, so the advertised video features may not be confirmed by the available evidence.

Mitigation: Review the CLI package and decide whether to trust it before installing it or entering dLazy API credentials.

Risk: Prompts and local media provided to the skill are sent to dLazy's hosted API and media storage.

Mitigation: Submit only prompts and media that are appropriate to share with the hosted service.

## Reference(s):

- [Happy Horse 1.0 skill release](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [CLI repository (listed in the skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Video/media assets]

**Output Format:** [Structured JSON response with hosted media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include hosted media URLs; asynchronous requests can return a task ID before results are ready.]

## Skill Version(s):

1.3.41 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
