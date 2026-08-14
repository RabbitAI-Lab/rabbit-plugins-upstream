## Description:

Provides a Chinese private-domain operations toolkit for WeChat and Enterprise WeChat workflows, including content planning, group messaging, welcome scripts, customer diagnosis, market research, compliance checks, and customer archive/report handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

External operators, consultants, and business teams use this skill to plan and review Chinese private-domain growth work, route requests to focused modules, draft operational materials, and manage follow-up customer records. It is especially oriented toward WeChat and Enterprise WeChat private-domain scenarios where current vendor, pricing, policy, or platform-rule claims must be verified before use.

### Deployment Geography for Use:

Global, with practical relevance to Chinese-language private-domain operations and WeChat or Enterprise WeChat workflows.

## Known Risks and Mitigations:

Risk: The skill may keep unencrypted customer archives and reports under ~/.siyu.

Mitigation: Use explicit save, restore, and report commands only when needed; redact sensitive customer data before saving; and review local file access controls before deployment.

Risk: Restore and report workflows can expose or reuse customer context too broadly.

Mitigation: Confirm the customer, scope, and intended recipient before restoring or sharing reports, and remove unrelated customer details from generated outputs.

Risk: Vendor, pricing, platform-rule, policy, feature, case-study, and company-status claims can become stale or incorrect.

Mitigation: Require current public-source verification with dates and links before using those claims, and mark unsupported facts as unverifiable rather than making recommendations from them.

Risk: Private-domain messaging and growth recommendations can create compliance risk if they overpromise outcomes or collect personal information without authorization.

Mitigation: Run compliance review before execution, avoid absolute claims, and remove unauthorized personal-data collection from scripts and campaign plans.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-siyu)
- [Project homepage](https://github.com/maojiebc/majia-siyu-team)
- [Release notes](https://github.com/maojiebc/majia-siyu-team/releases)
- [New user guide](references/新手教程.md)
- [Boss-level setup guide](references/整盘怎么搭-老板版.md)
- [Module index](modules/index.json)
- [Runtime route contract](modules/_runtime/route-contract.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured text with optional code, configuration, or shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local customer archives and reports when explicit save, restore, or report commands are used.]

## Skill Version(s):

1.4.2 (source: server release metadata, target metadata, and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
