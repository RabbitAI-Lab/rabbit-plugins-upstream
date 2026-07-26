## Description: <br>
Helps researchers translate Chinese academic prose into publication-oriented English or polish English manuscript paragraphs and complete sections for SCI, SSCI, or interdisciplinary submission. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yila-ai](https://clawhub.ai/user/yila-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External researchers and manuscript authors use this skill to translate Chinese academic prose into English or polish English SCI, SSCI, and interdisciplinary manuscript passages while preserving scientific claims, numbers, citations, limitations, and conclusions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Manuscript text can be confidential or unpublished. <br>
Mitigation: Use the skill only in an agent environment appropriate for the sensitivity of the manuscript text. <br>
Risk: Language polishing can accidentally alter numbers, citations, limitations, claim strength, or causal meaning. <br>
Mitigation: Require the preservation audit described by the skill and manually review claim direction, modality, citation attachment, limitations, and conclusions. <br>
Risk: The optional invariant script checks only deterministic items such as numbers, citations, and protected terms. <br>
Mitigation: Treat a passing script result as a first-pass check, not as proof that the scientific meaning was preserved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yila-ai/skills/sci-ssci-polishing) <br>
- [Corpus and distillation method](references/corpus-method.md) <br>
- [Preservation invariants](references/invariants.md) <br>
- [Output contract](references/output-contract.md) <br>
- [Rhetorical routing](references/rhetorical-routing.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown containing polished English text, a concise change summary, a preservation audit, and author queries when needed; may include shell commands for the optional local invariant check.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are preservation-first and require manual review for claim direction, modality, causal strength, citation attachment, limitations, and conclusions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
