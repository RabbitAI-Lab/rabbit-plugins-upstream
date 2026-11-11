## Description:

Analyzes pet hospital waiting-area videos for visible stress behaviors and returns an anxiety level from 1 to 5 to support triage, without diagnosing disease or prescribing treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Veterinary and pet-care staff can use the skill to review waiting-area footage, note visible stress behaviors, and prioritize pets that may need attention or comfort. The result supports workflow decisions and is not a clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video may be uploaded to a remote service even when `--export-env-only` is requested, and `--api-url` may not determine the upload destination.

Mitigation: Use only non-sensitive footage until the export-only and destination-selection issues are fixed; verify the actual destination before sending a clip.

Risk: The skill may create remote accounts and uses shared plaintext credentials; service retention and access terms are not established in the available evidence.

Mitigation: Confirm the provider's retention and access terms and review account creation and credential storage before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-pet-hospital-waiting-anxiety-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Structured assessment report with behavior observations, an anxiety level from 1 to 5, and a report link when available; detail can be returned as basic, standard, or JSON output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Triage support only; not a disease diagnosis or treatment plan.]

## Skill Version(s):

1.0.18 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
