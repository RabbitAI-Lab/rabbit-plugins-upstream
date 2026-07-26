## Description: <br>
Helps agents provide basic AWS architecture design, service selection, read-only resource inventory, and cost optimization guidance for prototype and early-growth workloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and independent builders use this skill to choose basic AWS MVP or growth-stage services, inventory existing VPC/EC2/RDS resources, and identify common cost pitfalls. It is not intended for deep security hardening, enterprise compliance review, migration planning, or IaC generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AWS command examples can create, modify, or delete real cloud resources even though the skill advertises read-only help. <br>
Mitigation: Require explicit human approval before executing any AWS CLI command, and prefer dry-run or review-only use for provisioning examples. <br>
Risk: Commands run against a production AWS account could introduce unplanned cost or security exposure. <br>
Mitigation: Use a least-privilege profile or sandbox account, verify the active account and Region first, and restrict automatic execution of modifying commands. <br>


## Reference(s): <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aws-cloud-architect-free) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown, text] <br>
**Output Format:** [Markdown guidance with AWS CLI command examples and optional JSON-shaped result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include read-only inventory commands, architecture recommendations, cost notes, and examples that require explicit human approval before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
