## Description: <br>
Enable agents to collaborate using shared memory, team inboxes, and user artifacts via Fulcra's versioned file storage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulcra](https://clawhub.ai/user/fulcra) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to set up Fulcra-backed team workspaces, exchange inbox messages, preserve shared progress, and store approved user artifacts across one or more agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shared team memory can expose private workspace context or files to another agent or principal. <br>
Mitigation: Require explicit authorization before transferring data between agents, define the team and allowed data scope up front, and avoid sharing raw private files unless the user clearly intends it. <br>
Risk: Automated heartbeat or cron checks can continue processing team inboxes beyond the user's expected scope. <br>
Mitigation: Enable automation only with explicit consent, document the exact team, inbox, task scope, and duration, and include current team and member context in each automated run. <br>
Risk: Inbox cleanup can remove the visible copy of a task before the agent has preserved it. <br>
Mitigation: Archive the inbox message first, verify the archived file exists, and delete the inbox copy only after that verification succeeds. <br>
Risk: Artifact uploads can store sensitive generated files in Fulcra. <br>
Mitigation: Ask for explicit approval before uploading artifacts and place non-markdown outputs only in the documented artifact namespace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fulcra/skills/fulcra-agent-teams) <br>
- [Fulcra Agent Teams CLI Reference](references/fulcra-agent-teams-cli.md) <br>
- [Fulcra CLI documentation](https://raw.githubusercontent.com/fulcradynamics/agent-skills/main/skills/fulcra-onboarding/references/fulcra-cli.md) <br>
- [Open Knowledge Format specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with file path conventions and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update Fulcra file-store content only after user consent.] <br>

## Skill Version(s): <br>
0.0.8 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
