## Description:

Analyzes infant-monitoring videos for virtual safety-zone crossings and provides alerts, findings, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers use the skill to review infant-monitoring footage for crossings of designated safety zones and access analysis reports. Its alerts supplement, rather than replace, direct supervision and physical safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home or child-monitoring footage is processed by lifeemergence.com cloud services.

Mitigation: Use only footage you are authorized to share and accept cloud processing before submitting it.

Risk: Account identity tokens are created and stored locally, and account-linked report history can expose sensitive records.

Mitigation: Protect local workspace data and restrict access to account-linked reports.

Risk: A hidden caller-supplied identity option could affect access to another account's history.

Mitigation: Do not expose or accept arbitrary --open-id values until the identity flow is fixed.

Risk: Missed or incorrect alerts could compromise infant safety if used as the sole safeguard.

Mitigation: Maintain adult supervision and physical protections; treat alerts as supplementary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-virtual-fence-intrusion-warning-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis findings or report listings with links, printed as text or Markdown and optionally saved to a file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include safety warnings, recommendations, and links to historical reports.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
