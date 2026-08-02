## Description: <br>
Helps software teams add useful unit tests, raise coverage, and document verification steps for existing codebases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, open-source maintainers, and product teams use this skill to plan and produce unit-test improvements for existing codebases. It supports implementation steps, reusable checklists or workflows, code changes, test commands, and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may activate the skill for general testing or quality requests. <br>
Mitigation: Explicitly name the intended skill or workflow when a task is not about unit-test coverage, and confirm the selected workflow before following its recommendations. <br>
Risk: Generated test plans, code changes, or shell commands may be incomplete or incorrect for a specific repository. <br>
Mitigation: Review proposed changes before applying them, run the repository's local test suite or coverage command, and keep assumptions and remaining risks visible in the final output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/unit-test-coverage-helper-030357) <br>
- [Requirement plan](references/requirement-plan.md) <br>
- [sw-loop.sh Monolith Decomposition into Focused Modules](https://github.com/sethdford/shipwright/issues/779) <br>
- [Reconcile CRM schema documentation with canonical migrations 015 and 016](https://github.com/saberistic-team/agent-web/issues/277) <br>
- [docs: resync 4 stale fr/es quickstart translations + re-baseline i18n-lag](https://github.com/mnemom/docs/issues/409) <br>
- [CI Monitor Daily Report 2026-07-22](https://github.com/bingxche/sglang-ci-bot/issues/143) <br>
- [Flaky Vulkan unit test results on some Intel Battlemage Linux systems](https://github.com/ggml-org/llama.cpp/issues/25767) <br>
- [Preventing LLM unit test spam](https://blog.larah.me/test-slop/) <br>
- [Skillgrade: unit tests for agent skills](https://github.com/mgechev/skillgrade) <br>
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with optional code blocks and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, limits, reusable checklists or workflows, and verification notes.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
