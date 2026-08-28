## Description:

Query Redfin data from a shell through the fpx CLI to resolve locations and addresses, search for-sale listings, inspect property details, market trends, comparable rentals, climate risk, photos, and signed-in saved homes or searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compose one-shot fpx commands for Redfin research workflows without running the redfin-mcp server. It is suited for retrieving public listing, property, market, rental, climate, and photo data, with optional signed-in access to saved Redfin homes and searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access account-specific saved homes and saved searches when fpx is paired with a signed-in Redfin browser tab.

Mitigation: Use a separate browser profile or sign out of Redfin when only public listing data is needed, and treat saved homes and saved searches as private account information.

Risk: Commands make Redfin requests through the user's active browser session.

Mitigation: Install and run the skill only when that browser-session access is acceptable for the intended workflow.

## Reference(s):

- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with bash and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands commonly return Redfin JSON envelopes after removing the {}&& prefix; callers should check resultCode before using payload data.]

## Skill Version(s):

0.10.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
