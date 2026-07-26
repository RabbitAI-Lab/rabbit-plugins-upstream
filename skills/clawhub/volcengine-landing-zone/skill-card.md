## Description: <br>
Use when the user asks to analyze, consult, setup, manage, configure, or design a Volcengine Landing Zone, including organization, accounts, finance, identity, cloudtrail, or network infrastructure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to design, prepare, and execute Volcengine Landing Zone workflows for organization, account setup, finance, identity, logging, networking, account baselines, and failure recovery. It supports both read-only consulting and confirmed cloud changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform cloud account, billing, identity, logging, and network changes. <br>
Mitigation: Proceed only after reviewing phase impact summaries and giving explicit confirmation for each write phase. <br>
Risk: The workflow may save a newly generated administrator password or login information into a local Markdown file. <br>
Mitigation: Keep the workspace private, do not commit or share generated output files, rotate the initial password immediately after first login, and delete the password file when it is no longer needed. <br>
Risk: Cloud credentials are required for Volcengine CLI and Terraform operations. <br>
Mitigation: Use the selected supported credential path, keep secrets out of chat and repository files, and refresh or rotate credentials if preflight reports missing, expired, or invalid authentication. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/volc-sdk-team/skills/volcengine-landing-zone) <br>
- [Display Protocol](references/display-protocol.md) <br>
- [Preflight Checks](references/preflight-checks.md) <br>
- [Landing Zone Setup Guide](references/landing-zone-setup/guidebook.md) <br>
- [Account Factory Workflow](references/account-factory/guidebook.md) <br>
- [Failure Recovery Workflow](references/failure-recovery.md) <br>
- [Account Factory Baseline Schema](references/account-factory/baseline.schema.json) <br>
- [Volcengine CLI README](https://github.com/volcengine/volcengine-cli/blob/master/README.MD) <br>
- [Volcengine Terraform Provider README](https://github.com/volcengine/terraform-provider-volcenginecc) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown responses with shell commands, configuration snippets, JSON/Terraform files, and local HTML or Markdown review artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cloud-changing actions are gated by explicit confirmations; sensitive outputs are handled as local files rather than pasted into chat.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.8.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
