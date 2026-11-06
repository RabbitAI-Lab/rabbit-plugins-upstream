## Description:

Adds an experience-inheritance workflow for coding agents by recalling validated fixes, tracking their use, and saving new fixes, with optional controlled experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to recall relevant, reviewed fixes at the start of coding tasks and record useful fixes after solving non-obvious failures. It also provides an optional controlled workflow for measuring whether experience inheritance helps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared or imported fixes and exports may expose private information or introduce unreviewed content into agent context.

Mitigation: Use local recall where possible, review imported fixes individually, keep community imports quarantined, and inspect full exports before sharing.

Risk: Installing hooks or configuration can affect existing files.

Mitigation: Back up existing hooks and configuration before installation.

Risk: Controlled experiments may affect project files or send inputs to a model provider.

Mitigation: Run experiments in a disposable clone with an isolated experience store and fresh output directory; use an approved provider and no confidential inputs.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Publisher profile](https://clawhub.ai/user/stwhwing)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Numbered fix suggestions and Markdown command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recall results are limited to relevant reviewed fixes; experiments are optional.]

## Skill Version(s):

0.37.0 (source: SKILL.md frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
