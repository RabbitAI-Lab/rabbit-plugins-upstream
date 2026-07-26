## Description: <br>
Orders food delivery from DoorDash, Uber Eats, or Grubhub via browser automation when a user-created calendar event specifies a direct restaurant order or discovery criteria. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thisisjeron](https://clawhub.ai/user/thisisjeron) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to turn their own calendar events into food delivery workflows across DoorDash, Uber Eats, and Grubhub. It helps compare restaurants, prepare carts, and request explicit confirmation before placing a live order. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate logged-in food delivery services through a Chrome profile with saved account, address, and payment details. <br>
Mitigation: Use it only when comfortable with agent control of those sites, and review the restaurant, items, address, fees, tip, total, ETA, and payment method before confirming. <br>
Risk: The skill can place real orders that charge a saved payment method. <br>
Mitigation: Require the pre-checkout summary and proceed only after the user explicitly answers "yes" for the exact live order. <br>
Risk: A calendar event from a shared or external source may not represent the user's intent. <br>
Mitigation: Use calendar events created by the user and surface external or recently modified events in the pre-confirmation summary. <br>
Risk: Food allergy or dietary information may be incomplete or ambiguous in restaurant menus. <br>
Mitigation: Skip items or restaurants when allergen or dietary safety cannot be confirmed, and report substitutions or uncertainty before checkout. <br>


## Reference(s): <br>
- [DoorDash Browser Flow](references/doordash.md) <br>
- [Grubhub Browser Flow](references/grubhub.md) <br>
- [Uber Eats Browser Flow](references/ubereats.md) <br>
- [Food Calendar Order on ClawHub](https://clawhub.ai/thisisjeron/skills/food-cal-order) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown task instructions and plain-text order summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include restaurant comparisons, cart summaries, totals, ETA, allergy accommodations, and order confirmation or failure status.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
