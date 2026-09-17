## Description:

OSS Insight (ossinsight.io) lets an agent search and read OSS Insight repository analytics through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve OSS Insight analytics for GitHub repositories, including stars, issues, pull requests, creators, countries, organizations, collections, trending repositories, and rankings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup guidance includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only from a verified source or inspect the installer before running it; do not let an agent execute the remote installer pipeline automatically.

Risk: The skill depends on the OOMOL oo CLI and a signed-in OOMOL account for connector execution.

Mitigation: Use the skill only when the user is comfortable with that dependency, and sign in only when intentionally using OSS Insight.

## Reference(s):

- [OSS Insight](https://ossinsight.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ossinsight)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns OSS Insight data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
