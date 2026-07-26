## Description: <br>
Automation Workflow Builder designs and runs cross-platform automation workflows with triggers, conditional logic, and multi-step actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evezart](https://clawhub.ai/user/evezart) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and business users can use this skill to design workflow automations for data synchronization, content publishing, report generation, monitoring alerts, customer service, and project status updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad file, network, command, and messaging capabilities can affect local files, external services, published content, or notifications if a workflow is not reviewed first. <br>
Mitigation: Review each workflow before it runs, restrict the skill to trusted folders and destinations, and require confirmation before command execution, file moves or deletes, uploads, publishing, or message sending. <br>
Risk: Cron and webhook workflows can run unattended before their behavior is fully tested. <br>
Mitigation: Test workflows in a safe directory first and avoid unattended cron or webhook operation until scope, approvals, and rollback expectations are clear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/evezart/automation-workflow-builder) <br>
- [Publisher profile](https://clawhub.ai/user/evezart) <br>
- [CHANGELOG.md](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Code, Shell commands] <br>
**Output Format:** [Markdown with workflow examples, configuration snippets, and command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute workflows that read and write files, call network endpoints, run commands, and send notifications.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, CHANGELOG.md, artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
