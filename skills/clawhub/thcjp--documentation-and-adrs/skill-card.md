## Description: <br>
Automates documentation and ADR handling with structured input and output, multi-format support, and error handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering teams, and automation users use this skill to create or manage documentation and architecture decision records with structured outputs and repeatable workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command-execution capability and includes broad API and credential guidance beyond its documentation-and-ADR purpose. <br>
Mitigation: Use it in a constrained environment, avoid providing secrets unless the exact API use is understood, and require explicit approval for command execution. <br>
Risk: The documented automation behavior is broad and may not define a tightly bounded workflow for each task. <br>
Mitigation: Limit use to documentation and ADR workflows, review proposed outputs before applying them, and confirm inputs and file targets before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/documentation-and-adrs) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include execution status, metadata, and error details when producing structured results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
