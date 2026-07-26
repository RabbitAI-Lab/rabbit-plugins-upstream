## Description: <br>
Automates an end-to-end requirement or defect delivery workflow from PingCode intake through preparation, development, submission, verification, delivery reporting, and REDoc synchronization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[insistcp](https://clawhub.ai/user/insistcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and delivery engineers use this skill to coordinate a complete software delivery flow for a PingCode work item or a natural-language requirement, including branch work, MR creation, testing, deployment checks, merge gates, and traceable reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install or upgrade CLIs and other skills, changing the local development environment. <br>
Mitigation: Run it only in a controlled work environment and require explicit approval before installing or upgrading tools. <br>
Risk: The workflow can create or update external project records, including PingCode subtasks, MRs, test submissions, and status transitions. <br>
Mitigation: Require approval before external work item creation, MR creation, test submission changes, and live endpoint calls. <br>
Risk: The workflow can push code, trigger CI, approve or merge MRs, and synchronize reports to REDoc. <br>
Mitigation: Keep explicit human gates before pushes, CI deployment, merge operations, and external report uploads; review generated reports before publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/insistcp/skills/e2e-delivery) <br>
- [Environment precheck](artifact/references/env-precheck.md) <br>
- [Five-phase execution flow](artifact/references/flow.md) <br>
- [Report template and generation rules](artifact/references/report-template.md) <br>
- [Session schema](artifact/references/session-schema.md) <br>
- [Troubleshooting](artifact/references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, shell commands, JSON session records, and local Markdown reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes session state under ~/.claude/e2e-sessions and delivery reports under docs/e2e-reports or ~/.claude/e2e-reports; can also synchronize reports to REDoc.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
