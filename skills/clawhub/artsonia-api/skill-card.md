## Description:

Access Artsonia student-art portfolios, comments, fans, teacher feedback, artwork downloads, and account pages from a shell using curl against authenticated server-rendered member pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized Artsonia account holders use this skill to retrieve and manage Artsonia member data with curl when the MCP server is not installed or a shell-based workflow is preferred.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive student portfolio data through an authenticated Artsonia account.

Mitigation: Use it only with accounts, students, artwork, and account actions that the operator is authorized to access or manage.

Risk: Cookie jars, downloaded HTML, and parsed outputs may contain sensitive account or child-related data.

Mitigation: Store these files in protected locations, avoid sharing them, and delete them when they are no longer needed.

Risk: Full-resolution artwork images may be reachable through unauthenticated CDN URLs, including private pieces.

Mitigation: Avoid bulk downloading, redistributing, or retaining private artwork unless the operator has explicit authorization and a clear need.

Risk: Account-changing POST requests can silently fail or change more state than intended if form values are not preserved.

Mitigation: Re-read the affected page after each write, verify the intended field changed, and preserve unrelated profile form values exactly.

Risk: Unpinned external parser code could run while credentials, cookies, or sensitive downloaded pages are present.

Mitigation: Review and pin parser dependencies before use, and keep credentials and cookie jars out of the parser runtime when possible.

## Reference(s):

- [Artsonia endpoints - curl + parser recipes](references/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and endpoint recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl request patterns, parsing recipes, verification checks, and operational cautions for authenticated Artsonia sessions.]

## Skill Version(s):

0.12.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
