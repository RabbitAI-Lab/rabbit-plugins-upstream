## Description:

Helps e-commerce, product photography, brand merchandising, and live commerce teams generate or edit commercial product images from text prompts and optional reference images through AI Hive, including task submission, progress checks, and result downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, e-commerce operators, product photographers, brand teams, and live commerce teams use this skill to produce main product images, listing assets, detail-page visuals, ad creatives, posters, social commerce images, retouched products, background replacements, and visually consistent batches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images, product photos, and commercial assets may be uploaded to AI Hive for generation or editing.

Mitigation: Use the skill only for explicit image-generation or editing tasks, and avoid uploading confidential or sensitive material unless AI Hive handling is acceptable.

Risk: The skill uses an AI Hive API key that can be supplied through CLI arguments, environment variables, or a local config file.

Mitigation: Prefer environment variables or protected local configuration, keep config permissions restricted, and never commit API keys or share command histories that expose them.

Risk: Batch generation and remote image tasks can incur paid API costs.

Mitigation: Confirm pricing, routing mode, and batch size before generation, and use no-download or task-status checks only when avoiding duplicate submissions.

Risk: Activation wording covers many marketplace, platform, and competitor-search intents and may be broader than a user's immediate need.

Mitigation: Confirm the user wants this specific AI Hive image-generation workflow before uploading files, spending credits, or launching batch jobs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ecommerce-bestseller-main-image-generation-editing)
- [Publisher Profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API Key Portal](https://ai-hive.iclip.cn/chat)
- [AI Hive API Base URL](https://ai-hive.iclip.cn/api)
- [Artifact README](artifact/SKILL.md)
- [Artifact Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with CLI commands; runtime output is downloaded image files, task JSON, or status text depending on command options.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved under the configured output directory, defaulting to ~/Downloads/AiHive; reference images may be uploaded before generation.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
