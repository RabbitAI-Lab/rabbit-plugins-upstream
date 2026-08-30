## Description:

Helps users plan a unified desktop agent workspace across files, browser workflows, office software, and AI-HIVE by producing a task home, permission matrix, input directory, media workflow, and delivery index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Personal users, small and midsize businesses, and operations teams use this skill to turn desktop work goals into auditable AI-HIVE task plans, model-routing choices, approval gates, and delivery records. It is intended for Chinese desktop workflows that combine document handling, marketing planning, visual production, and human confirmation before paid or irreversible actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send AI_HIVE_API_KEY to an environment-selected server if AI_HIVE_BASE_URL is changed.

Mitigation: Keep AI_HIVE_API_KEY in a trusted environment and set AI_HIVE_BASE_URL only to known, trusted destinations.

Risk: Activation and safety controls are broader than the helper code enforces.

Mitigation: Require explicit confirmation before paid, bulk, public-posting, deletion, or permission-changing actions, and treat pause, revoke, and audit controls as workflow requirements to verify.

## Reference(s):

- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [OpenAI: ChatGPT Work and Codex](https://help.openai.com/zh-hans-cn/articles/20001275-chatgpt-work-and-codex)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-hot-desktop-agent-hub)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON execution-plan files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans should record model, routing mode, pricing snapshot, input hash, taskId, status, and outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
