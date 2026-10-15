## Description:

Analyzes pet video, with optional audio, to identify sneezing and coughing events and report their frequency and timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet caregivers, veterinary teams, and boarding staff use the skill to review pet camera footage for possible sneezing or coughing episodes and consult current or historical analysis reports. Results support observation, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet camera media or media URLs are sent to LifeEmergence cloud services.

Mitigation: Use only footage approved for cloud processing and review the destination before installation.

Risk: An automatically managed account reuses tokens stored in the workspace data directory.

Mitigation: Restrict access to the workspace data directory and review identity and token handling before use.

Risk: Cloud report history may be associated with a reused identity in shared environments.

Mitigation: Avoid multi-user deployment until report ownership and access controls are verified.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-sneeze-cough-detection-analysis)
- [Pet sneeze/cough API documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional result file; analysis and history reports may include report links.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
