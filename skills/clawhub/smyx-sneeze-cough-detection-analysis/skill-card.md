## Description:

Analyzes pet videos, optionally with audio, to identify and record possible sneezing and coughing events for observation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, veterinary teams, and boarding staff can use the skill to review pet video, optionally with audio, and track possible sneeze or cough events over time. It provides behavioral observations and report links, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only option may still run analysis.

Mitigation: Do not rely on export-only behavior until it is fixed; verify what the command will do before running it.

Risk: Video is sent to a provider, and the supplied security guidance says retention practices need review.

Mitigation: Review the provider's retention practices and account controls, and avoid sensitive footage until those safeguards are understood.

Risk: Saved account credentials lack clear destination safeguards.

Mitigation: Wait for credential destination restrictions to be fixed before using real credentials; review the configured destinations first.

## Reference(s):

- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-sneeze-cough-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report in JSON or Markdown, with event observations and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event timing and frequency; results are for behavioral observation and are not a veterinary diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
