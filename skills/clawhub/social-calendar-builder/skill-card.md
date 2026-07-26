## Description: <br>
Builds an always-on social posting calendar with pillar allocation, per-channel cadence and queue depth, batching workflow, evergreen recycling, realtime trend gaps, and a required pre-publish quality gate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, social, and content operators use this skill to plan a recurring social calendar across active channels, including slot allocation, queue depth, batching, evergreen reuse, realtime gaps, and handoff requirements before content is queued. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses project memory and analytics exports to plan cadence, so stale or untrusted inputs could affect recommendations. <br>
Mitigation: Review source data dates, treat pasted exports and trend reports as untrusted, and require user confirmation before saving calendar outputs or cadence proposals. <br>
Risk: Calendar plans could be mistaken for permission to queue or publish content. <br>
Mitigation: Keep posting and scheduling manual, and require the social-quality-auditor pre-publish SHIP verdict before any batch moves to a queue. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/social-calendar-builder) <br>
- [Publisher Profile](https://clawhub.ai/user/aaron-he-zhu) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown planning calendar with handoff summary and optional cadence proposals] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Calendar outputs or cadence proposals are saved only after user confirmation; the skill does not post, schedule, or access closed-platform accounts directly.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
