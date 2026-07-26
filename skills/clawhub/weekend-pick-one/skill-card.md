## Description: <br>
周末去哪玩｜只推一个 helps Chinese-speaking users make a same-day or weekend outing decision by resolving relative dates, weighing location, time, budget, energy, transport, weather, crowding, opening status, and return feasibility, then choosing one primary plan with backups, avoid-list items, and verification evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killsnake01](https://clawhub.ai/user/killsnake01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Chinese-speaking ClawHub users use this skill when they have not chosen a destination and want one practical weekend, day-trip, or evening outing decision instead of a broad itinerary or activity list. It is aimed at quick local, suburban, and nearby regional choices where the agent should make a concise recommendation and explain current evidence gaps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use public search or browser access to gather outing candidates and current facts. <br>
Mitigation: Limit browsing to public pages needed for the current request; do not log in, bypass access controls, scrape in bulk, download media, or interact with platform accounts. <br>
Risk: Outing facts such as weather, hours, tickets, transport, and safety status can change close to departure. <br>
Mitigation: Mark these items for pre-trip verification and prefer official weather, venue, ticketing, transport, or government sources for key facts. <br>
Risk: Preference memory can expose personal travel patterns if stored without consent. <br>
Mitigation: Use preferences only for the current session unless the user explicitly chooses to remember them and the host supports persistent memory. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/killsnake01/skills/weekend-pick-one) <br>
- [Publisher profile](https://clawhub.ai/user/killsnake01) <br>
- [Date and evidence contract](references/decision-evidence.md) <br>
- [Safety boundaries](references/safety.md) <br>
- [Search query playbook](references/search-query-playbook.md) <br>
- [Regional trip policy](references/regional-trip-policy.md) <br>
- [Escape plan schema](schemas/escape-plan.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, HTML] <br>
**Output Format:** [Markdown outing verdict with fixed fields, evidence links, optional JSON-conformant plan data, and optional share-card HTML when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary recommendations must name only one main destination or route; backups and avoid-list items are secondary decision aids.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
