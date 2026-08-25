## Description:

Read and manage a My Hot Lunchbox school-lunch account from a shell with curl, including sign-in, student lists, lunch calendar and cart reads, orders, deliveries, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access My Hot Lunchbox account data from shell commands when the MCP server is unavailable or when scripting direct account reads. It can also guide account-changing actions, but writes and payment commands require careful human review before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes manual account-changing and live payment paths for a My Hot Lunchbox account.

Mitigation: Inspect the exact payload, verify totals and student or order details, and confirm readiness for a real account change or card charge before running write or checkout commands.

Risk: Failed sign-in attempts can lead to CAPTCHA or loss of server-side sign-in for the account.

Mitigation: Do not retry after an invalid_grant response; stop and verify credentials before attempting another login.

Risk: Unverified write request bodies may clear omitted fields or return a success status without proving the intended change landed.

Mitigation: Fetch the current model, review the complete request body, prefer the MCP's typed tools and dry-run previews when available, and re-read the resource after writes.

## Reference(s):

- [My Hot Lunchbox endpoints](artifact/references/endpoints.md)
- [My Hot Lunchbox API host](https://ordernow.myhotlunchbox.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read account data, modify lunch orders, or initiate live payment flows; users should inspect payloads before write or checkout commands.]

## Skill Version(s):

0.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
