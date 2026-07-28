## Description: <br>
Identifies missing, ambiguous, or conflicting details in customer requirements and drafts low-burden clarification questions that are ready to send. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer communication and sales users use this skill to inspect a customer's original request, identify key missing or conflicting parameters, and produce a short sequence of clarification questions before quoting or committing to availability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is marked as draft and examples/tests are still pending, so generated clarification questions may miss real-world edge cases. <br>
Mitigation: Validate outputs against desensitized real customer cases before relying on the skill in routine customer workflows. <br>
Risk: Generated questions could accidentally imply unconfirmed facts, pricing, stock, or delivery commitments if reviewed too lightly. <br>
Mitigation: Review the parameter status table and customer-ready wording before sending, and keep unverified information explicitly marked as missing, conflicting, or pending verification. <br>
Risk: Customer requests may contain sensitive commercial or personal details. <br>
Mitigation: Provide only relevant request details to the skill and desensitize customer information where practical. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Structured Markdown with parameter status tables, confirmed requirements, missing or conflicting information, recommended question order, and customer-ready clarification wording] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompt-only output; no shell commands, API calls, or file changes are produced by the skill.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
