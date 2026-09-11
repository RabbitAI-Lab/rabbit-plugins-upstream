## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and their agents use this skill to work with an authenticated Candor financial workspace: review accounts, spending, recurring bills, cashflow, investments, debt, benefits, tax-preparation evidence, goals, and follow-up. It supports bounded record maintenance and reversible workspace writebacks while leaving external financial actions to separate user authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive financial workspace data and make bounded reversible updates to Candor records.

Mitigation: Install only for agents that should access the user's Candor financial workspace, and review requests that could update notes, transaction corrections, rules, imports, budgets, goals, or other records.

Risk: Incomplete or stale account coverage can make financial conclusions misleading.

Mitigation: Check coverage, freshness, caveats, provenance, currency, and observation dates before making claims, and state practical limits when records cannot answer a material question.

Risk: Background monitoring can create unwanted recurring financial review activity.

Mitigation: Enable monitoring only after an explicit cadence choice, use one stable scheduled job, and notify the user only when attention, input, or authority is needed.

Risk: External financial actions such as payments, transfers, purchases, cancellations, applications, elections, filings, trades, messages, and professional engagements may exceed the skill's workspace authority.

Mitigation: Treat those actions as separate consent moments and recover or ask for explicit authority before proceeding.

## Reference(s):

- [Candor Start](https://candor.money/START.md)
- [ClawHub skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Quiet monitoring recipes](references/monitoring.md)
- [Insurance and plan-year workflows](methods/candor-insurance-plan-year/references/workflows.md)
- [Workplace-retirement workflows](methods/candor-workplace-retirement/references/workflows.md)
- [Portfolio and fee workflows](methods/candor-portfolio-fees/references/workflows.md)
- [FSA, HSA, and benefits workflows](methods/candor-benefits-fsa-hsa/references/workflows.md)
- [Budgeting and cash-flow workflows](methods/candor-budgeting-cashflow/references/workflows.md)
- [Cash, liquidity, and yield workflows](methods/candor-cash-liquidity-yield/references/workflows.md)
- [Income-integrity workflows](methods/candor-income-integrity/references/workflows.md)
- [Transaction-organization workflows](methods/candor-transaction-organization/references/workflows.md)
- [Credit-health workflows](methods/candor-credit-health/references/workflows.md)
- [Tax-preparation workflows](methods/candor-tax-preparation/references/workflows.md)
- [Credit-card rewards workflows](methods/candor-card-rewards/references/workflows.md)
- [Vault-gardening workflows](methods/candor-vault-gardening/references/workflows.md)
- [Goal and scenario workflows](methods/candor-goals-scenario-planning/references/workflows.md)
- [Money-recovery workflows](methods/candor-money-recovery/references/workflows.md)
- [Evidence-capture workflows](methods/candor-evidence-capture/references/workflows.md)
- [Trial-watchdog workflows](methods/candor-trial-watchdog/references/workflows.md)
- [Financial-review workflows](methods/candor-financial-review/references/workflows.md)
- [Cashflow-projection workflows](methods/candor-cashflow-projection/references/workflows.md)
- [Debt promotional-rate workflows](methods/candor-debt-promotional-rates/references/workflows.md)
- [Recurring-bill workflows](methods/candor-recurring-bills/references/workflows.md)
- [Spare-cash-allocation workflows](methods/candor-spare-cash-allocation/references/workflows.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell command recipes, financial findings, record links, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded Candor query instructions, exact amounts and dates, caveats, follow-up notes, and reversible workspace writeback guidance.]

## Skill Version(s):

0.1.77 (source: server release metadata; artifact frontmatter metadata.version is 0.1.0 and candor-skill-version is 2026-09-10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
