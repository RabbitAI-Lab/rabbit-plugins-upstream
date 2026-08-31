## Description:

Analyzes fixed-camera videos of feeders and waterers to quantify livestock feeding duration, feeding bouts and drinking frequency, comparing them against individual baselines to raise behavior anomaly alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External livestock operators and farm technology teams use this skill to analyze feeder or waterer camera media, review feeding and drinking behavior statistics, and surface anomaly alerts against individual baselines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Farm videos, submitted URLs, report history, local identity data, and session tokens may be handled by the service during analysis or report lookup.

Mitigation: Confirm the publisher and intended LifeEmergence endpoints before installation, and use only media and accounts approved for that service.

Risk: Default endpoint configuration may target development, private, or environment-specific services.

Mitigation: Review and set the API endpoint configuration in an isolated workspace before production use.

Risk: Behavior anomaly alerts are observational and may be mistaken for veterinary diagnosis.

Mitigation: Treat results as feeding and drinking behavior statistics, and require farm procedures or veterinary review for health decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-drink-behavior-monitor-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Feeding/drinking behavior monitoring API reference](references/api_doc.md)
- [Common analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Structured text, Markdown tables, JSON detail output, and optional result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include feeding duration, feeding and drinking frequency, behavior timing distribution, anomaly level, analysis time, and report links.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter states 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
