## Description: <br>
政府采购评审专家数字分身 helps users analyze Chinese government procurement evaluation, invalid-bid, complaint, collusion-risk, procurement-file, response-file, and legal-basis questions from an independent evaluation-committee perspective. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and procurement practitioners use this skill to structure government procurement questions, identify applicable Chinese government-procurement rules, assess bid validity and complaint risk, and produce concise evaluation guidance. It is not intended to replace formal legal advice for high-stakes disputes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat procurement guidance as formal legal advice or rely on outdated or incomplete legal references. <br>
Mitigation: Verify cited law, local rules, and project facts before use, and consult a qualified professional for high-stakes procurement disputes. <br>
Risk: The skill's answers may depend on ima knowledge bases that are not available in the runtime environment. <br>
Mitigation: Check that the expected knowledge bases are mounted; if they are unavailable, treat answers as general guidance and require explicit source verification. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/govproc-evaluation-expert) <br>
- [Project repository](https://github.com/chesaram/my-skill-hub) <br>
- [README](artifact/README.md) <br>
- [Sample invalid-bid answer](artifact/demo/sample_invalid_bid.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured analysis sections, risk labels, legal-basis summaries, and operational recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Answers may depend on mounted ima knowledge bases and should state when those sources are unavailable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
