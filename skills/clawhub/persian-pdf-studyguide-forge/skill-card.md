## Description:

Converts operator-authorized Persian and English RTL lecture PDFs into offline HTML study guides with OCR evidence, source-grounded enrichment, fidelity reports, QA checks, and verified packaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers, educators, and agent operators use this skill to turn authorized Persian or mixed RTL lecture PDFs into reviewable offline study guides with source-page evidence, study aids, QA reports, and package verification. It is useful when fidelity, reproducibility across model providers, or an offline mock path is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text and generated prompts may be sent to configured or ambient external AI providers.

Mitigation: Use FORGE_MOCK=1 for offline runs, provide a tightly scoped providers.json when AI is needed, and clear unrelated provider API keys from the environment before execution.

Risk: Private, copyrighted, medical, or exam material can be exposed or relied on incorrectly if processed without controls.

Mitigation: Confirm authorization, run in a dedicated workspace, set FORGE_CACHE_DIR to a controlled location, and require qualified review before using generated medical or exam study content.

Risk: Skipping verification or automatic session selection can produce unreviewed study guides or lose verification markings.

Mitigation: Avoid --no-verify and --auto-sessions for publishable output; review session boundaries, rendered-page evidence, fidelity reports, QA reports, and verification markings before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/persian-pdf-studyguide-forge)
- [README](README.md)
- [Agent discovery card](AGENT_DISCOVERY.md)
- [Model and agent compatibility](docs/MODEL_COMPATIBILITY.md)
- [Workflow playbook](docs/WORKFLOW_PLAYBOOK.md)
- [Integrations guide](integrations/README.md)
- [Agent manifest](agent-manifest.json)
- [Tool specification](integrations/tool-spec.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, HTML, JSON, files]

**Output Format:** [Offline self-contained HTML study guide plus JSON evidence, QA reports, manifests, ZIP package, and command-oriented agent guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs keep extraction evidence, reconstruction, and enrichment separate; generated guides may require human review for session boundaries, fidelity exceptions, medical or exam content, and redistribution rights.]

## Skill Version(s):

1.5.1 (source: frontmatter, release metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
