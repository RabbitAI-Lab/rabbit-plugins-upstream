## Description: <br>
Generates a complete, execution-ready event planning report from event type, budget, audience, timing, location, and goals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[simonomi2](https://clawhub.ai/user/simonomi2) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, operations, community, and event teams use this skill to turn event requirements into a structured HTML plan covering strategy, creative direction, timelines, budget allocation, promotion, staffing, scripts, risk planning, and post-event evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Event plans may include attendee photos, contact details, QR lead forms, invitations, reminders, surveys, or marketing follow-up data. <br>
Mitigation: Apply privacy safeguards before sharing or storing generated plans, and avoid including sensitive personal data unless it is necessary for the event workflow. <br>
Risk: The skill writes a generated HTML report to the user's current working directory. <br>
Mitigation: Confirm the intended output location and filename before saving, and avoid overwriting important files. <br>
Risk: The artifact includes self-stated security-audit language. <br>
Mitigation: Use the server-provided security evidence as the authoritative source and do not treat self-stated badges or claims as policy approval. <br>


## Reference(s): <br>
- [Activity Planner ClawHub Page](https://clawhub.ai/simonomi2/skills/activity-planner) <br>
- [Activity Framework](artifact/references/activity_framework.md) <br>
- [Budget Guide](artifact/references/budget_guide.md) <br>
- [Copywriting Templates](artifact/references/copywriting_templates.md) <br>
- [Promotion Monitor](artifact/references/promotion_monitor.md) <br>
- [Script Templates](artifact/references/script_templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Files, Guidance, Configuration] <br>
**Output Format:** [Structured HTML report with tables, timelines, copy blocks, scripts, and planning guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes an HTML event plan file to the user's current working directory using the bundled plan template.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
