## Description:

Analyzes images or videos of plant cuttings in transparent containers to detect visible root primordia, classify rooting stage, and produce a structured report with monitoring results and transplant-timing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, propagation-box operators, tissue-culture teams, and agricultural researchers use this skill to monitor cutting-rooting progress from non-invasive transparent-container media and decide when to continue observation or transplant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted plant media, URL values, identity values, and generated reports may be sent to lifeemergence.com services and associated with a locally persisted user or token record.

Mitigation: Use only plant images or public, non-sensitive URLs, and avoid installing in workspaces containing sensitive media or shared agent identity data unless the publisher documents storage, deletion, and authorization behavior.

Risk: Identity, token, history-query, URL-fetching, and local persistence behavior is under-disclosed in the release evidence.

Mitigation: Review the security summary and publisher documentation before installation, and restrict use to contexts where cloud-based analysis and report history storage are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cutting-rooting-status-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface document](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports and JSON-formatted analysis output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and Markdown tables for history queries.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact SKILL.md frontmatter states 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
