## Description:

Expand reading insights into detailed notes using local templates only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[harrylabsj](https://clawhub.ai/user/harrylabsj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn short reading insights into structured notes, related concepts, and reflection prompts without configuring external services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A source install may resolve third-party packages dynamically because the artifact does not include a lockfile and uses npm dependency ranges.

Mitigation: Prefer the trusted ClawHub release path or install in a low-privilege environment; review resolved dependencies before source installation.

Risk: The artifact describes local-only note processing, but dependency documentation may make the scope of external dependencies unclear.

Mitigation: Treat local-only as applying to note-processing behavior, not as a guarantee that npm installation has no package dependencies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/harrylabsj/skills/reading-notes)
- [OpenClaw documentation](https://docs.openclaw.ai)
- [ClawHub skill registry](https://clawhub.ai/skill/reading-notes)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with note sections, bullet lists, and numbered prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local templates and returns brief, detailed, comprehensive, related-concept, or prompt-focused responses.]

## Skill Version(s):

1.0.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
