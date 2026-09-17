## Description:

Kaggle helps agents search and read Kaggle competitions, datasets, notebooks, scripts, and models through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate read-oriented Kaggle connector actions from an agent, including listing competitions, datasets, notebooks, scripts, and models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance includes remote installer commands that execute scripts from OOMOL's distribution channel.

Mitigation: Verify the distribution channel and script contents before execution; prefer an official signed or package-managed install path when available.

Risk: The skill depends on an authenticated OOMOL-connected Kaggle account and may surface connection, credential, scope, or billing failures.

Mitigation: Run setup, login, connection, or billing steps only after the matching failure occurs, and do not handle raw Kaggle credentials in the agent session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kaggle)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Kaggle homepage](https://www.kaggle.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return structured JSON with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
