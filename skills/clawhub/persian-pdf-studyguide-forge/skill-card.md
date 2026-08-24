## Description:

Executable fidelity-first pipeline that converts authorized Persian RTL PDFs into accessible offline HTML study guides using dual OCR, rendered-page evidence, optional multi-model primary/reviewer correction, session-grounded maximum enrichment, self-contained images, interactive search/quizzes, measured fidelity, QA gates, and verified ZIP packaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers, educators, and operators use this skill to convert operator-authorized Persian or mixed RTL educational PDFs into accessible offline study guides with source-page evidence, correction/enrichment workflows, search, quizzes, fidelity reports, QA gates, and verified packaging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized, private, or copyrighted PDFs may be processed or distributed without proper rights.

Mitigation: Process only operator-authorized PDFs in a dedicated workspace and confirm permission before distributing generated study guides or source-page images.

Risk: Provider-assisted correction or enrichment sends selected extracted document text to configured AI services.

Mitigation: Use provider mode only with explicit approval and acceptable data-sharing terms; local extraction, rendering, build, and QA can run without sending content off-device.

Risk: Very large or untrusted PDFs can consume excessive local CPU, memory, disk, or OCR time.

Mitigation: Run in a constrained environment and cap page count, DPI, and worker count before processing high-risk inputs.

Risk: OCR, reconstruction, or enrichment can introduce factual errors into educational or medical study material.

Mitigation: Use rendered-page evidence, fidelity reports, QA gates, and qualified review before relying on the generated guide.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/persian-pdf-studyguide-forge)
- [README](README.md)
- [Workflow Playbook](docs/WORKFLOW_PLAYBOOK.md)
- [Agent Discovery Card](AGENT_DISCOVERY.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance and shell commands, with generated HTML study guides, JSON evidence/reports, manifests, and ZIP artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local-only extraction and build by default; optional provider-assisted correction and enrichment require explicit operator configuration.]

## Skill Version(s):

1.3.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
