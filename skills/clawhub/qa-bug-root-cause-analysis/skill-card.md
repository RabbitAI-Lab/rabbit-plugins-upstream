## Description: <br>
Guides agents through structured QA bug root-cause analysis by classifying symptoms, tracing direct, indirect, and systemic causes, and producing fix and prevention recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and incident reviewers use this skill to analyze recurring or production bugs, identify root causes, assess impact, and define fixes and prevention measures. It is suited for post-defect analysis when logs, environment details, reproduction steps, and bug descriptions are available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger phrases may activate the skill during general troubleshooting. <br>
Mitigation: Confirm the user wants a formal QA root-cause analysis before applying the workflow to generic debugging requests. <br>
Risk: Bug reports, logs, screenshots, and payment or customer examples can contain sensitive production data. <br>
Mitigation: Mask production logs, customer identifiers, payment details, screenshots, credentials, and environment secrets before using the skill. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/kokxi/skills/qa-bug-root-cause-analysis) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/kokxi) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured root-cause analysis fields, traceability IDs, tables, and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include ROOT-XXXX traceability, BUG-XXXX linkage, root cause, contributing factors, impact assessment, fix suggestions, prevention measures, and verification guidance.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
