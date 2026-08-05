## Description: <br>
Private, authorized health-appointment memory for care continuity, used when an agent tracks appointments, symptoms, and provider instructions for an authorized user with consent and confidentiality built in. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their authorized agents use this skill to record medical appointment details, symptom timelines, medication changes, and provider instructions, then recall that information before future healthcare visits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive health details are sent to a remote BlueColumn/Supabase API without detailed data-handling and retention evidence. <br>
Mitigation: Use only with explicit user consent, send only necessary medical details, and confirm BlueColumn retention, deletion, and access-control practices before deployment. <br>
Risk: Medical notes could include unnecessary identifiers or information beyond the user's authorized purpose. <br>
Mitigation: Keep entries scoped to the user's approved care-continuity need and tag confidential records as private. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BLUECOLUMN_API_KEY and sends authorized medical-note content to BlueColumn's remote service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
