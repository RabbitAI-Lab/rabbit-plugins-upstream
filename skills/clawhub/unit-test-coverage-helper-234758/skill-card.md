## Description: <br>
Helps software maintainers, QA engineers, open-source contributors, and product teams plan, add, and verify useful unit tests that improve coverage for existing codebases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, maintainers, open-source contributors, and product teams use this skill to turn testing goals into practical unit-test plans, code or checklist outputs, and verification steps. It is intended for existing codebases where teams need higher test confidence without relying on cloud-only or large-training workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad testing or quality-related wording may cause the skill to be invoked when the user did not specifically ask for unit-test coverage help. <br>
Mitigation: Use explicit prompts when unit-test coverage assistance is desired, and confirm the intended testing goal before applying generated changes. <br>
Risk: Generated test guidance or code changes may be incorrect, brittle, or misaligned with the repository's expected behavior. <br>
Mitigation: Review all generated tests and run the relevant project test commands before accepting or merging changes. <br>


## Reference(s): <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [Unit Test Coverage Helper on ClawHub](https://clawhub.ai/kyro-ma/skills/unit-test-coverage-helper-234758) <br>
- [Preventing LLM unit test spam](https://blog.larah.me/test-slop/) <br>
- [Skillgrade: Unit tests for your agent skills](https://github.com/mgechev/skillgrade) <br>
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional code snippets, shell commands, checklists, and verification notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's repository context and should expose assumptions, limits, required inputs, validation commands, and remaining risks when relevant.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
