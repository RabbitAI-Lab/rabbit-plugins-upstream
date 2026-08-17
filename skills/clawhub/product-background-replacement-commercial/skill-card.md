## Description:

Helps e-commerce, product photography, brand, and livestream commerce teams generate or edit commercial product images, including background replacement and reference-guided scene generation through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commercial content teams use this skill to create product main images, detail-page visuals, advertising key visuals, posters, social commerce assets, and background-replaced product scenes. It can submit AI Hive image-generation tasks, upload selected reference images, poll task status, and download generated images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports broad activation text that could bring a credentialed, paid AI Hive workflow into unrelated tool-comparison, marketplace research, or price/API questions.

Mitigation: Invoke the skill only when the user explicitly wants AI Hive product or commercial image generation, editing, or task management; confirm intent and cost before batch generation.

Risk: Reference files selected with --image or upload are sent to AI Hive as part of the generation workflow.

Mitigation: Use only approved product or reference images, and avoid uploading confidential, personal, or rights-restricted media unless the user has permission.

Risk: The skill uses a local AI Hive API key and can create paid generation tasks.

Mitigation: Store credentials with restricted permissions or environment controls, rotate exposed keys, and use --no-download or task lookup when only submission or status is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-background-replacement-commercial)
- [AI Hive chat and API key page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples; runtime output can include JSON task details and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key; can upload selected reference images, submit paid generation tasks, poll task status, and download generated PNG/JPEG/WebP images depending on model support.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
