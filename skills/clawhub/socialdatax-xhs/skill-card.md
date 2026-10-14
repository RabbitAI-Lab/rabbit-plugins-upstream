## Description:

Helps agents research Xiaohongshu (XHS/RedNote) hot searches, notes, comments, and creator profiles through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to explore Xiaohongshu trends, search notes, inspect note details and comments, and research creators and their posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned npm package can execute changed code with access to the SocialDataX API key.

Mitigation: Review the package and install a pinned version through a controlled path instead of using @latest.

Risk: The data-access process could receive unrelated environment secrets.

Mitigation: Run it with only the required SocialDataX API key and necessary environment variables.

## Reference(s):

- [SocialDataX XHS skill on ClawHub](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with search results, source links, and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data access; requires a SocialDataX API key.]

## Skill Version(s):

0.1.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
