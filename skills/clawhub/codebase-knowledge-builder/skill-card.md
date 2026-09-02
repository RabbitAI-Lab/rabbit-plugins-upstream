## Description:

Study unfamiliar codebases and produce evidence-backed knowledge artifacts for repository orientation, architecture mapping, subsystem tracing, onboarding, or codebase documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to study an unfamiliar repository within explicit safety boundaries and produce a source-cited, revision-specific knowledge artifact. It supports repository reconnaissance, architecture mapping, subsystem tracing, onboarding, and codebase documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository analysis can expose secrets or sensitive project details if the target scope is too broad.

Mitigation: Keep the skill's default limits on secret access, redaction, target-root containment, and approved output locations.

Risk: Running target code or dependency scripts during documentation work can change the repository or execute untrusted behavior.

Mitigation: Use the skill read-only by default and require explicit user authorization before code execution, dependency installation, build scripts, Git state changes, or in-repository writes.

Risk: A generated knowledge artifact may overstate uncertain architecture or behavior.

Mitigation: Require source citations, evidence labels, confidence statements, validation checks, exclusions, and unresolved questions for consequential claims.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/OthmanAdi/codebase-knowledge-builder/tree/main/skills/codebase-knowledge-builder)
- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/codebase-knowledge-builder)
- [Reconnaissance checklist](references/recon-checklist.md)
- [Deep-dive methodology](references/deep-dive-methodology.md)
- [Knowledge artifact template](templates/knowledge_artifact.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance and source-cited knowledge artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be evidence-backed, revision-specific, redacted where needed, and cite source locations or command receipts.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
