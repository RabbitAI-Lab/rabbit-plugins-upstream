## Description: <br>
Reads Momentum.io meeting, user, signal prompt, signal definition, and signal execution data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operators, and agents use this skill to read Momentum.io meetings, organization users, AI signal prompts, signal definitions, and signal execution data through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Momentum.io meeting, user, signal prompt, definition, and execution data may contain business-sensitive information. <br>
Mitigation: Use the skill only for user-requested Momentum.io read tasks, apply the narrowest useful filters, and avoid exposing returned data beyond the requested answer. <br>
Risk: Broad Momentum.io trigger wording may cause the skill to activate for ambiguous Momentum references. <br>
Mitigation: Confirm the user intends Momentum.io before running connector actions when the request is ambiguous. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-momentum-io) <br>
- [Momentum.io Homepage](https://www.momentum.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Momentum.io connector actions return data with a meta.executionId value.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
