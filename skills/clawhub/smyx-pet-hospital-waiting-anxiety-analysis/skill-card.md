## Description:

Analyzes pet hospital waiting-area video files or URLs through server-side APIs to identify anxiety-related behavior signals and return a standardized 1-5 anxiety level for care-prioritization support, without diagnosing disease or prescribing treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External veterinary clinic staff and pet-care operators use this skill to assess stress signals in waiting-area pet videos, prioritize high-stress animals, and review prior analysis reports. Results are for workflow triage and observation support, not medical diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload clinic videos or video URLs to remote services.

Mitigation: Use only with footage that the clinic is authorized to process remotely, and review data-handling expectations before installing in workflows with client, staff, or identifiable pet footage.

Risk: The skill can silently create or reuse an identity and store authentication tokens locally.

Mitigation: Review local storage, token lifecycle, and account-association behavior before deployment, especially on shared clinic workstations.

Risk: Broad history-report triggers can query cloud reports without an explicit confirmation step.

Mitigation: Restrict use to trusted operators and confirm that report-history access is appropriate for the current user and clinical context.

Risk: The anxiety score is observational and may be affected by video quality, camera angle, pet breed, and individual differences.

Mitigation: Treat results as triage support only and require staff to combine the score with direct observation and clinical judgment.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-hospital-waiting-anxiety-analysis)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown or JSON analysis report with optional saved output file and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or video URLs, pet type, detail level, optional output path, and a history-list mode.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
