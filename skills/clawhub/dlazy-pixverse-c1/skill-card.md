## Description:

PixVerse C1 generates videos from text prompts, reference images, or first and last frames, with a focus on action, visual effects, and fast motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to request PixVerse C1 video generation from text prompts, reference images, or specified first and last frames, and receive generated media results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanner evidence reports a benign verdict with medium confidence, but says the reported login workflow is not established as supporting the documented video-generation purpose and some references could not be checked.

Mitigation: Before installation or use, review the declared CLI package and confirm its login and generation behavior matches the documented video workflow.

Risk: The skill sends prompts to dLazy's hosted API and uploads supplied local media to its media service.

Mitigation: Avoid sending sensitive prompts or media unless permitted, and rotate or revoke the organization API key if it is exposed.

## Reference(s):

- [dLazy CLI source (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm (declared in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [Generated video assets with result URLs in a JSON response; shell commands for requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports synchronous or asynchronous generation and optional saving to a local path.]

## Skill Version(s):

1.2.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
