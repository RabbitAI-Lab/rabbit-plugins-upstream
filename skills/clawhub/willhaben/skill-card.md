## Description: <br>
Create and manage Willhaben.at marketplace listings by handling photo uploads, German listing drafts, pricing suggestions, and browser-assisted posting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benjaminorthner](https://clawhub.ai/user/benjaminorthner) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to prepare and post Austrian Willhaben marketplace listings from item details and photos. It researches comparable prices, drafts German listing copy, estimates package size, applies saved selling preferences, and guides browser automation for publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may publish an inaccurate or unintended live marketplace listing. <br>
Mitigation: Review the generated title, description, price, photos, location/contact details, shipping choices, and package-size selection before publication. <br>
Risk: The skill operates a signed-in Willhaben browser session and can post under the user's account. <br>
Mitigation: Install and use it only when supervised posting to a signed-in Willhaben session is intended. <br>
Risk: Local selling preferences may retain location, shipping, pricing, and description defaults. <br>
Mitigation: Review or delete config/user-preferences.json when those saved preferences should not persist. <br>
Risk: Paid promotion options may appear during the Willhaben publishing flow. <br>
Mitigation: Confirm no paid promotion is selected and the total remains zero before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/benjaminorthner/skills/willhaben) <br>
- [Willhaben listing creation](https://www.willhaben.at/iad/anzeigenaufgabe) <br>
- [Willhaben Bot Setup](references/SETUP.md) <br>
- [Willhaben Categories](references/categories.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown listing drafts, German marketplace copy, browser-action guidance, and JSON preference configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May store local selling preferences in config/user-preferences.json and uses a signed-in browser session for Willhaben posting.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
