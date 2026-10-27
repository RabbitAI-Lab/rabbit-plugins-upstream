## Description:

Finds newly seen AI models, products, and repositories, then ranks related keywords by estimated demand and search opportunity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuyansen](https://clawhub.ai/user/zhuyansen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover emerging AI names and decide which related search terms merit a page or tool. It can also research names supplied by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries are sent to external providers, and installing the pinned Python package requires trusting code outside the supplied artifact.

Mitigation: Review configured sources and approve estimated API costs before paid runs; install only the pinned release from a source you trust.

## Reference(s):

- [Clawhub skill release](https://clawhub.ai/zhuyansen/skills/new-term-radar)
- [Example source configuration](https://github.com/zhuyansen/new-term-radar/blob/v0.6.0/config.example.json)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Markdown report or JSON data with a keyword priority table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes estimated search demand, prioritization, and applicable source and estimate caveats.]

## Skill Version(s):

0.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
