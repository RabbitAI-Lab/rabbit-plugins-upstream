## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agents use the skill to find stock video footage by keyword and retrieve matching video URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires dLazy authentication and invokes an external CLI whose behavior was not established by the partial scan.

Mitigation: Before installing, consider whether you are comfortable using dLazy authentication and the external CLI; review the declared CLI package information and use the pinned version specified by the skill.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON search results containing stock video URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the search query and available Pixabay footage.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
