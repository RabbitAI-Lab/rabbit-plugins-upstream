## Description:

This skill helps AI companies plan and produce Chinese image, short-video, and content marketing assets with audience strategy, content calendars, prompts, AI-HIVE task records, and review gates for factual claims and authorized media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, product, and developer-relations teams use this skill to create reviewable AI-company marketing plans, prompts, image/video generation workflows, and channel-specific adaptations. It is intended for content that can be checked against real product facts, authorized media, budget constraints, and platform requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation can upload reference media to an external service.

Mitigation: Use only authorized materials and confirm the user intends to use AI-HIVE before submitting media.

Risk: Generation tasks may incur cost or use an unsuitable speed, cost, or success-rate route.

Mitigation: Confirm budget and routing before generation and preserve pricing snapshots and task IDs for review.

Risk: API keys could be exposed through files, screenshots, logs, or shared command history.

Mitigation: Store the API key in an environment variable or chmod-0600 config file and avoid embedding it in generated assets or logs.

Risk: Marketing claims about product capability, customers, safety, compatibility, pricing, or performance could be misleading if unchecked.

Mitigation: Require human review of factual claims, mark uncertain facts as pending verification, and do not present AI-generated visuals as real cases.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/industry-ai-company-marketing-ai-hive)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [AI Company Image and Video Marketing Industry Playbook](references/industry-playbook.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese marketing plans, structured JSON briefs, prompts, task records, and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prepare API-backed image or video generation workflows that upload authorized media, submit tasks, poll task status, and download local outputs after user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
