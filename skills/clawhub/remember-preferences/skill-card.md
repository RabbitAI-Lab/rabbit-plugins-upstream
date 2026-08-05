## Description: <br>
A preference ledger that lets agents honor how each user likes things done - tone, tools, timing, and turn-offs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to record and recall user preferences so interactions can match a user's stated tone, timing, tooling, and communication rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Named preferences may include personal, workplace, or sensitive information that is sent to BlueColumn/Supabase-hosted endpoints. <br>
Mitigation: Use the skill only where users understand that preference data may be sent to those endpoints, and avoid sensitive details unless the user explicitly agrees. <br>
Risk: The workflow encourages immediate storage without clear consent, deletion, or data-minimization guidance. <br>
Mitigation: Confirm high-stakes preferences, store only the minimum useful rule, and review retention or deletion expectations before deployment. <br>


## Reference(s): <br>
- [BlueColumn API reference](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/remember-preferences) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance, configuration] <br>
**Output Format:** [Markdown with bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BLUECOLUMN_API_KEY credential and sends requests to BlueColumn/Supabase-hosted endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
