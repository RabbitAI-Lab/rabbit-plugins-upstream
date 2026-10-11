## Description:

Searches Douyin videos by keyword and returns video details and engagement metrics, with optional sorting and time or duration filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and researchers use this skill to find Douyin videos matching a keyword and compare their publication dates and engagement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit can change the local tooling environment.

Mitigation: Prefer a preinstalled or pinned qhkit version and review any proposed local installation or upgrade.

Risk: Configuring a Qinghu API token may leave long-lived third-party credentials on the device.

Mitigation: Use an environment variable when possible and avoid persistently storing the token unless needed.

Risk: Paid searches consume Qinghu credits, with charges increasing for larger results.

Mitigation: Check the estimated credit cost and get user approval before paid calls or large searches.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-douyin-video-search)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise answer with a short preview; tabular file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes relevant video metadata, engagement metrics, and credits charged when a paid search runs.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
