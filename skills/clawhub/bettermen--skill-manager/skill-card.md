## Description: <br>
Skill 管理器 manages the WorkBuddy Skill lifecycle, including listing, viewing, creating, deleting, searching, auditing, packaging, installing, and dashboard-based administration of local and marketplace skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and WorkBuddy users use this skill to manage installed skills, inspect skill metadata, run health audits, clean common installation artifacts, and operate a local dashboard for skill inventory and review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad local file access and deletion behavior could remove or alter skills unexpectedly. <br>
Mitigation: Install and test in an isolated workspace or with backups until path validation and delete safeguards are reviewed. <br>
Risk: The local dashboard can expose skill metadata and management actions if served beyond localhost. <br>
Mitigation: Bind the web UI to localhost and avoid exposing the service on shared or public networks. <br>
Risk: Automatic repair or delete actions can make irreversible local changes. <br>
Mitigation: Use preview or dry-run style review first, require explicit confirmation, and inspect the affected paths before running fix or delete operations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/bettermen/skill-manager) <br>
- [Python](https://python.org) <br>
- [FastAPI](https://fastapi.tiangolo.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown reports, shell commands, JSON audit data, and local dashboard/API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include skill inventory tables, audit summaries, repair previews, exported JSON, and generated package paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
