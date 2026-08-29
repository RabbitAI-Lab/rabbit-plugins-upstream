## Description:

This skill helps footwear brands, cross-border sellers, buyers, and social commerce teams create AI-HIVE footwear try-on previews, styling variants, prompts, runnable commands, and quality checks from authorized shoe, person, scene, pose, and platform inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External footwear brands, sellers, buyers, and content teams use this skill to turn AI footwear try-on requests into reviewable production plans, image prompts, AI-HIVE generation commands, task records, and acceptance checks. It is intended for authorized materials and commercial preview workflows, not unauthorized replication, false product claims, or fabricated testimonials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billable AI-HIVE generation calls can be submitted if the user proceeds with generation.

Mitigation: Review prompts, model parameters, routing mode, and pricing snapshot before submitting generation tasks; start with small samples for batch work.

Risk: Uploaded media may include protected, private, or unauthorized product, person, logo, or reference material.

Mitigation: Use only media the user is authorized to upload, confirm rights before reference-based editing, and provide abstract structure guidance when authorization is unclear.

Risk: Stored API keys can remain in local configuration after use.

Mitigation: Use environment variables or protected local config, avoid logging or committing keys, and remove or rotate the AI-HIVE API key when it is no longer needed.

Risk: Generated footwear previews may be mistaken for verified product performance or real fit evidence.

Mitigation: Label outputs as visual previews, mark unverified facts, and avoid claims about sizing, comfort, certification, sales, ranking, or platform approval unless independently verified.

## Reference(s):

- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base URL](https://ai-hive.iclip.cn/api)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/footwear-tryon-preview-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Chinese workflow sections, inline shell commands, JSON task records, prompts, and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local blueprint JSON files and may call AI-HIVE APIs for media upload, generation, polling, and downloads after user confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
