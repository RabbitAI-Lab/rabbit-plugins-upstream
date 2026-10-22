## Description:

Automates multi-round code review and improvement with parallel reviews, validation, and a defensive-programming mode for incremental coding tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use Iterate to review, fix, and validate codebases over successive rounds, or to apply defensive checks while completing incremental coding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing instructions may allow pending code to be published despite stating that user approval is required.

Mitigation: Resolve the contradictory instructions before granting push access; initially use a copy without push access and review every configured validation command.

Risk: Installation choices and the build-dependency pin require review.

Mitigation: Select only intended assistants, retain signature verification, and request an updated build-dependency pin.

## Reference(s):

- [Iterate on ClawHub](https://clawhub.ai/jingzhao-l/skills/iterate-skill)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Repository code and file changes, configuration, shell commands, and Markdown guidance or review summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify the target codebase; review changes and validation results before accepting them.]

## Skill Version(s):

3.7.0 (source: release evidence, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
