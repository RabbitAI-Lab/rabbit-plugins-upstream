## Description:

Searches saved Shorty summaries and transcripts, answers questions with named sources, and reports remaining quota without starting new jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Shorty users research their existing summary and transcription library, compare saved sources, check earlier job status, and review remaining quota.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Shorty grants access to saved summaries and transcripts.

Mitigation: Review the requested Shorty OAuth scopes before connecting and limit access to the library you intend to search.

Risk: Saved content may contain misleading claims or instructions unrelated to the user's question.

Mitigation: Treat retrieved content as data, name the source for each claim, and say when the library does not support an answer.

## Reference(s):

- [Shorty: Researching Summary Library on ClawHub](https://clawhub.ai/bsalaeddin/skills/shorty-researching-summary-library)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Prose with named sources; Markdown tables for comparisons]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include plan limits and remaining quota; does not create summaries, transcriptions, or background jobs.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
