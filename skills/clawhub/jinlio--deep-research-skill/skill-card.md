## Description:

OpenClaw workflow skill for deep research that reuses already-authorized host tools to clarify requirements, verify source evidence, disclose conflicts, and produce auditable reports and evidence bundles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jinlio](https://clawhub.ai/user/jinlio)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and research-oriented agent users use this skill to run structured competitive, industry, selection, risk, or source-material research with clarification rounds, multi-source verification, conflict disclosure, and traceable deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research artifacts can contain sensitive source material, credentials, or personal data when users include them in a run.

Mitigation: Keep sensitive material out of prompts, logs, and research-run artifacts unless needed, and run the included sensitive-data scan with the final gates before sharing deliverables.

Risk: The skill may use host-provided web, browsing, file-writing, and optional sub-agent capabilities already available in the session.

Mitigation: Use it only in sessions whose permissions and workspace write scope are acceptable, and keep writes restricted to the intended research-run bundle.

Risk: Reports may contain unsupported, stale, or conflicting claims if source retrieval or verification is incomplete.

Mitigation: Require source-positioned evidence for factual claims, disclose unknowns and conflicts, and review the final report before sharing.

Risk: Missing runtime capabilities can reduce coverage or prevent parallel verification.

Mitigation: Follow the documented degraded modes, record unavailable capabilities in the run manifest, and avoid presenting blocked sources as verified evidence.

## Reference(s):

- [Project homepage](https://github.com/jinlio/deep-research-skill)
- [Workflow](references/workflow.md)
- [Runtime Capability Contract](references/adapter-contract.md)
- [Agent Prompt Contracts](references/agent-contracts.md)
- [Artifact Protocol](references/artifact-schema.md)
- [Quality Gates](references/quality-gates.md)
- [OpenClaw Capability Profile](profiles/openclaw.md)
- [OpenClaw Skills documentation](https://docs.openclaw.ai/tools/skills)
- [OpenClaw Sandboxing documentation](https://docs.openclaw.ai/gateway/sandboxing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, JSON/JSONL/YAML run artifacts, shell commands, and structured guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an auditable research-run bundle with sources, evidence, claims, conflicts, agent packets, a run manifest, audit output, and a final report.]

## Skill Version(s):

0.2.7 (source: frontmatter, VERSION, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
