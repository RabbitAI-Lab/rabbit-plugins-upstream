## Description: <br>
Measure a skill's reliability by running Caliper evaluations, interpreting results, and helping design .eval.yaml specs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edonadei](https://clawhub.ai/user/edonadei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to validate, run, extend, and interpret Caliper evaluation specs for agent skills. It helps compare a skill against a baseline, measure pass@k reliability, and turn expected behavior into observable eval tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Evaluation specs can execute setup, cleanup, assertion blocks, and MCP declarations through Caliper. <br>
Mitigation: Review each .eval.yaml file before running it, including command blocks, assertions, environment-variable references, and MCP server declarations. <br>
Risk: Saved Caliper results may include private prompts, files, or tool outputs when transcripts are recorded. <br>
Mitigation: Treat .caliper result files as sensitive, avoid committing private run artifacts, and review result JSON before sharing it. <br>


## Reference(s): <br>
- [Evaluate Skill on ClawHub](https://clawhub.ai/edonadei/skills/evaluate-skill) <br>
- [Caliper Reference](REFERENCE.md) <br>
- [Evaluate Skill Eval Spec](evaluate-skill.eval.yaml) <br>
- [Simple Eval Example](references/examples/simple.eval.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline YAML, Python, and bash snippets; may create or edit .eval.yaml specs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for Caliper workflows and may reference saved .caliper result JSONs.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
