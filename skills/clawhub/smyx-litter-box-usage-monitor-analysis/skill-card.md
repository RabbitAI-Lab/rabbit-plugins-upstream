## Description:

Analyzes litter-box video to summarize each cat's visit frequency and duration, compare behavior with historical patterns, and flag possible urinary-health concerns without providing a diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, catteries, veterinary wards, and boarding facilities use this skill to monitor litter-box visits from video and review behavior-based alerts and historical reports, particularly for multi-cat households. The alerts are not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Litter-box-area videos or URLs and identity-linked report history are sent to a cloud service and may reveal private interiors or people.

Mitigation: Submit only non-sensitive footage, avoid people and private interiors, and confirm that cloud processing and report retention are acceptable before use.

Risk: The skill can silently create or reuse a remote account and store local tokens for later report access.

Mitigation: Use it only when account creation and persistent access are acceptable; protect local credentials and review the associated cloud reports.

Risk: Behavior-based urinary-health alerts can be mistaken for a medical diagnosis.

Mitigation: Treat alerts as screening information and consult a veterinarian about concerning symptoms.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-litter-box-usage-monitor-analysis)
- [Litter-box analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured analysis text or JSON; historical report listings as Markdown tables with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include per-cat visit counts, durations, behavioral alerts, and links to exported reports.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled frontmatter lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
