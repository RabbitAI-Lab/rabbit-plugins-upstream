## Description: <br>
Money helps agents give sequenced personal-finance guidance for debt payoff, emergency funds, budgeting, investing readiness, retirement, housing, insurance, taxes, windfalls, shocks, and scam or adviser checks while recording durable decisions in local Clawic files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their agents use Money to decide where the next unit of money should go, produce payoff, savings, coverage, retirement, housing, tax, windfall, and crisis decisions with numbers and dates, and preserve durable finance records for later sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and updates sensitive local finance, money, contact, and project records. <br>
Mitigation: Install only if this local-file access is acceptable, and require the agent to preview and confirm every persistent write or deletion. <br>
Risk: Personal-finance and tax guidance can be jurisdiction dependent or unsuitable for complex situations. <br>
Mitigation: Require the skill to state jurisdiction assumptions, avoid specific product or provider recommendations, and route red-flag cases to qualified professionals. <br>
Risk: Users may paste credentials or secret values while discussing financial accounts. <br>
Mitigation: Preserve the artifact rule that credentials are never written under Clawic data paths; store only references such as keychain, 1Password, Bitwarden, vault, environment variable, or file pointers. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/money) <br>
- [Clawic Money Skill](https://clawic.com/skills/money) <br>
- [Skill Instructions](artifact/SKILL.md) <br>
- [Working File Templates](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown prose, tables, checklists, and local file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update local Clawic finance, contact, project, and memory files; does not move money, open accounts, transact, or submit forms.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
