## Description: <br>
JSON Param Parser helps agents inspect provided JSON or log content to find a target parameter's full path, matching values, formatted JSON, and SQL extraction suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mmfeng6](https://clawhub.ai/user/mmfeng6) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data engineers use this skill to locate fields in nested JSON logs, including embedded JSON strings, and to produce SQL get_json_object extraction patterns for downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mmfeng6/skills/json-param-parser) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [JSON parameter parser script](artifact/scripts/json_param_parser.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, guidance] <br>
**Output Format:** [Plain text and Markdown with command examples and SQL snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs parameter paths, matched values, similar-field suggestions, and get_json_object extraction examples from user-provided JSON.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
