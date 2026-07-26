## Description: <br>
Architects, deploys, and optimizes AWS infrastructure while helping avoid cost overruns and security pitfalls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operations engineers, and independent builders use this skill to plan, operate, troubleshoot, and optimize AWS infrastructure with attention to security, cost, and deployment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-credentialed shell execution may create, modify, delete, or incur charges for AWS resources without clearly documented command boundaries. <br>
Mitigation: Use a constrained AWS account or profile, require explicit approval before resource-changing or cost-incurring commands, and review planned commands before execution. <br>
Risk: Broad production credentials could expose sensitive infrastructure before the publisher documents exact command boundaries and safeguards. <br>
Mitigation: Start with read-only or least-privilege credentials and avoid production accounts until command scope and safeguards are reviewed. <br>


## Reference(s): <br>
- [ClawHub Aws skill page](https://clawhub.ai/thcjp/skills/aws) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured JSON examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require AWS credentials, cloud connectivity, and user approval before resource-changing or cost-incurring commands.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
