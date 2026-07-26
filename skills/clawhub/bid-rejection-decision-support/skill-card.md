## Description: <br>
Provides procurement evaluation committees with decision support on whether a specific bidder response should be rejected or clarified, including clause/legal basis and report-ready rejection wording. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External procurement evaluation committee members use this skill to assess concrete bidder responses against tender clauses, distinguish mandatory rejection from clarifiable deficiencies, and draft defensible evaluation-report wording. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Procurement rejection decisions are high-stakes and may affect bidder rights or trigger complaints. <br>
Mitigation: Use the output as decision support only; the evaluation committee or legal counsel should verify the tender clause, bidder response, source records, and final wording before official use. <br>
Risk: Knowledge-base citations or complaint-review analogies may be unavailable, incomplete, or mismatched to the procurement system. <br>
Mitigation: Verify cited knowledge-base entries before relying on them, and state the knowledge-base gap when retrieval is unavailable rather than inventing cases or legal authority. <br>
Risk: Incomplete inputs can lead to an incorrect rejection or improper clarification recommendation. <br>
Mitigation: Require the concrete bidder response and corresponding tender clause before making a determination; ask follow-up questions when the legal system, facts, or clause basis is missing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-rejection-decision-support) <br>
- [Decision framework](references/decision_framework.md) <br>
- [Discipline redlines](references/discipline_redlines.md) <br>
- [Knowledge-base mounting](references/kb_mounting.md) <br>
- [Rejection wording templates](references/rejection_wording_templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown decision opinion with structured sections and report-ready wording] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the actual bidder response, matching tender clause, and retained source records; may cite configured IMA knowledge bases when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, manifest.yaml, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
