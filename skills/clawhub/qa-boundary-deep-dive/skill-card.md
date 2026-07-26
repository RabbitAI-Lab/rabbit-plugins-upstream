## Description: <br>
Systematically identifies boundary conditions across input, state, time, and resource dimensions, then labels each condition with risk level and expected result. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and test designers use this skill to deepen boundary testing after scenario mapping or equivalence-class analysis. It produces a traceable boundary checklist for systems with input fields, state transitions, timing constraints, or resource limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad Chinese-language mentions of boundaries. <br>
Mitigation: Confirm the user wants boundary-condition analysis or narrow the trigger wording before applying it in workflows where generic boundary discussion is common. <br>
Risk: Examples and outputs may involve sensitive order, payment, screenshot, identity, phone, customer, or financial data. <br>
Mitigation: Use masked or synthetic data in prompts and review generated examples before sharing or storing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-boundary-deep-dive) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown boundary analysis with structured identifiers, linked scenario IDs, risk levels, and expected results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Boundary items use BD-XXXX identifiers and may reference SC-XXXX scenario IDs.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
