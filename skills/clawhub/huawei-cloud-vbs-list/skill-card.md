## Description: <br>
Query Huawei Cloud VBS/CBR backup inventory, list backups in a project, and filter results by status, name, resource type, vault, availability zone, resource ID, or time range. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and support engineers use this skill to inspect Huawei Cloud backup inventory for daily checks, troubleshooting, and filtered lookup of VBS backups now managed through CBR. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill queries cloud backup inventory and depends on Huawei Cloud credentials. <br>
Mitigation: Use a least-privilege IAM user with cbr:backups:list and do not paste AK/SK values into chat. <br>
Risk: Installing the Huawei Cloud CLI from a remote script can introduce supply-chain risk. <br>
Mitigation: Verify the hcloud installer source from Huawei before running it. <br>
Risk: Using legacy VBS commands or missing region parameters can produce incorrect or failed backup queries. <br>
Mitigation: Use CBR ListBackups with an explicit --cli-region value and validate results with the provided verification method. <br>


## Reference(s): <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [CLI Installation and Authentication Guide](references/cli-installation-guide.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-vbs-list) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON-oriented CLI output, and summarized text tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Huawei Cloud CBR/VBS listing; confirms region and filters before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
