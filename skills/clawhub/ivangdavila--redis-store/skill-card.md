## Description: <br>
Designs, tunes, and debugs Redis data modeling, commands, caching, queues, persistence, replication, clustering, security, and production incidents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and application operators use this skill to choose Redis data structures, write Redis commands and Lua scripts, troubleshoot incidents, tune memory and persistence, and plan migrations or managed Redis deployments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Redis commands may delete keys, alter server configuration, shut down a server, or export sensitive production data. <br>
Mitigation: Review commands before execution, require explicit confirmation for destructive operations, and treat Redis snapshots and broad key scans as sensitive data handling events. <br>
Risk: The skill may read and update local Redis memory and preferences under ~/Clawic/data/redis-store/. <br>
Mitigation: Keep secrets out of local skill memory, periodically review stored context, and remove observations that are no longer needed. <br>


## Reference(s): <br>
- [ClawHub Redis Skill Page](https://clawhub.ai/ivangdavila/skills/redis-store) <br>
- [Clawic Redis Skill Page](https://clawic.com/skills/redis-store) <br>
- [Publisher Profile](https://clawhub.ai/user/ivangdavila) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline Redis commands, shell commands, configuration snippets, and code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose redis-cli commands, Redis configuration changes, Lua scripts, and operational checklists; production-impacting commands require review before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
