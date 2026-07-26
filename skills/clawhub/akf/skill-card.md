## Description: <br>
Agent Knowledge Format helps agents stamp trust metadata into files, including trust scores, provenance, evidence, labels, and replay recipes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hmakt99](https://clawhub.ai/user/hmakt99) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to check, stamp, inspect, audit, and replay AKF trust metadata for files an AI agent creates or modifies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides agents to mutate files by stamping or embedding AKF metadata. <br>
Mitigation: Use deliberately and avoid signed, hash-sensitive, third-party, or confidential files unless embedded metadata is intended. <br>
Risk: AKF replay recipes can execute recorded commands when run with --run. <br>
Mitigation: Read and trust replay recipes before execution, preferably in a constrained workspace. <br>


## Reference(s): <br>
- [AKF website](https://akf.dev) <br>
- [AKF GitHub repository](https://github.com/HMAKT99/AKF) <br>
- [AKF schema specification](https://github.com/HMAKT99/AKF/blob/main/spec/akf-v1.1.schema.json) <br>
- [ClawHub skill page](https://clawhub.ai/hmakt99/skills/akf) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown] <br>
**Output Format:** [Markdown with inline bash command examples and configuration metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the akf CLI for command execution; optional pip and npm installation paths are documented.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
