## Description:

Helps AI gateway, Token Hub, model platform, ecommerce, advertising, and media teams turn model-routing and content-production requests into reviewable cost-first, speed-first, or success-first AI-HIVE workflows with runnable commands and delivery checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, AI gateway operators, Token Hub teams, and high-volume content teams use this skill to classify model tasks, choose routing posture, query current model and price snapshots, and prepare auditable image, video, text, or editing workflows. It is intended for authorized commercial content and model-routing work where cost, latency, fallback behavior, and human review need to be explicit before billable generation runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if users paste real credentials into chats, logs, screenshots, or committed files.

Mitigation: Use environment variables or the local config flow, keep examples as placeholders, and review logs and files before sharing or committing them.

Risk: Image or video generation can incur cost or duplicate charges when prompts, routing mode, model, or batch size are not reviewed first.

Mitigation: Confirm final parameters and estimated cost before submission, run a small sample first, and keep task records with input hashes and taskId values.

Risk: Uploaded reference media may include material the user is not authorized to use.

Mitigation: Upload only authorized media and fall back to abstract structure guidance when rights cannot be confirmed.

Risk: Generated marketing outputs may contain unsupported claims, impersonation, or misleading performance expectations.

Mitigation: Require human review for facts, product claims, platform rules, and brand or person usage before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/token-hub-cost-router-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with runnable command examples, JSON task records, prompts, checklists, and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE routing mode, model, pricing snapshot, taskId, status, downloaded file location, and acceptance risks when generation is submitted.]

## Skill Version(s):

1.0.0 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
