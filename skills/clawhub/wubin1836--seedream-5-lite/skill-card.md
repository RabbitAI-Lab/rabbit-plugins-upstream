## Description:

Generates and edits images with Seedream 5.0 Lite through AI Hive, including text-to-image, reference-based edits, product visuals, marketing assets, posters, detail-page imagery, character concepts, and batch creative production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and ecommerce teams use this skill to prepare prompts, submit AI Hive Seedream 5.0 Lite image-generation or editing jobs, upload reference images, poll tasks, and download outputs for product and campaign visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced images are sent to AI Hive or its storage backend.

Mitigation: Use only content that is approved for AI Hive processing, and avoid sensitive personal, confidential, or unreleased brand assets unless AI Hive's data handling terms meet the user's requirements.

Risk: The skill stores an AI Hive API key locally, which can authorize account usage and paid generation.

Mitigation: Protect the local configuration file, prefer scoped credentials where available, rotate exposed keys, and remove credentials from shared machines.

Risk: Generated images can contain incorrect product, brand, text, pricing, certification, or legal details.

Mitigation: Review generated assets before publication and manually verify complex text, claims, prices, certifications, and legal information.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wubin1836/skills/seedream-5-lite)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key and account page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown guidance with inline shell commands; downloaded image files and JSON task responses from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference images, batch generation, model parameters, task polling, output directories, and submit-only mode.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
