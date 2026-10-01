## Description:

This skill guides agents through LinkPix workflows for recreating short-form Vidu Q2 promotional videos by analyzing a reference video, adapting the script to a user's product, and generating the result through qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketing operators, and agents use this skill to recreate the structure and pacing of trending short-form commerce videos while substituting the user's product, assets, and selling points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit, Node.js, or npm packages, including unpinned package versions.

Mitigation: Prefer a preinstalled or pinned qhkit version, review install commands before execution, and avoid persistent shell-profile or runtime changes unless explicitly intended.

Risk: The workflow requires an API key for qhkit access.

Mitigation: Use a secure secret store or environment variable and avoid pasting API keys into chat transcripts.

Risk: Generation commands can create paid tasks and consume account credits.

Mitigation: Run estimates where supported and require explicit user confirmation of model, duration, assets, and expected credit cost before submitting generation tasks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-vidu-q2-clone)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include script rewrites, model-selection guidance, task-status instructions, and generated media delivery guidance.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
