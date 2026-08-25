## Description:

Prechecks ecommerce ad copy and media for high-risk claims, evidence gaps, platform material risks, suggested replacements, and human review needs, with optional AI-HIVE workflows for image and video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Commerce merchants, ad operations teams, legal first-reviewers, and content operators use this skill to turn ecommerce advertising materials into reviewable risk lists, evidence gaps, fixes, scripts, prompts, commands, and acceptance checks. It is intended for draft compliance prechecks and production workflow planning, not as legal advice or a guarantee of platform approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send prompts and selected media to AI-HIVE or object storage during optional generation workflows.

Mitigation: Use only authorized, non-confidential materials unless the user accepts external processing; require separate approval before uploading media or submitting generation tasks.

Risk: Image and video generation workflows may incur costs.

Mitigation: Show final prompts, parameters, routing mode, and current price snapshot before execution; run a small sample before batch jobs.

Risk: Compliance outputs are drafts and may miss current platform, legal, or regulated-product requirements.

Mitigation: Mark unverifiable facts, cite current rules when available, and route key product, legal, brand, privacy, medical, financial, and child-related issues to human review.

Risk: The skill could be misused for unauthorized imitation, false product claims, fake testimonials, or platform-rule evasion.

Mitigation: Require proof of reference-material rights, preserve only abstract structure from references when rights are unclear, and refuse requests to fabricate claims, endorsements, or evasion tactics.

Risk: API keys can be exposed if copied into prompts, logs, screenshots, or committed files.

Mitigation: Use environment variables or the local AI-HIVE config file, keep real keys out of generated content, and avoid echoing credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ecommerce-ad-compliance-precheck-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with checklists, inline bash commands, prompts, code snippets, and optional JSON task records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE routing choices, model or price snapshots, task IDs, downloaded file paths, and recheck records when generation tasks are used.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
