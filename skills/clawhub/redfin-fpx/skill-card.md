## Description:

Connects the fpx command-line tool to Redfin through an approved browser tab so agents can resolve locations, search listings, inspect property and market data, and access saved homes when signed in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Redfin data users can query U.S. property listings, property details, market trends, comparable rentals, climate risk, photos, and signed-in saved homes from a shell-based workflow.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Saved-homes examples can leave private account data in a temporary file with inadequate protections.

Mitigation: Pipe responses directly into extraction commands, or use a private, uniquely created file and remove it when finished.

Risk: The browser bridge uses approved Redfin access and may remain paired after the task.

Mitigation: Approve only Redfin fetch access and revoke pairing when finished.

## Reference(s):

- [Redfin endpoint examples](artifact/references/stingray-endpoints.md)
- [Redfin](https://www.redfin.com)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [Fetchproxy extension reference](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [JSON data, Shell commands, Guidance]

**Output Format:** [Redfin property and market data in JSON, with Markdown guidance and inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may need anti-CSRF prefix removal and result-code checking before use.]

## Skill Version(s):

1.3.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
