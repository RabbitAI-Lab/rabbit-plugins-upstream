## Description: <br>
Generates concise pre-meeting briefings from recent phone notifications and, when relevant, current web search results around user-specified topics and people. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vivalavida-say-hi](https://clawhub.ai/user/vivalavida-say-hi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users use this skill to prepare for meetings by turning recent notifications and relevant online developments into a focused briefing with overview, key findings, and suggested concerns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill searches recent phone notifications for meeting topics and followed people, which may expose sensitive personal or business context. <br>
Mitigation: Use it only in environments where notification access is expected, and avoid providing sensitive topics or names unless the user has approved that access. <br>
Risk: The skill may automatically install byted-web-search from a remote source when the dependency is missing. <br>
Mitigation: Confirm the dependency is already installed or review and approve the remote source before allowing the local skill environment to change. <br>
Risk: When web search is unavailable, briefings may be based only on notification data and omit relevant external developments. <br>
Mitigation: Treat notification-only briefings as incomplete and follow up with direct stakeholder confirmation or separate web research for external topics. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vivalavida-say-hi/skills/yoooclaw-meeting-preparations-en) <br>
- [byted-web-search Dependency Source](https://skills.volces.com/skills/bytedance/agentkit-samples) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands] <br>
**Output Format:** [Markdown session text with source-labeled findings and suggested focus points] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces no files; may downgrade to notification-only briefing when web search is unavailable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
