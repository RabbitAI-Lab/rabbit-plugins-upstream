## Description:

Identifies bird species in images and videos, covering at least 500 common species and supporting customized model training.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, including birdwatchers and ecological observers, use the skill to identify birds in supplied photos or videos and review structured recognition reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may be mixed across users.

Mitigation: Use an isolated, single-user workspace.

Risk: Service credentials may be mishandled or sent to an unintended destination.

Mitigation: Use dedicated credentials and verify the destination before running the skill.

Risk: Media is uploaded to the LifeEmergence service, including when using --export-env-only.

Mitigation: Do not rely on --export-env-only to prevent uploads; use non-sensitive media and verify the provider's retention commitments separately.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-bird-recognition-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface notes](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured recognition report text; JSON or Markdown depending on the operation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include species classifications, confidence information, recommendations, report links, or historical report listings.]

## Skill Version(s):

1.0.25 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
