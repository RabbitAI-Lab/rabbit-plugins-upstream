## Description:

Queries the public Awareness Open Deal Board to help agents find or publish business supply and demand listings, including AI hardware, colocation, and logistics leads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[everest-an](https://clawhub.ai/user/everest-an)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operators use this skill to search public supply and demand listings or intentionally publish new listings for AI hardware, compute capacity, colocation, and logistics. The agent reports listing evidence and URLs without claiming listings are verified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user may publish confidential business details to a public deal board.

Mitigation: Before publishing, confirm the user intends the listing details to be public and avoid including confidential business information.

Risk: Listings may be mistaken for verified or guaranteed facts.

Mitigation: Present listings as leads, report the available publisher evidence and anchored status, and avoid calling listings trustworthy, verified, or guaranteed.

Risk: Empty results may be misread as proof that no market supply or demand exists.

Mitigation: State that empty results can also mean the board is temporarily unavailable, and suggest broadening or adjusting filters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/everest-an/skills/awareness-deals)
- [Awareness Open Deal Board](https://awareness.market/deals.md)
- [Awareness public deals API](https://awareness.market/api/v1/public/deals)
- [Awareness deal publishing page](https://awareness.market/deals/new)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text summaries with listing details, publisher evidence, anchored status, and listing URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include public board query URLs; contact details are not returned directly by the board data.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
