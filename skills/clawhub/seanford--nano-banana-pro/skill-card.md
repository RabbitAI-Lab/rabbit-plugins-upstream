## Description:

Generate or edit images with Nano Banana Pro (Gemini 3 Pro Image), supporting text-to-image and image-to-image workflows at 1K, 2K, and 4K resolutions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate new PNG images or edit existing images through Google's Gemini image service while preserving the user's creative intent and saving outputs into the active workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and input images are sent to Google's Gemini service during generation or editing.

Mitigation: Use the skill only for content that can be shared with that service and avoid sending confidential, regulated, or sensitive images unless approved.

Risk: API keys may be exposed if pasted into chat, shell history, or command arguments.

Mitigation: Set GEMINI_API_KEY through a protected environment or secret manager and avoid passing keys inline with --api-key where possible.

Risk: Python dependencies are specified with lower bounds rather than pinned exact versions.

Mitigation: Run the script in an isolated environment and pin or lock dependencies before production use.

## Reference(s):

- [Nano Banana Pro on ClawHub](https://clawhub.ai/seanford/skills/nano-banana-pro)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [PNG image files with terminal status output and concise usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are saved as PNG files at the requested filename or path; supported resolutions are 1K, 2K, and 4K.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
