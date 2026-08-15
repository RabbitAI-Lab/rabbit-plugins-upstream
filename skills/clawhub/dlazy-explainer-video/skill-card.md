## Description:

Turns a document, topic, or brief into a narrated explainer video with outline, storyboard, voiceover, build, and validation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask dLazy's hosted file-to-video agent to convert documents, topics, or briefs into explainer, courseware, report-summary, or training videos. It supports new file-to-video projects, continuing existing project sessions, and optional local file attachments through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy API and media storage services.

Mitigation: Use the skill only with content approved for dLazy processing, and avoid attaching confidential or regulated documents unless the user's organization has approved that service path.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use per-invocation environment variables or npx when a persistent install is not desired, restrict local config access, and rotate or revoke the API key from dLazy when needed.

Risk: Hosted project sessions keep context for follow-up turns.

Mitigation: Use project-specific sessions intentionally, clear or compact sessions when appropriate, and avoid adding sensitive context that should not persist across turns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands for authentication, project discovery, project continuation, session control, and file attachment through the dLazy CLI.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
