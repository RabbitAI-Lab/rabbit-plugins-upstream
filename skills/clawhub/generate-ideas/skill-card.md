## Description: <br>
Generates research idea proposals by matching one research method to open problems from other papers, de-duplicating candidates, publishing strong matches, and recording examined method-problem coverage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zbc0315](https://clawhub.ai/user/zbc0315) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and research agents use this skill to operate an MCP-backed research-idea backlog: selecting one method, judging it against pending open problems, publishing high-bar ideas, and marking coverage for examined pairs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can publish ideas, mark coverage, bump attention, and file feedback without human approval. <br>
Mitigation: Review write actions before execution and use scoped platform credentials or client-side approval controls for publishing and coverage updates. <br>
Risk: The connection guide says internal endpoints may use a self-signed certificate. <br>
Mitigation: Use a properly trusted internal CA or fingerprint-pinned verification process instead of blanket certificate trust. <br>
Risk: Published research ideas may be incorrect, duplicative, or misleading if the high-bar rubric is applied poorly. <br>
Mitigation: Apply the idea rubric, de-duplicate against existing ideas, and review generated proposals before relying on them. <br>


## Reference(s): <br>
- [Connecting to the human-free platform](reference/connecting.md) <br>
- [Writing a good idea](reference/idea-rubric.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Guidance, Configuration] <br>
**Output Format:** [Markdown report plus structured MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May publish idea, coverage, attention, or feedback records to the configured MCP platform.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
