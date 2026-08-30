## Description:

Helps Amazon sellers, cross-border brands, and listing operations teams turn product facts and authorized assets into listing image plans, prompts, runnable AI-HIVE commands, delivery checklists, and English listing copy without inventing certifications, effects, or testimonials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, cross-border brands, and listing operations teams use this skill to plan Amazon listing visuals, A+ image drafts, commercial image prompts, AI-HIVE generation commands, task records, and acceptance checks. It is intended for workflows that rely on truthful product facts, authorized source assets, and user review before any paid generation task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid AI-HIVE generation can incur cost or submit unintended model parameters.

Mitigation: Review and confirm the model, route, uploaded files, prompt, batch size, and pricing snapshot before running generation commands.

Risk: Unlicensed product, brand, person, or reference assets could be uploaded or transformed.

Mitigation: Use only assets the user has rights to use, and fall back to abstract structure guidance when authorization is not established.

Risk: Generated listing content could imply unsupported product claims, certifications, rankings, or testimonials.

Mitigation: Require factual product inputs and human review; avoid claims that are not supported by provided evidence.

Risk: API-key initialization may store credentials locally under ~/.ai-hive/config.json.

Mitigation: Prefer environment variables for temporary use, keep the local config file permission-restricted, and avoid logging, committing, or screenshotting API keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/amazon-listing-image-studio-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with runnable bash commands, JSON task records, prompts, checklists, and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE model, route, pricing snapshot, taskId, status, and downloaded file locations when generation is executed.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
