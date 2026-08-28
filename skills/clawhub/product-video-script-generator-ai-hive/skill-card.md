## Description:

Helps ecommerce merchants, product operators, and short-video directors turn product video needs into reviewable Chinese storyboards, voiceover copy, shot prompts, AI-HIVE generation commands, task records, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, product operators, advertisers, and video creators use this skill to plan product short videos, generate scripts and prompts, and optionally submit AI-HIVE image or video tasks after reviewing facts, rights, routing, and pricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use an AI-HIVE API key and upload user-selected media files.

Mitigation: Install only if comfortable granting that access, pass only media the user is authorized to use, and keep the stored API key file private.

Risk: Generation commands may incur AI-HIVE costs or use unsuitable model, routing, or pricing choices.

Mitigation: Review prompts, routing, model configuration, and pricing snapshots before submitting tasks, especially before batch generation.

Risk: Product video outputs can include unsupported claims, unauthorized lookalike content, or misleading endorsements if inputs are not checked.

Mitigation: Require factual product inputs, rights-confirmed source material, and human review before publishing or using generated content commercially.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-video-script-generator-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and optional JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create project blueprints, submit AI-HIVE tasks, poll asynchronous results, and download generated files when the user provides credentials and confirms execution.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
