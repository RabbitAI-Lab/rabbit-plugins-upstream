## Description: <br>
Searches, compares, books, and fixes flights, including fares, fare rules, connections, baggage, seats, miles, delays, passenger rights, and trip-critical travel documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-assistance agents use this skill to find and compare flights, evaluate fare and loyalty choices, manage post-ticket issues, and draft or track claims. It advises by default and does not complete payments on the user's behalf. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can maintain local travel memory containing bookings, watched routes, traveler constraints, loyalty balances, claims, deadlines, and related shared rows. <br>
Mitigation: Install only when local travel memory is desired, review the configured data paths, and use it for another person's travel details only with permission. <br>
Risk: Travel workflows can involve sensitive credentials, identity documents, programme PINs, card numbers, and boarding-pass data. <br>
Mitigation: Store only pointers to credentials and secrets, and do not persist passport numbers, ID numbers, boarding-pass barcodes or images, loyalty PINs, or card numbers in local notes. <br>
Risk: Flight prices, fare rules, API pricing, regulatory compensation thresholds, and travel-document requirements can change quickly. <br>
Mitigation: Verify current provider prices, fare terms, official travel rules, and compensation thresholds before purchase, ticket changes, claims, or implementation decisions. <br>


## Reference(s): <br>
- [ClawHub Flight Skill Page](https://clawhub.ai/ivangdavila/skills/flight) <br>
- [Clawic Flight Skill Page](https://clawic.com/skills/flight) <br>
- [Flight Skill Definition](artifact/SKILL.md) <br>
- [Flight Memory Template](artifact/memory-template.md) <br>
- [Flight Data APIs](artifact/apis.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with comparison tables, checklists, claim drafts, and local-note update instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May maintain local travel memory under configured Clawic data paths; no payments are completed by the skill.] <br>

## Skill Version(s): <br>
1.0.3 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
