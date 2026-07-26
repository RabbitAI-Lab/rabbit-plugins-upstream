## Description: <br>
Provides entry-level cloud architecture guidance for AWS, Azure, and GCP service selection, migration strategy, cost optimization, basic security, compliance, and infrastructure-as-code planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and cloud practitioners use this skill to draft single-cloud architecture plans, choose core cloud services, evaluate 6Rs migration options, and produce basic cost, security, and IaC guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill's examples can read live AWS account cost, inventory, and utilization data. <br>
Mitigation: Use the skill for architecture advice only unless you intentionally approve the exact command, cloud account, region, and data being accessed. <br>
Risk: Callback URLs can send results to an external destination. <br>
Mitigation: Avoid callback_url unless the destination is trusted and the data being sent is appropriate for that endpoint. <br>


## Reference(s): <br>
- [Cloud Architect Free on ClawHub](https://clawhub.ai/thcjp/skills/cloud-architect-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with architecture recommendations, service-selection rationale, Terraform examples, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include executable AWS CLI or Terraform examples; review commands, account, region, and accessed data before running them.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
