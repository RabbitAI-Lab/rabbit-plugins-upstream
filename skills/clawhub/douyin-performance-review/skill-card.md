## Description:

Retrieves public Douyin posts, comments, search results, and trending topics to support content-performance reviews and actionable content planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content teams, brands, and creators use this skill to review public Douyin engagement, research competitor posts and comments, identify trends, and plan testable content improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords or links and the GUAIKEI API token are sent to a third-party service.

Mitigation: Use only with approved data and credentials after confirming the service's data-sharing terms.

Risk: Search, post, and comment results may persist in local logs, including sensitive research or personal comments.

Mitigation: Restrict access to logs and delete results that should not be retained.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-performance-review)
- [GUAIKEI service](https://www.guaikei.com)
- [Command options](artifact/references/options.md)
- [Release changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, JSON data, Analysis, Guidance]

**Output Format:** [Structured JSON results with a concise natural-language review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, posts, and comments may be saved to local logs.]

## Skill Version(s):

1.3.0 (source: ClawHub release, frontmatter, changelog, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
