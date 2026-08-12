## Description:

Checks Chinese food, drug, medical device, health food, special medical food, and cosmetics advertising copy before publication, flags six categories of high-risk prohibited phrases, and returns severity and remediation guidance while running locally without network access or dynamic execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, ecommerce, legal, and compliance users can run this skill as a pre-publication guardrail for Chinese food, drug, medical device, health food, special medical food, and cosmetics copy. It is intended for fast keyword-level screening and drafting feedback, not final legal approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyword matching can miss non-obvious violations or flag benign negated statements.

Mitigation: Review flagged and unflagged copy in context and use formal advertising compliance review before external publication.

Risk: The output may be mistaken for legal approval.

Mitigation: Treat findings as drafting assistance only and require qualified legal or compliance approval for regulated advertising.

Risk: The skill does not verify licenses, approvals, registrations, or other administrative status.

Mitigation: Check advertising approval documents, product registrations, advertiser qualifications, and substantiation records through a separate review process.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wwumit/skills/food-drug-cosmetics-ad-guard)
- [README.md](README.md)
- [SKILL.md](SKILL.md)
- [CHANGELOG.md](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON findings from a local CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports decision, risk level, finding count, matched terms, categories, severities, offsets, and remediation suggestions.]

## Skill Version(s):

1.0.0 (source: server release evidence, SKILL.md frontmatter, package.json, CHANGELOG.md released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
