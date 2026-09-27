## Description:

Derive supplier matching rules and reconcile supplier names.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and operations teams use this skill to create supplier-name matching guidance and reconcile supplier aliases into canonical names for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplier records may contain confidential business data.

Mitigation: Avoid including unnecessary confidential supplier records in prompts or examples.

Risk: Ambiguous supplier-name matches can create incorrect canonicalization decisions.

Mitigation: Review ambiguous matches manually and prefer stable identifiers such as registration or tax IDs before applying changes in business systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/supplier-reconciliation-studio)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Concise text guidance and a JSON-like match result object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces matching_guidance as a string and match_result as an object with matched, left_canonical, right_canonical, and score.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
