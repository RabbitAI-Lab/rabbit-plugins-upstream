## Description:

Turns PDFs and other documents into explainer, report, courseware, or training videos by using dLazy's hosted file-to-video workflow for parsing, outlining, storyboarding, voiceover, building, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill when they have a PDF or document and want an agent to produce an explanatory video, report broadcast, courseware video, or training video through the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents, prompts, and attached files may be uploaded to dLazy's hosted service.

Mitigation: Avoid uploading sensitive documents unless dLazy's terms and the user's organizational policies allow it.

Risk: The dLazy CLI stores an organization API key locally unless a per-run environment variable is used.

Mitigation: Prefer scoped credentials, rotate or revoke keys when needed, and use the DLAZY_API_KEY environment variable when persistent local storage is not acceptable.

Risk: The skill relies on an external CLI package and hosted API endpoints.

Mitigation: Review the dLazy CLI package and source before installation and install only if third-party hosted execution is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned dLazy CLI package and sends prompts, options, and attached files to dLazy's hosted service.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
