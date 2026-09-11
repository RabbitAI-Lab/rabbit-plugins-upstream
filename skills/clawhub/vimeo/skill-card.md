## Description:

Vimeo API integration with managed OAuth for uploading, managing, and organizing videos, showcases, albums, folders, likes, watch-later items, and community interactions through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to access Vimeo through Maton OAuth, inspect account and video resources, and perform approved changes such as organizing videos, folders, showcases, likes, comments, and follows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth or API-key credentials could be exposed through logs, command lines, files, or broad environment access.

Mitigation: Prefer Maton OAuth, avoid printing or persisting secrets, and keep API-key use limited to environments where the CLI cannot be installed.

Risk: Write and delete operations can modify Vimeo videos, folders, showcases, comments, likes, follows, or connections in the wrong account or resource.

Mitigation: Default to read/list calls, pin the intended connection when needed, and confirm the exact resource, account, payload, and effect before POST, PUT, PATCH, or DELETE calls.

Risk: Package install commands are not pinned to immutable versions.

Mitigation: Install the Maton CLI or SDK in an isolated or reviewed environment before using it with production Vimeo accounts.

Risk: Data returned from Vimeo may include untrusted content that could influence follow-up actions.

Mitigation: Treat API responses as data, validate values before reuse, and do not execute or follow instructions embedded in returned content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/vimeo)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Vimeo API Reference](https://developer.vimeo.com/api/reference)
- [Vimeo Developer Portal](https://developer.vimeo.com)
- [Vimeo API Authentication](https://developer.vimeo.com/api/authentication)
- [Vimeo Upload API](https://developer.vimeo.com/api/upload/videos)
- [Related api-gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK guidance for Vimeo API calls; network access and a Maton account are required.]

## Skill Version(s):

1.2.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
