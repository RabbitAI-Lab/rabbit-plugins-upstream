## Description:

OpenClaw pure-workflow deep research skill that does not bind to a model or search service, orchestrates host tools into a reviewable process, and supports competitive, industry, selection, risk, and document research with clarification rounds, source verification, conflict disclosure, auditable reports, and evidence bundles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jinlio](https://clawhub.ai/user/jinlio)

### License/Terms of Use:

MIT

## Use Case:

Developers and research operators use this skill to run structured deep-research workflows in OpenClaw-compatible agent environments. It guides clarification, planning, source discovery, extraction, verification, challenge, synthesis, and audit delivery into a reproducible research-run bundle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated research reports may contain misleading conclusions if sources are incomplete, stale, inaccessible, or insufficiently checked.

Mitigation: Use the skill's clarification, evidence, verification, challenge, and quality-gate workflow, then review the generated research-run artifacts before relying on the report.

Risk: Research materials, prompts, logs, or artifacts could expose credentials, private data, or sensitive local files if the run is not scoped carefully.

Mitigation: Do not place credentials in research materials, confirm which local files may be used as sources, keep external operations read-only, and use the provided sensitive-data checks.

Risk: Host-provided search, browsing, sub-agent, and file capabilities vary by runtime and may fail or degrade coverage.

Mitigation: Probe and record observed runtime capabilities, disclose degradations in the run manifest, and fall back to serial or user-provided-source workflows when capabilities are missing.

## Reference(s):

- [Skill Homepage](https://github.com/jinlio/deep-research-skill)
- [ClawHub Skill Page](https://clawhub.ai/jinlio/skills/deep-research-skill)
- [Standard Research Workflow](references/workflow.md)
- [Runtime Capability Contract](references/adapter-contract.md)
- [Agent Prompt Contracts](references/agent-contracts.md)
- [Artifact Protocol](references/artifact-schema.md)
- [Quality Gates](references/quality-gates.md)
- [OpenClaw Capability Profile](profiles/openclaw.md)
- [Codex Capability Profile](profiles/codex.md)
- [Claude Code Capability Profile](profiles/claude-code.md)
- [HermesAgent Capability Profile](profiles/hermesagent.md)
- [OpenCode Capability Profile](profiles/opencode.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown and structured local research-run artifacts, including JSONL, YAML, JSON, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces auditable reports and evidence bundles while keeping external operations read-only by default.]

## Skill Version(s):

0.2.5 (source: frontmatter, VERSION, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
