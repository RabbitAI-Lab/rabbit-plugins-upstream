## Description:

Guides agents through using @fetchproxy/cli to capture Credit Karma browser-session cookies and shell commands that call Credit Karma transaction and refresh endpoints directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to retrieve Credit Karma transaction data from a signed-in browser session in scripts or shell workflows without running creditkarma-mcp.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow extracts and reuses live Credit Karma session cookies and bearer credentials in shell commands.

Mitigation: Run it only on a private machine, avoid shared terminals and shell history, keep tokens in session variables when possible, and sign out or revoke the session if exposure is suspected.

Risk: The documented commands write sensitive financial responses and request bodies to predictable /tmp paths.

Mitigation: Replace fixed temporary paths with protected temporary files and avoid pasting tokens or transaction output into logs, chats, or shared files.

## Reference(s):

- [Credit Karma request reference](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl, jq, and fpx command patterns for transaction retrieval and token refresh.]

## Skill Version(s):

2.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
