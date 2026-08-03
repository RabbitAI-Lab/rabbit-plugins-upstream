## Description: <br>
Helps agents architect, deploy, and optimize AWS infrastructure while watching for cost and security pitfalls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to plan, troubleshoot, and manage AWS infrastructure tasks, including deployment guidance, cost optimization, and security checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated plans or commands may create, resize, stop, delete, expose, or otherwise mutate AWS resources and can affect cost or availability. <br>
Mitigation: Use least-privilege IAM roles, start with read-only credentials where possible, and verify every command or deployment plan before execution. <br>
Risk: The skill requests command, file, and cloud credential authority for deployment work without clear built-in guardrails around mutating resources. <br>
Mitigation: Review the skill before installation, avoid broad production credentials, and monitor for operations that change resources or expose data. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with optional JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate deployment plans, configuration steps, and commands that require user review before use against real AWS accounts.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
