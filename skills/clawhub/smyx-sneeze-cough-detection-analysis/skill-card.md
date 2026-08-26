## Description:

AI-powered pet sneeze and cough detection analyzes pet video, optionally with audio, to identify respiratory behavior events, frequency, severity patterns, and report links for observation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet-care operators, and developers use this skill to submit pet video or video URLs for sneeze and cough behavior analysis, structured reports, and cloud report history lookup. The output is for behavior observation and does not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet media and identity-linked data to remote services for analysis and report history.

Mitigation: Install and run it only when remote processing and persistent account-linked report history are acceptable for the user and deployment context.

Risk: The skill can automatically create or reuse a local identity and stores account tokens locally.

Mitigation: Review local identity and token storage before deployment, and restrict use to trusted workspaces and accounts.

Risk: Respiratory behavior analysis could be mistaken for veterinary diagnosis.

Mitigation: Present results as observation support only and direct users to veterinary care for frequent, severe, or concerning symptoms.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-sneeze-cough-detection-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write analysis output to a user-specified file path and may return cloud report history.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
