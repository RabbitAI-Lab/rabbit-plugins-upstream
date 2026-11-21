## Description:

Turn a website URL into a promotional, social advertising, or product demo video by capturing the site, deriving its brand, and creating a storyboard, voiceover, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn a webpage or landing page into a promotional, social advertising, or product demo video through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that project-listing and login steps are not clearly tied to the advertised URL-to-video workflow.

Mitigation: Review these steps and confirm they are relevant before running the corresponding commands.

Risk: The security review was partial and did not analyze the external CLI as an executable.

Mitigation: Review the pinned CLI package and its source before installation, and use the documented pinned version.

Risk: Prompts and attached files are sent to dLazy's hosted service, and attached files are uploaded to its media storage.

Mitigation: Avoid sending sensitive URLs, prompts, or files unless they are appropriate to share with the service.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, Text, Guidance, Shell commands]

**Output Format:** [Video deliverables and streamed text responses; Markdown instructions with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A prompt can include a URL and optional reference files; attached files are uploaded to the service.]

## Skill Version(s):

1.0.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
