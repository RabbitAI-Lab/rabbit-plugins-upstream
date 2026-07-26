## Description: <br>
Cloud Ops Orchestrator gives agents Terraform and Ansible guidance for multi-cloud infrastructure workflows, including plan review, drift detection, credential separation, rollback, and guarded destruction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and operators use this skill to ask an agent for infrastructure-as-code workflows that separate Terraform resource lifecycle tasks from Ansible configuration tasks across AWS, GCP, and Azure. It is intended for planning, reviewing, and executing cloud operations with explicit confirmation gates for risky actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-assisted cloud operations can affect real infrastructure, including apply, destroy, override-lock, force, or credential-related commands. <br>
Mitigation: Before execution, verify the selected environment, cloud profile, Terraform state backend, and generated plan; require explicit confirmation for high-risk commands. <br>
Risk: A wrong profile, backend, or environment can cause changes to be planned or applied against the wrong cloud resources. <br>
Mitigation: Keep dev, staging, and prod separated by state backend and IAM role, and review plan output before apply or destroy. <br>
Risk: Credentials can be exposed if cloud secrets are placed in Terraform files or committed to source control. <br>
Mitigation: Use cloud profiles, environment injection, CI OIDC, or Vault-style secret retrieval, and keep state, local variable, and credential files out of version control. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/thcjp/skills/cloud-ops-orchestrator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell, JSON, YAML, and HCL examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Terraform, Ansible, cloud CLI, policy, and environment-isolation guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
