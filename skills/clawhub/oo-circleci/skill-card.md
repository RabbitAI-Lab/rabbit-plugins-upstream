## Description:

Provides agent guidance for operating CircleCI through the OOMOL oo CLI connector, including read operations and guarded pipeline triggers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect CircleCI projects, pipelines, workflows, jobs, artifacts, users, environment variables, and Insights metrics. It can also help trigger project pipelines when the user confirms the payload and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands that execute downloaded shell or PowerShell content.

Mitigation: Review the oo CLI installation path before installing and prefer an official, versioned installer or package-manager flow with integrity verification.

Risk: The skill can trigger CircleCI project pipelines, which changes CircleCI state.

Mitigation: Confirm the exact action payload and intended effect with the user before running a write action.

## Reference(s):

- [CircleCI homepage](https://circleci.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-circleci)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CircleCI connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
