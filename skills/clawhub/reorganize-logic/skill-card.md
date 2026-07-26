## Description: <br>
Rebuilds a project's design-contract layer when docs have drifted past sync by re-deriving architecture, structure, and interface contracts from code and gate-verifying them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when existing architecture, structure, or interface contract docs are too stale for incremental sync and need a code-derived rebuild with a review-gated deletion manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is intended for a heavy documentation rebuild and prepares a deletion manifest for stale legacy contract docs. <br>
Mitigation: Review the generated contracts and deletion manifest before applying any deletions; legacy files should not be deleted automatically. <br>
Risk: The workflow reads project code and old contract docs, which can be broad in sensitive or very large repositories. <br>
Mitigation: Use the scope option for sensitive or large repositories and review generated outputs before accepting them. <br>
Risk: The local gate verifies structural ties between documented interfaces and code but does not prove all prose or diagrams are semantically faithful. <br>
Mitigation: Run the verification script to PASS and complete the fresh-reader review against code before reporting completion. <br>


## Reference(s): <br>
- [The rebuild protocol](references/protocol.md) <br>
- [Contract format](references/contract-format.md) <br>
- [Gate design](references/gate-design.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/vincentjiang06/skills/reorganize-logic) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown contract files with Mermaid diagrams, interface tables, shell commands, and a deletion manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces docs/contracts/architecture.md, docs/contracts/structure.md, docs/contracts/interfaces.md, and docs/contracts/deletion-manifest.md; expected to pass local verification before completion.] <br>

## Skill Version(s): <br>
0.2.1 (source: release evidence and frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
