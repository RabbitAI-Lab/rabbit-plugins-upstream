## Description: <br>
Openclaw Marshal helps agents define workspace security policies, audit installed skills against command, network, data-handling, and workspace hygiene rules, and generate compliance reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, security reviewers, and workspace administrators use this skill to establish local policy files, audit agent skills and workspace configuration, check individual skills, and produce audit-ready compliance status reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence marks the skill as suspicious because it has under-documented enforcement commands that can rename installed skills and replace policy files. <br>
Mitigation: Use audit, check, report, and status for read-focused review first; run enforce, protect, quarantine, or templates only after backing up the workspace and accepting the possible changes. <br>
Risk: Policy and template workflows can create or replace .marshal-policy.json, which may change how future audits and enforcement classify skills. <br>
Mitigation: Review the policy before and after changes, keep a backup of the existing policy, and confirm organization-specific allow, block, and review lists before relying on results. <br>
Risk: Compliance findings and recommendations can be incomplete or misleading if the policy does not match the workspace's actual security requirements. <br>
Mitigation: Treat generated reports as review inputs, customize the policy for the target environment, and have a human reviewer approve high-impact remediation decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/atlaspa/skills/openclaw-marshal) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Plain text and Markdown reports with JSON policy files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with python3; mutating commands can create or replace policy files and rename skills during quarantine workflows.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
