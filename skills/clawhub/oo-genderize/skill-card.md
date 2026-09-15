## Description:

Provides agent guidance for using Genderize through OOMOL's oo CLI to predict gender probabilities for individual names or batches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route Genderize requests through an OOMOL-connected account, including single-name predictions and batch predictions for up to 10 names.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts for the oo CLI.

Mitigation: Use a verified, user-reviewed installation method for the oo CLI before running the skill.

Risk: The skill relies on OOMOL as an intermediary for Genderize requests and credential handling.

Mitigation: Use the skill only when the user accepts OOMOL-mediated access and has connected the intended Genderize account.

## Reference(s):

- [ClawHub Genderize skill page](https://clawhub.ai/oomol/skills/oo-genderize)
- [Genderize homepage](https://genderize.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON response expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction; documented batch requests support up to 10 names.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
