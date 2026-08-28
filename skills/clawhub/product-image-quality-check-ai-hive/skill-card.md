## Description:

AI商品图自动质检｜AI-HIVE helps e-commerce design, product operations, brand review, and batch-generation teams turn product-image quality-check requests into review workflows, runnable AI-HIVE commands, issue lists, and repair guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce teams, and developers use this skill to compare product images against real references, brand rules, packaging text, and platform requirements, then produce a prioritized quality checklist and repair plan. When generation is needed, it guides AI-HIVE model configuration, media upload, routing, polling, and result download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected images, video, audio, or other media may be uploaded to AI-HIVE.

Mitigation: Confirm file selection, usage rights, privacy expectations, and upload intent before running upload or generation commands.

Risk: AI-HIVE generation tasks may incur charges, especially for batch or retry workflows.

Mitigation: Show the final prompt, model, routing mode, parameters, and price snapshot before submission, and run a small sample before batch generation.

Risk: API keys can be exposed if pasted into scripts, logs, screenshots, or versioned files.

Mitigation: Use environment variables or the local config file, keep examples as placeholders, and avoid committing or echoing real API keys.

Risk: Automated quality checks can miss or overstate product, regulatory, brand, or factual claims.

Mitigation: Mark uncertain facts as needing verification and keep human final review for key SKUs, legal claims, packaging text, brand usage, and platform compliance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/product-image-quality-check-ai-hive)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include issue lists, evidence locations, risk levels, repair recommendations, AI-HIVE routing mode, price snapshot, task ID, task status, and downloaded file locations when generation is run.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
