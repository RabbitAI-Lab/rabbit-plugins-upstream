## Description:

Analyzes dog-toilet or walking-path images and videos for stool color, shape, blood, and mucus, returning observational findings rather than a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caretakers use this skill to review stool appearance in dog-toilet or outdoor-walking footage and identify observations worth following up; it does not diagnose disease.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private household or walking-path images and videos may be sent to the provider's cloud APIs.

Mitigation: Use only media whose cloud transfer is acceptable; avoid private household footage unless these data flows are approved.

Risk: The skill creates or reuses a persistent cloud-linked identity and stores tokens locally.

Mitigation: Review local credential persistence and access before installation; use a workspace appropriate for those tokens.

Risk: Matching history-request phrases can trigger cloud report queries without clear end-user consent controls.

Mitigation: Confirm authorization before requesting history and review whether automatic cloud queries are acceptable.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured observation report or JSON; history results may include report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional result file; observational findings are not a diagnosis]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata; bundled SKILL.md declares 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
