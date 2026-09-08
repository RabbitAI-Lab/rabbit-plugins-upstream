## Description:

Converts PDFs into explainer, report, courseware, or training videos by using the dLazy CLI to parse content, plan storyboards and voiceover, build the video, and validate the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn PDFs and other documents into dLazy video-generation projects for explainers, report briefings, courseware, or training videos. The skill is suited for agents that need to guide authentication, file attachment, project discovery, and dLazy CLI execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local files are sent to dLazy services for video generation.

Mitigation: Attach only files intended for upload to dLazy and confirm the content is appropriate for a third-party SaaS workflow.

Risk: The skill depends on the third-party @dlazy/cli npm package and can be installed globally.

Mitigation: Review the package or source before use, and prefer npx or an isolated environment when a persistent global install is not desired.

Risk: All requests require a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Use a revocable API key, keep it scoped to the intended organization, and rotate or revoke it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and dLazy CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids, authentication state, and attached files handled by the dLazy CLI.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
