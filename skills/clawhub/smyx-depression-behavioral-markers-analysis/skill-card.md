## Description:

Analyzes multi-day home-camera observations of bed time and eating behavior against personal baselines, flagging sustained changes for family or care-team follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families and community care teams can use the skill to review sustained changes in an older or solo-living person's bed time and eating behavior. Its reports are behavioral observations for follow-up, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks this release suspicious because account enrollment, identity and token handling, and remote video processing are not clearly aligned with its stated purpose. The scan is partial because a referenced local path was missing.

Mitigation: Do not install until the publisher explains why these behaviors are needed and what data is sent or retained; the available scan evidence does not cover everything.

Risk: Bedroom and dining-area camera footage can expose highly sensitive personal and health-related behavior.

Mitigation: Obtain the subject's informed consent and apply the documented privacy protections, including face blurring and retaining only anonymized measurements where possible.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured behavioral summaries and alerts, with JSON results and Markdown report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes observed bed-time and eating measures, baseline comparisons, sustained-change alerts, and report links.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
