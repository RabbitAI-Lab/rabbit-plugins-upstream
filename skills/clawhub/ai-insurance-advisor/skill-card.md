## Description:

A Chinese-language insurance advisor for mainland China that helps users analyze coverage needs, compare products, estimate premiums, design insurance plans, review compliance topics, and draft insurance sales or training content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to plan personal or family insurance coverage, compare products, estimate premiums, and understand insurance concepts and compliance considerations. Insurance agents may also use it to draft social posts and training or sales scripts.

### Deployment Geography for Use:

China mainland

## Known Risks and Mitigations:

Risk: The skill may give high-impact insurance recommendations based on static or inconsistent product data.

Mitigation: Verify product availability, policy terms, premiums, and suitability with official insurer materials or licensed professionals before acting.

Risk: The skill processes sensitive family, income, budget, mortgage, health, and existing-coverage details.

Mitigation: Use only with data the user is comfortable sharing in the agent environment, and avoid retaining or redistributing personal details outside the insurance-planning task.

Risk: The skill can recommend sales contacts after plan design or product recommendations.

Mitigation: Treat sales contact information as a referral lead only and independently confirm licensing, jurisdiction, and product access.

Risk: Generated compliance and legal guidance may be incomplete or outdated.

Mitigation: Use the compliance content as a starting point and confirm regulatory obligations with qualified professionals or current official sources.

## Reference(s):

- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Compliance Reference](references/compliance.md)
- [Insurance Product Data](references/products.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese Markdown responses, JSON reports from local Python scripts, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product recommendations should include freshness and verification disclaimers; calculations and plans are advisory and require confirmation with licensed professionals or official insurer materials.]

## Skill Version(s):

2.0.77 (source: server release metadata; artifact frontmatter says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
