## Description:

Provides a Xiaohongshu / XHS / RedNote data assistant for hot search lists, note search, note details, comment analysis, creator profiles, and creator note lists using SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve and analyze Xiaohongshu / XHS / RedNote search trends, notes, comments, and creator data through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill submits XHS search terms, note URLs or IDs, and profile URLs to the SocialDataX service.

Mitigation: Confirm users trust the SocialDataX npm package and service before running commands with sensitive or proprietary inputs.

Risk: Returned full note URLs may contain xsec_token query parameters that can be shareable link data.

Mitigation: Preserve full note URLs only where needed for the task and treat them as potentially sensitive when sharing or storing outputs.

## Reference(s):

- [SocialDataX API access page](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and summarized API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node, npm, and SOCIALDATAX_API_KEY. Returned full note URLs should be preserved exactly when displayed or reused.]

## Skill Version(s):

0.1.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
