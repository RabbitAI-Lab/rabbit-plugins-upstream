## Description:

Creates Organization, Article, and FAQ JSON-LD from confirmed brand information and visible page text, then packages HTML snippets and local validation reports while checking question-and-answer pairing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site owners use the skill to prepare structured data from confirmed company information and visible page content, check the markup and FAQ pairing locally, and hand the HTML snippet to their website workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local validation pass could be mistaken for proof of factual accuracy or search eligibility.

Mitigation: Check claims against confirmed source material and use external validators when needed; the local report does not establish Google eligibility.

Risk: The optional aimeGeo follow-up may involve account access or publication actions.

Mitigation: Review the account access and publication actions before authorizing that follow-up.

## Reference(s):

- [Local rules and validation scope](artifact/references/local-rules.md)
- [Schema.org Validator](https://validator.schema.org/)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [aimeGeo Schema Markup project](https://github.com/xxjrq/aimegeo-schema-markup)
- [aimeGeo documentation](https://geo.aimmme.com/docs/)
- [aimeGeo website](https://geo.aimmme.com/)
- [aimeGeo Gitee mirror](https://gitee.com/xxjrq/aimegeo)

## Skill Output:

**Output Type(s):** [JSON-LD, HTML, JSON reports, Markdown guidance]

**Output Format:** [JSON-LD, an HTML snippet, a JSON validation report, and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local checks do not establish factual accuracy or search eligibility; Google Rich Results testing is not run by the skill.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
