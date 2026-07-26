## Description: <br>
绿灵 · Blooming Elf helps users create plant-care records, receive watering and fertilizing reminders, diagnose plant status, and maintain long-term care logs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shirley1011](https://clawhub.ai/user/shirley1011) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External plant owners and hobbyists use this skill to set up plant profiles, track watering and care history, receive reminders, and get concise plant-care guidance from conversation and saved records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may save plant-care details locally or in IMA notes. <br>
Mitigation: Review ~/.workbuddy/MEMORY.md and any created plant files or IMA notes to audit, edit, or remove saved data. <br>
Risk: Broad activation phrases can cause the plant-care workflow to start during related conversations. <br>
Mitigation: Confirm the intended task before allowing the skill to create notes, update records, or configure reminders. <br>
Risk: Weather or plant lookups may affect watering advice and can be unavailable or inaccurate. <br>
Mitigation: Use observed plant condition and local environment data as the final check before acting on care guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shirley1011/skills/lvling) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Conversational text with Markdown tables, note templates, care-log entries, and reminder configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save plant-care details locally or in IMA notes and may configure reminders after user confirmation.] <br>

## Skill Version(s): <br>
3.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
