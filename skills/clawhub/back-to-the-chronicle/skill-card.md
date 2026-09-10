## Description:

Reconstructs a project's missing founding or historical Chronicle from approved session logs, Git history, receipts, artifacts, and external-state readbacks while preserving witnessed, artifact-measured, and inferred-intent boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and project maintainers use this skill to reconstruct founding decisions, abandoned experiments, corrections, and causal project history from explicitly approved evidence. It prepares a reviewable backfill manifest before any approved append-only Chronicle integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can expose sensitive repository, path, identity, session-log, hash, and artifact metadata while reconstructing history.

Mitigation: Run it only on explicitly approved projects and session stores, keep inventory and manifest outputs private, and review derivatives for their exact audience before disclosure.

Risk: Chronicle appends, commits, pushes, publication, or broad home-directory session scans can exceed the intended authority scope.

Mitigation: Require explicit approval for the exact scan scope and for any canonical write, commit, push, publication, or broad session-store scan.

Risk: A reconstructed history can overstate absent logs, inferred intent, historical approvals, or stale external state.

Mitigation: Classify each claim as witnessed, artifact-measured, or inferred; keep unavailable evidence explicit; and re-check drift-prone external state before relying on it.

## Reference(s):

- [Chronicle compatibility](references/chronicle-compatibility.md)
- [Backfill evidence standard](references/evidence-standard.md)
- [Session JSONL custody](references/session-jsonl-custody.md)
- [AntreasAntoniou/chronicle](https://github.com/AntreasAntoniou/chronicle)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON manifest examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce private JSON inventory/session metadata files and a proposed Chronicle backfill manifest; canonical Chronicle writes require separate approval.]

## Skill Version(s):

1.0.0 (source: server release metadata and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
