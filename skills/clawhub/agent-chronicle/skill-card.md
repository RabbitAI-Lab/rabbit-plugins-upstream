## Description: <br>
AI-powered diary generation for agents that creates reflective journal entries with quote tracking, curiosity backlog, decision archaeology, relationship notes, mood analytics, weekly digests, On This Day resurfacing, and cron auto-generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use Agent Chronicle to create and manage persistent diary entries, weekly summaries, quotes, curiosities, decisions, relationship notes, and mood or topic analyses from agent work sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can summarize local session history into persistent diary, memory, quote, decision, and relationship files. <br>
Mitigation: Install only when persistent journaling is intended; avoid use around secrets, regulated data, or private third-party conversations, and review generated entries before saving or exporting. <br>
Risk: Broad diary and reflection triggers may capture more personal or collaborative context than expected. <br>
Mitigation: Disable auto-generation, memory integration, quote capture, and relationship tracking unless those records are explicitly wanted. <br>
Risk: Exported HTML may expose sensitive diary content or inherit unwanted remote styling behavior. <br>
Mitigation: Prefer non-HTML export for sensitive material unless the remote stylesheet is removed and the output is reviewed before sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/robbyczgw-cla/skills/agent-chronicle) <br>
- [README.md](README.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>
- [config.example.json](config.example.json) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown diary entries and digests, JSON task payloads and analytics, plus shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local diary, quote, curiosity, decision, relationship, memory, and export files according to configuration; PDF and HTML export require additional local tooling.] <br>

## Skill Version(s): <br>
0.7.2 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
