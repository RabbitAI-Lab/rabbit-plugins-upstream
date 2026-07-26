## Description: <br>
Compares tender or procurement checklists against bid response checklists item by item, flagging quantity, unit, specification, structure, arithmetic, and special-condition differences without making legal review decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement reviewers, bid teams, and compliance staff use this skill to compare tender or procurement item lists with bidder response lists and produce a structured record of mismatches for human review. It is intended as a comparison aid and does not decide whether a mismatch is legally material or disqualifying. <br>

### Deployment Geography for Use: <br>
Global; content is tailored to Chinese tendering and government-procurement workflows. <br>

## Known Risks and Mitigations: <br>
Risk: A comparison report could be mistaken for a final legal or procurement decision. <br>
Mitigation: Use the report as a comparison aid only; final determinations remain with the appropriate evaluation, negotiation, or procurement review body. <br>
Risk: Knowledge-base references may be treated as complete legal authority without review. <br>
Mitigation: Verify cited regulations and cases in the relevant tendering or government-procurement source before relying on them. <br>
Risk: Ambiguous, reordered, scanned, or low-quality checklist inputs can lead to incorrect matches or unreadable values. <br>
Mitigation: Require human confirmation for ambiguous matches and unreadable rows, and avoid inferring missing or unclear values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/list-responsiveness-comparer-1-0-0) <br>
- [Publisher profile](https://clawhub.ai/user/chesaram) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact manifest](artifact/manifest.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown comparison report with tabular findings and a JSON diff_items handoff object] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Flags findings as red, yellow, or blue and keeps legal or procurement determinations for human reviewers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
