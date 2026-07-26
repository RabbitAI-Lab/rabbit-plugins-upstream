## Description: <br>
Advertised as a JSON string decoder, this skill processes JSON arrays by executing Python snippets found in python_code fields and can write execution results to a JSON file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ltsbihuo](https://clawhub.ai/user/ltsbihuo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and reviewers can use this skill only when they explicitly intend to execute trusted Python snippets embedded in JSON and collect execution status. It should not be treated as a normal JSON string decoding helper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: JSON input can trigger execution of Python code with local user privileges. <br>
Mitigation: Run the skill only with trusted JSON input inside an isolated sandbox with least-privilege filesystem and network access. <br>
Risk: Default detached execution can leave background processes running after the command returns. <br>
Mitigation: Prefer wait-mode execution for review runs and monitor or terminate reported process IDs when detached mode is used. <br>
Risk: The public description as a decoder does not match the observed code execution behavior. <br>
Mitigation: Present the skill as a JSON-driven Python executor and require explicit user confirmation before running it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ltsbihuo/skills/mystrdecoder) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON execution summary and command-line guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include process identifiers, execution counts, result records, errors, and timestamps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
