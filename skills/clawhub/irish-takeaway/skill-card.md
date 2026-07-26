## Description: <br>
Find nearby takeaways in Ireland and browse menus via Deliveroo/Just Eat using Google Places API discovery and browser automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cotyledonlab](https://clawhub.ai/user/cotyledonlab) <br>

### License/Terms of Use: <br>


## Use Case: <br>
People looking for takeaway restaurants in Ireland use this skill to find nearby options, filter by cuisine or rating, and browse restaurant menu details on Deliveroo or Just Eat. <br>

### Deployment Geography for Use: <br>
Ireland <br>

## Known Risks and Mitigations: <br>
Risk: Location and restaurant searches may be shared with Google Places, Deliveroo, or Just Eat. <br>
Mitigation: Use town, postcode, or approximate coordinates when possible and avoid sharing a full home address unless necessary. <br>
Risk: Google Places API use can expose API-key quota or billing if the key is unrestricted. <br>
Mitigation: Use a restricted Google Places API key and monitor quota and billing. <br>
Risk: Browser automation could drift from menu browsing into login, payment, or ordering flows. <br>
Mitigation: Keep use to discovery and menu viewing unless a future version explicitly scopes ordering behavior. <br>


## Reference(s): <br>
- [Deliveroo Ireland](https://deliveroo.ie/) <br>
- [Just Eat Ireland](https://www.just-eat.ie/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and menu summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires goplaces, GOOGLE_PLACES_API_KEY, and browser automation for menu browsing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
