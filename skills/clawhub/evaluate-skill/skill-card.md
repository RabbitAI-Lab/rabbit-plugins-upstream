## Description:

Measures a skill's reliability by running repeated Caliper evaluations, helping design or interpret eval specs, and comparing skill runs against ablated base-agent runs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[edonadei](https://clawhub.ai/user/edonadei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to validate, run, compare, and improve Caliper evaluation specs for agent skills. It is suited for reliability measurement, regression checks, ablation comparisons, and guidance on observable pass/fail criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Evaluation specs can run setup and cleanup commands, configure MCP servers, use model CLIs, contact services, consume tokens, and save transcripts or results locally.

Mitigation: Review .eval.yaml files from other parties before running them, with particular attention to shell commands, git sources, MCP configuration, backend selection, environment variables, and output locations.

Risk: The skill can help author or modify evaluation specs, so incorrect guidance or weak pass/fail criteria can produce misleading reliability results.

Mitigation: Validate specs with Caliper, include observable success criteria and deterministic assertions where practical, and compare against an ablated run before treating results as release evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/edonadei/skills/evaluate-skill)
- [Publisher profile](https://clawhub.ai/user/edonadei)
- [Caliper Reference](artifact/REFERENCE.md)
- [Evaluate Skill Eval](artifact/evaluate-skill.eval.yaml)
- [Simple Eval Example](artifact/references/examples/simple.eval.yaml)
- [Bundled Eval Examples](artifact/references/evals/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML snippets and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update .eval.yaml files and may report Caliper validation, run, list, report, or compare results.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
