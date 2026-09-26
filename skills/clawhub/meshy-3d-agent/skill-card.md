## Description:

Create 3D models, textures, reference images, rigging and animation with Meshy, and prepare models for physical 3D printing: white or multicolor prints, Creative Lab products, sizing and slicer handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arlieeee](https://clawhub.ai/user/arlieeee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and makers use this skill to guide an agent through Meshy CLI workflows for generating 3D assets, preparing models for printing, and delivering resulting files in a user-selected workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend Meshy credits through paid generation or processing tasks.

Mitigation: Verify estimated costs and user authorization before starting paid work, and report actual consumed credits when the task completes.

Risk: Prompts, input images, models, and task requests may be sent to Meshy.

Mitigation: Use the skill only with assets the user is comfortable uploading to Meshy.

Risk: The Meshy CLI can reuse local credentials and download generated files.

Mitigation: Keep credential handling inside the CLI flow, avoid exposing tokens, and rely on the documented workspace and overwrite limits for local file writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arlieeee/skills/meshy-3d-agent)
- [Meshy 3D Agent homepage](https://github.com/meshy-dev/meshy-3d-agent)
- [Setup](references/setup.md)
- [Digital asset pipelines](references/pipelines.md)
- [Printing recipes](references/printing.md)
- [Cost, waiting, previews, delivery and follow-ups](references/delivery.md)
- [Troubleshooting](references/troubleshooting.md)
- [Meshy API pricing](https://docs.meshy.ai/en/api/pricing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, file paths, and JSON-oriented CLI outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide the agent to create, inspect, download, or hand off 3D asset files within the requested workspace.]

## Skill Version(s):

0.6.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
