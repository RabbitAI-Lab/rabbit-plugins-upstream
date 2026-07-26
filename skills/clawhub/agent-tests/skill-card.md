## Description: <br>
Define, run, and track tests for agent behavior with test cases, assertions, regression tracking, and performance benchmarking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to define behavioral tests, run assertion checks, benchmark test cases, and review regressions before or after agent changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Test prompts, expected outputs, assertions, fixtures, and result history are stored on disk and may contain sensitive data if users include it. <br>
Mitigation: Do not place API keys, passwords, private customer data, or other secrets in tests or fixtures unless the storage location is managed appropriately. <br>
Risk: The framework simulates agent output for its core test runner unless integrated with actual agent execution. <br>
Mitigation: Use results as framework-level behavioral checks and connect actual agent output before relying on pass rates for production regression decisions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and terminal text with inline shell commands and JSON-backed test data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores test definitions, results, and benchmark history in local JSON files under memory/agent-tests or a configured directory.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
