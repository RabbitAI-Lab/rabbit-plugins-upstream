## Description: <br>
Provides a one-page company snapshot covering market quote, identity, valuation, and growth signals, with guidance to use companion skills for deep research or peer comparisons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jerryzhou](https://clawhub.ai/user/jerryzhou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill to answer lightweight company and stock questions such as current price, one-page fundamentals, valuation, growth, shareholder, and batch comparison snapshots. For deep business analysis, industry structure, or long-form investment research, the skill directs the agent to companion analysis or industry-member skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market and fundamentals snapshots can be stale, incomplete, or unsuitable as the sole basis for financial decisions. <br>
Mitigation: Review returned freshness fields and source deeplinks, then corroborate important figures before relying on them for investment or financial decisions. <br>
Risk: The skill is scoped to a lightweight company card and can mislead users if treated as deep company, peer, or industry analysis. <br>
Mitigation: Route deep business analysis, peer comparisons, and industry-structure questions to the companion skills named in the artifact, and label key numbers with the source skill and returned deeplinks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jerryzhou/skills/wm-company-card) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [Structured JSON with optional markdown deeplinks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports single-symbol and batch requests up to 50 symbols; returned freshness fields indicate quote and report dates.] <br>

## Skill Version(s): <br>
1.2.9 (source: SKILL.md frontmatter, manifest.json, evidence release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
