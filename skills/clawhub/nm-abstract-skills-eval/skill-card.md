## Description: <br>
Evaluate Claude skill quality through auditing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to audit Claude and OpenClaw skill packages, evaluate quality, plan improvements, and verify structure, token use, integration, and performance guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Benchmarking and integration-test examples can execute commands against local skill projects. <br>
Mitigation: Run examples only on trusted skill packages, review commands before execution, and use sandboxing for untrusted inputs. <br>
Risk: Examples using --scan-all, --directory ., --auto-fix, chmod, pip install, or CI snippets can inspect or modify project files. <br>
Mitigation: Review scope and flags before running examples, avoid automatic fixes until changes are understood, and keep changes under version control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-skills-eval) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Evaluation criteria](modules/evaluation-criteria.md) <br>
- [Evaluation workflows](modules/evaluation-workflows.md) <br>
- [Skill authoring best practices](modules/skill-authoring-best-practices.md) <br>
- [Integration testing](modules/integration-testing.md) <br>
- [Performance benchmarking](modules/performance-benchmarking.md) <br>
- [Pressure testing](modules/pressure-testing.md) <br>
- [Troubleshooting](modules/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes audit checklists, scoring rubrics, workflow steps, command examples, and configuration examples.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
