## Description: <br>
Query OneHome (CoreLogic) from a shell with the fpx CLI, resolving saved-search scope and reading listing data through authenticated GraphQL and REST calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users can use this skill to query OneHome saved searches, listings, listing details, photos, and related local data from scripts without running the OneHome MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill teaches users to capture and reuse a live OneHome bearer token that can access private real-estate account data. <br>
Mitigation: Use only with explicit authorization for the account or session, avoid shared machines, keep tokens and generated JSON out of logs and screenshots, and delete temporary files that contain credentials. <br>
Risk: The security verdict is suspicious because the credential-handling flow lacks enough guardrails. <br>
Mitigation: Prefer sanctioned APIs or safer delegated-auth flows where available, and review the fpx CLI, Transporter extension, and local machine access before use. <br>


## Reference(s): <br>
- [OneHome GraphQL + REST operations for fpx](artifact/references/graphql-operations.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onehome-fpx) <br>
- [OneHome portal](https://portal.onehome.com) <br>
- [OneHome GraphQL endpoint](https://services.onehome.com/graphql) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls, JSON] <br>
**Output Format:** [Markdown with inline shell, GraphQL, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces command patterns and request bodies for authorized OneHome sessions; returned data depends on the user's session scope and permissions.] <br>

## Skill Version(s): <br>
0.13.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
