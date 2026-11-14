## Description:

Turn a novel into a fully playable game on the selected target platform, orchestrating requirements intake, story analysis, game and art design, environment-adapted building, and blind-playtest QA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Novelists, game designers, and developers can use this skill to turn a novel or writing project into a playable game. It coordinates source analysis, interactive concept and art direction, implementation, and playtest-based quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security analysis coverage is partial because several local references could not be resolved in the release bundle.

Mitigation: Review the complete reference set and scan the installed skill bundle before deployment.

Risk: The full workflow depends on companion skills that ClawHub does not install automatically.

Mitigation: Install the four companion skills at the versions listed in INSTALL.md before running the complete pipeline.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/novel-to-game)
- [Pipeline contract](references/pipeline-contract.md)
- [Intake method](references/intake-method.md)
- [Companion skill installation](INSTALL.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown project documents, game source code, configuration, and QA verification records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs follow the selected target platform, language, and project scope; implementation and playtest results depend on the available tools and environment.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
