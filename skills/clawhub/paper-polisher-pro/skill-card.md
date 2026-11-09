## Description:

Provides authors with local AI-writing self-checks and academic writing guidance, including terminology and style checks, paragraph attribution, compliance-label checks, and sentence-level suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Authors use the toolkit to review and improve their own academic writing, check terminology and style, and inspect advisory AI-writing signals before submission. It supports disclosure and self-review; its scores are not proof of authorship or institutional compliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-writing scores may be mistaken for proof of authorship or compliance.

Mitigation: Use results as writing advice, follow institutional disclosure policies, and do not rely on the scores as proof.

Risk: Medical terminology or suggested edits may be inaccurate.

Mitigation: Manually verify medical terminology and review proposed edits before using them.

Risk: Confidential drafts and generated reports may be exposed through report storage or an exposed MCP HTTP listener.

Mitigation: Prefer stdio integration, do not expose the unauthenticated HTTP listener through port forwarding, protect generated reports, and remove leftover temporary directories when handling confidential drafts.

Risk: Optional dependencies and separately obtained model binaries have independent review needs.

Mitigation: Review optional dependencies and model binaries separately before use.

Risk: Accuracy claims depend on evaluation scope and operating mode.

Mitigation: Treat scores as advisory and consult the documented evaluation scope and mode when interpreting them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Project repository (linked from README)](https://github.com/docsor1212/paper-polisher-pro)
- [Best practices](references/best-practices.md)
- [FAQ](references/faq.md)
- [Architecture](references/architecture.md)
- [Documentation site](https://docsor.cn)
- [ModelScope skill page](https://modelscope.cn/skills/Docsor/paper-polisher-pro)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, JSON, Markdown, HTML reports, CSV reports]

**Output Format:** [Text, JSON, Markdown, HTML, and CSV reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report contents depend on selected checks; texts under 100 characters receive no AI-risk verdict.]

## Skill Version(s):

7.6.0 (source: ClawHub release metadata, skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
