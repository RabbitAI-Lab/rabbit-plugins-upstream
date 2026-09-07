## Description:

DeepEvidence public API skill for physicians' evidence-based clinical decision support, generating source-grounded answers from retrieved literature and guidelines for clinical reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cindy8753](https://clawhub.ai/user/cindy8753)

### License/Terms of Use:

MIT-0

## Use Case:

External clinicians and developers use this skill to ask DeepEvidence for evidence-based clinical decision-support responses, guideline interpretation, drug-safety review, trial evidence synthesis, and supported medical image analysis. Outputs are for clinical reference and require clinician verification before patient-care decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clinical questions, images, and metadata may be sent to an external DeepEvidence service.

Mitigation: De-identify patient information, confirm consent and compliance terms before use, and avoid sending patient-identifiable data unless the integration explicitly permits it.

Risk: Default storage behavior for submitted clinical content is unclear.

Mitigation: Use no-store behavior where available and verify retention, deletion, and logging controls with the service owner before broad deployment.

Risk: The release bundles an unnecessary compiled Python bytecode file.

Mitigation: Ask the publisher to remove bundled bytecode and review source-only artifacts before deployment.

Risk: The dependency declaration is broad and may resolve to unexpected OpenAI SDK versions.

Mitigation: Pin and review dependencies in the deployment environment before production use.

## Reference(s):

- [DeepEvidence Open Platform Docs](https://deepevid.medsci.cn/platform/docs)
- [DeepEvidence Homepage](https://deepevid.medsci.cn/)
- [DeepEvidence API Reference](references/api_reference.md)
- [ClawHub Skill Page](https://clawhub.ai/cindy8753/skills/deepevidence)
- [ClawHub Publisher Profile](https://clawhub.ai/user/cindy8753)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, OpenAI-compatible API examples, CLI output, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves returned citation markers and reference lists when DeepEvidence returns them; can include token usage metadata for API calls.]

## Skill Version(s):

1.0.12 (source: server release evidence; skill frontmatter reports 1.6.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
