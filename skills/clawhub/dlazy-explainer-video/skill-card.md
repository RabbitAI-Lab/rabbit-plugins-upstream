## Description:

Helps turn documents, topics, or briefs into narrated explainer videos through outlining, storyboarding, voiceover, production, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to develop narrated explainers, courseware, and training videos from documents or briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files are sent to dLazy.

Mitigation: Review prompts and attachments for sensitive content before sending them.

Risk: Authentication uses a dLazy API key that may be stored locally.

Mitigation: Use DLAZY_API_KEY per invocation if a saved key is not desired; rotate or revoke keys when needed.

Risk: The skill depends on an external npm CLI.

Mitigation: Review the CLI package and source before installing if stronger supply-chain assurance is required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text with CLI commands and streamed project responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [dLazy generates the video through a project-scoped session.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
