## Description:

Analyzes gecko and lizard tail images or videos for possible tail loss and produces event alerts and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers and enclosure operators use this skill to review tail images or videos for signs of autotomy, track events, and decide when to seek a reptile veterinarian's assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reptile images, videos, or media URLs are sent to the LifeEmergence cloud service.

Mitigation: Use only media you are comfortable sharing; confirm the service's retention and account controls before submitting sensitive footage.

Risk: The skill creates or reuses an identity, registers or logs in remotely, and stores service tokens locally.

Mitigation: Review this account behavior before installation and protect access to the workspace data directory and cloud report history.

Risk: Image-based injury alerts may be unsuitable as a veterinary diagnosis.

Mitigation: Treat results as screening guidance and consult a reptile veterinarian for wound care or suspected infection.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-reptile-tail-loss-detection-analysis)
- [Reptile tail-loss API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Alerts, Reports, Guidance]

**Output Format:** [JSON reports and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include estimated tail length, injury indicators, event timestamps, alert severity, and recommended actions.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release; artifact frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
