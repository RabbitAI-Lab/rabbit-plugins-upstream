## Description: <br>
Persistent cognitive memory for AI agents: query, record, review, and consolidate knowledge across sessions with spreading activation, FSRS scheduling, and NLI contradiction detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[idapixl](https://clawhub.ai/user/idapixl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to give agents durable local memory for retrieving prior decisions, recording observations and questions, tracking work across sessions, and consolidating knowledge over time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Durable local memory can retain sensitive project context across sessions. <br>
Mitigation: Install only where persistent memory is intended, review what agents store, and manage the local database according to the deployment's data-handling expectations. <br>
Risk: The skill depends on an external package and local services before its memory tools are available. <br>
Mitigation: Review the @fozikio/cortex-engine package and start the local services deliberately with the documented service commands. <br>


## Reference(s): <br>
- [Cortex Engine GitHub repository](https://github.com/Fozikio/cortex-engine) <br>
- [@fozikio/cortex-engine npm package](https://www.npmjs.com/package/@fozikio/cortex-engine) <br>
- [ClawHub skill page](https://clawhub.ai/idapixl/skills/cortex-engine) <br>
- [Publisher profile](https://clawhub.ai/user/idapixl) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline tool examples and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides an agent to use an external local MCP memory service; it does not itself execute commands.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
