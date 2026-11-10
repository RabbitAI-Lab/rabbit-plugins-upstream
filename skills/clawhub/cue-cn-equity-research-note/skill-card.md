## Description:

Creates a pre-earnings, single-company research draft with five sections, tying each figure and judgment to a source quote and location.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to prepare a source-traceable draft about a company before its next financial report. The draft covers its business, competitive position, drivers, risks, and key figures without ratings or price forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-backed retrieval may make remote catalog and tool-discovery requests.

Mitigation: Assess whether the reported remote catalog and routing requests are acceptable before enabling retrieval.

Risk: The partial security scan reports weaknesses in the note validator, so flawed or incomplete notes may pass checks.

Mitigation: Manually verify source quotes, anchors, calculations, and the note's stated scope against the original materials.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-cn-equity-research-note)

## Skill Output:

**Output Type(s):** [Markdown]

**Output Format:** [Five-section Markdown research draft with source quotes, anchors, and a key-figures table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each figure and judgment is tied to a source quote and location; excludes ratings, target prices, and share-price forecasts.]

## Skill Version(s):

0.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
