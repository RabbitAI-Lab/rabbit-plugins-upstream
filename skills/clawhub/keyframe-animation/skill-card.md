## Description:

Animates motion between two supplied still images by using one as the first frame and the other as the last frame in a single Ofox video job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they have a start image and an end image and want an agent to brief, price, and run an Ofox video generation workflow that fills in the transition between them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovery guidance can lead users to install unpinned skills globally for every agent.

Mitigation: Install only the required ofox-video-core dependency from a pinned or reviewed version, and avoid global all-agent installation unless that scope is intentional.

Risk: Video generation sends selected images to Ofox and uses OFOX_API_KEY after cost approval.

Mitigation: Use only images the user is authorized to submit, disclose the external Ofox processing step, and require explicit cost approval before running the job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/keyframe-animation)
- [Publisher profile](https://clawhub.ai/user/ofoxai)
- [Skill homepage](https://github.com/ofoxai/skills/tree/main/skills/keyframe-animation)
- [Ofox app](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate Ofox API video-generation jobs after user cost approval and requires OFOX_API_KEY, curl, and jq.]

## Skill Version(s):

1.1.0 (source: server release metadata, skill frontmatter, and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
