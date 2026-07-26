## Description: <br>
Muninn provides a local per-project memory layer for AI agents using the Context Exchange Protocol (CXP). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[endgegnerbert-tech](https://clawhub.ai/user/endgegnerbert-tech) <br>

### License/Terms of Use: <br>
UNLICENSED <br>


## Use Case: <br>
Developers and agent operators use Muninn to initialize a project-local memory layer, search indexed project context, and persist project-specific decisions through MCP tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent project instructions may be added to agent rule files during initialization or reindexing. <br>
Mitigation: Review diffs after initialization or reindexing, especially CLAUDE.md, .cursorrules, .antigravityrules, .gitignore, and .muninn contents. <br>
Risk: Project memories and indexes may retain sensitive information if users store secrets or sensitive user data. <br>
Mitigation: Avoid storing secrets or sensitive user data in memories and inspect or delete local .muninn memory files when needed. <br>
Risk: The skill runs a local indexing executable as part of its project memory workflow. <br>
Mitigation: Install only when local indexing and workflow-shaping behavior are desired, and review the package before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/endgegnerbert-tech/skills/muninn) <br>
- [Muninn homepage](https://www.muninn.space) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [MCP tool responses with Markdown context and locally written project memory/configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates project-local .muninn state and agent rule files during initialization or reindexing.] <br>

## Skill Version(s): <br>
2.3.7 (source: SKILL.md frontmatter, package.json, and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
