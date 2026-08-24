## Description:

Nano Banana 2 精准文字图片 helps agents design short-text image prompts for Nano Banana 2, generate or edit images through AI Hive, and require manual proofing before use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent operators use this skill to create or edit product, social, packaging, and poster images that contain very short Chinese or English text. It is suited to draft generation with character-by-character review, not unattended production of legal, pricing, date, model, QR code, or long-form copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to AI Hive.

Mitigation: Use only prompts and images that are appropriate to share with that provider.

Risk: Running init stores an API key locally.

Mitigation: Prefer scoped keys, keep the local config private, and rotate the key if it is exposed.

Risk: Generated text may be misspelled, incomplete, or unsuitable for legal, pricing, date, model, QR code, or promotional claims.

Mitigation: Transcribe and compare every text cell manually, require business-owner review for sensitive copy, and switch to a text-free image plus post-production layout after repeated failures.

Risk: Generated image files are downloaded to the user's Downloads folder by default.

Mitigation: Use a deliberate output directory or no-download mode when generated files should not be saved automatically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-exact-text-image)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash examples, CLI text or JSON status, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses fixed public_model_nano_banana_2; optional reference images may be uploaded; generated files default to ~/Downloads/AiHive.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
