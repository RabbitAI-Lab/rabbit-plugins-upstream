## Description: <br>
Create and configure scheduled TIMER triggers for Huawei Cloud FunctionGraph functions using Quartz Cron expressions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to create, validate, and verify scheduled TIMER triggers for Huawei Cloud FunctionGraph functions using Cron or Rate schedules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Huawei Cloud credentials that can create or manage FunctionGraph triggers. <br>
Mitigation: Use a least-privilege test account first, keep credentials in environment variables, and avoid exposing real secrets in logged terminals. <br>
Risk: The skill can perform real cloud changes against the function URN and schedule provided by the user. <br>
Mitigation: Verify the function URN, trigger name, schedule, region, and project before execution, and start with a disabled or test trigger when practical. <br>
Risk: Troubleshooting guidance may weaken TLS if SSL verification is disabled with real credentials. <br>
Mitigation: Do not disable SSL verification for real credentials or production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-functiongraph-trigger-create) <br>
- [SDK Installation Guide](references/sdk-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Cron Expression Reference](references/cron-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Code, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces commands and scripts that can create real Huawei Cloud FunctionGraph TIMER triggers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
