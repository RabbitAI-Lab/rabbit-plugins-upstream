## Description:

Through a fixed camera in a reptile enclosure, the skill analyzes 24-hour video with motion-detection techniques to estimate hourly activity, identify activity peaks, compare behavior with the species' natural rhythm, and produce a circadian activity report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, enclosure operators, breeders, and researchers use this skill to analyze fixed-camera reptile enclosure video for daily activity distribution, rhythm alignment, possible day/night inversion, and environment-review guidance. It supports current analysis and cloud-backed historical report lookup for the associated analysis identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reptile enclosure videos or video URLs are sent to the Life Emergence cloud service, and analysis history is tied to an internally managed identity.

Mitigation: Use the skill only with footage approved for cloud processing, and confirm consent, retention, deletion, and history-access controls before using private or sensitive footage.

Risk: The skill performs silent account setup and persists identity tokens with limited user-facing control.

Mitigation: Review identity and token storage before installation, restrict local workspace access, and clear stored credentials or history through available platform controls when decommissioning.

Risk: Motion-based circadian analysis can be misleading when video requirements are not met or when biological context explains activity changes.

Mitigation: Require fixed-camera footage covering at least 24 hours with stable IR night vision, species rhythm metadata, lighting schedule, and context such as shedding, brumation, egg laying, or recent environment changes; treat health concerns as a reason to contact a reptile veterinarian.

## Reference(s):

- [Reptile Circadian Activity Analysis API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Life Emergence Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-reptile-circadian-activity-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [JSON or Markdown report text with analysis fields and an optional report export link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include hourly activity arrays, peak and quiet hours, day/night activity ratios, rhythm classification, consistency score, alert level, recommended actions, disclaimers, and historical report records.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact SKILL.md frontmatter lists 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
