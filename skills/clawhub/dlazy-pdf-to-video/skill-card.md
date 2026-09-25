## Description:

Converts PDFs and other documents into explainer, report, courseware, or training videos by using the dLazy hosted document-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, educators, and business users use this skill to turn uploaded PDF or document content into project-scoped explainer, report, courseware, or training videos through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy's API and media storage.

Mitigation: Avoid attaching sensitive documents unless dLazy's terms and your data-handling requirements permit that use.

Risk: Authentication may store a dLazy API key in local CLI configuration.

Mitigation: Use normal local account protections, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation environment variables where persistent storage is not desired.

Risk: Use depends on dLazy hosted-service availability and account credits.

Mitigation: Confirm the target organization has access and credits before starting time-sensitive video-generation work.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a project-scoped hosted workflow and may stream responses from the dLazy CLI.]

## Skill Version(s):

1.0.18 (source: server release metadata; artifact frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
