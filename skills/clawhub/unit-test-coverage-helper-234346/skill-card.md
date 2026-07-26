## Description: <br>
Helps software teams add useful unit tests and improve coverage for existing codebases through a repeatable local workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Software maintainers, QA engineers, open-source contributors, and product teams use this skill to plan and produce unit tests, coverage-improvement checklists, code changes, and verification notes that reduce regression risk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may auto-activate for broad testing or quality prompts. <br>
Mitigation: Invoke it explicitly or narrow activation triggers when tighter control is needed. <br>
Risk: Generated testing guidance or code changes can miss project-specific behavior or create low-value tests. <br>
Mitigation: Review proposed tests against project requirements and run the relevant test or coverage commands before relying on the result. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/unit-test-coverage-helper-234346) <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [Preventing LLM unit test spam](https://blog.larah.me/test-slop/) <br>
- [Skillgrade: Unit tests for agent skills](https://github.com/mgechev/skillgrade) <br>
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown responses with optional code snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include checklists, implementation steps, assumptions, validation commands, and follow-up risks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
