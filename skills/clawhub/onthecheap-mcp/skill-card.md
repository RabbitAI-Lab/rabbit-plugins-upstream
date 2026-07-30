## Description: <br>
Finds free and cheap things to do in supported US cities, including daily event listings with times, prices, venues, local deals, festivals, kids activities, and local guides from the On the Cheap network. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to find public free or low-cost events, deals, and local guides for supported US cities. It is useful when a user asks what is happening locally, wants ideas for a date or weekend, or needs family activities, festivals, or local deals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may query the wrong city, date, category, or location because supported sites and filter IDs are city-specific. <br>
Mitigation: Confirm the intended city and date before querying, use the returned site and site_name fields, and resolve category or location IDs for the same site before applying them. <br>
Risk: Monthly overview results are previews and may be mistaken for complete daily schedules. <br>
Mitigation: Use the total count to describe volume and call the daily event listing for a specific date before presenting a complete schedule. <br>
Risk: Expired deals can appear if explicitly requested for historical research. <br>
Mitigation: Only include expired results when the user asks for past deals or history, and clearly label those offers as no longer current. <br>


## Reference(s): <br>
- [On the Cheap network](https://livingonthecheap.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Markdown or plain text summaries with event, deal, venue, time, price, and follow-up guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only public content; no credentials are required.] <br>

## Skill Version(s): <br>
0.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
