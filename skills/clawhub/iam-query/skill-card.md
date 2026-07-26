## Description: <br>
iam-query uses read-only Huawei Cloud Python SDK scripts to query IAM users, groups, policies, agencies, access keys, MFA devices, security policies, compliance status, and account quotas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[changhui123456](https://clawhub.ai/user/changhui123456) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to inspect Huawei Cloud IAM identity, policy, credential, MFA, security, and quota information without creating, modifying, or deleting resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs local code execution, dependency installation, and persistent virtual environment creation during setup. <br>
Mitigation: Install in an isolated environment and review the setup scripts before allowing package installation or persistent files. <br>
Risk: The skill validates live Huawei Cloud credentials and the security guidance warns against using production AK/SK or bearer tokens. <br>
Mitigation: Use least-privilege, non-production, or temporary Huawei Cloud credentials and avoid exposing credential values in prompts or outputs. <br>
Risk: The security summary flags insecure network handling, and artifact code disables TLS certificate verification. <br>
Mitigation: Do not use the skill for sensitive environments until TLS verification is fixed and proxy settings are explicitly reviewed. <br>


## Reference(s): <br>
- [IAM script usage guide](references/iam/guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/changhui123456/skills/iam-query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and structured IAM query results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Query output depends on live Huawei Cloud IAM API responses and may include JSON-like or tabular fields depending on the script.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
