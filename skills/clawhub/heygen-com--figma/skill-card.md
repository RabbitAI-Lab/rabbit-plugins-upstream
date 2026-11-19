## Description:

Bring Figma into a HyperFrames video - rendered assets, brand tokens, components, storyboard frames as reconstructed motion (frames read as states, not slides), shaders and connector-assisted motion. Use when the person pastes a figma.com link or asks to use a Figma design, frame, logo or brand.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and designers use this skill to bring Figma designs into HyperFrames videos by importing assets, brand tokens, components, and motion or storyboard states.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reported a Windows executable lookup weakness.

Mitigation: Review executable lookup paths on Windows before use and ensure commands resolve to trusted tools.

Risk: ClawScan flagged the usage beacon because its telemetry appears unrelated to the skill's purpose.

Mitigation: Review the beacon's event data and use the documented opt-out if the telemetry is not acceptable.

Risk: ClawScan coverage was partial and its guidance also flags undeclared tool scope and an unpinned package.

Mitigation: Review all supplied components, command and dependency scope, and package versions before installation or execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/figma)
- [HyperFrames plugin installation rules](../hyperframes/references/plugin-installation.md)

## Skill Output:

**Output Type(s):** [Files, Code, Shell commands, Guidance]

**Output Format:** [HyperFrames assets and component files, timeline code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Imported files are saved locally in the project; motion and shader workflows can use a Figma connector or native exports.]

## Skill Version(s):

1.0.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
