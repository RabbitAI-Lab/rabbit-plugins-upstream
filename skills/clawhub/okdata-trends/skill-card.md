## Description:

Looks up current hot-search boards and posts across supported social platforms through the okdata API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content or marketing teams can check current hot-search boards across supported social platforms, compare shared topics, and inspect posts behind a topic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to the external okdata API, and the security scan reported partial coverage.

Mitigation: Consider whether the external API is appropriate and needed before use, and review the skill because some local references were unresolved during scanning.

## Reference(s):

- [okdata hot search API](https://okdata.online/tools/hot-search/)
- [ClawHub release page](https://clawhub.ai/conn-ho/skills/okdata-trends)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown summary with ranked topics, platform details, post engagement, and source links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A point-in-time snapshot; use ranks rather than heat values to compare topics across platforms.]

## Skill Version(s):

0.1.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
