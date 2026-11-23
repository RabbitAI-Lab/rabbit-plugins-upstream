## Description:

Searches public Douyin videos, creator profiles, comments, and trending lists, returning structured data for content research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, brand researchers, and creators can use it to find public Douyin posts and accounts, inspect post details and comments, and follow trending topics for research and planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted Douyin links or IDs are sent to the third-party GuaiKei service.

Mitigation: Before querying, confirm the user is comfortable sharing those links or IDs with the service; do not submit private or sensitive URLs.

Risk: The security assessment is medium confidence and some files were only partially analyzed.

Mitigation: Review package changes before installing or upgrading, and consider the coverage limits when deciding whether to use it.

## Reference(s):

- [Request and response format](references/contract.md)
- [Command options](references/options.md)
- [Error handling](references/errors.md)
- [GuaiKei API service and token help](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON results on stdout with usage and analysis guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are also saved as JSON files for supported queries; available result counts depend on the token plan, and media links may expire.]

## Skill Version(s):

1.5.0 (source: frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
