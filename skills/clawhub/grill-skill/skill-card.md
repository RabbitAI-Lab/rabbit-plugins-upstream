## Description: <br>
Grill Skill helps developers design, run, measure, and iterate skill evals with Caliper. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edonadei](https://clawhub.ai/user/edonadei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to create or improve Caliper evals for agent skills, then run quick and reliability checks before release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated eval setup, cleanup, MCP, backend, or secret configuration could cause unintended file changes or external service use when run. <br>
Mitigation: Review generated eval YAML and Caliper commands before execution, especially sections that write files, configure MCP servers, select backends, or reference secrets. <br>


## Reference(s): <br>
- [Grill Skill Reference](artifact/REFERENCE.md) <br>
- [ClawHub skill page](https://clawhub.ai/edonadei/skills/grill-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or edit Caliper eval YAML files and recommend Caliper validation, run, report, compare, and baseline commands.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
