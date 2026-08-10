## Description:

Runs a CCPA/CPRA compliance audit covering 20 core items and can produce scored text, JSON, or HTML reports through the CQDev cloud compliance engine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Privacy and compliance teams, developers, and agents use this skill to preview CCPA/CPRA audit checks, collect pass/fail answers, and generate a compliance report. Scored audits use the CQDev cloud service at compliancehub.cn and require an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored audits send audit answers to compliancehub.cn and use an API key.

Mitigation: Run scored audits only when the user trusts CQDev/compliancehub.cn with the answers, and confirm the destination before sending data.

Risk: The inspected preview path can attempt a cloud request before displaying preview output.

Mitigation: Block network access or run in a restricted environment when a local-only preview is required.

Risk: The optional login flow handles account passwords and writes a persisted API key.

Mitigation: Use --login only with explicit user consent, prefer environment-provided keys when appropriate, and protect or rotate stored keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/ccpa-audit)
- [ComplianceHub account page for ccpa-audit](https://compliancehub.cn/account.html?skill=ccpa-audit)
- [ComplianceHub service endpoint](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; runtime reports can be text, JSON, or HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses COMPLIANCEHUB_API_KEY or a user-created key file for scored audits; preview and scored runs may contact compliancehub.cn.]

## Skill Version(s):

1.0.6 (source: server release evidence, package.json, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
