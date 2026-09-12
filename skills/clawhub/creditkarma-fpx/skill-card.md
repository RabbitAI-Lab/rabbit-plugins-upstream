## Description:

Query Credit Karma transactions from a shell with the fpx CLI by capturing signed-in session cookies once and then using curl against Credit Karma transaction and refresh endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to retrieve authorized Credit Karma transaction data from shell scripts or machines where the Credit Karma MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credit Karma session credentials may expose financial account data if printed, logged, persisted, or reused on an untrusted machine.

Mitigation: Run only on trusted systems, keep tokens in shell variables when possible, avoid shared logs and recordings, protect any written token files with strict permissions, and revoke the session if exposure is suspected.

Risk: The skill relies on unpublished Credit Karma endpoints and session-cookie behavior that may change without notice.

Mitigation: Review commands before execution, use only with accounts you are authorized to access, and treat endpoint or schema failures as a reason to stop and reassess rather than repeatedly retrying credentials.

## Reference(s):

- [Credit Karma request examples](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on short-lived session credentials and Credit Karma transaction JSON responses.]

## Skill Version(s):

2.8.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
