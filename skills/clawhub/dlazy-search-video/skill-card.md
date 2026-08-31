## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to search for stock video material by keyword and retrieve video URLs and metadata for footage sourcing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends search terms to dLazy as an intermediary for Pixabay-style video search and requires a dLazy account or API key.

Mitigation: Use npx for one-off use, avoid passing local file paths or --save unless uploads or downloads are intended, and rotate or revoke the dLazy API key when access is no longer needed.

Risk: The documentation contains inconsistent parameter examples for the search command.

Mitigation: Use dlazy search_video -h before execution and prefer --query for search terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include asynchronous task metadata when --no-wait is used.]

## Skill Version(s):

1.3.11 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
