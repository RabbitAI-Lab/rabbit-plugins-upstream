## Description: <br>
Engagement Inbox Manager helps an agent triage social comments, DMs, and mentions; detect register and commenter class; draft ranked human-posted replies; maintain escalation and moderation workflows; and collect UGC repost permission evidence without auto-sending messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Social, community, and marketing operators use this skill to process exported or pasted inbox batches, prioritize response work, flag escalations, prepare draft replies for human posting, and structure UGC permission collection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles potentially sensitive comments, DMs, mentions, and UGC permission evidence. <br>
Mitigation: Review exports, proposed memory writes, and permission evidence before approving any saved result or registry proposal. <br>
Risk: Draft replies or moderation recommendations could be posted prematurely or without appropriate context. <br>
Mitigation: Keep all replies as drafts for a human to review and post; route tripped escalation rows to the named owner before continuing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/engagement-inbox-manager) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown triage report with ranked draft replies, escalation rows, SLA deadlines, moderation notes, UGC permission candidates, and handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Replies are drafts for human posting; memory writes and registry proposals require user confirmation.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
