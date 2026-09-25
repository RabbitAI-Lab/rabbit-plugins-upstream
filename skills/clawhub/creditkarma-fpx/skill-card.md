## Description:

Query Credit Karma transactions from a shell with the fpx CLI by capturing a signed-in browser session cookie and calling the Credit Karma transaction endpoints directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically proficient users use this skill to retrieve Credit Karma transaction data from shell scripts without running the creditkarma-mcp server. The workflow is intended for users who understand the risks of handling browser session cookies, refresh tokens, and financial data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can expose Credit Karma session cookies, access tokens, refresh tokens, and transaction data.

Mitigation: Run it only on a trusted machine, keep token values in shell variables when possible, restrict permissions on any files that contain credentials, and remove temporary outputs after use.

Risk: A leaked CKAT, CKTRKID, ACCESS, or REFRESH value could grant access to the signed-in Credit Karma session.

Mitigation: Treat these values as account credentials, avoid shared machines, and sign out or invalidate the session if any token output may have been exposed.

Risk: The skill uses unpublished Credit Karma endpoints and persisted query hashes that may change without notice.

Mitigation: Check HTTP status and in-body GraphQL errors before trusting output, and review any endpoint or hash changes before rerunning the workflow.

## Reference(s):

- [Credit Karma requests for fpx + curl](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes session capture, transaction pagination, token refresh, and credential-handling precautions.]

## Skill Version(s):

3.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
