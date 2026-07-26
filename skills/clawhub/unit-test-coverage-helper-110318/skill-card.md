## Description: <br>
Helps developers and QA teams add useful unit tests, improve coverage, and verify code changes with practical workflows, checklists, commands, and implementation support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, maintainers, QA engineers, open-source contributors, and product teams use this skill to plan or implement targeted unit tests, raise coverage, and verify that code changes do not break existing behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may invoke the skill for general testing or quality requests. <br>
Mitigation: Confirm the task is about unit testing, coverage, regression testing, or quality assurance before relying on its workflow. <br>
Risk: The skill may propose code changes or test commands that affect a repository. <br>
Mitigation: Review generated changes and commands, then run tests in a controlled local workspace before adoption. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/unit-test-coverage-helper-110318) <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [Preventing LLM unit test spam](https://blog.larah.me/test-slop/) <br>
- [Skillgrade: "Unit tests" for your agent skills](https://github.com/mgechev/skillgrade) <br>
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with optional code blocks, shell commands, checklists, and verification notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tailored to the user's repository context; proposed changes and commands should be reviewed before applying.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
