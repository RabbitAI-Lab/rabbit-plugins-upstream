## Description:

Find Skills recommends relevant WorkBuddy or CodeBuddy skills from built-in, local, cached, and remote sources based on a user's natural-language task description or keyword search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to discover, compare, and optionally install relevant skills for a described task across local directories, built-in WorkBuddy skills, SkillHub, Xiaping, GitHub, ClawHub, and Vercel Skills sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches can send user-provided skill queries to external marketplaces and GitHub.

Mitigation: Avoid sensitive query content in restricted environments and review network destinations before use.

Risk: The skill can install third-party skills into persistent WorkBuddy or CodeBuddy agent directories.

Mitigation: Require explicit installation confirmation, prefer pinned versions or commits, validate archives, and verify publishers before installation.

Risk: A GitHub token may be used automatically when present in the environment.

Mitigation: Use a least-privilege token, unset the token when it is not needed, and avoid exposing credentials in logs or prompts.

Risk: The artifact requires a promotional footer in each result.

Mitigation: Remove or disable mandatory promotional text before enterprise, neutral, or policy-constrained deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guipi888/skills/find-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown recommendations with source labels, match rationale, local paths, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include third-party service names, installation destinations, and install confirmation prompts.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 1.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
