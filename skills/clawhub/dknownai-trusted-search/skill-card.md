## Description:

dknowc trusted search retrieves and verifies authoritative-source materials for policy, legal, standards, compliance, subsidy, tax-benefit, and government-service research, then delivers sourced answers with clickable provenance reports and clean Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve and verify authoritative Chinese policy, legal, government-service, standards, subsidy, tax-benefit, and compliance materials. It supports sourced answers, clickable provenance HTML reports, clean Markdown deliverables, and optional policy visualization reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Policy or legal search queries are sent to the third-party provider.

Mitigation: Use the skill only when the user is comfortable sharing the query with the provider; avoid unnecessary sensitive details in search prompts.

Risk: If no key is configured, the skill may initiate a phone/SMS account and API-key onboarding flow.

Mitigation: Disclose the onboarding flow before collecting a phone number, require user consent, and do not persist the returned key unless the user explicitly requests future reuse.

Risk: Fallback answers produced without sourced search are unverified.

Mitigation: Label fallback content as unverified, avoid presenting it as authoritative, and do not generate provenance deliverables for unsourced fallback answers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-trusted-search)
- [Search introduction](reference/search_intro.md)
- [Sample search result](reference/sample_search_result.md)
- [Sample trace report](reference/sample_trace_report.html)
- [DKnowC dependable search API](https://open.dknowc.cn/dependable/search)
- [DKnowC deep query API](https://open.dknowc.cn/api/services/deep-query/v3)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Direct answer text with sourced Markdown, clickable provenance HTML reports, clean Markdown files, JSON intermediate results, and optional self-contained visualization HTML or SVG.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY for verified search. Deep search and visualization are optional workflows triggered by user request or confirmation.]

## Skill Version(s):

1.1.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
