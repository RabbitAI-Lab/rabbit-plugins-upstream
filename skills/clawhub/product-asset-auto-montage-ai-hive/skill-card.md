## Description:

This skill turns product media libraries into auditable ecommerce video montage workflows, runnable AI-HIVE generation commands, and delivery checklists for multi-SKU product content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, content operations teams, agencies, and advertising post-production teams use this skill to organize authorized product media, plan multi-SKU short-video edits, generate missing shots through AI-HIVE when approved, and produce traceable delivery records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may require an AI-HIVE API key and may upload selected product media to AI-HIVE.

Mitigation: Install and run it only if that service, credential use, and media upload are acceptable; use environment variables or the generated local config file and avoid pasting real API keys into prompts, logs, screenshots, or version control.

Risk: AI-HIVE generation can create paid tasks or cost-bearing batch work.

Mitigation: Review prompts, routing mode, model configuration, price snapshot, output path, and task parameters before submission; run a small sample before batch generation.

Risk: Product videos can become misleading if unlicensed media, cross-SKU assets, outdated prices, or unverified claims are used.

Mitigation: Use only authorized media, keep SKU assets separated, mark uncertain claims for review, and verify product, pricing, inventory, efficacy, and platform-sensitive statements before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-asset-auto-montage-ai-hive)
- [AI-HIVE chat and API access entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL used by scripts](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown with structured production plans, JSON artifacts, inline shell commands, and task records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON briefs, ffmpeg command outputs, AI-HIVE task records, and downloaded generated media when the user runs the provided scripts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
