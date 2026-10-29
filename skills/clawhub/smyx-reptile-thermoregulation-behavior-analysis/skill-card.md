## Description:

Through fixed enclosure cameras, the system analyzes reptile behavior videos and measures movement frequency and dwell time between basking and hiding zones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers and breeding operations use the skill to summarize enclosure video into zone dwell times, movement frequency, activity rhythms, and husbandry suggestions. Its behavior-based results are not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video may be uploaded for remote processing, including when using an option described as not performing analysis.

Mitigation: Treat footage as remotely processed and submit only clips approved for that use; confirm the upload behavior before execution.

Risk: Automatic account enrollment, possible charges, and persistent credential storage lack clear user control.

Mitigation: Review enrollment, billing, and credential handling before use; request explicit user control and separation of API secrets from user identifiers before production deployment.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-reptile-thermoregulation-behavior-analysis)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Guidance]

**Output Format:** [Structured behavior analysis with zone-use metrics, activity patterns, alerts, husbandry suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes behavior-based observations and recommendations; it does not provide a veterinary diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
