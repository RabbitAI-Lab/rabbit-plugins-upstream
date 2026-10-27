## Description:

Creates concise, evidence-linked competitor decision briefs with actionable recommendations, explicit fact, inference, and opinion labels, and a transparent account of evidence gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Product and strategy teams use this skill for due-diligence background, meeting preparation, and strategy discussions. Comparative claims must be grounded in an evidence table, and unsupported or uncovered dimensions are excluded; it is not intended for legal conclusions or inference from non-public data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Cue connection checks may expose the API key because destination safeguards are incomplete.

Mitigation: Avoid the optional Cue connection until credential-bearing commands enforce approved HTTPS destinations and block unsafe redirects.

Risk: Unsupported comparisons may mislead readers, and document uploads or service costs may have separate consequences.

Mitigation: Review dependencies before installing, approve document uploads and costs separately, and verify unsupported comparisons before relying on a brief.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-competitive-brief)
- [Evidence standards](artifact/references/evidence-standards.md)
- [Cue onboarding](artifact/references/cue-onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown evidence table and concise decision brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Comparative claims include source and date with fact, inference, or opinion labels; the brief reports evidence coverage and gaps.]

## Skill Version(s):

0.3.31 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
