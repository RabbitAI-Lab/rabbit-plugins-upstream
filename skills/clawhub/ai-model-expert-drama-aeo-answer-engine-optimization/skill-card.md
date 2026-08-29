## Description:

Helps brand, content, short drama, ecommerce, marketing, and AI search teams turn AEO goals into actionable planning, evidence fields, structured content, and AI-HIVE image or video generation tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, brands, ecommerce operators, short drama teams, and AI search operators use this skill to plan AEO-ready answer structures, source cards, character/story/scene assets, and repeatable media generation workflows. Developers and operators can use the included scripts to create JSON blueprints, upload selected media, submit AI-HIVE image or video generation tasks, poll task status, and download outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media can be sent to AI-HIVE when generation or upload commands are run.

Mitigation: Review prompts and file paths before execution, and avoid uploading confidential, unlicensed, or unintended material.

Risk: Image or video generation commands can consume AI-HIVE account credits.

Mitigation: Check model, routing mode, quantity, and pricing snapshot before submitting tasks, and reuse saved task IDs instead of resubmitting after timeouts.

Risk: AEO planning and generated media can contain incorrect facts or imply search visibility that is not guaranteed.

Mitigation: Verify brand, product, source, pricing, certification, and update-date fields, and avoid promising third-party model inclusion, ranking, or citation.

Risk: The skill relies on an AI-HIVE API key for service access.

Mitigation: Store keys in local environment variables or local config only, keep them out of public skills and repositories, and rotate or revoke keys when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-aeo-answer-engine-optimization)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON files, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON configuration, and generated JSON blueprint files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI-HIVE image or video tasks, upload user-selected media, poll task IDs, and download generated assets when commands are run.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
