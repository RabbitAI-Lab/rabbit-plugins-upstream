## Description: <br>
This skill helps bidders run pre-submission mechanical checks on blind-bid technical documents by comparing tender formatting requirements against DOCX/PDF evidence, flagging identity leaks and metadata residue, and producing risk-ranked revision guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External bidders and proposal teams use this skill before sealing or uploading a blind-bid technical submission to find formatting mismatches, hidden identity signals, and document metadata that could create disqualification or point-loss risk. It is limited to mechanical compliance checking and does not evaluate proposal quality or predict scores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded bid documents and generated reports may contain confidential bid text, metadata, or short identity-match snippets. <br>
Mitigation: Run checks in a trusted local workspace, keep reports confidential, remove temporary scan outputs, and avoid sharing sensitive bid material through external feedback channels. <br>
Risk: PDF scans are best-effort for formatting fields such as fonts, margins, line spacing, and alignment. <br>
Mitigation: Prefer DOCX inputs for automated format checks and require manual review for PDF-only formatting findings, embedded images, EXIF data, hidden layers, and signature blocks. <br>
Risk: The skill can surface compliance risks but cannot replace tender-specific legal, procurement, or evaluator judgment. <br>
Mitigation: Confirm the extracted requirement profile with the user, treat tender clauses as authoritative, and perform a final human review before submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-blind-bid-format-scanner) <br>
- [Blind bid specifications](artifact/references/blind_bid_specs.md) <br>
- [Identity patterns](artifact/references/identity_patterns.md) <br>
- [Blind bid failure cases](artifact/references/blind_bid_failure_cases.md) <br>
- [Self-check list](artifact/references/self_check_list.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with comparison tables, risk labels, JSON-backed scan summaries, and optional VBA/Python revision commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include short context snippets from uploaded documents; DOCX checks are more reliable than PDF format checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and artifact/manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
