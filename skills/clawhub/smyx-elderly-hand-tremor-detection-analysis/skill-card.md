## Description:

Analyzes video of an older person's hand at rest to report tremor measurements and screening-level risk indicators, with access to historical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and care teams use recordings of an older person's resting hand to review tremor frequency, amplitude, screening-level risk indicators, and prior reports. Results do not replace a neurological evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive recordings and health information are sent to Life Emergence cloud services.

Mitigation: Use only with the subject's informed consent, trusted service endpoints, and appropriate data-retention and deletion arrangements.

Risk: Reused local identity and stored tokens may expose or mix report histories in shared workspaces.

Mitigation: Avoid shared or multi-user workspaces until identity isolation is fixed; protect or clear locally stored data and tokens.

Risk: A screening indicator can be mistaken for a clinical diagnosis.

Mitigation: Present findings as screening information only and refer concerning results for professional neurological assessment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-elderly-hand-tremor-detection-analysis)
- [Tremor analysis API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [JSON-style analysis report or Markdown historical-report table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tremor frequency and amplitude, risk indicators, follow-up suggestions, and report links.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
