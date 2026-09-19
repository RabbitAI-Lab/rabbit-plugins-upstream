## Description:

Search and analyse Swedish real estate on booli.se, including active for-sale listings, sold prices, area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Swedish property listings, retrieve sold-price comparables, resolve Booli area IDs, and summarize area-level market statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests may be proxied through a local Booli browser tab via the Transporter extension, which can expose browser-session metadata to the workflow.

Mitigation: Use a dedicated browser profile or tab for Booli, approve the pairing intentionally, and avoid routing through a general browsing session when session metadata exposure is a concern.

## Reference(s):

- [Booli skill page](https://clawhub.ai/chrischall/skills/booli)
- [Booli public site](https://www.booli.se)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or concise text with Swedish real estate listings, sold-price comparables, market statistics, and setup checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only outputs; monetary values are in SEK, areas are in square meters, and rooms are numeric counts.]

## Skill Version(s):

2.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
