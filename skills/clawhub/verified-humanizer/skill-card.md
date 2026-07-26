## Description: <br>
Legacy verification-guided rewriting skill. Makes AI-generated text more natural while encouraging claims to stay grounded and attributable. Does not perform cryptographic verification, emit receipts, verify receipts, or prove that rewritten text is true. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nutstrut](https://clawhub.ai/user/nutstrut) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers can use this skill to rewrite stiff or formulaic AI-assisted drafts into clearer, more natural text while preserving meaning and documenting before/after evaluation metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional verification could expose sensitive or private text if raw content is sent outside the local workflow. <br>
Mitigation: Use optional verification only with structured metrics such as counts, deltas, and boolean checks; do not send original or rewritten text. <br>
Risk: The included OpenClaw hook changes session behavior by adding a bootstrap reminder. <br>
Mitigation: Review the hook behavior before deployment and confirm the reminder is appropriate for the target agent environment. <br>
Risk: Humanized text may be mistaken for proof of human authorship or factual correctness. <br>
Mitigation: Treat the skill as a rewriting and evaluation workflow only; independently review factual claims and do not use it as an authorship or truth verifier. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nutstrut/skills/verified-humanizer) <br>
- [Verified Humanizer examples](references/examples.md) <br>
- [OpenClaw integration notes](references/openclaw-integration.md) <br>
- [Rewrite checklist](assets/REWRITE-CHECKLIST.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Rewritten text with Markdown or JSON transformation summaries and optional local shell-script pattern counts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should preserve meaning, keep rewriting local, and include only structured metrics if optional verification is used.] <br>

## Skill Version(s): <br>
0.0.8 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
