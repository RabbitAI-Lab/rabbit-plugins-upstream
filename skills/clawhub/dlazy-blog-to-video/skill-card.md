## Description:

Converts blog posts or articles into narrated videos with storyboards, voiceover, and video assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this agent skill to turn blog posts, articles, or other documents into narrated videos for social media, YouTube, explainers, or training. It submits prompts and selected attachments to dLazy's hosted agent and supports continuing work in a project session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local attachments are sent to dLazy's hosted service; project sessions retain context for later turns.

Mitigation: Send only content you are comfortable sharing, verify the intended project and attachments before each request, and clear a saved session when it is no longer needed.

Risk: Authentication saves an organization API key in local CLI configuration unless supplied per invocation; generated work may consume service credits.

Mitigation: Protect the local configuration file, use the supported environment-variable option when appropriate, and confirm the selected organization and available credits before generating.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [CLI repository listed in skill metadata (not server-resolved provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Guidance, Video]

**Output Format:** [Markdown guidance and CLI commands; generated video and streamed agent responses are returned by the dLazy service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation runs through dLazy's hosted service; output details depend on the prompt and project.]

## Skill Version(s):

1.0.32 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
