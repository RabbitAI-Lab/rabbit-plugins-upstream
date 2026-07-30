## Description: <br>
Reviews full tender documents from a bidder perspective to identify potentially exclusionary, discriminatory, or tailored clauses and draft risk-ranked challenge material. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bidders, procurement teams, and bid advisors use this skill to scan tender documents for clauses that may unfairly narrow competition. It produces issue locations, risk levels, legal-citation direction, and draft challenge or complaint framing for human review. <br>

### Deployment Geography for Use: <br>
China-focused <br>

## Known Risks and Mitigations: <br>
Risk: The skill's legal citation guidance can be wrong or mix government procurement and tendering law references. <br>
Mitigation: Verify the project type and every legal citation against current authoritative legal sources before relying on the output. <br>
Risk: Users may treat generated challenge material as legal advice or a final procurement-law conclusion. <br>
Mitigation: Use the output as drafting support only and have qualified professionals review major disputes. <br>
Risk: Incomplete tender documents can cause missed clauses or overconfident findings. <br>
Mitigation: Require full-document input or clearly label the scan scope, and preserve blind-spot warnings for unread sections, attachments, payment terms, and hard-marker clauses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-carrot-pit-1-0-0) <br>
- [Carrot-pit signal rubric](references/carrot-pit-signals.md) <br>
- [Legal anchor table](references/legal-anchors.md) <br>
- [Report template](templates/carrot-pit-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with tables, clause excerpts, risk levels, legal-citation direction, and optional inline shell command for section splitting.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes blind-spot checks, combination reasoning, challenge drafting prompts, lawful response options, and disclaimers; does not provide final legal determinations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
