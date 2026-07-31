## Description: <br>
Helps maintainers, QA engineers, contributors, and product teams add useful unit tests, raise coverage, and verify changes against existing behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, software maintainers, QA engineers, open-source contributors, and product teams use this skill to plan, implement, and validate unit-test improvements for existing codebases. It is intended for repeatable testing workflows that produce actionable artifacts such as checklists, code changes, scripts, and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked for broad testing or quality-related requests because implicit invocation is enabled. <br>
Mitigation: Review the request context before applying the workflow, and tighten trigger wording or require explicit invocation when deploying in environments where accidental activation would be disruptive. <br>
Risk: Generated unit tests or coverage plans can be misleading if they assert implementation details instead of intended behavior. <br>
Mitigation: Review proposed tests against expected behavior and run the recommended verification commands before accepting code changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/unit-test-coverage-helper-234446) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Implement: process-worktree-isolation](https://github.com/higress-group/issue-spec/issues/177) <br>
- [Make E2E execution selective, exact-SHA, isolated, and diagnostic](https://github.com/sgajbi/lotus-core/issues/730) <br>
- [cqlite-flight LIMIT/predicate harness finding](https://github.com/pmcfadin/cqlite/issues/2157) <br>
- [Chained-compare and abs floors fixture issue](https://github.com/TSavo/sugar/issues/4190) <br>
- [Preventing LLM unit test spam](https://blog.larah.me/test-slop/) <br>
- [Fix numeric legacy symlink ownership during adoption](https://github.com/chadmhohn/skyjo-online/issues/90) <br>
- [Skillgrade: unit tests for agent skills](https://github.com/mgechev/skillgrade) <br>
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown with optional code blocks, command snippets, checklists, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's repository context and should state assumptions, limits, and validation steps.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
