## Description:

Provides Xiaohongshu/XHS/RedNote data lookup for hot searches, note search and details, comments, creator profiles, and creator note lists through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, marketers, and agents use this skill to retrieve read-only Xiaohongshu/XHS data for trend research, note analysis, comment analysis, and creator research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to run an unpinned npm package at runtime with SOCIALDATAX_API_KEY.

Mitigation: Review before installing and prefer a pinned, reviewed package version instead of @latest.

Risk: The SocialDataX CLI receives SOCIALDATAX_API_KEY when the skill performs data calls.

Mitigation: Use only when comfortable granting that CLI access to the API key, and manage the key through the user's environment.

Risk: Returned XHS URLs can contain xsec_token values.

Mitigation: Treat tokenized URLs as sensitive and avoid forwarding or storing them unless needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and API-key configuration guidance; returned SocialDataX data may be JSON before the agent summarizes it.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY, node, and npm; returned XHS note URLs may include xsec_token values that should be handled as sensitive.]

## Skill Version(s):

0.1.21 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
