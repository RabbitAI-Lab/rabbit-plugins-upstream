## Description:

Uses Meshy CLI with browser sign-in to generate and convert 3D models, textures, reference images, rigging, animations, and motion clips, and prepares models for physical printing and slicer handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arlieeee](https://clawhub.ai/user/arlieeee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and 3D creators use this agent to generate or adapt 3D assets with Meshy and prepare selected models for physical printing, including analysis, repair, sizing, and slicer handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, input images, and models selected for a task are sent to Meshy for cloud processing.

Mitigation: Submit only prompts and assets the user is comfortable sharing with Meshy.

Risk: Model generation and related tasks can spend Meshy credits.

Mitigation: Agree on a credit budget before generation and review current pricing for requested work.

Risk: Using the CLI can involve package installation, a reusable Meshy login, and a browser authorization code.

Mitigation: Follow the machine's installation policy, complete authorization only through Meshy's sign-in page, and never expose session tokens or API keys; clarify with the publisher how the displayed authorization code should be handled.

## Reference(s):

- [Meshy 3D Agent on ClawHub](https://clawhub.ai/arlieeee/skills/meshy-3d-agent)
- [Meshy project homepage (listed in skill metadata)](https://github.com/meshy-dev/meshy-3d-agent)
- [Meshy API pricing documentation](https://docs.meshy.ai/en/api/pricing)

## Skill Output:

**Output Type(s):** [3D model and texture files, Reference images and animation clips, Print-preparation files, Shell commands and usage guidance]

**Output Format:** [Asset files such as GLB, glTF, OBJ, FBX, STL, 3MF, and images, with shell commands and guidance as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [File formats and processing steps depend on the requested generation, animation, conversion, or printing workflow.]

## Skill Version(s):

0.8.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
