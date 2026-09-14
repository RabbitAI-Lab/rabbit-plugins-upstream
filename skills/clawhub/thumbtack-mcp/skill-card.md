## Description:

Query thumbtack.com from a shell to search local service pros by trade and zip code and read pro profiles with ratings, reviews, credentials, business hours, and pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compose shell-based Thumbtack lookups, extract public search and profile data, and inspect returned JSON with curl, Node.js, and jq. It is suited for read-only research and workflow automation that does not require a Thumbtack account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to make anonymous network requests to Thumbtack.

Mitigation: Install and use it only when that network access is acceptable, and restrict profile URLs and fetched pages to Thumbtack.

Risk: Adding cookies, account credentials, or login workflows would expand the skill beyond its read-only anonymous posture.

Mitigation: Do not add cookies, account credentials, booking actions, messaging, or project-management workflows to generated commands.

Risk: The undocumented Thumbtack GraphQL recipes and page data shapes may change or be governed by Thumbtack's terms.

Mitigation: Check GraphQL errors explicitly, branch on variable response shapes, and review Thumbtack terms before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/thumbtack-mcp)
- [Thumbtack discovery recipes](artifact/references/discovery.md)
- [Thumbtack](https://www.thumbtack.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell, JavaScript, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only command recipes and local parsing guidance; generated commands may make anonymous network requests to Thumbtack.]

## Skill Version(s):

0.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
