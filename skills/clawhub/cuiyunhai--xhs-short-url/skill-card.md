## Description:

Converts batches of Xiaohongshu note links into shareable xhslink.com short links using a paid third-party service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to shorten batches of Xiaohongshu note URLs for sharing and review the resulting links or export task results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default HTTP service endpoint can expose account tokens and submitted links in transit.

Mitigation: Use a valid HTTPS service endpoint; do not send tokens or links over untrusted networks with the HTTP default.

Risk: The paid third-party service stores a bearer token in local configuration.

Mitigation: Use the service only if its pricing and local token storage are acceptable; protect the local configuration and avoid sharing the token.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cuiyunhai/skills/xhs-short-url)
- [ClawHub publisher profile](https://clawhub.ai/user/cuiyunhai)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON results containing short links; optional CSV export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports batches of up to 50 links and asynchronous task polling.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
