## Description:

Your wedding planning co-pilot. Budget tracker that doesn't lie, vendor manager that doesn't forget, seating chart solver that minimizes family drama. 200+ decisions in 6-12 months. This skill remembers all of them. Self-learning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[realteamprinz](https://clawhub.ai/user/realteamprinz)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill as a local wedding planning co-pilot for tracking budgets, vendors, guest lists, seating constraints, timelines, day-of schedules, and couple decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wedding budgets, vendor contacts, guest details, dietary or mobility notes, and family or seating context may be stored in local plaintext files.

Mitigation: Use restrictive filesystem permissions on ~/.wedding-skill/, avoid entering unnecessary sensitive third-party details, and delete or redact records when planning is complete.

Risk: Budget tracking output could be mistaken for financial advice.

Mitigation: Use the skill for planning records and spending visibility only; consult a qualified financial advisor for loans, credit, or financial planning decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/realteamprinz/skills/wedding)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown and JSONL planning records with human-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores user-provided wedding planning data locally under ~/.wedding-skill/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
