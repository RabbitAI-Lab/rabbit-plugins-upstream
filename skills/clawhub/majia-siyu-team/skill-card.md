## Description:

A Chinese private-domain operations toolkit that routes users through WeChat content, group messaging, welcome scripts, compliance checks, market research, diagnostics, and local customer archive/report workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

External business operators, consultants, and marketing teams use this skill to plan and produce Chinese private-domain operations work, including WeChat moments posts, group broadcasts, welcome scripts, vendor research snapshots, diagnostics, and shareable reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local customer archives and reports can contain sensitive business or customer information in plaintext.

Mitigation: Use explicit save, restore, and report commands only when needed, avoid storing sensitive customer data unless local plaintext files are acceptable, and review reports before sharing.

Risk: Vendor, product, pricing, policy, platform-rule, and company-status guidance can become stale or unverifiable.

Mitigation: Use the market-research flow for these topics, require dated public sources for key claims, and provide only a research framework when current web verification is unavailable.

Risk: Generated private-domain operations materials may introduce compliance or overclaiming issues before deployment.

Mitigation: Run the bundled compliance checks and review customer-facing copy before publishing or sending it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-siyu-team)
- [Project homepage](https://github.com/maojiebc/majia-siyu-team)
- [GitHub releases](https://github.com/maojiebc/majia-siyu-team/releases)
- [README](README.md)
- [新手教程](references/新手教程.md)
- [整盘怎么搭-老板版](references/整盘怎么搭-老板版.md)
- [Module index](modules/index.json)
- [Knowledge manifest](modules/_knowledge/manifest.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance, structured checklists, shell commands, and local Markdown archive/report files when explicitly requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local plaintext customer archives and reports during save, restore, and report workflows.]

## Skill Version(s):

1.4.1 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
