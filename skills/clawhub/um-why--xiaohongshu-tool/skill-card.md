## Description:

Retrieves public Xiaohongshu notes, comments, and creator data as structured JSON for topic research, competitor review, KOL screening, and audience analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

Creators, marketers, and agencies use the skill to retrieve public Xiaohongshu posts, note details, comments, and creator metrics for topic research, competitor monitoring, KOL screening, and sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is suspicious with medium confidence and the artifact was only partially inspected.

Mitigation: Review the skill and its behavior before installing or running it.

Risk: Queries send Xiaohongshu keywords or links to the third-party service.

Mitigation: Use only inputs you are comfortable sharing with that service, and sanitize sensitive request details before contacting support.

## Reference(s):

- [Product and token information](https://www.guaikei.com)
- [Routing guide](artifact/references/routing.md)
- [Output contract](artifact/references/contract.md)
- [Command options](artifact/references/options.md)
- [Error handling](artifact/references/errors.md)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A shared JSON envelope returns public search, note, comment, or creator data with success, empty, or error status.]

## Skill Version(s):

1.2.4 (source: frontmatter, changelog, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
