## Description:

Conducts open-ended Q&A on image content based on computer vision and large language models, supporting any questions to receive natural language responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to ask natural-language questions about images or image URLs and receive model-generated visual Q&A results. It can also query cloud report history when the user asks for prior records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends image inputs, questions, and report-history requests to a third-party cloud backend.

Mitigation: Install only when the publisher and backend service are trusted, and avoid sensitive images or questions unless data handling has been approved.

Risk: The evidence security summary reports silent identity handling and reusable local token behavior.

Mitigation: Review identity resolution and token storage behavior before deployment, and use an isolated runtime for initial evaluation.

Risk: The evidence security summary reports an active plaintext development API configuration.

Mitigation: Verify production endpoint configuration before use and remove or disable development HTTP endpoints in deployed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-visual-qa-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, shell commands, guidance]

**Output Format:** [Markdown or JSON text, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include visual question-answering responses, structured analysis content, report links, or report-history tables depending on the requested action.]

## Skill Version(s):

1.0.16 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
