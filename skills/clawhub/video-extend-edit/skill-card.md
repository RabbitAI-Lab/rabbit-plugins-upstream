## Description:

Helps an agent extend an existing video clip or replace its ending by extracting a frame, using it to generate a new segment, and joining the generated segment back to the source clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative operators use this skill when they already have footage and want to extend the clip, continue from its final frame, or replace everything after a chosen timestamp. It is not for editing objects, backgrounds, or other visual content inside existing footage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The missing-dependency recovery path recommends unpinned and overly broad global skill installation.

Mitigation: Install only the required ofox-video-core dependency from a trusted source and version; avoid wildcard global all-agent fallback installation.

Risk: Extracted frames and prompts are sent to Ofox for paid generation and require an OFOX_API_KEY.

Mitigation: Confirm the user intends to use the paid Ofox service, protect the API key, and obtain cost approval before submitting generation jobs.

Risk: Real-person footage can involve likeness, privacy, or authorization issues.

Mitigation: Process real-person footage only when the user has the right to use the person's likeness and understands the limits documented by the skill.

Risk: Joining generated segments to source footage can silently create variable-resolution or truncated output when rescaling or audio padding is skipped.

Mitigation: Normalize video dimensions before concatenation, pad or intentionally choose the audio hand-off, and verify the finished file across the join.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/video-extend-edit)
- [Project homepage from metadata](https://github.com/ofoxai/skills/tree/main/skills/video-extend-edit)
- [Ofox API key portal](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes pre-flight checks, frame extraction, Ofox generation setup, video joining, audio hand-off, and verification guidance.]

## Skill Version(s):

1.1.0 (source: frontmatter, release evidence, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
