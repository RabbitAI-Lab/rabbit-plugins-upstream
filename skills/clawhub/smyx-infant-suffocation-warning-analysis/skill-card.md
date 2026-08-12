## Description:

Identifies prone sleeping positions, head covering, and occlusion of the mouth/nose by bedding or clothing; provides real-time high-risk alerts to safeguard infant sleep safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and caregivers use this skill to analyze infant sleep monitoring video or image inputs for prone sleeping, head covering, and mouth or nose occlusion risks, then receive structured risk reports, guidance, and report links. It also supports cloud-backed history lookup for prior alert reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant sleep videos, URLs, platform identity fields, and report history requests may be sent to Life Emergence cloud services.

Mitigation: Use the skill only with explicit consent and after confirming account, retention, and deletion controls for real household footage.

Risk: Stored reports and export links may expose sensitive household or infant sleep information.

Mitigation: Treat generated reports and links as sensitive, restrict sharing, and avoid placing them in public logs or long-term conversation memory.

Risk: The skill is an auxiliary monitoring tool and its alerts may be incomplete or delayed.

Mitigation: Do not use it as a replacement for adult supervision or professional medical advice; immediately check the infant when high-risk output appears.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-infant-suffocation-warning-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [Analysis API interface documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files]

**Output Format:** [Markdown or JSON analysis reports with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured suffocation warning results, risk labels, safety suggestions, historical report lists, and cloud report export links.]

## Skill Version(s):

1.0.10 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
