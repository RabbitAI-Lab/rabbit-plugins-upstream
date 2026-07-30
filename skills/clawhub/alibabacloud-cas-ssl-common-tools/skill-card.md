## Description: <br>
SSL certificate toolkit for Alibaba Cloud CAS covering identity configuration, domain verification, certificate download and upload, CSR generation, format conversion, and certificate matching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to manage Alibaba Cloud CAS SSL certificate lifecycle tasks, including credential profile setup, DNS or HTTP domain validation, certificate export and import, local format conversion, and key-certificate matching. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad Alibaba Cloud CAS, DNS, RAM, CLI/plugin update, and private-key handling actions. <br>
Mitigation: Use a dedicated least-privilege RAM role, review CLI/plugin updates before allowing them, and keep certificate private keys and PFX/JKS passwords out of chat, logs, and unencrypted storage. <br>
Risk: Certificate and DNS operations can affect production TLS availability and domain validation. <br>
Mitigation: Confirm user intent and all user-customizable parameters before API calls, and review generated commands before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-cas-ssl-common-tools) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Identity Resolver Commands](references/identity-resolver-commands.md) <br>
- [Domain Verify Commands](references/domain-verify-commands.md) <br>
- [Certificate Download Commands](references/cert-download-commands.md) <br>
- [Certificate Upload Commands](references/cert-upload-commands.md) <br>
- [RAM Policies](references/ram-policies.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, environment exports, policy JSON, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local certificate processing commands and file paths; private keys and export passwords must be handled as secrets.] <br>

## Skill Version(s): <br>
0.0.1-beta.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
