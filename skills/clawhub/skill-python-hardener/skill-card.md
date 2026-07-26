## Description: <br>
Hardens Python scripts by applying a security review, clean-code refactoring, robust error handling, proper logging, and docstring coverage, then produces a companion Markdown documentation file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kikikari](https://clawhub.ai/user/kikikari) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review and harden Python scripts, especially when they need security fixes, safer error handling, logging, type hints, docstrings, and maintainability improvements. It is intended for user-provided Python files and preserves original filenames while adding one companion documentation file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may make in-place changes to Python files, and broad requests such as fixing an entire script can produce larger diffs than expected. <br>
Mitigation: Review the generated diff before accepting changes, especially when multiple Python files are involved. <br>
Risk: Security hardening and refactoring can unintentionally change behavior in code that lacks tests or clear runtime expectations. <br>
Mitigation: Run the project's tests or a representative smoke test after applying the changes. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/KikiKari/OpenClaw/tree/main/packages/skill-python-hardener) <br>
- [ClawHub skill page](https://clawhub.ai/kikikari/skills/skill-python-hardener) <br>


## Skill Output: <br>
**Output Type(s):** [code, markdown, guidance] <br>
**Output Format:** [Edited Python files plus one Markdown documentation file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves original Python filenames and writes one companion documentation file unless the user explicitly asks for additional files.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
