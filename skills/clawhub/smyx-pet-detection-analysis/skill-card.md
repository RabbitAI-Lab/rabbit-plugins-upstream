## Description:

Detects cats, dogs, and birds in images and video for home pet monitoring and provides structured detection reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home pet owners and developers use the skill to check images or video for cats, dogs, and birds, review detection reports, and retrieve past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home-monitoring images or videos are sent to lifeemergence.com services for analysis.

Mitigation: Inform users and obtain consent before sending household media to the cloud.

Risk: The skill silently creates or reuses a local identity and stores service tokens in the workspace data directory.

Mitigation: Make identity creation and token storage explicit and user-controllable; restrict access to stored tokens.

Risk: Historical home-media reports can be retrieved from the cloud.

Mitigation: Confirm the user intends to retrieve history and limit access to the relevant account's reports.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured detection report or Markdown table of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection results, suggestions, and report links.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; artifact frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
