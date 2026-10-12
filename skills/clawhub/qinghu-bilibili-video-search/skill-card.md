## Description:

Searches Bilibili videos by keyword and reports titles, duration, engagement metrics, and whether videos are collaborations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and researchers use this skill to find Bilibili videos matching a keyword and review their engagement and collaboration indicators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask the agent to install or upgrade qhkit and Node/npm packages.

Mitigation: Review installation steps and prefer a preinstalled, pinned qhkit version.

Risk: The search requires a qhkit token and paid Qinghu credits.

Mitigation: Keep the token in a managed secret store, review the estimated charge, and approve paid calls before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-bilibili-video-search)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary with optional tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits spent when paid searches run.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
