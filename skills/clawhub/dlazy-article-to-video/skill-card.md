## Description:

This skill turns articles, text, news items, or documents into narrated explainer videos by guiding outline, storyboard, voiceover, build, and validation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn written articles, documents, or reference files into narrated explainer, report, courseware, or training videos through a dLazy-hosted workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy services for processing.

Mitigation: Avoid attaching sensitive documents unless dLazy's terms and the user's organization policy allow that data transfer.

Risk: Authentication may store a dLazy API key in local CLI configuration.

Mitigation: Use normal key rotation and revocation controls, and prefer per-invocation environment variables when persistent local storage is not desired.

Risk: A globally installed third-party CLI persists on the user's system.

Mitigation: Use the pinned npx invocation when a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may upload attached files to dLazy-hosted services.]

## Skill Version(s):

1.0.23 (source: server release metadata; artifact frontmatter states 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
