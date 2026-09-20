## Description:

Converts presentations and other documents into explainer, pitch, courseware, or training video workflows by using dLazy's hosted file-to-video agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and content teams use this skill to start or continue dLazy file-to-video projects from PPT, PowerPoint, Keynote, PDF, Word, Excel, and related document inputs. It is intended for producing explainers, report readouts, courseware, pitch videos, and training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files can be sent to dLazy API and file storage.

Mitigation: Use the skill only with files and prompts approved for processing by dLazy, and avoid sensitive inputs unless the user's policy allows that transfer.

Risk: The PPT-branded release can also process broader document-to-video tasks.

Mitigation: Confirm that the requested file-to-video task matches the user's intent before uploading files or starting a dLazy project.

Risk: The workflow depends on a pinned third-party npm CLI and API credentials.

Mitigation: Review @dlazy/cli version 1.2.3 before global installation, use npx when appropriate, and prefer DLAZY_API_KEY for per-run credentials when a saved local key is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and streamed agent responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; attached local files may be uploaded to dLazy file storage through the CLI.]

## Skill Version(s):

1.0.15 (source: evidence.release.version; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
