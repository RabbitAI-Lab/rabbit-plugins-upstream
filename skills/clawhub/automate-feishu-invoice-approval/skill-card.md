## Description: <br>
Scaffolds, configures, validates, runs, and maintains a Feishu/Lark invoice approval bot that uses Codex vision, validates buyer headers, selects expense categories, drafts approval reasons, sends uploader confirmation cards, and submits only after confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wuhaorui](https://clawhub.ai/user/wuhaorui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to build or troubleshoot Feishu invoice-to-approval workflows, approval form mappings, dry-run tests, confirmation-card callbacks, and duplicate protection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated bot handles sensitive invoice images, extracted invoice JSON, sender open IDs, approval payloads, SQLite records, and approval instance codes. <br>
Mitigation: Install only where the Feishu bot is authorized for invoice messages and approvals, restrict Feishu app permissions, protect the local data directory, and define an approved retention policy. <br>
Risk: A misconfigured deployment can create real approval requests or use stale approval widget and option IDs. <br>
Mitigation: Keep dry-run enabled through initial testing and approval-form changes, validate mappings and tests, and disable dry-run only after explicit user authorization. <br>
Risk: Broader-than-needed bot access can expose invoice workflow data to unintended users or actions. <br>
Mitigation: Use the optional uploader allowlist when needed, keep the confirmation gate, and accept card actions only from the original uploader. <br>


## Reference(s): <br>
- [Setup reference](references/setup.md) <br>
- [Operations reference](references/operations.md) <br>
- [ClawHub skill page](https://clawhub.ai/wuhaorui/skills/automate-feishu-invoice-approval) <br>
- [Publisher profile](https://clawhub.ai/user/wuhaorui) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a Python service scaffold, example configuration, JSON schema, tests, validation commands, and operational guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
