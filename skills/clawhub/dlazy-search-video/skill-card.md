## Description:

Searches for stock video footage by keyword and returns video URLs and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find stock video footage by keyword, duration, category, or video type for media projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries go through dLazy rather than directly to Pixabay.

Mitigation: Share only queries you are comfortable sending to dLazy.

Risk: The dLazy API key is stored in local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

Risk: The external CLI may upload local media supplied to it.

Mitigation: Review the CLI package before use and do not pass private media unless you intend to upload it to dLazy storage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include stock video URLs and metadata; asynchronous requests may return a task ID.]

## Skill Version(s):

1.3.27 (source: ClawHub release; bundled skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
