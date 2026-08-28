## Description:

This skill helps e-commerce merchants, lifestyle brands, and short-video creators turn first-person POV product-ad ideas into scripts, shot prompts, AI-HIVE video tasks, runnable commands, and delivery checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, e-commerce operators, and creators use this skill to plan and generate first-person POV product advertising workflows, scripts, prompts, AI-HIVE task commands, and quality checks. It is intended for authorized product media and truthful claims, with review before any paid generation call.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected uploads may include media the user is not authorized to use.

Mitigation: Confirm rights to images, video, logos, copy, and references before uploading or generating derivative content.

Risk: AI-HIVE image or video generation can trigger paid API calls.

Mitigation: Review final prompts, model choice, routing mode, and price snapshot before submitting generation tasks.

Risk: API keys can be exposed through local configuration, logs, screenshots, or shared files.

Mitigation: Use environment variables or a protected local config file, keep placeholders in examples, and avoid echoing real keys.

Risk: Generated ads can imply unsupported product claims or fake user testimony.

Mitigation: Mark unverified claims for review and do not present generated scenes as real tests, endorsements, or guaranteed results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/pov-product-ad-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown with Chinese production plans, prompts, shell commands, and optional JSON or media-file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use AI-HIVE API calls, media uploads, async task polling, downloads, and local ffmpeg processing after user review.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
