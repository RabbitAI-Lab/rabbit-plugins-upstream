## Description:

Converts blog posts or articles into narrated videos with storyboard, voiceover, and build support for social or YouTube use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn blog posts, articles, and supported documents into narrated explainer videos for social or YouTube distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy services, including uploaded user-selected documents.

Mitigation: Use the skill only when external processing is acceptable, and avoid attaching sensitive documents unless approved by the organization.

Risk: The skill behavior is broader than the blog-to-video label and may handle documents as well as blog posts.

Mitigation: Review the requested task and attached files before invocation so users understand what content may be processed.

Risk: Installing or running @dlazy/cli introduces third-party CLI and npm package supply-chain exposure.

Mitigation: Prefer the pinned npx invocation or an isolated account, and verify the package and source before use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to use a project-scoped dLazy CLI session and may reference uploaded user-selected files.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
