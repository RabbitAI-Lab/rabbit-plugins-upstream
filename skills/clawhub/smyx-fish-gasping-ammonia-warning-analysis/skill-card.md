## Description:

Analyzes aquarium-camera video for gasping and abnormal breathing, providing visual warnings of possible ammonia poisoning or low oxygen.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and aquaculture operators use camera footage to spot signs of fish distress, review warning reports, and decide when to check water quality or seek expert help.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos or video URLs and user-linked report requests are sent to a cloud service.

Mitigation: Use only when comfortable sharing that media and report history with LifeEmergence; minimize sensitive content before submission.

Risk: The skill silently creates or reuses an identity and may retain tokens in the local workspace database.

Mitigation: Prefer a separate workspace and account; treat local data as sensitive and delete it when no longer using the skill.

Risk: Visual distress warnings can be mistaken for a confirmed cause or a basis for unattended intervention.

Mitigation: Confirm with water tests and a qualified aquatic specialist; require user approval before changing aquarium equipment.

## Reference(s):

- [Skill listing on ClawHub](https://clawhub.ai/18072937735/skills/smyx-fish-gasping-ammonia-warning-analysis)
- [API and warning criteria](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report or historical report list with risk warnings, suggested actions, and an optional report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can be saved to a file; visual warnings are not a confirmed diagnosis.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
