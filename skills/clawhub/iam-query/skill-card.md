## Description: <br>
Queries Huawei Cloud IAM resources through read-only Python SDK scripts, covering users, groups, policies, agencies, access keys, MFA devices, login and password policies, compliance settings, and quotas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[changhui123456](https://clawhub.ai/user/changhui123456) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and security reviewers use this skill to inventory Huawei Cloud IAM identities, policies, access keys, MFA devices, agencies, and related account security settings before automation, audit, or permission review work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup and SDK configuration weaken TLS verification while the skill handles Huawei Cloud credentials. <br>
Mitigation: Run the skill only in an isolated environment with temporary or least-privilege Huawei Cloud credentials, and avoid sensitive production accounts unless the TLS-verification bypass has been reviewed and accepted. <br>
Risk: The environment setup can install or upgrade Python dependencies from package indexes before queries run. <br>
Mitigation: Review the setup scripts before installation, run them in the skill-created virtual environment, and pin or pre-approve dependency versions for controlled deployments. <br>
Risk: Query output can expose IAM users, access keys, MFA status, policy bindings, tokens, and identity-provider metadata. <br>
Mitigation: Do not share or persist raw query output unless it is redacted and stored according to the organization's secrets and identity-data handling rules. <br>


## Reference(s): <br>
- [IAM Python Script Usage Guide](references/iam/guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and structured query results from Python scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Huawei Cloud credential environment variables and can return sensitive IAM identity, access-key, MFA, policy, and agency metadata.] <br>

## Skill Version(s): <br>
1.1.100 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
