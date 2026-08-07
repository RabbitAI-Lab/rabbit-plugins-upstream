## Description: <br>
Provides temporary SSH remote connection for Huawei Cloud Ascend devices, with NPU monitoring, disk and LVM management, container management, security auditing, log analysis, and confirmation prompts for sensitive operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to connect to Huawei Cloud Ascend hosts over SSH, monitor NPU health, inspect disks and containers, and perform administrative troubleshooting. Use should be limited to trusted hosts and accounts with scoped privileges. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad remote administration capability over target hosts. <br>
Mitigation: Install only for trusted hosts, prefer a non-root account with tightly scoped sudo, and restrict SSH access to trusted networks. <br>
Risk: The security evidence says safety claims are not consistently enforced. <br>
Mitigation: Do not rely on confirmation prompts or command blocking as a complete safety control; review proposed commands before execution and use host-level permissions to limit impact. <br>
Risk: Password-based SSH use can expose credentials through command-line handling or weak authentication practices. <br>
Mitigation: Prefer SSH keys with strict host key verification, avoid passing passwords on the command line, and rotate credentials used during testing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ascend-remote-connect) <br>
- [IAM Permission Policy](references/iam-policies.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>
- [Verification Method](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style text with inline shell commands and remote command results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote command results may include target host, command, exit code, stdout, stderr, and duration.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
