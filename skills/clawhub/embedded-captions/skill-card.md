## Description:

Adds verbatim, cinematic, or themed captions to existing single-subject talking-head videos using local transcription, matting, preview, and render workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, video teams, and developers use this skill to add readable subtitle rails, behind-subject caption effects, or named visual caption identities to suitable talking-head clips. It is intended for single-subject footage where the transcript, matte, layout, and preview checks can be reviewed before rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local media pipeline can process private source videos and generated intermediates.

Mitigation: Keep sensitive footage only in project directories intended for the skill to access and review outputs before sharing or retaining them.

Risk: The workflow can download model or tool dependencies and asks to update HyperFrames/OpenClaw skills before use.

Mitigation: Approve update and dependency steps only in an environment where those downloads and local executions are acceptable.

Risk: Incorrect transcripts, unsuitable source clips, or poor caption placement can create misleading or unreadable video output.

Mitigation: Use the documented refusal checks, sanity-read transcript output, and inspect preview frames before running the final render.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [Catalog](CATALOG.md)
- [Theme system](themes/README.md)
- [DNA registry](dna/README.md)
- [Rail caption rules](references/rail.md)
- [Composition craft](references/composition-craft.md)
- [Failure modes](references/failure-modes.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce project configuration such as cinematic.json or theme.json and direct local media render commands.]

## Skill Version(s):

1.0.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
