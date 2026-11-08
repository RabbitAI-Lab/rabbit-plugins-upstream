## Description:

Analyzes houseplant image sequences for leaf aging and estimates leaf-fall risk over the next 3–7 days, with care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Houseplant owners, plant-care teams, and greenhouse staff use daily images or video to monitor leaf aging, anticipate leaf fall, and adjust plant care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account handling may mix users’ reports in a shared agent workspace.

Mitigation: Wait for sender-isolation fixes before using the skill in a shared workspace.

Risk: Credential forwarding destinations are unrestricted.

Mitigation: Wait for destination restrictions before using credentials in a shared agent workspace.

Risk: The export-only option still runs analysis.

Mitigation: Wait for this behavior to be fixed; do not rely on export-only to prevent analysis.

Risk: Media is uploaded to the configured Life Emergence service; remote retention and forecast accuracy are unverified.

Mitigation: Confirm privacy and charging terms before supplying private recordings, and treat predictions as unverified.

## Reference(s):

- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-leaf-aging-fall-prediction-analysis)
- [API interface reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report in JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include aging indicators, a predicted fall window, at-risk leaf identifiers, cause hints, care suggestions, and report links.]

## Skill Version(s):

1.0.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
