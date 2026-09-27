## Description:

Helps agents query homes.com listings, property details, and signed-in saved homes or searches through the user's paired browser tab without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search US real-estate listings, inspect property information, and retrieve saved homes or searches when the user authorizes access to a signed-in homes.com tab.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: A paired signed-in browser tab can expose private saved homes and saved searches.

Mitigation: Pair only if comfortable granting access to the signed-in tab, and retrieve saved account data only when specifically requested.

Risk: Address lookup can return a nearby property rather than the requested one.

Mitigation: Confirm the returned street address before presenting or relying on property details.

## Reference(s):

- [Homes FPX release](https://clawhub.ai/chrischall/skills/homes-fpx)
- [Homes.com request recipes](references/homes-requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text, JSON]

**Output Format:** [Markdown instructions and shell examples; retrieved results can be extracted as text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved homes and searches require an authorized signed-in browser session.]

## Skill Version(s):

2.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
