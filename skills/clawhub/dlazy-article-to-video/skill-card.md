## Description:

Turns articles, text, news, or documents into narrated explainer videos with outlining, storyboarding, voiceover, build, and validation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask the dLazy hosted agent to convert written content or attached documents into narrated explainer, report, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files are sent to dLazy services for processing.

Mitigation: Use the skill only when dLazy's service terms and retention practices meet the user's data-handling requirements, and avoid uploading confidential documents otherwise.

Risk: The skill installs or invokes a third-party CLI package.

Mitigation: Prefer the pinned npx/on-demand invocation or review the linked CLI source before global installation.

Risk: The skill depends on an API key for access to dLazy services.

Mitigation: Use a revocable dLazy API key and rotate or revoke it from the dLazy dashboard when access is no longer needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream responses from the dLazy CLI and may reference generated project state managed by dLazy.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
