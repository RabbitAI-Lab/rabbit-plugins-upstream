## Description: <br>
Implements structured usage logging and audit trails for cost and session tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add local structured JSONL usage logging, session tracking, audit trails, and cost or analytics queries to agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local usage logs can retain sensitive operational details if prompts, secrets, file contents, customer data, or other sensitive values are placed in metadata fields. <br>
Mitigation: Keep sensitive details out of log metadata and periodically review or delete logs under ~/.claude/leyline/usage when retention matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-usage-logging) <br>
- [Leyline homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with JSON, Python, YAML, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes JSONL log schemas, session lifecycle patterns, default local log storage, and query examples.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
