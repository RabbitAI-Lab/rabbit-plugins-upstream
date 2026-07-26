## Description: <br>
Zwjh Skill provides a local long-term memory and knowledge graph layer for agents, with semantic and timeline retrieval, health checks, backups, and a localhost graph viewer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent users and developers use this skill to capture conversations or files into local long-term memory, query that memory through semantic search and timelines, inspect entity relationships, and run health, backup, restore, and scheduled maintenance workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create daily scheduled tasks and index local memory logs, which may process sensitive personal or project data without repeated prompts. <br>
Mitigation: Review the scheduled task setup before enabling it, limit the memory directory to intended content, and disable or remove the task when automatic processing is not needed. <br>
Risk: The localhost web UI serves graph data derived from local memory and loads a third-party CDN script. <br>
Mitigation: Use the web UI only on trusted machines, avoid exposing the localhost service beyond the local host, and accept the CDN dependency risk before launching it. <br>
Risk: Backup, restore, and maintenance commands can overwrite or transform local memory data. <br>
Mitigation: Create a backup before restore or maintenance commands, inspect paths and targets, and run destructive or state-changing operations only on data you intend to modify. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/zwjh-skill) <br>
- [Publisher profile](https://clawhub.ai/user/fyniujin) <br>
- [Local graph viewer](http://127.0.0.1:8080) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and command-line guidance with Python commands, JSON-style API responses, Mermaid graph output, and local web UI data views.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local files under the user's memory directory, can register daily scheduled tasks, can run a localhost web UI, and can perform backup or restore operations when invoked.] <br>

## Skill Version(s): <br>
2.1.0 (source: evidence.json release.version, artifact SKILL.md frontmatter, and artifact version.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
