## Description:

Generates condensed album highlights based on specified keywords or targets, extracting target segments from long videos and compiling them into a summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze local videos or video URLs, find clips matching requested people, scenes, events, or keywords, and produce condensed time-lapse album summaries. It can also return account-scoped history and report links through the configured cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends videos or video URLs to a configured cloud service.

Mitigation: Use it only for media that is acceptable to process with that service, and avoid sensitive family, private, or regulated media unless the account, retention, and authorization model is acceptable.

Risk: The skill creates or reuses local identity state and stores service tokens in the workspace data directory.

Mitigation: Review local workspace data handling before installation and restrict access to token and identity state.

Risk: The skill can list prior account-scoped reports.

Mitigation: Confirm that report-history lookup behavior matches the intended account and privacy expectations before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-custom-timelapse-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown or JSON analysis output with report links; optional file output when an output path is provided.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact SKILL.md frontmatter: 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
