## Description: <br>
Helps evaluate whether to accept a return or exchange request and identify required evidence, return-shipping conditions, freight boundaries, return deadlines, and post-receipt inspection paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Aftersales, support, and operations staff use this skill to structure RMA decisions from customer case facts, order and warranty information, responsibility status, shipping constraints, and available evidence. It is intended as decision support and requires authorized staff to retain final RMA, refund, legal, or management approvals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat the output as automatic refund, replacement, or RMA authority. <br>
Mitigation: Keep the skill as aftersales decision support and require authorized staff to make final RMA, refund, legal, or management approvals. <br>
Risk: Customer, order, warranty, shipping, or evidence details may contain sensitive case information. <br>
Mitigation: Provide only relevant and preferably desensitized case information when using the skill. <br>
Risk: Incomplete or conflicting case facts can lead to premature responsibility or solution conclusions. <br>
Mitigation: Use the required parameter status table, preserve conflicts and unverified information, and proceed to formal analysis only after the minimum operating conditions are met. <br>
Risk: Shipping, customs, packaging, and supplier-window constraints can make a return path impractical or risky. <br>
Mitigation: Check return feasibility, freight responsibility, packaging requirements, deadlines, and customs constraints before accepting a return. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-rma) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [examples.md](artifact/examples.md) <br>
- [tests.md](artifact/tests.md) <br>
- [changelog.md](artifact/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with structured parameter status, RMA decision, conditions, shipping requirements, freight boundaries, inspection path, deadlines, and sendable response sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided RMA case facts and does not request system access, credentials, persistence, or automatic actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact documents v0.1 draft content) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
