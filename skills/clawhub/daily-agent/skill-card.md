## Description: <br>
Classify, route, and orchestrate incoming agent tasks by determining task type, complexity, skill match, and execution path. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill as an orchestration layer for incoming user messages, including task classification, complexity assessment, skill matching, and delegation to main-session, spawned, or scheduled execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can save conversation-derived personal data into memory or profile files. <br>
Mitigation: Constrain or disable profile extraction and memory sync, and review generated records before allowing durable storage. <br>
Risk: The skill can run local scripts, spawn background work, schedule work, and commit repository changes. <br>
Mitigation: Require explicit user approval for script execution, spawned or scheduled work, and commits; disable autocommit and cron/spawn behavior unless needed. <br>
Risk: Broad routing and orchestration behavior can affect many tasks when installed as an always-on helper. <br>
Mitigation: Install only when an always-on task router is intended, and limit its scope through agent permissions and workspace policies. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/daily-agent) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and plain text with optional inline code or command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include routing decisions, task briefs, plans, memory/profile updates, scheduled work, or repository changes depending on enabled behavior.] <br>

## Skill Version(s): <br>
2.15.1 (source: server release evidence; artifact frontmatter reports 2.17.0, package.json reports 2.2.0, and _meta.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
