## Description: <br>
Audit and fix provenance in knowledge base notes. Ensure every factual claim has an inline citation with date and source. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jjjhenriksen](https://clawhub.ai/user/jjjhenriksen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Knowledge base maintainers, documentation owners, and agents use this skill to audit notes for missing or malformed provenance, draft citation fixes, and summarize remaining citation gaps without fabricating sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads knowledge base notes that may contain private or sensitive information. <br>
Mitigation: Use it only on notes the agent is authorized to audit and review the scanned scope before running broad citation checks. <br>
Risk: Incorrectly approved citation edits could alter provenance or add misleading context. <br>
Mitigation: Review proposed fixes before batch apply; missing citations should be flagged rather than fabricated. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown audit report with grouped findings, suggested fixes, counts, and review queue items] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only by default; proposed citation fixes are applied only with user approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
