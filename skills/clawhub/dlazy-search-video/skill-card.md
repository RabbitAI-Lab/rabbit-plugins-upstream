## Description:

Searches for stock video footage by keyword and returns video URLs and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find stock video footage for their projects by searching keywords and reviewing returned URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the dLazy CLI runs a third-party package.

Mitigation: Review the package and its source before installation.

Risk: Search terms and parameters go to dLazy-hosted services; supplied local media paths may cause file uploads.

Mitigation: Avoid sensitive queries or local file paths unless you intend to share them with dLazy.

Risk: Saved API keys may remain on shared systems.

Mitigation: Use the DLAZY_API_KEY environment variable rather than saved login on shared systems.

Risk: The example command and published release metadata differ from the artifact's CLI help and embedded version.

Mitigation: Check dlazy search_video -h and use the documented --query option before running a search.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with search results and video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include video URLs and metadata; asynchronous requests can return a task ID instead of immediate results.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
