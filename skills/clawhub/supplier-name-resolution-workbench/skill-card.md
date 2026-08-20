## Description:

Reconcile supplier names.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users or agents handling supplier reconciliation use this skill to compare supplier names from the current request and return a concise match decision with canonical names and a score.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The match result depends on the supplier data and matching guidance supplied in the current request.

Mitigation: Provide only the supplier data needed for the current reconciliation task and review the returned match decision before using it in business records.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/supplier-name-resolution-workbench)
- [Publisher Profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise structured text with match_result fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns matched, left_canonical, right_canonical, and score for the current request.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
