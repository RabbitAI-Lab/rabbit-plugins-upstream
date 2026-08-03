## Description: <br>
Guides an agent through live WeChat Mini Program debugging with the system `vince-mp` JSON CLI, including session startup, runtime inspection, uid-based actions, scans, console and doctor checks, log correlation, and failure handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to debug a live WeChat Mini Program runtime through a persistent local CLI session. It is suited for inspecting page data, querying and acting on UI elements, running camera-less scan checks, diagnosing DevTools connection failures, and correlating client errors with backend logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control a live WeChat Mini Program runtime through tap, input, scan, navigation, storage, media, and log-related commands. <br>
Mitigation: Use non-production targets when possible, ask for explicit authorization before side-effecting actions, and verify each action with the CLI's JSON evidence. <br>
Risk: Backend environment and log commands may target the wrong environment or require administrative tokens. <br>
Mitigation: Confirm the selected backend environment before env or log commands, provide admin tokens only when needed, and report backend/log failures with the returned error code. <br>
Risk: Live runtime evidence can be misleading when the simulator is not running, DevTools automation is unavailable, or asynchronous UI handlers have not settled. <br>
Mitigation: Run the documented session, doctor, wait, and re-poll workflows before concluding results, and report failures such as `APP_NOT_RUNNING`, `AUTOMATION_PORT_TIMEOUT`, or `STALE_OR_UNKNOWN_UID` verbatim. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vincentjiang06/skills/mp-cli-sup) <br>
- [Runtime Protocol](rules/runtime-protocol.md) <br>
- [CLI Contract](references/cli-contract.md) <br>
- [Evidence and Known Failures](references/evidence-and-failures.md) <br>
- [Skyline Media](references/skyline-media.md) <br>
- [Skill Design Record](assets/skill-design-record.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are expected to return structured JSON evidence from the `vince-mp` CLI; file outputs must stay under the workspace root.] <br>

## Skill Version(s): <br>
0.2.2 (source: server release evidence, frontmatter metadata, and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
