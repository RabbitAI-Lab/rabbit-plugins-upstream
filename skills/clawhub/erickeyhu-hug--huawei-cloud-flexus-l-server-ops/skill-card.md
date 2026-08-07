## Description: <br>
Based on Huawei Cloud Flexus L API for instance management and operations, this skill supports querying instance lists and details, querying traffic packages, batch start, stop, and reboot operations, password resets, and instance information updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and support engineers use this skill to inspect and operate Huawei Cloud Flexus L instances, including lifecycle actions, password resets, metadata updates, and traffic package checks. It is intended for account-scoped operational workflows that require explicit instance IDs, regions, and Huawei Cloud credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles powerful Huawei Cloud credentials and some instructions can expose secrets if copied into chat, command-line history, or logs. <br>
Mitigation: Use least-privilege, preferably temporary Huawei Cloud credentials; pass secrets through environment variables or secure secret handling; avoid printing credentials or running verification commands that echo environment values. <br>
Risk: Lifecycle and password reset actions can interrupt production workloads or lock out access when applied to the wrong instance. <br>
Mitigation: Require explicit Flexus L instance IDs, validate instance type and region before action, obtain confirmation for disruptive operations, and verify final status after lifecycle changes. <br>
Risk: IAM scope that is broader than the documented Flexus L, ECS, and BSS operations can increase blast radius if credentials are misused. <br>
Mitigation: Configure a custom least-privilege IAM policy for the documented ECS server and BSS resource usage actions, and review permissions before installing or using the skill. <br>


## Reference(s): <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Huawei Cloud Flexus Application Server L Instance Documentation](https://support.huaweicloud.com/intl/zh-cn/flexusl_faq/faq_01_0003.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and command output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include operational status, instance identifiers, traffic usage summaries, and error guidance; secrets should not be echoed or logged.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
