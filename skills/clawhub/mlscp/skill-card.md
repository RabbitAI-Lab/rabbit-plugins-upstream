## Description: <br>
Mlscp helps agents parse, validate, and generate compact MLSCP commands for token-efficient agent-to-agent communication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sirkrouph-dev](https://clawhub.ai/user/sirkrouph-dev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use Mlscp as a protocol-reference skill for parsing, validating, and generating compact MLSCP commands when coordinating agent-to-agent work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Compact MLSCP commands can describe file reads, writes, modifications, and deletes in abbreviated form. <br>
Mitigation: Expand compact commands into plain language, validate target paths, and obtain user approval before execution. <br>
Risk: The skill artifact references scripts and a Python API that are not included in the provided artifact. <br>
Mitigation: Inspect any referenced scripts or Python package separately before running or integrating them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sirkrouph-dev/skills/mlscp) <br>
- [GitHub project listed in skill artifact](https://github.com/sirkrouph-dev/mlcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with command examples and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Protocol examples should be expanded and reviewed before any file operation is executed.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
