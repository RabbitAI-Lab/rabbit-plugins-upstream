## Description: <br>
Create and configure scheduled TIMER triggers for Huawei Cloud FunctionGraph functions using Quartz Cron expressions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to create, configure, and verify scheduled TIMER triggers for existing Huawei Cloud FunctionGraph functions. It supports Quartz Cron and fixed-rate schedules for periodic jobs such as backups, monitoring, notifications, and data processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Huawei Cloud access keys and secret keys are required for trigger creation and verification. <br>
Mitigation: Use temporary or least-privilege credentials, keep secrets in environment variables, avoid printing them, and rotate credentials after testing or automation changes. <br>
Risk: Creating or changing scheduled triggers can alter production function execution frequency and cost. <br>
Mitigation: Confirm the function URN, region, trigger name, schedule, and enable status before execution; test with DISABLED status or non-production functions before enabling production schedules. <br>
Risk: Troubleshooting guidance includes disabling SSL verification, which can weaken transport security. <br>
Mitigation: Keep SSL verification enabled for normal use and resolve certificate issues through trusted certificate configuration instead of disabling verification. <br>


## Reference(s): <br>
- [SDK Installation Guide](references/sdk-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Cron Expression Reference](references/cron-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Python SDK command examples, trigger configuration values, verification steps, and success or error response JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
