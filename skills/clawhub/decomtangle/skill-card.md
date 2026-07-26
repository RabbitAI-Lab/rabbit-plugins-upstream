## Description: <br>
Decomtangle teaches OpenClaw-style agents to execute multi-step, stateful procedures as atomic observable tool calls, with observation between steps and verification before reporting side effects as complete. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jason-vaughan](https://clawhub.ai/user/jason-vaughan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and agent builders use this skill to reduce silent stalls, parser failures, and ambiguous side effects when agents run browser automation, API sequences, migrations, or other multi-step tool workflows. It is a tool-stepping discipline rather than a planner, router, or model-selection skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may increase the number of small tool calls an agent makes during multi-step workflows. <br>
Mitigation: Use the included single-call guidance and targeted-read practices so only stateful or decision-dependent steps are decomposed. <br>
Risk: The skill changes how an agent uses already-granted tools, so real-world risk depends on the underlying tools and task domain. <br>
Mitigation: Review it together with any high-impact domain skills and require verification before reporting side-effecting work as complete. <br>


## Reference(s): <br>
- [Decomtangle on ClawHub](https://clawhub.ai/jason-vaughan/skills/decomtangle) <br>
- [Decomposition heuristics](references/decomposition-heuristics.md) <br>
- [Atomic-call checklist](references/atomic-call-checklist.md) <br>
- [Bad mega-script stall example](examples/bad-mega-script-stall.md) <br>
- [Good multicalendar atomic example](examples/good-multicalendar-atomic.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline command and API-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill changes agent tool-use posture and does not declare tools, permissions, environment variables, network access, or executable code.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release evidence; release notes state content is identical to 0.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
