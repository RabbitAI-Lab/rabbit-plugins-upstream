## Description:

Provides concise, source-backed answers to factual questions and claims using bounded web searches and explicit confidence labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vincentjiang06](https://clawhub.ai/user/vincentjiang06)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and other users can quickly check a factual question or claim and receive a short answer with sources, supporting evidence, and a confidence rating. It is not intended for exhaustive research reports or subjective recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unpinned remote installation command in the README may fetch an unreviewed release.

Mitigation: Install the reviewed ClawHub artifact or pin a known release.

Risk: The advertised speed targets are not established by the bundled comparison against a baseline.

Mitigation: Treat the time targets as goals rather than guaranteed performance.

Risk: Fact-checking may send search queries to external web services; a structurally valid answer may still cite unsupported claims.

Mitigation: Avoid putting sensitive data in search queries and read each cited page to confirm it supports the answer.

## Reference(s):

- [ClawHub fact-check skill listing](https://clawhub.ai/vincentjiang06/skills/fact-check)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bottom-line answer with tier, confidence, cited evidence, numbered sources, and caveats when needed. The optional validator checks format and citation resolution, not factual support.]

## Skill Version(s):

1.1.0 (source: server-resolved release, skill metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
