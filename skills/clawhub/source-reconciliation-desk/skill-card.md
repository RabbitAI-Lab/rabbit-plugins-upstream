## Description:

Derive source agreement rules and resolve conflicting source values.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users, analysts, and agents use this skill to derive source-agreement guidance from a source profile and resolve imported field values against that guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can return incorrect reconciliation guidance or select an unsuitable imported value if the supplied source profile or source guidance is incomplete.

Mitigation: Provide clear source counts, field importance, and disagreement preferences, then review the returned source_guidance or source_resolution before applying it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/source-reconciliation-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration]

**Output Format:** [String and JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces source_guidance as a string and source_resolution as an object with field, disposition, selected_value, and agreement_count.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
