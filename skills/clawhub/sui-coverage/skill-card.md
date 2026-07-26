## Description: <br>
Analyze Sui Move test coverage, identify untested code, write missing tests, and perform security audits. Includes Python tools for parsing coverage output and generating reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[easonc13](https://clawhub.ai/user/easonc13) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to analyze Sui Move coverage, identify uncovered functions, assertions, and branches, and create or refine tests with security-oriented review notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the skill directs agents to stage and commit repository changes without an explicit approval step. <br>
Mitigation: Require explicit user approval before any git add or git commit, and review diffs before accepting generated tests or audit findings. <br>
Risk: The skill runs local Sui coverage commands and may write generated reports or tests in a Move package. <br>
Mitigation: Run it in a trusted workspace, confirm target package paths, and review generated files before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/easonc13/skills/sui-coverage) <br>
- [Sui install guide](https://docs.sui.io/guides/developer/getting-started/sui-install) <br>
- [Sui Coverage homepage](https://github.com/EasonC13-agent/sui-coverage-demo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON summaries, Move test code, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write coverage reports such as coverage.md or JSON when invoked with output flags; requires python3 and sui binaries.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
