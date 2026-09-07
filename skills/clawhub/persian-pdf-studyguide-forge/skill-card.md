## Description:

Converts operator-authorized Persian or mixed RTL lecture PDFs into accessible offline HTML study guides with OCR evidence, optional AI-assisted correction and enrichment, QA reports, and verified packaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and agent operators use this skill to turn authorized Persian or mixed RTL lecture PDFs into source-linked study guides with flashcards, quizzes, summaries, fidelity checks, and packaged offline output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text can be sent to automatically discovered or custom AI providers using ambient API keys.

Mitigation: Use FORGE_MOCK=1 or a trusted local model for private PDFs, or explicitly review provider lists, base URLs, headers, and API-key environment variables before enabling remote AI.

Risk: Prompt and completion content can be cached outside the workspace.

Mitigation: Set FORGE_CACHE_DIR to a controlled location or purge the default cache after sensitive runs.

Risk: The skill executes a local PDF/OCR/build pipeline with third-party dependencies.

Mitigation: Install and run it only in a dedicated workspace, and prefer pinned dependencies or a locked environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/persian-pdf-studyguide-forge)
- [Agent discovery card](AGENT_DISCOVERY.md)
- [Model and agent compatibility](docs/MODEL_COMPATIBILITY.md)
- [Workflow playbook](docs/WORKFLOW_PLAYBOOK.md)
- [Integrations guide](integrations/README.md)
- [Agent manifest](agent-manifest.json)
- [Tool schema](integrations/tool-spec.json)

## Skill Output:

**Output Type(s):** [Files, HTML, JSON, Shell commands, Guidance]

**Output Format:** [Offline HTML study guide, JSON status and evidence reports, Markdown guidance, and ZIP package artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports fully offline FORGE_MOCK=1 mode; optional provider-backed correction and enrichment should use authorized inputs only.]

## Skill Version(s):

1.5.4 (source: server release metadata; artifact frontmatter is 1.5.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
