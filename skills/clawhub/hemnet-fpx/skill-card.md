## Description: <br>
Query Hemnet property data from a shell with fpx, including location resolution, for-sale and sold listing searches, and listing details through one-shot GraphQL calls via a signed-in browser tab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to script anonymous Hemnet property data lookups without running the Hemnet MCP server. It helps agents produce fpx setup guidance, GraphQL request bodies, jq recipes, and troubleshooting steps for Hemnet searches. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow depends on a third-party CLI, a browser extension, and persistent browser pairing. <br>
Mitigation: Confirm trust in @fetchproxy/cli and the Transporter extension before use, and keep the fpx profile scoped to hemnet.se. <br>
Risk: The skill accesses Hemnet data through the user's browser session and public GraphQL surface. <br>
Mitigation: Use it only for Hemnet data access consistent with Hemnet's terms and avoid account or private-data workflows. <br>


## Reference(s): <br>
- [Hemnet GraphQL queries for fpx](references/graphql-queries.md) <br>
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet-fpx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON request bodies, and jq examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are guidance and command examples; the skill itself does not execute Hemnet requests.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
