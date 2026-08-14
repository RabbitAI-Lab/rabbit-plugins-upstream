## Description:

Converts documents such as Word, Markdown, PPT, Excel, and PDF files into explainer, report, courseware, or training videos through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users use this skill to start or continue dLazy document-to-video projects from document inputs and supporting files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy's hosted service.

Mitigation: Only upload documents approved for dLazy processing and avoid sensitive files unless policy permits.

Risk: The CLI can store an API key in the user's local configuration.

Mitigation: Use a per-run DLAZY_API_KEY when local credential persistence is not desired, and rotate or revoke keys from the dLazy dashboard.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Streams responses from the dLazy hosted service and may include project-oriented next steps.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter is 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
