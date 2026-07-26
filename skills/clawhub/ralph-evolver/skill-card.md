## Description: <br>
Recursive self-improvement engine. Think from first principles, let insights emerge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hsssgdtc](https://clawhub.ai/user/hsssgdtc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to inspect a local project, collect signals such as commit history, TODO/FIXME comments, error patterns, tests, and hotspots, and generate a first-principles improvement prompt for repair or discovery work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Project-defined commands may execute during health checks. <br>
Mitigation: Review package scripts and run the skill only in trusted, sandboxed repositories. <br>
Risk: Repository contents can be gathered into improvement prompts, which may expose secrets or sensitive code context. <br>
Mitigation: Check for secrets and sensitive files before running the skill, and limit use to repositories approved for agent analysis. <br>
Risk: Reset and loop/self-evolve modes can have high impact on local state and iterative workflows. <br>
Mitigation: Use disposable branches or worktrees, review proposed changes each cycle, and invoke reset or loop modes deliberately. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hsssgdtc/skills/ralph-evolver) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown/plain text evolution prompt with inline command and code guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local .ralph state and history files in the target project while preparing iterative improvement prompts.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
