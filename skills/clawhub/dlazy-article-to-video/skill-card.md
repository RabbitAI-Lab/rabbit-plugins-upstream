## Description:

Turns articles, text, news, essays, and documents into narrated explainer videos with outline, storyboard, voiceover, build, and validation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask the dLazy hosted agent to convert provided articles, text, or documents into narrated explainer, report, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, project context, and explicitly attached files are sent to dLazy's hosted service.

Mitigation: Review data sensitivity before use and avoid attaching confidential files unless dLazy's service terms and controls are acceptable.

Risk: Authentication relies on revocable dLazy API keys stored locally or provided by environment variable.

Mitigation: Prefer DLAZY_API_KEY for tighter per-run control where appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: The skill runs a pinned npm CLI package.

Mitigation: Use npx @dlazy/cli@1.2.3 when a persistent global install is unnecessary and review the linked source or npm package before installing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and the pinned @dlazy/cli@1.2.3 package; prompts, project context, and explicitly attached files are sent to dLazy hosted endpoints.]

## Skill Version(s):

1.0.19 (source: server release metadata; artifact frontmatter is 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
