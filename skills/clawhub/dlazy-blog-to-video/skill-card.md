## Description:

Helps turn blog posts or documents into narrated videos using dLazy's hosted file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and teams use this skill to request narrated social or YouTube videos from blog posts, articles, or documents through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite its blog-focused label, the skill invokes a broader file-to-video workflow that can upload local documents.

Mitigation: Review the requested task and attachments; do not submit sensitive business or personal documents without approval.

Risk: Using the dLazy CLI sends prompts to dLazy and stores a revocable API key locally.

Mitigation: Confirm the service is approved before use, protect the local key, and rotate or revoke it when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text responses with project updates and video results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation occurs through the dLazy service; the agent can return project information and video links.]

## Skill Version(s):

1.0.24 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
