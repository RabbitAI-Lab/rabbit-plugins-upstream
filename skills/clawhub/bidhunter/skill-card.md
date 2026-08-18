## Description:

BidHunter monitors Chinese state-owned enterprise and public procurement notices, evaluates eligibility against configurable qualification rules, generates bid-analysis reports, and can deliver summaries through DingTalk, WeCom, or email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[419597334-sudo](https://clawhub.ai/user/419597334-sudo)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement teams, bid agents, and supplier qualification managers use this skill to collect bid notices, classify whether opportunities are investable, not investable, or need review, and prepare daily reports or notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill scrapes procurement sites and can send generated summaries to configured DingTalk, WeCom, or email recipients.

Mitigation: Use dry-run or --no-push first, verify each webhook or email destination carefully, and enable delivery only after the recipient scope is correct.

Risk: Local bid caches, reports, push history, and push configuration may contain business-sensitive opportunity data or delivery credentials.

Mitigation: Keep the push configuration private, preserve restrictive file permissions, and review generated files before sharing them outside the intended team.

Risk: Qualification matching may produce incorrect or incomplete bid-readiness judgments if the rules do not reflect the user's actual licenses and capabilities.

Mitigation: Customize the qualification rules for the user's own entities, run the rules health check, and manually review items marked not investable or needing confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/419597334-sudo/skills/bidhunter)
- [Supported Platforms and Configuration](artifact/references/platforms.md)
- [Filtering Rules and Conditions](artifact/references/filter_rules.md)
- [Bid Field Standardization Schema](artifact/references/field_standard.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown and text reports, HTML reports, JSONL bid records, CSV quote drafts, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local bid caches, reports, quote drafts, push history, and push configuration files; optional delivery sends summaries to configured channels.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
