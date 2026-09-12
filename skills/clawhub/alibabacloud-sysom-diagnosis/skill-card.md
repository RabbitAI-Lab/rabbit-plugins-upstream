## Description:

Troubleshoots Linux server performance and stability issues across CPU, memory, disk IO, network, and Java domains using SysOM diagnosis outputs, and surfaces recommendations without applying fixes automatically.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to diagnose Alibaba Cloud ECS Linux performance and stability incidents, route symptoms to the appropriate SysOM command, interpret returned diagnosis envelopes, and present evidence-based remediation targets.

### Deployment Geography for Use:

China Mainland and Hong Kong

## Known Risks and Mitigations:

Risk: The SysOM CLI installer is fetched and executed from a remote URL and may be run with elevated local privileges.

Mitigation: Inspect and verify the installer before use, and prefer the documented user-local install path over sudo where possible.

Risk: Alibaba Cloud credentials and backend-directed SysOM commands can carry significant cloud or diagnostic authority.

Mitigation: Use the skill only in an environment where those credentials and commands are appropriate, and confirm follow-up commands match the documented SysOM command inventory before execution.

Risk: Long-running Java profiling or collection commands can add runtime overhead or affect the target process during diagnosis.

Mitigation: Explain the expected duration and impact, obtain confirmation before running those commands, and avoid duplicate profiling runs after client timeouts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-sysom-diagnosis)
- [Supported Environments](references/supported-environments.md)
- [Deep Actions Reference](references/deep-actions.md)
- [Parameter Guide](references/parameter-guide.md)
- [RAM Policies](references/ram-policies.md)
- [Report Interpretation](references/report-interpretation.md)
- [Java Application Diagnosis Reference](references/java/README.md)
- [Java Profiling Playbook](references/java/memory/profiling-playbook.md)
- [SysOM CLI installer](https://sysom-prd-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/sysom_prd/skill_cli/install.sh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown diagnosis summaries with inline command references and concise remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not apply fixes automatically; may ask for confirmation before long-running, profiling, or sensitive diagnostic commands.]

## Skill Version(s):

0.0.7 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
