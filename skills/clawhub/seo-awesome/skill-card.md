## Description:

SEO-Awesome helps agents advise on first-party Google API driven SEO automation, including keyword research, pSEO page generation, staged publishing, monetization, deployment, and GA4-based review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsorgcn](https://clawhub.ai/user/adsorgcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and growth teams use this skill to plan and operate an automated SEO workflow based on first-party Google data, staged pSEO publishing, monetization paths, and analytics-driven iteration. It is most relevant when the user explicitly wants the SEO-Awesome workflow rather than general SEO advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GA4 credentials, Google API keys, and lead data can expose sensitive business or user information if mishandled.

Mitigation: Use read-only scopes where possible, keep secrets out of chats and repositories, store credentials in a secrets manager or environment variables, and avoid retaining raw user-level analytics data.

Risk: Publishing automation and analytics-driven strategy changes can create unintended production changes at scale.

Mitigation: Test in staging or dry-run mode, require human approval before production publishing, set change limits, keep publish logs, and maintain rollback controls.

Risk: Lead-generation workflows can create privacy and compliance risk if users are not clearly informed or opted in.

Mitigation: Use clear privacy notices, collect explicit opt-in consent, limit data collection to the business purpose, and check target-market requirements such as GDPR and CCPA.

## Reference(s):

- [SEO-Awesome ClawHub release](https://clawhub.ai/adsorgcn/skills/seo-awesome)
- [iLang homepage](https://ilang.ai)
- [Gefei SEO](https://seo.web.cafe/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured steps and occasional code, shell, JSON, or configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include SEO workflow plans, Google API setup guidance, pSEO templates, staging checks, rollback guidance, and analytics review recommendations.]

## Skill Version(s):

1.2.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
