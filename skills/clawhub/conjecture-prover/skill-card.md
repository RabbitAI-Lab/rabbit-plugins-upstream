## Description: <br>
Conjecture Prover guides agents through a cross-domain workflow for decomposing conjectures, exploring equivalences or reductions, validating evidence, and producing proof-oriented reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and technical writers use this skill to structure conjecture analysis across domains, distinguish proof from numerical or experimental support, and produce papers, proof sketches, review notes, verification scripts, and follow-up research tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated mathematical or scientific claims may be incomplete, incorrect, or supported only by numerical or experimental evidence. <br>
Mitigation: Treat outputs as research drafts; independently verify proofs, citations, assumptions, and any claimed reductions before relying on them. <br>
Risk: Generic trigger words such as proof or conjecture may activate the skill in contexts where a lighter response is expected. <br>
Mitigation: Narrow activation or invocation rules when deploying the skill in environments with broad mathematical, scientific, or writing workflows. <br>


## Reference(s): <br>
- [Conjecture Prover Catalog](references/conjecture-prover-catalog.md) <br>
- [Conjecture Prover Requirements](references/conjecture-prover-requirements.md) <br>
- [Exemplars](references/exemplars.md) <br>
- [RH Verification Script](scripts/rh_proof_verify.py) <br>
- [ClawHub Skill Page](https://clawhub.ai/wangjiaocheng/skills/conjecture-prover) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown prose with optional code blocks, scripts, and generated report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include proof status labels, numerical or experimental validation notes, references, and reproducibility artifacts.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
