## Description:

Discovers, deduplicates, evaluates, and exports evidence-backed concepts from a URL or a configured author pool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers can track a field or review an author's work to identify and export concepts supported by cited evidence. It scans one URL or a configured author pool; Feishu delivery is optional and requires an explicit request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured sources or local storage paths may not match the user's intended scope.

Mitigation: Review configured sources and storage paths before scanning.

Risk: Gist scans use an existing GITHUB_TOKEN when one is set, which enables authenticated access.

Mitigation: Unset GITHUB_TOKEN if authenticated access is unwanted.

Risk: Feishu delivery shares the generated digest through an external channel.

Mitigation: Review the digest and explicitly request Feishu delivery only when intended.

## Reference(s):

- [Concept Radar on ClawHub](https://clawhub.ai/bonniegeng-max/skills/concept-radar)
- [Evidence Policy](references/evidence-policy.md)
- [Concept Quality Rubric](references/quality-rubric.md)
- [Concept Card Schema](references/card-schema.json)
- [State Contract](references/state-contract.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands]

**Output Format:** [Markdown and JSON concept reports.]

**Output Parameters:** [1D (single URL or configured author-pool scan)]

**Other Properties Related to Output:** [Concept cards include evidence-linked claims, maturity, confidence, action recommendations, and comparison sources. Feishu delivery is optional and requires an explicit user request.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
