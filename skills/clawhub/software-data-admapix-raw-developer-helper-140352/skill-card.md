## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams plan and validate AdMapix-style software/data workflows for bug fixing, setup hardening, reliability improvements, and adjacent skill development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, AI-agent users, skill authors, maintainers, and teams use this skill to turn AdMapix-style software/data requests into actionable workflows, artifacts, checklists, code changes, and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has overly broad activation wording and may be invoked for loosely related software/data requests. <br>
Mitigation: Prefer explicit invocation by skill name when using it for AdMapix-style workflow support. <br>
Risk: The skill produces advisory workflow, code, command, and configuration guidance that may be incomplete or incorrect for a specific environment. <br>
Mitigation: Review proposed changes before execution and run the verification steps included with the output. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/software-data-admapix-raw-developer-helper-140352) <br>
- [AdMapix Demand Signal](https://clawhub.ai/skills/admapix) <br>
- [Agent Template Security Signal](https://github.com/fips-agents/agent-template/issues/230) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with optional code blocks, shell commands, checklists, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, constraints, validation steps, and remaining risks when relevant] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
