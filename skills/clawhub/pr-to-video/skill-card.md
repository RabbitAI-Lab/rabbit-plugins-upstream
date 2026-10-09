## Description:

Turns a GitHub pull request into a code-change explainer video using its diff, commits, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to turn a GitHub pull request into a narrated walkthrough of its changes, from source review and storyboard to rendered video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads pull-request data using local GitHub authentication, including potentially private repository content.

Mitigation: Run with a trusted, limited-access GitHub account or in a sandboxed environment when working with private repositories.

Risk: HyperFrames updates and registry blocks may change the code executed during the workflow.

Mitigation: Review the package versions and registry blocks before approving installation or updates.

Risk: The workflow writes a persistent project cache, uses configured media providers, and starts a temporary preview server.

Mitigation: Review provider access and project contents, and stop the preview server after review.

## Reference(s):

- [PR to Video on ClawHub](https://clawhub.ai/heygen-com/skills/pr-to-video)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Video]

**Output Format:** [Markdown plans and scripts, HTML frames, and an MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rendering requires a GitHub pull request, HyperFrames tooling, and user review before the final MP4.]

## Skill Version(s):

1.0.48 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
