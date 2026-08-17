## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor financial workspace, review personal financial records, maintain approved budgets and goals, investigate savings or recovery opportunities, and preserve evidence-backed follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill works with sensitive personal-finance records through an authenticated Candor workspace.

Mitigation: Install only when that access is acceptable, use Candor's secure account and payment pages, and do not ask users to paste credentials, payment details, or verification codes into chat.

Risk: Internal Candor record writebacks or bulk transaction rules could change how financial records are organized.

Mitigation: Keep changes bounded and reversible, review previews for bulk rules, and require recoverable user authority for broad, value-laden, or conflicting changes.

Risk: Background monitoring can create recurring financial checks.

Mitigation: Enable monitoring only after the user explicitly accepts a cadence and purpose, configure one stable scheduler job, and contact the user only when attention is needed.

Risk: Financial conclusions can be misleading when coverage, freshness, rates, terms, or external rules are incomplete.

Mitigation: Check coverage and freshness, use current authoritative sources for external rates and rules, state practical limits, and stop before unsupported conclusions or external financial actions.

## Reference(s):

- [Candor setup and OpenClaw materials](https://candor.money/START.md?v=0.1.28)
- [Quiet monitoring recipes](references/monitoring.md)
- [ClawHub skill page](https://clawhub.ai/candor/skills/candor-finance)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell command recipes and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and Candor CLI >=0.3.64 <0.4.0; workspace changes are bounded by the user's authority and harness policy.]

## Skill Version(s):

0.1.28 (source: ClawHub release metadata; artifact frontmatter metadata.version is 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
