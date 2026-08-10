## Description: <br>
Deep, source-traceable long-form Chinese album review skill for producing one comprehensive critique from a primary music credit and album name. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to generate long-form Chinese album criticism with researched discographic facts, genre-adapted analysis, and a source-backed evidence appendix. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled backing validator may depend on a missing schema_check helper. <br>
Mitigation: Confirm the validator imports and runs in the packaged release before relying on traceability validation; fix packaging if the helper is absent. <br>
Risk: The deterministic gate checks length, sections, and traceability, but does not prove that long Chinese prose is substantive rather than repeated. <br>
Mitigation: Keep human or judge review of the judge-must-flag negatives and treat validator success as evidence of measurable requirements only. <br>
Risk: Web research may be unavailable or too thin for obscure albums. <br>
Mitigation: Degrade honestly to caller-supplied material, record research gaps, and avoid invented track, personnel, date, or reception claims. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vincentjiang06/skills/album-review) <br>
- [Music source roster](artifact/references/source-roster.md) <br>
- [Research protocol](artifact/rules/research-protocol.md) <br>
- [Genre lenses](artifact/rules/genre-lenses.md) <br>
- [Review output template](artifact/rules/output-template.md) <br>
- [Backing JSON schema](artifact/schemas/backing.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Long-form Chinese Markdown review plus backing JSON for claim-to-evidence traceability.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Review prose targets 10,000-15,000 CJK Chinese characters and includes an evidence appendix; fact-class claims are expected to cite backing evidence.] <br>

## Skill Version(s): <br>
0.2.0 (source: frontmatter, server evidence, changelog released 2026-07-31) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
