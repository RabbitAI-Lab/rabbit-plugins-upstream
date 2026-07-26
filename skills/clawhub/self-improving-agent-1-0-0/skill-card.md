## Description: <br>
Captures learnings, corrections, feature requests, and error reports in project markdown files so agents can review and promote recurring knowledge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dc-acronym](https://clawhub.ai/user/dc-acronym) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to capture command failures, user corrections, missing capabilities, knowledge gaps, and recurring best practices as structured project notes. Teams can review those notes and selectively promote broadly useful guidance into persistent agent memory files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist conversation-derived content and error context into project learning logs, which may expose confidential data in shared, proprietary, or version-controlled repositories. <br>
Mitigation: Require confirmation before logging conversation-derived content and redact secrets, personal data, and confidential project details before writing or committing logs. <br>
Risk: The skill can recommend durable updates to agent memory files, which may influence future agent behavior if incorrect or overly broad guidance is promoted. <br>
Mitigation: Manually review proposed changes to CLAUDE.md or AGENTS.md before accepting them, and keep promoted guidance concise, scoped, and reversible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dc-acronym/skills/self-improving-agent-1-0-0) <br>
- [Learnings template](artifact/LEARNINGS.md) <br>
- [Entry examples](artifact/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured markdown entry templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces project-local learning, error, and feature-request entries under .learnings/ and may propose updates to CLAUDE.md or AGENTS.md.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
