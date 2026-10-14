## Description:

Helps users inspect SEOmatic SEO proposals, record their approval decisions, monitor execution, and request rollback of live changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[minh42](https://clawhub.ai/user/minh42)

### License/Terms of Use:

MIT-0

## Use Case:

SEO teams and site owners use this skill to review proposed SEO changes with supporting evidence, explicitly approve or dismiss them, verify outcomes, and undo unwanted edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect SEO changes may be applied if proposals are approved without reviewing their evidence.

Mitigation: Show the supporting evidence and exact proposed change, and record a decision only after the user approves or dismisses it.

Risk: Noindex and redirect changes can remove pages from search results or reroute traffic, with effects that may take weeks to reverse.

Mitigation: Show the exact URL and consequence, require explicit confirmation, and check the available rollback before undoing a bad change.

Risk: Connecting SEOmatic grants account access and executing changes may require a paid plan.

Mitigation: Connect only the intended account, use the least-privileged credential available, and check the stated execution cost before approving.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/minh42/skills/seomatic-approval-workflow)
- [SEOmatic](https://app.seomatic.ai)
- [SEOmatic agent connection settings](https://app.seomatic.ai/dashboard/settings?tab=ai-agents)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes proposal evidence, user decisions, execution status, before-and-after changes, and rollback options.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
