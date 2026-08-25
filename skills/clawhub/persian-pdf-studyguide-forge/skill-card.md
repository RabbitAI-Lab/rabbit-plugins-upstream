## Description:

Converts operator-authorized Persian and English RTL lecture PDFs into offline HTML study guides with dual OCR, rendered-page evidence, optional AI-assisted correction, source-linked study aids, QA gates, and ZIP verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and education teams use this skill to turn authorized Persian or mixed RTL educational PDFs into accessible offline study guides with searchable source evidence, flashcards, quizzes, tables, summaries, and QA reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes PDFs that may contain private or copyrighted material.

Mitigation: Use it only in a dedicated workspace with PDFs the operator supplied or is authorized to process, and confirm distribution rights before sharing generated guides.

Risk: Optional AI provider mode can send selected OCR or source text to configured providers.

Mitigation: Keep network mode disabled unless explicitly approved, use provider configurations that reference environment-variable names, and avoid storing literal secrets in artifacts.

Risk: OCR and AI-assisted reconstruction can introduce omissions, garbled RTL text, or factual errors.

Mitigation: Review rendered-page evidence, fidelity reports, source-linked references, flashcard verification results, and QA gates before relying on generated educational or medical content.

Risk: Dependency drift can make pipeline behavior non-repeatable.

Mitigation: Pin dependencies or use a lockfile for repeatable installs before production use.

Risk: The security guidance says not to rely on the bundled manifest until the publisher fixes its package verification mismatch.

Mitigation: Treat manifest verification as advisory for this release and rely on independent workspace review and scan results before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/persian-pdf-studyguide-forge)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [Workflow playbook](docs/WORKFLOW_PLAYBOOK.md)
- [Agent discovery card](AGENT_DISCOVERY.md)
- [Golden example output](examples/01_sleep_eating_review.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, generated HTML study guides, QA reports, manifests, and ZIP packages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are workspace-local by default; optional provider-assisted steps require explicit operator approval and local provider configuration.]

## Skill Version(s):

1.3.2 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
