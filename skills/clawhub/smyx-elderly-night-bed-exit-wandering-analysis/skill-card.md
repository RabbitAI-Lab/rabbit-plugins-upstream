## Description:

Using fixed infrared cameras in nursing-home or home bedrooms, this skill monitors nighttime bed-exit status and movement trajectories, detects wandering, and outputs threshold-based alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams, family caregivers, and agent developers use this skill to analyze nighttime bedroom or hallway monitoring video for elderly bed-exit duration and wandering alerts. It produces behavior statistics and alert information for caregiver review, not medical diagnosis or care instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private night-monitoring video and identity-linked report data may be sent to configured services.

Mitigation: Use only with informed consent, approved service endpoints, production HTTPS, and documented retention and deletion controls.

Risk: The skill can create or reuse identities and store tokens locally.

Mitigation: Review identity handling and token storage before installation, restrict local file permissions, and define token rotation or deletion procedures.

Risk: Security evidence marks the release as suspicious because sensitive monitoring data is handled with limited user control.

Mitigation: Install only after security review, deployment configuration review, and confirmation that data handling matches the care setting's privacy requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-night-bed-exit-wandering-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration]

**Output Format:** [Markdown tables or JSON structured analysis with alert text, behavior statistics, and report links when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an optional result file when an output path is supplied.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
