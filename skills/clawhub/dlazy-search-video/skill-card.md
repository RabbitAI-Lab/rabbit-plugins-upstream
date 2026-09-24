## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search for stock video footage by keyword and receive video URLs and metadata for sourcing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party dLazy CLI stores an API key locally and sends search inputs to dLazy endpoints.

Mitigation: Install and use only when that SaaS flow is acceptable; rotate or revoke the dLazy API key from the publisher dashboard if access should be removed.

Risk: Local file paths passed through media-related options may be uploaded to dLazy-hosted storage.

Mitigation: Avoid passing local file paths unless upload is intended, and review command arguments before execution.

Risk: The artifact documents both --query and --prompt usage for search_video, which may confuse routine use.

Mitigation: Check `dlazy search_video -h` and prefer the server-reported help output before automating repeated calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [json, shell commands, configuration, guidance]

**Output Format:** [JSON responses with video URLs and metadata, plus command-line setup or error-handling guidance when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy CLI authentication; --no-wait can return an asynchronous task identifier instead of immediate outputs.]

## Skill Version(s):

1.3.21 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
