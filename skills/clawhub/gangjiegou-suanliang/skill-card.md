## Description:

Calculates a reviewable steel tonnage estimate band from an existing steel geometry JSON contract and produces JSON, Markdown, and CSV reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

Developers and structural engineers use the skill to estimate steel tonnage from an already prepared steel geometry contract and review section, grade, member, connection, coating, and quantity evidence. Its estimate is a draft for professional review, not a final quantity for design, settlement, or pricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CAD reader and project-sharing bus are separate dependencies whose implementations are not included in this release; project information handled by them may need separate review.

Mitigation: Review those dependencies before sharing confidential project data.

Risk: Generated reports can overwrite files that already use the selected output prefix.

Mitigation: Choose a dedicated output prefix and use trusted dependency paths.

Risk: The ±15% output is a draft estimate and does not establish a final project quantity.

Mitigation: Have a qualified professional review the estimate and its drawing evidence before relying on it.

Risk: Server release evidence identifies MIT-0, while the packaged LICENSE.md and frontmatter identify CC BY-NC-SA 4.0.

Mitigation: Confirm the applicable license before redistribution or commercial use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/gangjiegou-suanliang)

## Skill Output:

**Output Type(s):** [JSON, Markdown, CSV]

**Output Format:** [JSON, Markdown, and CSV files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft ±15% tonnage estimate with final_quantity=false and review items retained.]

## Skill Version(s):

0.2.1 (source: frontmatter, changelog, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
