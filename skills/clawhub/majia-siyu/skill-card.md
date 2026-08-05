## Description:

A Chinese-language private-domain operations assistant for routing and producing WeChat private-domain content, outreach scripts, vendor research snapshots, diagnosis, reports, and local client records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

External operators, consultants, and business teams use this skill to plan and execute Chinese private-domain operations, including WeChat Moments copy, group messages, welcome scripts, vendor research, operational diagnosis, and client follow-up records. It is intended to route a user's current business problem to the most relevant private-domain workflow and produce practical Chinese-language deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Client consultation notes may contain sensitive business or personal information and can be stored as local plaintext under ~/.siyu/.

Mitigation: Avoid saving secrets or regulated personal data, obtain appropriate consent before storing client details, redact sensitive content before saving, and protect local files with the user's normal device and filesystem controls.

Risk: Vendor, product, price, policy, platform-rule, and company-status guidance can become misleading if it is not current.

Mitigation: Use the skill's market-research workflow to collect dated source links and verification status before analysis; when network access is unavailable, provide only a research framework rather than concrete vendor or price recommendations.

Risk: Some workflows can run local compliance-check commands or update the skill package when explicitly invoked.

Mitigation: Review commands before execution, install or update only from the trusted release source, and avoid running update workflows when local policy requires pinned packages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-siyu)
- [Project README and source](https://github.com/maojiebc/majia-siyu-team)
- [Version history](https://github.com/maojiebc/majia-siyu-team/releases)
- [新手教程](references/新手教程.md)
- [整盘怎么搭-老板版](references/整盘怎么搭-老板版.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese-language Markdown, plain text, tables, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write and read local plaintext client archives under ~/.siyu/ when save, restore, or report modules are invoked.]

## Skill Version(s):

1.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
