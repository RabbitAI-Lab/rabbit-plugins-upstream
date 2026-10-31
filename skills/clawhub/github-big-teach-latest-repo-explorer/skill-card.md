## Description:

Finds recently created repositories with more than 1,000 stars from a configured list of major technology companies’ GitHub organizations and summarizes a selected repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zengzuo613](https://clawhub.ai/user/zengzuo613)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to discover a recent, high-star repository from a maintained list of major technology organizations and get a structured overview of its purpose and approach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically use a GitHub credential from OpenClaw’s private configuration without clearly disclosing that access.

Mitigation: Remove the automatic ~/.openclaw/.env lookup before use, or ensure the skill cannot read that file. Use a dedicated GitHub token with only the access needed for public-repository discovery.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zengzuo613/skills/github-big-teach-latest-repo-explorer)
- [Publisher profile](https://clawhub.ai/user/zengzuo613)
- [Organization list](references/organizations.json)
- [Output template](references/output_template.md)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Structured Markdown repository summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes repository metadata, candidate statistics, and concise explanations of the project, the problem it addresses, and its approach.]

## Skill Version(s):

1.3.1 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
