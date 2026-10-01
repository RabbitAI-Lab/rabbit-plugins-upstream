## Description:

Guides agents to generate short text-to-video or image-to-video clips with Veo 3.1 Fast through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to make short videos from prompts or images, or extend a video through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI may expose the environment to untrusted code.

Mitigation: Review the CLI source before use; prefer the pinned on-demand npx invocation if a persistent global installation is unnecessary.

Risk: A dLazy API key is required and may be stored in the local CLI configuration.

Mitigation: Limit access to the key and local configuration, and rotate or revoke the key if exposed.

Risk: Prompts and selected local media are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive prompts or media unless the service's handling of that data is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source referenced by the skill](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON with generated asset links or an asynchronous task ID; assets can be saved locally.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
