## Description:

公众号内容工坊 is a WeChat Official Account content creation and operations skill for viral article discovery, article drafting, title generation and scoring, copy rewriting, prohibited-word checks, cover design, and account diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, WeChat account operators, brand teams, MCN agencies, editors, and content strategists use this skill to turn RedFox-backed WeChat trend data into publish-ready articles, titles, compliance checks, cover concepts, reports, and account optimization guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses RedFox-backed network/API calls and may process drafts, URLs, files, images, and account-related content.

Mitigation: Install only if RedFox is an acceptable backend service, and avoid submitting confidential drafts, private local files, or sensitive account material.

Risk: REDFOX_API_KEY is required and one script can print the full API key in debug logs.

Mitigation: Use a revocable key, keep it in the environment rather than prompts or files, and do not run debug mode during normal use.

Risk: Normal operation can create local JSON, HTML, and text report files.

Mitigation: Review generated files before sharing and remove local reports that contain sensitive content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/wechat-creator)
- [RedFoxHub](https://redfox.hk)
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?souce=github)
- [README.en.md](artifact/README.en.md)
- [M1 API specification](artifact/references/m1_api_spec.md)
- [M1 category mapping](artifact/references/m1_category_mapping.md)
- [M5 prohibited-word workflow](artifact/references/m5_prohibited_word_core_workflow.md)
- [M7 account diagnosis workflow](artifact/references/m7_core_workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with tables, article drafts, scoring summaries, rewrite outputs, image-generation prompts, and optional HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY for RedFox-backed data access and may create local JSON, HTML, and text report files during normal use.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
