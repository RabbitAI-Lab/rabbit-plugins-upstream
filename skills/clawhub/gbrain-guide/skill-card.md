## Description: <br>
Guides agents in operating a local GBrain knowledge base through WorkBuddy MCP, including content import, classification prefixes, linking, schema pack selection, health governance, batching large libraries, and Obsidian handoff. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noaheleven](https://clawhub.ai/user/noaheleven) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge-base operators use this skill to have agents manage GBrain-backed local knowledge workflows, including importing files, applying schema prefixes, creating links and tags, checking health, and planning large-batch ingestion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may move or import local knowledge-base files without sufficiently explicit user review. <br>
Mitigation: Require the agent to show source paths, destination prefixes, files to import, and MCP write tools before execution; prefer copy or dry-run workflows. <br>
Risk: Admin maintenance or repair actions could alter a GBrain knowledge base without an easy rollback path. <br>
Mitigation: Keep backups for large imports and require explicit approval before running admin maintenance commands. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/NoahEleven/gbrain-guide) <br>
- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/gbrain-guide) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown guidance with MCP tool names, workflow steps, tables, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent-facing operational instructions for GBrain and WorkBuddy MCP usage.] <br>

## Skill Version(s): <br>
0.1.1 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
