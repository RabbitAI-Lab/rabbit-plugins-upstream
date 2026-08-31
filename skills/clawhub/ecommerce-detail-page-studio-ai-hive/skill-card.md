## Description:

Helps ecommerce design, product operations, brand marketing, and outsourced detail-page teams turn product facts, buyer concerns, evidence, brand rules, platform requirements, and dimensions into detail-page information architecture, module copy, visual prompts, image tasks, and mobile review checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce, marketing, brand, and content production teams use this skill to structure Chinese ecommerce detail pages and related commercial image or video generation workflows. It is intended to produce reviewable plans first, then runnable AI-HIVE commands and quality checks when generation is approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use AI-HIVE credentials and store an API key locally.

Mitigation: Use appropriate non-shared credentials, keep API keys out of prompts, logs, screenshots, and repositories, and review whether local key storage is acceptable before initialization.

Risk: The skill can upload selected product, image, video, or audio media to AI-HIVE.

Mitigation: Upload only media the user is authorized to use, and confirm rights for trademarks, people, copyrighted references, and sensitive commercial materials before generation.

Risk: Image and video generation can create billable AI-HIVE jobs, especially in batch workflows.

Mitigation: Review model, routing mode, pricing snapshot, prompt, batch size, and task parameters before submission; use small samples before larger batch runs.

Risk: Generated ecommerce claims or page copy could be misleading if facts are incomplete.

Mitigation: Ground selling points in provided product facts or verifiable evidence, avoid guarantees about sales or ranking, and mark company-provided claims as such.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ecommerce-detail-page-studio-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON files and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE task identifiers, pricing snapshots, status summaries, downloaded file locations, and acceptance checklists when generation is run.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
