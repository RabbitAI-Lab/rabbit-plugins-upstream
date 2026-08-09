## Description: <br>
Assesses whether products, services, people, venues, capacity, budgets, or other resources are available under specified timing and conditions, distinguishes confirmed, conditional, tentative, scheduled, limited, unavailable, stale, and unknown states, and drafts external wording that stays within the evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, operators, and developers use this skill to assess whether a resource can be promised for a specific time, place, quantity, and condition from supplied evidence. It helps produce status tables, availability judgments, limits, public wording, reconfirmation points, and next steps without treating weak evidence as a commitment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Availability assessments may be mistaken for bookings, resource locks, or delivery commitments. <br>
Mitigation: Use the skill only to structure evidence-based availability wording and require responsible-party confirmation before promising or reserving resources. <br>
Risk: Stale, missing, or conflicting evidence can lead to overpromising availability. <br>
Mitigation: Preserve evidence sources and timestamps, mark expired or conflicting inputs, and request reconfirmation instead of choosing the most optimistic status. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured availability assessment sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a parameter status table, current availability status, evidence and timestamps, confirmed scope, conditions and limits, unconfirmed items, public wording, reconfirmation point, and a minimal next step.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
