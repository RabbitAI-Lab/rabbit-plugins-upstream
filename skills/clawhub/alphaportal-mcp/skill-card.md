## Description:

Guides authorized users through accessing AlphaPortal student transportation, bus location, and notification data with shell commands instead of the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized parents, guardians, and developers use this skill to retrieve AlphaPortal student transportation details, live bus locations, and arrival notifications from a shell without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser refresh tokens and bearer tokens can expose sensitive student and live-location data if copied into shared shells, logs, or optional bridge tooling.

Mitigation: Use only an authorized account, treat tokens as credentials, and avoid shared terminals and logs; assess optional bridge access before pairing.

Risk: Documented write commands change transportation records without a built-in preview or confirmation.

Mitigation: Avoid write endpoints unless the exact student, endpoint, and payload have been checked through a separate confirmation step.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/alphaportal-mcp)
- [AlphaPortal endpoint reference](artifact/references/endpoints.md)
- [Optional ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands access live account data and return JSON from AlphaPortal.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
