## Description: <br>
Installs GitNexus, configures MCP/editor integration, and builds a code knowledge graph for the current project. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[babywhale](https://clawhub.ai/user/babywhale) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to install GitNexus, configure MCP support in supported editors, and index a repository for code graph queries such as context lookup, impact analysis, and search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make persistent local tooling and project-state changes, including global npm installation, MCP/editor configuration writes, repository indexing, .gitignore updates, and possible git init/add/commit steps. <br>
Mitigation: Require explicit user approval before those actions and review projects for secrets or uncommitted work before indexing or git operations. <br>


## Reference(s): <br>
- [Code Graph（代码图谱） on ClawHub](https://clawhub.ai/babywhale/skills/code-graph) <br>
- [Node.js](https://nodejs.org/) <br>
- [nvm](https://github.com/nvm-sh/nvm) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and command output interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local setup actions including npm installation, MCP/editor configuration, repository indexing, .gitignore updates, and git initialization guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
