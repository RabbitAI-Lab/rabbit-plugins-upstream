## Description:

Import Figma content into a HyperFrames composition: rendered assets, brand tokens, components, storyboard sections reconstructed as motion states, connector-assisted motion when available, and shaders from a connector or native export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video/composition builders use this skill to bring Figma files, frames, logos, brand tokens, components, motion, shaders, and storyboard sections into HyperFrames projects. It guides read-only Figma authentication, import routing, local asset freezing, verification, and follow-up commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to silently run a live npx self-update command before work, which can change installed skill behavior without clear user control.

Mitigation: Require visible approval for the update step or pin the installed skill version before use.

Risk: Motion, shader, and storyboard phases may send consent-gated usage events.

Mitigation: Confirm the user's telemetry consent posture before using those phases and avoid treating telemetry commands as required for Figma import correctness.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may produce local frozen media assets, component files, sidecar JSON/JSONL records, GSAP timeline code, and verification command output when followed by an agent.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
