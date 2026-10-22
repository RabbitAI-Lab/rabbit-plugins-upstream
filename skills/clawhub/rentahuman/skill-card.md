## Description:

Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, review applications, and coordinate real-world work. Use when the user needs something done in the physical world — picking up packages, attending events, photography, in-person meetings, taste-testing, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find people for physical-world tasks, post approved bounties, review applications, and coordinate work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Posting examples may omit approval checks or place private pickup details in a public bounty listing.

Mitigation: Start with free browsing; require approval of the exact listing and total cost before posting, explicitly authorize hiring and payments, and share sensitive pickup details only in private post-acceptance instructions.

Risk: Authenticated actions use an account API key and can affect hiring or payments.

Mitigation: Use a dedicated revocable API key, separately authorize account administration or recurring spending, and pin any optional MCP package version.

## Reference(s):

- [RentAHuman](https://rentahuman.ai)
- [API Reference](references/API.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free public browsing; bounty, messaging, and application actions require an API key.]

## Skill Version(s):

4.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
