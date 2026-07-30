## Description: <br>
Generates careful apology and issue-explanation drafts after the user provides confirmed facts, responsibility boundaries, and a resolution plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer communication teams use this skill to prepare apology and issue-explanation messages when failures, delays, wrong shipments, omissions, incorrect information, or customer experience issues occur. It helps the agent check facts, responsibility boundaries, solution status, and communication risks before drafting customer-facing text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may include sensitive customer, order, supplier, or internal business details in prompts or drafts. <br>
Mitigation: Use only appropriate, non-sensitive business details and remove unnecessary identifiers before sharing or sending generated text. <br>
Risk: A generated apology could imply liability, refunds, compensation, or delivery commitments that have not been approved. <br>
Mitigation: Review the draft before sending and confirm responsibility boundaries, compensation terms, and solution timelines with the appropriate business owner. <br>
Risk: Incomplete facts can produce misleading or overconfident customer-facing explanations. <br>
Mitigation: Require confirmed facts, current responsibility status, and an approved solution before producing a final sendable version; otherwise keep output preliminary and label missing or conflicting information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-apology) <br>
- [README](artifact/README.md) <br>
- [Skill source](artifact/SKILL.md) <br>
- [Examples template](artifact/examples.md) <br>
- [Test guidance](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown text with structured analysis, parameter status, risk notes, communication strategy, and a sendable draft] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may stop or mark output as preliminary when required facts, responsibility status, or confirmed solutions are missing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact rule version 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
