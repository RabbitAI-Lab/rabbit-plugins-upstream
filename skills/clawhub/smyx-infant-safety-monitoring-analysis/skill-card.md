## Description:

Analyzes infant images and videos for potential safety hazards and returns alerts, care suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers can submit infant media for supplemental safety analysis and review cloud-hosted reports of possible hazards. The skill is not a substitute for direct supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant footage and report history are sent to a cloud service without clear privacy, retention, deletion, and consent terms.

Mitigation: Review the publisher's privacy and consent terms before use; avoid sending private household footage until they are clear.

Risk: The skill silently creates or reuses a local identity and can retrieve sensitive cloud report history tied to it.

Mitigation: Limit access to the skill and report history to authorized caregivers, and review identity and history handling before installation.

Risk: Visual safety analysis may miss hazards or produce misleading warnings.

Mitigation: Treat reports as supplemental information, not a replacement for direct caregiver supervision.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-safety-monitoring-analysis)
- [Infant safety analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured safety analysis or JSON; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk warnings, care suggestions, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
