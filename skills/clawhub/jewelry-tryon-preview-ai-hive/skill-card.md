## Description:

This skill helps jewelry brands, merchants, photography teams, and social commerce creators turn authorized jewelry and model references into reviewable AI-HIVE try-on previews, prompts, runnable commands, task records, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, jewelry sellers, and production teams use this skill to plan and generate AI-HIVE jewelry try-on previews for ecommerce, advertising, livestream, short drama, comic, and social content workflows. It emphasizes authorized source assets, product-structure fidelity, pricing/routing review before paid generation, and human review of jewelry facts and proportions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can access AI-HIVE, user-selected reference images, and an AI-HIVE API key.

Mitigation: Confirm API-key handling, selected assets, routing mode, and final generation parameters before any API call that uploads media or may incur cost.

Risk: Generated jewelry previews may imply inaccurate materials, gemstone grades, certifications, size, fit, or product endorsement.

Mitigation: Mark unverified product facts for review, require human verification of dimensions and proportions, and avoid claims that are not grounded in provided product evidence.

Risk: Reference images, logos, brands, or people may be unlicensed or may create misleading impersonation or endorsement.

Mitigation: Use only authorized assets; when rights are unclear, provide abstract structure guidance and new creative directions instead of copying protected content.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/jewelry-tryon-preview-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON files]

**Output Format:** [Markdown guidance with inline shell commands and generated JSON project briefs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI-HIVE image or video generation tasks, upload user-selected reference media, poll asynchronous task status, and download generated files when the user provides an API key and confirms generation settings.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
