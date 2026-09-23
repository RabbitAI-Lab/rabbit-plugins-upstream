## Description:

Converts PPT, Word, Excel, PDF, and other documents into videos by using dLazy's hosted file-to-video agent to parse, outline, storyboard, voice over, build, and validate video output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, trainers, and business users use this skill when they have a document and want an explainer video, report broadcast, courseware, or training video. It helps an agent start or continue a dLazy project through the pinned file-to-video template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Files attached with --files are uploaded to dLazy storage, and prompts or options are sent to the dLazy API.

Mitigation: Avoid confidential documents unless the organization has approved dLazy's hosted data handling for the use case.

Risk: Using a persistent global CLI install may leave a long-lived local tool and configuration on the user's machine.

Mitigation: Use the pinned npx form for on-demand execution when a persistent global install is not desired.

Risk: A saved dLazy API key may continue to grant organization access if it is exposed or no longer needed.

Mitigation: Rotate or revoke the dLazy API key from the dLazy dashboard when access changes or compromise is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide use of dLazy project ids, prompts, attached files, authentication, and error handling.]

## Skill Version(s):

1.3.18 (source: release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
