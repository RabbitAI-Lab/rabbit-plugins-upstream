## Description: <br>
Runs a traveler's standing system for durable travel records and advice, including wishlists, documents, entry day counts, bookings, points, budgets, disruptions, companions, long stays, and post-trip debriefs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and personal travel assistants use this skill to maintain a standing travel archive, advise on entry readiness, bookings, budgets, disruptions, safety, health, companions, and loyalty, and prepare actions for the user to execute. It is not intended to execute purchases, bookings, cancellations, or one-trip day-by-day itinerary planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically reads and changes sensitive shared local records, including travel, booking, health, finance, contact, pet, and vehicle records. <br>
Mitigation: Install only when that local archive behavior is desired, review or back up Clawic data before use, and inspect material record changes before relying on them. <br>
Risk: Travel records can expose secrets or highly sensitive personal identifiers if full passports, payment cards, passwords, or document scans are stored directly. <br>
Mitigation: Store only pointers, issuing context, expiry dates, and last-four identifiers; strip full credential, passport, card, and scanned-document values from files under the Clawic data directory. <br>
Risk: Entry, health, safety, fee, and transport requirements can change and may cause bad advice if reused without verification. <br>
Mitigation: Verify destination-specific requirements on authoritative government, provider, or policy sources before they gate a booking or departure, and record the date checked. <br>


## Reference(s): <br>
- [ClawHub Travel Skill Page](https://clawhub.ai/ivangdavila/skills/travel) <br>
- [Clawic Travel Skill Page](https://clawic.com/skills/travel) <br>
- [Travel Skill Definition](artifact/SKILL.md) <br>
- [Working File Templates](artifact/memory-template.md) <br>
- [Documents: Passports, Visas, Authorizations, Day Counts](artifact/documents.md) <br>
- [Bookings: The Record, The Deadlines, The Changes](artifact/bookings.md) <br>
- [Health: Vaccines, Medication, Insurance, Arriving Functional](artifact/health.md) <br>
- [Safety: Risk, Scams, Devices, And The Emergency Card](artifact/safety.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown prose with structured table rows and local-file update guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update user-maintained Clawic travel, booking, health, finance, contact, pet, and vehicle records; stores pointers and partial identifiers rather than full credentials or document numbers.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
