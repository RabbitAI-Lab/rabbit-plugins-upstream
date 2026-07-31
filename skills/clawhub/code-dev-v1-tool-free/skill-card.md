## Description: <br>
A structured coding workflow skill for personal developers that guides planning, implementation, verification, testing, checkpoint tracking, and explicit preference memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to structure personal software work into request, planning, execution, verification, and delivery steps with checkpoints and optional local preference memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates through normal coding-assistant permissions, so proposed commands or file changes can affect the local project or workspace. <br>
Mitigation: Install only in an agent environment where those permissions are acceptable, keep work scoped to the intended project or ~/code workspace, and review commands before execution. <br>
Risk: Markdown boundary statements do not provide a technical sandbox. <br>
Mitigation: Rely on the agent platform and workspace permissions for enforcement rather than on the skill text alone. <br>
Risk: Generated development plans, checkpoints, and quality reports may be incomplete or misleading. <br>
Mitigation: Review generated guidance and verify code with the relevant tests, linting, type checks, and human review before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-dev-v1-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline text, bash commands, tables, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local preference and checkpoint files when the user asks the agent to do so.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
