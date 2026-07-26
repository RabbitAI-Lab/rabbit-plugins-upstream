## Description: <br>
Chinese-language bid rejection and invalid-bid risk Q&A that uses the public "招标投标专家否决汇集" knowledge base and web references to answer questions about rejection reasons, cases, and risk alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External bid teams and procurement practitioners use this skill to understand why bids are rejected or invalidated, compare common rejection scenarios, and generate practical risk-check guidance. It is informational and does not provide legal advice, bid-document drafting, or data collection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill provides bid rejection and invalid-bid risk guidance that users may mistake for legal advice. <br>
Mitigation: Treat outputs as informational only and keep the disclaimer visible; users should confirm decisions against the bid documents and applicable law. <br>
Risk: Knowledge-base searches or web references may return few or no relevant cases. <br>
Mitigation: Disclose low or missing hit counts, avoid inventing cases, and fall back to clearly labeled general legal or procedural reasoning. <br>
Risk: The skill may use web search for current policy or case references. <br>
Mitigation: Prefer recent public sources, cite the source basis in the answer, and separate internet references from knowledge-base cases. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-rejection-experience-1-0-3) <br>
- [Publisher profile](https://clawhub.ai/user/chesaram) <br>
- [README](artifact/README.md) <br>
- [Demo report](artifact/demo-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured risk summaries, case notes, reference notes, and a disclaimer footer] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should distinguish knowledge-base cases from web references, avoid fabricated cases, and include the required attribution and informational disclaimer.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact manifest version 1.0.3 and SKILL.md frontmatter version 1.0.1 differ) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
