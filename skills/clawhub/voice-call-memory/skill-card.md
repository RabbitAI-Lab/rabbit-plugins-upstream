## Description: <br>
Memory for voice agents and voice-first workflows that stores and recalls call summaries by caller, topic, and outcome so an agent can remember callers across conversations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators of voice agents use this skill to recall caller history at the start of a call, store structured post-call summaries, and hand off context so callers do not need to repeat prior conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Identifiable caller information and call summaries may be sent to and stored in an external BlueColumn/Supabase service. <br>
Mitigation: Use only when the voice-call workflow is authorized to share caller information with that service, and minimize or pseudonymize phone numbers where practical. <br>
Risk: Privacy, consent, retention, deletion, access, and regulated-data handling controls are not described in the evidence. <br>
Mitigation: Define caller consent language and confirm retention, access, deletion, and regulated-data requirements before production use. <br>
Risk: Stored notes may include behavioral or emotional observations about callers. <br>
Mitigation: Avoid unnecessary emotional profiling and keep stored summaries focused on the caller's request, commitments, and operational follow-up. <br>


## Reference(s): <br>
- [BlueColumn API reference](https://bluecolumn.ai/docs) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key supplied as BLUECOLUMN_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
