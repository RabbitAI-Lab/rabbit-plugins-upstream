## Description:

Guides agents in accessing Artsonia student-art account pages through authenticated curl requests and extracting portfolio, activity, comment, and feedback data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized account holders use this skill to retrieve Artsonia student artwork and account information through shell commands without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student artwork and account pages can contain sensitive information.

Mitigation: Access only accounts and student data you are authorized to use, and limit sharing of retrieved content.

Risk: A documented image URL may retrieve private artwork without authentication.

Mitigation: Avoid the unauthenticated private-image download recipe.

Risk: Fan invitations and account-changing requests can alter account state.

Mitigation: Get explicit confirmation before sending these requests and verify any intended changes afterward.

Risk: Saved session cookies and downloaded HTML can expose account data.

Mitigation: Restrict file permissions and delete local copies when finished.

## Reference(s):

- [Artsonia endpoint recipes](references/endpoints.md)
- [Artsonia](https://www.artsonia.com)
- [Artsonia API skill release](https://clawhub.ai/chrischall/skills/artsonia-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may save authenticated HTML and structured account data locally.]

## Skill Version(s):

1.2.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
