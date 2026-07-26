## Description: <br>
Ensures all relative time or current event queries first obtain the current date via session_status to provide accurate, up-to-date answers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to make assistants resolve the current date before answering relative-time or current-events questions, reducing wrong-year searches and unsupported time-sensitive claims. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make an agent more conservative on current-events and relative-date questions by requiring a current-date check and tool-backed answers. <br>
Mitigation: Install where explicit time verification is desired, and review agent behavior to ensure the added caution matches the deployment's response expectations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/time-awareness) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text] <br>
**Output Format:** [Markdown instructions for agent behavior] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Directs agents to call session_status before relative-time or current-events queries and to limit answers to current-session tool evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
