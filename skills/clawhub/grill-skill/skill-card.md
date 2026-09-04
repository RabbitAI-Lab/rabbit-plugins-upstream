## Description:

Build and harden a skill with evals — interview to design its eval tasks, then run, measure, and iterate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[edonadei](https://clawhub.ai/user/edonadei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to create, run, and improve Caliper evals for agent skills. It helps interview for eval coverage, serialize eval YAML, run validation and measurement commands, and iterate on results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated eval YAML can include setup, cleanup, and assertion code that affects local files when Caliper runs it.

Mitigation: Review the generated eval spec before execution, especially setup and cleanup commands.

Risk: The workflow relies on local Caliper execution and model CLI configuration.

Mitigation: Run it only in an intended workspace and confirm Caliper plus model CLI credentials are configured intentionally.

## Reference(s):

- [Grill Skill Reference](artifact/REFERENCE.md)
- [ClawHub Skill Page](https://clawhub.ai/edonadei/skills/grill-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML eval specifications and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update .eval.yaml files and suggest Caliper validation, run, report, and compare commands.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
