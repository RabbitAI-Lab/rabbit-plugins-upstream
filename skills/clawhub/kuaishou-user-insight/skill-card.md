## Description:

Retrieves public Kuaishou videos, creator posts, and comments to support audience insights and product opportunity research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and product researchers use public Kuaishou search results, creator posts, and comments to identify audience needs, content trends, and potential product opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms or Kuaishou URLs and the API token are sent to a third-party service.

Mitigation: Use only if comfortable sharing those inputs with guaikei.com; avoid private, login-only, or sensitive content.

Risk: Saved logs retain research results locally.

Mitigation: Exclude logs from source control and delete them when no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/kuaishou-user-insight)
- [Usage and options](references/options.md)
- [Skill readme](readme.md)
- [API token access](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis]

**Output Format:** [Structured JSON results with an optional text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes success, empty, or error status; results may be saved in local logs.]

## Skill Version(s):

1.0.0 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
