## Description:

Analyzes pet video, optional audio, and remote media URLs to identify sneeze and cough events, distinguish occasional from repeated episodes, and return structured observation reports with event timing, frequency, and links to cloud reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet-care operators use this skill to review pet camera footage for sneeze and cough behavior, including event type, frequency, timing, and non-diagnostic observation guidance. It is suited to home monitoring, veterinary ward observation, and pet boarding scenarios where media can be sent to the configured cloud analysis service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, optional audio, and remote media URLs are sent to the configured cloud analysis service.

Mitigation: Use only media that is appropriate for cloud processing and avoid private, internal, or sensitive household URLs unless that data sharing is acceptable.

Risk: The skill can create or reuse an account identity, store tokens locally, and retrieve cloud report history.

Mitigation: Review account and token handling before installation and run the skill only in environments where cloud-linked report history is expected.

Risk: The behavior analysis output may be mistaken for medical diagnosis.

Mitigation: Treat results as observation support only and refer frequent or severe symptoms to a veterinarian.

## Reference(s):

- [Pet sneeze/cough API documentation](references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text reports with optional JSON detail and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can query cloud report history and can write the generated analysis output to a caller-specified path.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
