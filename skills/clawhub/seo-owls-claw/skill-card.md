## Description:

Generates SEO-optimized content, briefs, audits, and content plans using persona-driven writing, brand profiles, locale-aware templates, and page-type SEO checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[larya-dot-eu](https://clawhub.ai/user/larya-dot-eu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to research SEO opportunities, create briefs and cluster plans, generate CMS-ready text or deploy-ready HTML, and run SEO quality checks before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ordinary SEO writing requests may invoke the skill unexpectedly.

Mitigation: Use explicit commands where possible and confirm the intended page type, target market, brand, and persona before producing output.

Risk: SEO briefs or plans may be saved to a path or with content the user did not intend.

Mitigation: Review the proposed file path and full content before approving a save; require explicit user confirmation before writing files.

Risk: Generated SEO content can contain inaccurate, misleading, or noncompliant claims if the prompt or research data is incomplete.

Mitigation: Run the documented SEO checks and review final copy, schema markup, brand compliance, and locale assumptions before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/larya-dot-eu/skills/seo-owls-claw)
- [README](artifact/README.md)
- [Command reference](artifact/COMMANDS.md)
- [SEO path workflow](artifact/SEO_PATH.md)
- [SEO schema markup reference](artifact/SEO_CHECKS/schema-markup.md)
- [SEO plan workflow](artifact/SEO_PLANS/plan_workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown, plain text, and HTML with structured data markup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SEO briefs, content cluster plans, page audits, localized copy, brand-aware content, and deploy-ready HTML.]

## Skill Version(s):

0.9.2 (source: server release evidence, artifact SKILL.md, README, COMMANDS.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
