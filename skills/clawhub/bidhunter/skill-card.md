## Description:

BidHunter monitors Chinese state-owned enterprise and public procurement tender notices, compares them against user-defined qualification rules, and generates concise bidability briefings with investable, not investable, and needs review decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[419597334-sudo](https://clawhub.ai/user/419597334-sudo)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, bid operations, and supplier qualification teams use this skill to collect public tender notices, screen them against their own business scope and red-alert rules, and prepare daily text, HTML, or quote-draft outputs for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts public tender websites, which may rate-limit, fail, or return incomplete data.

Mitigation: Use cached and dry-run modes for review, expect public-site request failures, and verify source links before acting on a tender decision.

Risk: Qualification decisions depend on placeholder business entities and user-maintained rules.

Mitigation: Customize qual_rules.json, run the built-in rule validation command, and manually review investable and needs-review items before bidding.

Risk: Generated HTML reports include data fetched from external sites.

Mitigation: Open reports with awareness that fetched titles, links, and content are external data, and validate suspicious source URLs directly.

Risk: Scheduled task and IM-push workflows are described for operators but are not implemented by the included scripts.

Mitigation: Review any local scheduler or messaging integration separately before deployment.

## Reference(s):

- [Field Standard](references/field_standard.md)
- [Filter Rules](references/filter_rules.md)
- [Supported Platforms](references/platforms.md)
- [ClawHub Skill Page](https://clawhub.ai/419597334-sudo/skills/bidhunter)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; runtime scripts output JSONL cache files, text briefings, HTML reports, and CSV quote drafts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires users to customize qual_rules.json before relying on qualification decisions.]

## Skill Version(s):

1.1.0 (source: server release metadata; SKILL.md frontmatter reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
