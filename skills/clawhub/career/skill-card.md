## Description: <br>
Advises users on career decisions including offer evaluation, salary and equity negotiation, promotions, pivots, and layoff response. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, job seekers, and career coaches use this skill to evaluate offers, compare compensation and equity, plan promotion or pivot strategies, and respond to layoffs, PIPs, firing, rescinded offers, or recruiter outreach while keeping the human user in control of decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may store privacy-sensitive career data, including compensation, constraints, values, visa-related status, targets, and coaching preferences, under ~/Clawic/data/career/. <br>
Mitigation: Install only when local career-profile retention is acceptable, and review or delete files under ~/Clawic/data/career/ when that history should not be retained. <br>
Risk: Career recommendations may touch compensation, tax, employment-law, visa, severance, or non-compete questions that depend on jurisdiction and user-specific documents. <br>
Mitigation: Use the skill as decision support, verify jurisdiction-specific legal, tax, and immigration questions with qualified professionals, and ground recommendations in user-provided written offer, equity, severance, or contract terms. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/career) <br>
- [Clawic Career Skill Homepage](https://clawic.com/skills/career) <br>
- [Career Skill Definition](artifact/SKILL.md) <br>
- [Setup](artifact/setup.md) <br>
- [Memory Template](artifact/memory-template.md) <br>
- [Offers](artifact/offers.md) <br>
- [Equity And Comp Math](artifact/equity.md) <br>
- [Market Position](artifact/market.md) <br>
- [Promotion](artifact/promotion.md) <br>
- [Pivots](artifact/pivots.md) <br>
- [Layoffs, Firings, And PIPs](artifact/layoffs.md) <br>
- [Executive Moves](artifact/executive.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with structured decision frameworks and local profile update instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local career profile files under ~/Clawic/data/career/ when the user provides career facts or preferences.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
