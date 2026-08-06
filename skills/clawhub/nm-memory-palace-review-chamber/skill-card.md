## Description: <br>
Captures and retrieves PR-review findings in memory palaces for future architectural decisions, patterns, standards, and lessons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill after PR reviews to capture durable review findings, classify them into project memory rooms, and retrieve relevant past decisions during future work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist private PR review context, including participant names, file references, findings, and architectural decisions. <br>
Mitigation: Use it only in projects where searchable retention of that review context is acceptable; define retroactive-capture rules and periodically prune outdated or confidential entries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-memory-palace-review-chamber) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/memory-palace) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with structured examples, command snippets, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces review-memory capture and retrieval guidance for an agent; does not itself execute repository changes.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
