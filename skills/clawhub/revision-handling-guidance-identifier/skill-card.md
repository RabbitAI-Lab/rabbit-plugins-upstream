## Description:

Set account merge guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People performing routine account maintenance use this skill to turn a supplied revision_profile into concise merge_guidance for preserving account fields during a merge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided revision profiles may contain sensitive account details.

Mitigation: Provide only the account details needed to generate merge guidance and avoid unnecessary sensitive data.

Risk: Merge guidance can affect account field-preservation decisions if applied without review.

Mitigation: Review the returned merge guidance against the current account-maintenance request before applying it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/revision-handling-guidance-identifier)
- [Publisher Profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [String returned in the merge_guidance field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No credentials, private file access, persistence, or execution authority requested.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
