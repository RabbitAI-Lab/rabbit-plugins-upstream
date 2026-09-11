## Description:

Use DeepEvidence for evidence-based clinical questions, including guideline interpretation, drug safety and interactions, dose adjustment, clinical-trial evidence, medical literature, and supported medical-image analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cindy8753](https://clawhub.ai/user/cindy8753)

### License/Terms of Use:

MIT-0

## Use Case:

Clinicians and clinical developers use this skill to query DeepEvidence for literature-backed clinical reference on guidelines, medication safety, dosing, clinical studies, and authorized medical image analysis. Outputs should support evidence review and should not be treated as emergency triage, diagnosis, or a substitute for licensed clinician judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clinical prompts, responses, image data, or user identifiers may contain sensitive health information.

Mitigation: Avoid sending patient-identifying information unless the organization has the required authorization, consent, contractual, and compliance controls for external processing.

Risk: API credentials could be exposed through chat, logs, screenshots, commits, or packaged artifacts.

Mitigation: Keep DEEPEVIDENCE_API_KEY in environment variables and avoid logging prompts, responses, image data, or keys.

Risk: DeepEvidence output may be mistaken for diagnosis, treatment instruction, emergency triage, or proof that no evidence exists after a failed retrieval.

Mitigation: Present responses as clinical reference only, direct urgent symptoms to local emergency care, and treat empty, timed-out, or failed retrievals as inconclusive.

## Reference(s):

- [DeepEvidence skill page](https://clawhub.ai/cindy8753/skills/deepevidence)
- [Publisher profile](https://clawhub.ai/user/cindy8753)
- [DeepEvidence Public API Reference](references/api.md)
- [DeepEvidence Safety Reference](references/safety.md)
- [DeepEvidence Error Handling](references/errors.md)
- [DeepEvidence Integration Examples](references/integration.md)
- [DeepEvidence Platform Docs](https://deepevid.medsci.cn/platform/docs)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text clinical reference content with optional citation markers; command examples are shown as shell snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful DeepEvidence responses should preserve returned citation markers and include a final source line when evidence content is retrieved.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
