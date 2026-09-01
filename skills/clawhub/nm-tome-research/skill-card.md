## Description:

Runs multi-source research across GitHub, HN, Reddit, arXiv, and Semantic Scholar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to coordinate technical research across source code, online discussion, academic literature, and TRIZ-style analysis, then synthesize the findings into a local report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research topics and results may be written to local report or session files.

Mitigation: Avoid sensitive topic names or confidential research prompts unless local storage of those details is acceptable.

Risk: The workflow can query external research sources and run parallel research agents.

Mitigation: Use it only in environments where external source queries and multi-agent research activity are approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-tome-research)
- [claude-night-market tome plugin](https://github.com/athola/claude-night-market/tree/master/plugins/tome)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report or brief with JSON-based agent findings and local session files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save reports under docs/research and local session state.]

## Skill Version(s):

1.9.19 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
