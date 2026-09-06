## Description:

Use when the user asks to analyze, consult, setup, manage, configure, or design a Volcengine Landing Zone, including organization, accounts, finance, identity, cloudtrail, or network infrastructure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud platform engineers and operations teams use this skill to plan, set up, and manage Volcengine landing-zone foundations across organization structure, account finance relationships, identity, centralized logging, networking, account creation, and baseline application.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact cloud operations across Volcengine organization, account, identity, logging, and network resources.

Mitigation: Install it only for Volcengine landing-zone operation, use least-privileged credentials for the selected phase, review confirmations carefully, and verify account and region targets before approving writes.

Risk: Workspace outputs may include sensitive administrator login information and initial password material.

Mitigation: Treat generated workspace outputs as sensitive until the password is changed and the files are removed or otherwise secured.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/volc-sdk-team/skills/volcengine-landing-zone)
- [Volcengine Landing Zone Setup Guide](references/landing-zone-setup/guidebook.md)
- [Preflight Checks](references/preflight-checks.md)
- [Account Factory Workflow](references/account-factory/guidebook.md)
- [Failure Recovery](references/failure-recovery.md)
- [Account Factory Baseline Schema](references/account-factory/baseline.schema.json)
- [Volcengine CLI README](https://github.com/volcengine/volcengine-cli/blob/master/README.MD)
- [Volcengine Terraform Provider README](https://github.com/volcengine/terraform-provider-volcenginecc)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, generated workspace files, and HTML report artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce workspace-local execution files, login information, status artifacts, and summary reports during approved workflows.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
