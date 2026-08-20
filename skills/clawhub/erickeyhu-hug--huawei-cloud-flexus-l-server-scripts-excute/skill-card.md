## Description: <br>
Based on Huawei Cloud COC (Cloud Operations Center) APIs for script management and remote execution. Supports creating custom scripts (Shell, Python, Bat) and batch execution on target host instances via UniAgent. Applicable to cloud operations automation and batch script deployment scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to create, list, inspect, execute, and query Huawei Cloud COC scripts for Flexus L instances. It supports operational automation such as batch deployment, log cleanup, backup scripts, health checks, and emergency response tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Privileged remote script execution on Huawei Cloud hosts can cause unintended system changes if the wrong script, instance, region, or execution user is selected. <br>
Mitigation: Review each script UUID, target instance resource ID, region, execution user, timeout, success rate, and rotation strategy before execution; test first on a single non-production instance and avoid root unless required. <br>
Risk: Credential exposure can occur when AK/SK/token values are supplied on the command line or shared in prompts and logs. <br>
Mitigation: Prefer environment variables or temporary credentials, avoid placing credentials in command history or conversation text, rotate keys regularly, and scope IAM permissions narrowly to the required COC actions. <br>
Risk: Under-scoped safety controls may permit broader script management or execution access than intended. <br>
Mitigation: Use a narrowly scoped IAM role for the required script and execution operations, verify permissions before batch use, and avoid broad administrator policies unless explicitly needed. <br>


## Reference(s): <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Huawei Cloud COC SDK package](https://pypi.org/project/huaweicloudsdkcoc/) <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-flexus-l-server-scripts-excute) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, API Calls, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI or JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Huawei Cloud credentials, COC script identifiers, target Flexus L instance resource IDs, regions, execution user, timeout, success rate, and rotation strategy.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and scripts/pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
