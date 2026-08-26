## Description:

Select the highest approved document version within the requested major release line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to choose the correct approved document version from a release profile when repositories contain drafts, superseded entries, and multiple major release lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An inaccurate release_profile could cause the agent to choose guidance for the wrong major release line or approval preference.

Mitigation: Confirm the release_profile states the intended major release line and eligibility preference before relying on the selection rule.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/draft-precedence-guidance-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [guidance, text]

**Output Format:** [Concise string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns selection_guidance describing the eligibility gate, version ordering, duplicate tie-breaker, and no-selection condition.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
