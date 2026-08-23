## Description:

Generates or edits images with exact Chinese, English, numeric, and short marketing text using Nano Banana Pro through AI Hive, with character-level review guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, ecommerce operators, and developers use this skill to create or edit AI-generated visuals that contain approved short text, brand layouts, product labels, social covers, and bilingual promotional copy. It emphasizes locking the intended text before generation and reviewing visible characters before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an AI Hive API key in ~/.ai-hive/config.json.

Mitigation: Use the environment variable or local config only in trusted user accounts, keep the file permissions restricted, and rotate the key if the machine or account is shared.

Risk: Reference files whose paths are supplied to the helper can be uploaded to AI Hive.

Mitigation: Pass only approved image files needed for the generation task and avoid private, unrelated, regulated, or confidential files.

Risk: The artifact includes unused generic chat and video helper code in addition to the image workflow.

Mitigation: For stricter environments, deploy a reduced version that keeps only the Nano Banana Pro image generation commands that are required.

Risk: Generated text in images can be incorrect, incomplete, duplicated, or unsuitable for high-stakes claims.

Mitigation: Use the skill's character-level acceptance checklist and place prices, legal terms, medical claims, and other non-tolerant text with approved design tools when exactness is mandatory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-exact-text-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generated image files and JSON task responses from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key; optional reference files are uploaded only when their paths are provided; generated outputs are downloaded to the configured output directory.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
