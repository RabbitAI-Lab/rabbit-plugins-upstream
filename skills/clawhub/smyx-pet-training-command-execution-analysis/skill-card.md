## Description:

Analyzes pet training videos or video URLs to determine whether a pet executed Sit, Down, or Stay commands, returning posture-match, timing, success, and report-link information without medical or behavior-therapy guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet training-area videos for command execution, posture matching, response latency, and training report retrieval. It is intended for smart dog-training devices, remote pet training, and behavior-correction workflows, not for medical diagnosis or behavior-therapy plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or supplied video URLs are sent to the publisher's remote analysis service.

Mitigation: Install only when that remote processing is acceptable, and obtain explicit consent before upload or history queries.

Risk: The skill creates or reuses a local account identity and persists tokens locally.

Mitigation: Document account and token storage for users and provide a reset or deletion path for persisted identity data.

Risk: The release includes private development API endpoints.

Mitigation: Replace private development endpoints with intended production HTTPS endpoints before approval.

## Reference(s):

- [Pet Training Command API Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-training-command-execution-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the rendered analysis to a user-specified output file.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter reports 1.0.11 and artifact _meta reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
