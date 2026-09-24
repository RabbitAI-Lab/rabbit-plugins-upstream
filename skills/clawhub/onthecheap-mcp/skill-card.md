## Description:

Find free and cheap things to do in a US city, including daily event listings with times, prices, venues, searchable deals, festivals, kids activities, and local guides from the On the Cheap network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find free or low-cost local events, deals, festivals, family activities, and article details for supported US city sites in the On the Cheap network.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Results come from public event and deal listings that may change, expire, or be incomplete.

Mitigation: Show dates, prices, venues, and source links so users can verify details before attending an event or relying on an offer.

Risk: Full post retrieval may fetch upstream article HTML when explicitly requested.

Mitigation: Prefer compact search results for browsing and request full post content only when the article body is needed.

## Reference(s):

- [On the Cheap network](https://livingonthecheap.com)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text summaries of events, deals, venues, prices, dates, and source links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results from public On the Cheap network content; compact search results omit full article bodies unless full post content is requested.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
