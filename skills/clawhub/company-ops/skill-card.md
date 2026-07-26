## Description: <br>
Run a self-improving autonomous company OS from a single CONSTITUTION and confidence-gated autonomy loop. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, agent-company builders, and AI-operations teams use this skill to run a governed autonomy loop for task selection, revenue tracking, operating rules, logging, and repository-oriented follow-through. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically modify and push repository contents with limited containment. <br>
Mitigation: Run it only in a dedicated least-privilege repository with no secrets or unrelated files, and require allowlists, review, and secret scanning before enabling automatic pushes. <br>
Risk: The bundled verifier executes Python during validation. <br>
Mitigation: Run verification only in an isolated environment for untrusted submissions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/company-ops) <br>
- [README](artifact/README.md) <br>
- [CONSTITUTION](artifact/CONSTITUTION.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with Python and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write operational logs and repository changes when the autonomy loop is executed.] <br>

## Skill Version(s): <br>
2.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
