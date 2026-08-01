## Description: <br>
Prepares for meetings by organizing objectives, attendees, agenda items, materials, decisions, risks, and expected outputs before the meeting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and teams use this skill to turn user-provided meeting details into a structured preparation brief with parameter status, objectives, attendee guidance, agenda, preparation items, decisions, risks, and expected outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting materials may contain sensitive attendee lists, business records, decisions, or risk details. <br>
Mitigation: Provide only the meeting materials the agent is intended to analyze, and remove sensitive details that are not needed for preparation. <br>
Risk: Incomplete, conflicting, or unverified inputs can produce unreliable meeting preparation guidance. <br>
Mitigation: Use the parameter status table to identify missing, conflicting, or pending details and ask for confirmation before producing final conclusions. <br>
Risk: The artifact notes draft testing status and pending real sanitized examples. <br>
Mitigation: Review outputs with representative sanitized meeting cases before relying on the skill in repeated workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-meeting) <br>
- [README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Structured Markdown response with a parameter status table and meeting-preparation sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided meeting details and at least one reliable evidence source; asks for missing critical parameters before final analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
