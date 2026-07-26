## Description: <br>
Overllm helps agents run a local static linter to find unnecessary GPT, Claude, or other LLM API calls that deterministic code can replace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[theadamdanielsson](https://clawhub.ai/user/theadamdanielsson) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to audit Python and JavaScript or TypeScript codebases for unnecessary LLM calls, review structured findings, and identify deterministic replacements before committing code or gating CI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may require installing and running the external overllm package. <br>
Mitigation: Install and run it only when that dependency is acceptable for the target environment. <br>
Risk: The --fix and --unsafe-fixes modes can edit files. <br>
Mitigation: Use normal read-only scans by default, review changes before applying fixes, and prefer --diff when assessing edits. <br>


## Reference(s): <br>
- [Overllm homepage](https://github.com/theadamdanielsson/overllm) <br>
- [Overllm on ClawHub](https://clawhub.ai/theadamdanielsson/skills/overllm) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and summarized linter findings; scans can also emit JSON, SARIF, GitHub annotations, Markdown, or human-readable text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Normal scans are read-only; structured runs should use --format json and --exit-zero so findings are not treated as command failures.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
