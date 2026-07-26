## Description: <br>
Based on Huawei Cloud COC (Cloud Operations Center) APIs for script management and remote execution. Supports creating custom scripts (Shell, Python, Bat) and batch execution on target host instances via UniAgent. Applicable to cloud operations automation and batch script deployment scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to create, list, execute, and query Huawei Cloud COC scripts on Flexus L instances. It supports batch maintenance, deployment, health checks, and incident response workflows where remote scripts must be managed through Huawei Cloud APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run scripts on cloud servers through Huawei Cloud COC. <br>
Mitigation: Manually confirm the script UUID, target resource ID, region, execution user, and timeout before execution; test scripts on a single low-risk instance before batch use. <br>
Risk: The skill handles Huawei Cloud AK/SK credentials and optional security tokens. <br>
Mitigation: Use least-privilege temporary credentials, prefer environment variables or hidden interactive input, and avoid putting secrets in prompts, command lines, logs, or reusable scripts. <br>
Risk: Broad IAM permissions could allow script creation, deletion, and execution across target instances. <br>
Mitigation: Grant only the COC script and execution permissions needed for the intended workflow, and use executor-style permissions rather than administrator permissions when creation or deletion is unnecessary. <br>


## Reference(s): <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Huawei Cloud COC SDK on PyPI](https://pypi.org/project/huaweicloudsdkcoc/) <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-flexus-l-server-scripts-excute) <br>
- [Publisher profile](https://clawhub.ai/user/huaweiclouddev) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, text] <br>
**Output Format:** [Markdown with inline shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate Huawei Cloud COC API calls that create or execute scripts on target instances when the user supplies valid credentials and confirms target details.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and scripts/pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
