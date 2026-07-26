## Description: <br>
Runs local awareness sensors, scores observations, and records significant events for an OpenClaw agent while requiring explicit notification recipients and bounded state retention. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[palxislabs](https://clawhub.ai/user/palxislabs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to run a local always-on awareness layer that watches configured paths, scores events, and queues important observations for agent attention. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Always-on local monitoring can record file activity and other local observations in state files. <br>
Mitigation: Keep watched paths narrow, avoid sensitive folders, and schedule the retention pruning script with limits appropriate for the environment. <br>
Risk: Custom sensors, and disabled audio or vision sensor stubs if enabled or replaced, can expand privacy exposure. <br>
Mitigation: Review sensor code and privacy implications before enabling custom, audio, or vision sensors. <br>
Risk: Observed content could be mistaken for instructions if consumed without guardrails. <br>
Mitigation: Treat sensor output as untrusted observations and require explicit confirmation for sensitive external actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/palxislabs/skills/ambient-awareness-local) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples; runtime state is JSON and JSONL.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local event logs and wake-request records; notifications require an explicit target.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
