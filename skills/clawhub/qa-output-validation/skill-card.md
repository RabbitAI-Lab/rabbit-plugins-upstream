## Description: <br>
Qa Output Validation performs a final anti-hallucination check on generated test cases by verifying requirement IDs, consistency, executability, and source traceability before final output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers and development teams use this skill as a final quality gate after AI-generated test cases are produced. It checks whether cases are grounded in the requirement decomposition, internally consistent, executable, and traceable before release or reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad requests to verify or check quality. <br>
Mitigation: Use it as a final QA gate for generated test cases and confirm that the requested validation scope matches the available source materials. <br>
Risk: Recommendations to delete or mark test cases could remove valid coverage if the source material is incomplete. <br>
Mitigation: Review deletion or marking recommendations manually, confirm source traceability, and back up source data before changing test assets. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-output-validation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown validation report with pass/fail status, check results, issue tables, and traceability notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Issue lists are tied to original test case IDs and the skill does not assign new unique IDs.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
