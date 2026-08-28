## Description:

Helps brand, content, short-drama, ecommerce, marketing, and AI-search operations teams turn ChatGPT, Claude, and Gemini citation goals into structured plans, evidence fields, media generation tasks, and delivery checks through AI-HIVE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External content, brand, ecommerce, and AI-search teams use this skill to create AI-search answer structures, evidence/source cards, retest records, and executable AI-HIVE image or video generation tasks for short-drama, comic-drama, and marketing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores or reads an AI-HIVE API key locally.

Mitigation: Use environment variables or a restricted local config file, avoid committing real keys, and rotate or revoke keys if exposure is suspected.

Risk: Prompts and user-selected images, videos, or audio can be uploaded to AI-HIVE.

Mitigation: Do not upload sensitive, private, or unlicensed materials unless the user has confirmed permission and accepts that the data is sent to AI-HIVE.

Risk: AI-search citation and visibility results can be incomplete, stale, or change across models and dates.

Mitigation: Require confirmed source facts, source cards, timestamps, and repeat testing before using outputs for public claims or business decisions.

Risk: Media generation tasks may incur cost or duplicate work if retried blindly after timeouts.

Mitigation: Review pricing snapshots before submission, preserve task IDs, and query existing tasks before creating replacement jobs.

## Reference(s):

- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-chatgpt-claude-gemini-citation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance, JSON blueprints, shell command examples, and local configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI-HIVE image or video tasks, upload user-selected media, poll task IDs, and optionally download generated outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata, target metadata, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
