## Description: <br>
Guides agents through real UCloud resource operations with the official ucloud CLI, including inspection, creation, updates, deletion, and web application deployment workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ucloud](https://clawhub.ai/user/ucloud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect, configure, and change UCloud resources through the official CLI. It is also used to plan and execute UCloud deployment workflows while checking the active profile, project, region, required parameters, and API fallback path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make real UCloud account changes from broad deployment requests. <br>
Mitigation: Confirm the intended profile, project, region, target resources, and billing impact before changes; prefer read-only checks first and show the exact product command or API action before write or delete operations. <br>
Risk: Credentials, tokens, or generated login material could be exposed in chat, command previews, or logs. <br>
Mitigation: Use existing profiles or OAuth where possible, redact keys and tokens, avoid placing real AK/SK values or passwords in commands or summaries, and rotate any credential that appears in a transcript. <br>


## Reference(s): <br>
- [UCloud CLI Usage](references/cli-usage.md) <br>
- [UCloud Documentation Sources](references/doc-sources.md) <br>
- [UCloud Deployment Defaults](references/deployment.md) <br>
- [UCloud CLI Quickstart](https://docs.ucloud.cn/cli/intro) <br>
- [UCloud CLI Repository](https://github.com/ucloud/ucloud-cli) <br>
- [UCloud API Documentation](https://github.com/UCloudDoc-Team/api) <br>
- [UCloud Product Documentation](https://docs.ucloud.cn/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with CLI command examples and concise tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include UCloud CLI commands, API payload guidance, profile selection notes, and redacted credential handling guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
