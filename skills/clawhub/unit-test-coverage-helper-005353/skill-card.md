## Description: <br>
Helps agents plan, implement, and verify useful unit tests and coverage improvements for existing codebases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, software maintainers, QA engineers, open-source contributors, and product teams use this skill to add practical unit tests, improve coverage, and verify that code changes preserve existing behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may invoke the skill on general software-quality requests. <br>
Mitigation: Use the explicit skill name when you want this behavior, and disable or narrow implicit activation if the agent supports that. <br>
Risk: Testing guidance or code-change proposals may be incomplete or mismatched to the target repository. <br>
Mitigation: Review proposed tests and run the repository's normal test and coverage commands before merging changes. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/unit-test-coverage-helper-005353) <br>
- [Hydraflow watchdog issue](https://github.com/T-rav/hydraflow/issues/9455) <br>
- [Hydraflow ADR duplicate issue](https://github.com/T-rav/hydraflow/issues/9457) <br>
- [Hydraflow pipeline poller test gap](https://github.com/T-rav/hydraflow/issues/9441) <br>
- [Angular Jasmine unit testing discussion](https://news.ycombinator.com/item?id=48375380) <br>
- [LLM generated code review discussion](https://news.ycombinator.com/item?id=48538778) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with optional code blocks and verification commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tailored workflows, checklists, implementation suggestions, assumptions, remaining risks, and next steps.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
