## Description:

Searches for stock video footage by keyword and returns video URLs and metadata through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find stock video footage by keyword and review matching URLs and metadata for their projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes a narrow Pixabay search but also describes broader hosted inference and file uploads.

Mitigation: Confirm what data the CLI sends to dLazy, and do not pass local file paths unless upload is intended.

Risk: The documented search option and example disagree on whether the command takes --query or --prompt.

Mitigation: Check the installed command's help before running searches.

Risk: Using the hosted CLI requires an API key and may download files to the local machine.

Mitigation: Protect the locally stored key and use --save only when a download is intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown summary of video URLs and metadata from JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results require a dLazy API key; optional downloads can save assets locally.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
