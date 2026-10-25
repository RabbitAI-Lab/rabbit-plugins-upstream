## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to search Pixabay for stock footage by keyword and retrieve matching video URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI package is pinned to a specific version and may execute code on the user's system.

Mitigation: Review the pinned @dlazy/cli version before installation, as the skill's security guidance recommends.

Risk: Search requests pass through dLazy and may consume organization credits; the documented example uses --prompt although the option list specifies --query.

Mitigation: Use --dry-run to review the payload and estimated cost, and confirm the correct query syntax before sending a request.

Risk: Authentication can save an organization API key in the local dLazy CLI configuration.

Mitigation: Restrict access to the local configuration and rotate or revoke the key if it may have been exposed.

Risk: The server-resolved release is 1.3.34, while the supplied artifact frontmatter says 1.3.6.

Mitigation: Confirm the artifact version matches the intended release before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Structured data, URLs, Metadata]

**Output Format:** [JSON containing matching stock-video URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches may run asynchronously; results can be saved to a local path.]

## Skill Version(s):

1.3.34 (source: server-resolved release evidence; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
