## Description:

Helps agents plan and generate dLazy commands, prompts, configuration, and assembly guidance for creating slide-first online course videos with a consistent digital lecturer avatar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, training teams, and course producers use this skill to turn course materials, scripts, and avatar images into a repeatable dLazy workflow for paid courses, public lessons, enterprise training, and LMS modules. It emphasizes limiting avatar-driven footage to openings, transitions, and endings while using slides and narration for the main lesson.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may store or use a dLazy API key locally.

Mitigation: Confirm the user is comfortable configuring the dLazy CLI, prefer environment-based secrets where appropriate, and avoid exposing keys in prompts, logs, or shared files.

Risk: Commands may upload course materials, generated assets, prompts, and audio to dLazy services.

Mitigation: Avoid private, regulated, or organization-restricted course content unless external processing is permitted by the user's policies.

Risk: Model calls can consume paid credits, especially avatar-driving steps.

Mitigation: Use the skill's dry-run guidance, verify model flags before execution, and keep avatar-driving time limited to the segments that need a visible lecturer.

Risk: Education and training content can create compliance issues through outcome guarantees, false credentials, or undisclosed AI-generated avatars.

Mitigation: Review course copy and generated visuals for prohibited claims, invented institutional signals, and required AI-generated content disclosures before publication.

Risk: Generated commands and media assembly instructions can produce incorrect, malformed, or misordered outputs if paths, dimensions, encodings, or durations are wrong.

Mitigation: Use UTF-8 JSON input files for Chinese prompts, inspect generated media before spending on downstream steps, zero-pad batch filenames, and measure actual clip durations before final assembly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [dLazy homepage](https://dlazy.com)
- [Pipeline guide](artifact/pipeline.md)
- [Recipe library](artifact/recipes.md)
- [Troubleshooting and compliance](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-reviewed workflow guidance; generated commands may call external dLazy services and consume paid model credits.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
