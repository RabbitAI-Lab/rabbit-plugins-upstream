## Description: <br>
Verifies math-heavy code for algorithmic correctness and numerical stability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review mathematical, scientific, statistical, numerical, and ML code for correct formulas, documented invariants, numerical stability, reproducibility, and sufficient test evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask an agent to run local tests, benchmarks, or notebooks in the target repository. <br>
Mitigation: Review proposed test commands and notebook contents before execution, especially in untrusted projects. <br>
Risk: Mathematical review output can be incomplete or misleading if requirements, standards, or test evidence are missing. <br>
Mitigation: Require citations, reproducible evidence, and human review before relying on approve or block recommendations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-math-review) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>
- [Derivation Verification](artifact/modules/derivation-verification.md) <br>
- [Numerical Stability Analysis](artifact/modules/numerical-stability.md) <br>
- [Requirements Mapping](artifact/modules/requirements-mapping.md) <br>
- [Testing Strategies for Mathematical Code](artifact/modules/testing-strategies.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown review report with tables, issue entries, recommendations, and inline code or shell command blocks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk classifications, mathematical invariants, derivation notes, stability findings, test evidence, and an approve or block recommendation.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
