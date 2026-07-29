## Description: <br>
Money helps an agent prioritize personal-finance decisions such as debt payoff, emergency funds, savings, affordability, retirement readiness, shocks, windfalls, and fee or fraud review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill for personal-finance triage and planning: allocating the next unit of money, sizing buffers and goals, reviewing debt, housing, insurance, taxes, investing, retirement, shocks, windfalls, and recording durable decisions in local notes. It advises and writes plans or records; it does not move money, open accounts, transact, or fill forms. <br>

### Deployment Geography for Use: <br>
Global; country-specific financial, tax, benefit, and consumer-protection guidance depends on the user's jurisdiction. <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to read and modify sensitive local financial records, including balances, rates, goals, decisions, reviews, tax notes, fraud notes, and related contacts. <br>
Mitigation: Install it only when local personal-finance record keeping is desired, keep backups of the Clawic data folders, and review announced writes to confirm they belong in the stated local files. <br>
Risk: The skill persists financial records without separate confirmation for each write. <br>
Mitigation: Run it in a workspace where durable local notes are expected, and audit the configured paths before using it with real financial information. <br>
Risk: Financial, tax, benefit, and consumer-protection guidance can be jurisdiction-specific and high impact. <br>
Mitigation: Confirm the user's jurisdiction before applying country-specific rules, and route regulated, legal, tax, debt-relief, cross-border, or unusually large decisions to a qualified professional. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/money) <br>
- [Publisher Profile](https://clawhub.ai/user/ivangdavila) <br>
- [Money Homepage](https://clawic.com/skills/money) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Working File Templates](artifact/memory-template.md) <br>
- [Debt](artifact/debt.md) <br>
- [Budget](artifact/budget.md) <br>
- [Investing](artifact/investing.md) <br>
- [Taxes](artifact/taxes.md) <br>
- [Scams, Fees, and Bad Products](artifact/scams.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Files] <br>
**Output Format:** [Markdown narrative with tables and local plain-text note updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and write local Clawic data files; does not move money or store credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
