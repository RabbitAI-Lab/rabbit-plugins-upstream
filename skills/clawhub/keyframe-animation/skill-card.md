## Description:

Creates a video transition from two still images by using one image as the first frame, one as the last frame, and generating the motion between them through Ofox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they already have start and end still images and want an agent to prepare a two-ended Ofox video-generation job with prompt guidance, cost review, and output verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The missing-core recovery path may install more of the publisher's skills than this single workflow needs.

Mitigation: Install only the required ofox-video-core dependency from a trusted publisher and version before using this skill.

Risk: The workflow uses OFOX_API_KEY and sends the selected images to Ofox for video generation.

Mitigation: Use a scoped API key where possible and avoid submitting sensitive images unless Ofox handling is acceptable for the use case.

Risk: Video generation can incur paid API charges.

Mitigation: Review the dry-run cost table and approve the spend before any real generation job is submitted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/keyframe-animation)
- [Publisher profile](https://clawhub.ai/user/ofoxai)
- [Clawdis homepage](https://github.com/ofoxai/skills/tree/main/skills/keyframe-animation)
- [Ofox API keys](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and cost-review instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires two user-provided image files; submitting a job requires OFOX_API_KEY, curl, jq, and user approval after a dry-run cost estimate.]

## Skill Version(s):

1.0.1 (source: server release metadata, skill frontmatter, and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
