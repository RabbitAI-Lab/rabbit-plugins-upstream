## Description:

Resolve imported field values.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to reconcile imported field values from supplied source-agreement guidance and return a concise source resolution for the current request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect, stale, or unintended source_guidance can lead to an incorrect source_resolution.

Mitigation: Provide only current, intended source_guidance and review the returned field, disposition, selected_value, and agreement_count before applying it.

Risk: Sensitive or unrelated guidance included in the request may be processed as part of the resolution.

Mitigation: Exclude source_guidance data that should not be used for the current resolution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/source-assurance-guidance-workbench)

## Skill Output:

**Output Type(s):** [Analysis, JSON]

**Output Format:** [Concise source resolution object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns field, disposition, selected_value, and agreement_count.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
