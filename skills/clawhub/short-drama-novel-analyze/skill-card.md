## Description:

Analyzes user-provided novels into traceable chapter notes, adaptation assessments, story units, character summaries, and short-drama episode candidates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Writers and adaptation teams use this skill to assess whether a novel merits short-drama adaptation and to create source-linked analysis and episode candidates for creator review. It does not write scripts or make final adaptation decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analysis can expose user-provided novel contents in local outputs.

Mitigation: Provide only material the agent may read, keep analysis outputs local, and review them before sharing.

Risk: Analyzing a novel without appropriate rights or proceeding from a sample assessment to full-book analysis prematurely.

Mitigation: Confirm rights to analyze the source and review triage.md before authorizing full-book analysis unless the whole pipeline was explicitly requested.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/short-drama-novel-analyze)
- [Adaptation triage](references/adaptation-triage.md)
- [Chapter extraction](references/chapter-extraction.md)
- [Aggregation and entities](references/aggregation-and-entities.md)
- [Adaptation value](references/adaptation-value.md)
- [Stage contract](references/stage-contract.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, JSONL]

**Output Format:** [Source-linked Markdown analysis, JSON chapter index, and JSONL episode candidates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs stay in the local source-analysis workspace; episode candidates are proposals, not approved scripts.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
