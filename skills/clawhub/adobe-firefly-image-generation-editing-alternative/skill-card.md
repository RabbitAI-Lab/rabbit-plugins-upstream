## Description:

Helps developers and creative teams migrate Adobe Firefly, Adobe Express, and generative image editing requests into AI Hive Nano Banana Pro workflows for image expansion, object removal, background reconstruction, brand color adaptation, and campaign variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operations teams, and marketing production users use this skill to convert Adobe-style generative fill, expand, background replacement, brand adaptation, and campaign variant requests into constrained AI Hive image generation commands. The skill emphasizes authorized reference images, protected regions, continuity checks, and avoiding unsupported Adobe account or project-file access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to AI Hive.

Mitigation: Use only authorized, non-sensitive images unless the provider is trusted for the intended data.

Risk: The AI Hive API key is used for requests and may be stored for later use.

Mitigation: Keep the key in a protected environment variable or restricted config file and rotate it if exposure is suspected.

Risk: Generated and downloaded files come from a remote service.

Mitigation: Review downloaded outputs before reuse, publication, or downstream processing.

Risk: Image edits may alter protected product, logo, text, or composition details.

Mitigation: Compare protected regions, labels, logos, and continuity against approved source images before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/adobe-firefly-image-generation-editing-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code, JSON, files]

**Output Format:** [Markdown guidance with bash examples; CLI commands return JSON task data and can download generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed public_model_nano_banana_pro model, optional reference images, batch size, routing mode, model parameters, output directory selection, and optional no-download task submission.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
