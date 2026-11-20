## Description:

Video search tool: queries the Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to find stock footage on Pixabay by keyword and refine results by video type, category, or duration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports medium confidence and a partial scan; Skillspector flags a dLazy CLI authentication workflow that is not shown to deliver the stated Pixabay search.

Mitigation: Before installing, review the setup and data-handling steps and confirm that dLazy authentication and CLI use are expected.

## Reference(s):

- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Video URLs, Video metadata]

**Output Format:** [JSON search results containing stock video URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be paginated; asynchronous requests may return a task ID, and assets can optionally be saved locally.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
