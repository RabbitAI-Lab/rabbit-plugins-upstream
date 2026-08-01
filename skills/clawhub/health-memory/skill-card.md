## Description: <br>
Give AI agents Remember health and fitness goals. using BlueColumn persistent memory. Use when an agent tracks health habits and goals; when the user wants to store, recall, or search health memory context. Requires a BlueColumn API key (bc_live_*). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to recall, store, and search health or fitness goal context in BlueColumn persistent memory. It is intended for personalized health habit tracking when the user has supplied a BlueColumn API key and opted in to storing notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive health or fitness information may be sent to a third-party memory service. <br>
Mitigation: Use the skill only with clear user opt-in, store explicit narrow notes, and avoid automatic summaries that include unnecessary medical details. <br>
Risk: Retention and deletion controls for stored health memory are not documented in the artifact evidence. <br>
Mitigation: Confirm BlueColumn retention and deletion behavior before using the skill with sensitive personal information. <br>
Risk: The skill requires a live BlueColumn API key. <br>
Mitigation: Store the API key only in the platform secret store or approved tooling, and review generated curl commands before execution. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/health-memory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends user-provided health memory text or recall queries to BlueColumn endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
