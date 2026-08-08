## Description: <br>
Give AI agents Remember courses and lessons learned using BlueColumn persistent memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and agent developers use this skill to recall prior learning context, personalize responses from stored lessons, and persist new learning summaries to BlueColumn memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Learning conversations may be sent to and retained by an external persistent memory service. <br>
Mitigation: Review the stored content before submission, avoid secrets and sensitive personal data, and use only a BlueColumn API key controlled by the deploying user or organization. <br>
Risk: The artifact does not describe opt-in, minimization, deletion, or retention controls for stored memory. <br>
Mitigation: Confirm BlueColumn retention and deletion controls before using the skill for private, regulated, or confidential learning records. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/learning-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline bash commands and API usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends recall, note, and memory requests to an external persistent memory service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
