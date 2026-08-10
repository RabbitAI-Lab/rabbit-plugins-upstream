## Description:

Find free and cheap things to do in a US city, including daily event listings with times, prices, venues, searchable deals, festivals, kids activities, and local guides from the On the Cheap network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find public free or low-cost local events, deals, festivals, kids activities, and local guides for supported US cities and dates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may receive listings for the wrong city if the selected site key does not match the requested location.

Mitigation: Confirm the supported site or call the site-listing tool first, and check that returned site and site_name fields match the user's request.

Risk: Event and deal availability can change, and expired deals may no longer be valid.

Mitigation: Use current lookups for the requested date or city and label expired results when the user explicitly asks to include them.

Risk: Monthly event overviews are previews and may not include every listing for a day.

Mitigation: Use total counts for monthly summaries and call the daily event listing tool for a complete schedule on a specific date.

## Reference(s):

- [On the Cheap network](https://livingonthecheap.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onthecheap-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, API Calls]

**Output Format:** [Markdown or concise text summaries with event, deal, venue, price, date, and source details where available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public listing lookups; no credentials, persistence, or local data access requested.]

## Skill Version(s):

0.3.3 (source: server release evidence, released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
