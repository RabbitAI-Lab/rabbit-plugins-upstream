## Description:

Query Redfin from a shell with the fpx CLI to resolve locations, search listings, inspect property details, market trends, comparable rentals, climate risk, photos, and explicitly requested signed-in saved-home data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agents use this skill to build Redfin data lookups without running the Redfin MCP server, especially from scripts or machines where the MCP is not installed. It is suited to real-estate research workflows that need shell commands and response-parsing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser pairing can allow later Redfin requests through the user browser session.

Mitigation: Pair only the intended redfin.com profile, keep site access scoped to Redfin, and revoke the pairing when finished.

Risk: Saved-home and saved-search flows can expose account-specific Redfin data when the browser tab is signed in.

Mitigation: Use those flows only when the user explicitly requests account-specific Redfin data and confirms the signed-in context.

Risk: An unpinned global @fetchproxy/cli install may run a newer unreviewed CLI version.

Mitigation: Prefer a pinned or reviewed @fetchproxy/cli version and avoid installing with sudo.

## Reference(s):

- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)
- [ClawHub redfin-fpx release](https://clawhub.ai/chrischall/skills/redfin-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON parsing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands depend on a paired fpx profile and Redfin response envelopes; saved-home and saved-search flows require an explicitly signed-in Redfin tab.]

## Skill Version(s):

0.13.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
