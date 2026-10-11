## Description:

Collects authorized X lists on request, excludes archived posts, and turns observed market viewpoints into daily writing reports and weekly off-topic statistics, with optional Feishu archiving and separately authorized scheduling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[0xcjl](https://clawhub.ai/user/0xcjl)

### License/Terms of Use:

MIT-0

## Use Case:

People monitoring authorized X lists use this skill to collect posts within a fixed window, summarize market viewpoints, and prepare evidence-linked daily writing digests. They can optionally archive digests to their authorized Feishu workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authenticated browser can access X content and local archives can retain collected posts.

Mitigation: Use only authorized lists and a user-selected data directory; review the browser and storage permissions before execution.

Risk: Optional Feishu publication or scheduling can send reports to an unintended destination or run without the user's awareness.

Mitigation: Confirm the Feishu profile and destination before publishing, verify the saved document, and enable scheduling only with separate explicit consent.

Risk: Partial collection or unverified posts can make market summaries misleading.

Mitigation: Preserve source links and coverage status, label incomplete runs, and review claims before relying on a digest.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/0xcjl/skills/x-list-digest)
- [Collection and coverage rules](artifact/references/collector.md)
- [Feishu archive guidance](artifact/references/feishu-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Chat summary, Markdown reports, and local SQLite archive]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Daily digests may include Sunday weekly statistics; optional Feishu copies require authorization and readback. Incomplete collection is labeled partial.]

## Skill Version(s):

2.0.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
