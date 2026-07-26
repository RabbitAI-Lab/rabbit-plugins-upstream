## Description: <br>
Finds free and cheap things to do in supported US cities, including daily event listings with times, prices and venues plus searchable deals, festivals, kids activities and local guides from the On the Cheap network. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer local activity and deal requests for supported US cities by selecting a city site, listing daily events, searching posts, and retrieving full article details. <br>

### Deployment Geography for Use: <br>
United States <br>

## Known Risks and Mitigations: <br>
Risk: Event availability, prices, and deal terms may change after retrieval. <br>
Mitigation: Verify details with the listing source before making plans or presenting firm commitments. <br>
Risk: Using the wrong site key or reusing category and location IDs across sites can return unrelated local results. <br>
Mitigation: Name the intended city, call otc_list_sites when unsure, and resolve categories or locations for the selected site. <br>


## Reference(s): <br>
- [On the Cheap network](https://livingonthecheap.com) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onthecheap-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or concise text with event and deal listings, source details, and follow-up guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only public event and deal results for selected supported sites; event availability and prices should be verified because listings can change.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
