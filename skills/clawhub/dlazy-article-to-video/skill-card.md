## Description:

Turns a written article or document into a narrated explainer video workflow with outline, storyboard, voiceover, build, and validation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run the dLazy article-to-video workflow for turning article, document, report, courseware, or training content into narrated explainer videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to the third-party dLazy cloud service.

Mitigation: Avoid attaching confidential documents unless dLazy's terms and data handling are acceptable for the intended use.

Risk: The dLazy CLI may save an API key in the local user configuration.

Mitigation: Use per-invocation credentials when appropriate and rotate or revoke organization-scoped keys from the dLazy dashboard if exposure is suspected.

Risk: Installing the CLI globally persists third-party executable code on the system.

Mitigation: Prefer the pinned npx command for on-demand use when a persistent global CLI is not needed, and review the external package or source before installing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are streamed through the dLazy CLI and may reference project-scoped chat sessions and uploaded files.]

## Skill Version(s):

1.0.20 (source: server release metadata; artifact frontmatter lists 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
