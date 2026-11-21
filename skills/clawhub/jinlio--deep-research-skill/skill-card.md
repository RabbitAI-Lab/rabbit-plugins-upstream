## Description:

Conducts OpenClaw-based research with iterative clarification, source-text verification, conflict disclosure, and an auditable report and evidence package, using tools already authorized in the host session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jinlio](https://clawhub.ai/user/jinlio)

### License/Terms of Use:

MIT

## Use Case:

Developers and other OpenClaw users can use this skill for competitor, industry, product-selection, risk, and source research. It structures research around located evidence and produces an auditable report and evidence bundle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious and reports network, local-file, and report-rendering weaknesses; its review is partial because a referenced path was missing.

Mitigation: Before installing, review the reported access and report-rendering concerns and account for the incomplete scan; limit permissions to what the host session needs.

## Reference(s):

- [Project homepage](https://github.com/jinlio/deep-research-skill)
- [ClawHub release page](https://clawhub.ai/jinlio/skills/deep-research-skill)
- [OpenClaw Skills documentation](https://docs.openclaw.ai/tools/skills)
- [OpenClaw Sub-agents documentation](https://docs.openclaw.ai/tools/subagents)
- [OpenClaw Sandboxing documentation](https://docs.openclaw.ai/gateway/sandboxing)
- [Research workflow](references/workflow.md)
- [Artifact schema](references/artifact-schema.md)
- [Quality gates](references/quality-gates.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Guidance]

**Output Format:** [Markdown report with a structured evidence bundle (JSONL, YAML, and audit files); optional self-contained HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Factual claims link to located evidence; conflicts, unknowns, and retrieval failures are disclosed.]

## Skill Version(s):

0.3.1 (source: skill frontmatter, VERSION, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
