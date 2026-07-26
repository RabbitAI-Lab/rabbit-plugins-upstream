## Description: <br>
Helps software maintainers, QA engineers, open-source contributors, and product teams add useful unit tests, raise test coverage, and verify that changes do not break existing behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, maintainers, QA engineers, and product teams use this skill to plan and produce unit-test coverage improvements, regression checks, implementation notes, and verification commands for existing codebases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Overbroad implicit invocation can route unrelated prompts involving testing, regression, or quality to this skill. <br>
Mitigation: Narrow or disable implicit invocation in environments with many development skills, and prefer explicit invocation for unit-test coverage work. <br>
Risk: Generated test plans, code changes, or shell commands may be incomplete or unsuitable for a specific repository. <br>
Mitigation: Review proposed changes before execution and run the repository's normal test and coverage commands before relying on the output. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Skill listing](https://clawhub.ai/kyro-ma/skills/unit-test-coverage-helper) <br>
- [GitHub issue: Mumble experience, performance, and platform parity](https://github.com/mongre25-droid/mumble/issues/12) <br>
- [GitHub issue: WAL replay query plan caching](https://github.com/verveguy/liminis-context-graph/issues/238) <br>
- [GitHub issue: Multi-Outcome Markets contract](https://github.com/Arena1X/InsightArena/issues/1329) <br>
- [GitHub issue: integration test CI job](https://github.com/StellarCommons/stellar-fee-tracker/issues/499) <br>
- [GitHub issue: Table UI definition](https://github.com/kitamura-tetsuo/outliner/issues/4238) <br>
- [GitHub issue: Reject empty payment batch payloads](https://github.com/mux-labs/mux-backend/issues/597) <br>
- [GitHub issue: Docker Compose local setup](https://github.com/mux-labs/mux-backend/issues/598) <br>
- [Hacker News: Clinical failure rates over the decades](https://news.ycombinator.com/item?id=49056211) <br>
- [Hacker News: LLM Usage in Debian](https://news.ycombinator.com/item?id=49053737) <br>
- [Hacker News: Harden AI changes before review](https://news.ycombinator.com/item?id=49053524) <br>
- [Hacker News: Engineering management after code cost changed](https://news.ycombinator.com/item?id=49050839) <br>
- [Hacker News: Buz fork of Bun](https://news.ycombinator.com/item?id=49045975) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown with optional code snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, checklists, implementation steps, verification notes, and follow-up risks.] <br>

## Skill Version(s): <br>
0.20260726.120312 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
