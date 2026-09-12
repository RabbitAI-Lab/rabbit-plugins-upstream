## Description:

Imports Figma designs, assets, brand tokens, components, storyboard sections, motion, and shader exports into local HyperFrames compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative engineers use this skill to bring Figma frames, assets, brand tokens, components, storyboards, motion, and shader exports into HyperFrames video or composition projects while keeping imported outputs local and deterministic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read any Figma files available to the configured token.

Mitigation: Use a read-only Figma token with the narrow file, metadata, library, and variable scopes needed for the intended import.

Risk: The skill creates local project artifacts such as frozen media, cache files, components, sidecars, and binding records.

Mitigation: Review generated files and run the project checks before approving or publishing imported compositions.

Risk: Motion and shader workflows may need a separate connector authorization or native Figma export, and unsupported paths can reduce fidelity.

Mitigation: Confirm connector availability before those phases, use native exports when required, and run the provided motion verification workflow for motion imports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/figma)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide an agent to create local frozen files, component files, sidecars, binding records, timeline scripts, and verification commands.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
