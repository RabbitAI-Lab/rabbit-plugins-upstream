## Description:

Helps an agent guide users through querying Canvas LMS with curl, bearer tokens, and institution-specific Canvas REST API endpoints instead of running the canvas-parent-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, students, and observers use this skill to retrieve Canvas courses, grades, assignments, submissions, calendar items, messages, discussions, and files from a shell. It is most useful when the user has a Canvas access token and wants repeatable curl commands or scripting guidance without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas bearer tokens and OAuth secrets may be exposed through shell history, logs, screenshots, or shared terminal transcripts.

Mitigation: Use a trusted Canvas base URL, avoid recording or sharing terminal output containing credentials, and unset credential environment variables after use.

Risk: The OAuth QR-login path uses an npm helper through npx and eval, which increases supply-chain and command-injection risk if the package is not verified.

Mitigation: Verify the helper package source and version before use, pin the package version, and avoid the npx/eval path unless that review has been completed.

Risk: Commands query live Canvas account data and can expose sensitive educational records if run with the wrong tenant or token.

Mitigation: Confirm CANVAS_BASE_URL before each workflow, use the least-privileged token available, and review outputs before storing or sharing them.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are guidance and command examples; users must supply their own Canvas base URL, token, and endpoint IDs.]

## Skill Version(s):

2.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
