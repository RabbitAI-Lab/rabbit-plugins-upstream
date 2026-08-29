## Description:

Query homes.com from a shell with the fpx CLI to search listings, resolve street addresses, fetch property detail, photos, history, nearby listings, market data, and signed-in saved homes or saved searches through the user's own browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate shell-based Homes.com data retrieval and extraction workflows without running the homes-mcp server. It is useful for listing search, property detail lookup, address resolution, history and tax extraction, nearby listing discovery, and signed-in saved-home or saved-search review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved homes and saved searches can expose private account data from the user's signed-in Homes.com browser session.

Mitigation: Run saved-account recipes only when the user intends to access that private data, and confirm the paired browser tab is the correct Homes.com session.

Risk: Fetched Homes.com HTML may be temporarily stored under /tmp and can contain listing details or account-page content.

Mitigation: Delete temporary files after use and avoid running these recipes on shared systems when sensitive saved-home data may be present.

Risk: Homes.com address resolution can return a closest candidate rather than a confirmed match.

Mitigation: Verify returned property candidates against the requested street address before using detail-page data in downstream decisions.

## Reference(s):

- [Homes.com request recipes](references/homes-requests.md)
- [Homes.com](https://www.homes.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, Node.js, and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that fetch HTML or JSON, write temporary files under /tmp, and extract structured listing or account-related data from Homes.com responses.]

## Skill Version(s):

1.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
