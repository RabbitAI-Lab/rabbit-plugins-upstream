## Description:

Provides agents with Keyword.com read access through OOMOL's oo CLI for user profiles, projects, regions, keywords, and ranking data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Keyword.com account, project, region, keyword, and ranking data from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may ask users to run an unverified internet installer directly in a shell.

Mitigation: Review the setup path before installing the oo CLI, prefer a verified or pinned installation source, and connect only a Keyword.com account whose accessible projects and keywords are appropriate to expose through OOMOL connector calls.

## Reference(s):

- [Keyword.com homepage](https://keyword.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-keyword)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should fetch the live connector schema before constructing request payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
