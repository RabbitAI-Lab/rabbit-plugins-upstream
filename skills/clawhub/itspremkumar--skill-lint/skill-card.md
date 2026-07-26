## Description: <br>
Lint ClawHub SKILL.md files for frontmatter, structure, command documentation, thin content, and common package issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Skill authors and release maintainers use this skill to validate ClawHub/OpenClaw skill folders before publishing, including frontmatter, structure, command documentation, file size, and JSON lint output checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The included CI verifier can run Python files from target folders without sandboxing. <br>
Mitigation: Run ci/verify_product.py only in isolated CI or container environments with no secrets when evaluating untrusted repositories or submitted skills. <br>
Risk: Static lint checks can miss behavioral or policy issues outside the checked frontmatter, structure, and file-size rules. <br>
Mitigation: Pair the linter results with human review and security scanning before deploying or publishing a skill. <br>


## Reference(s): <br>
- [ClawHub Skill Lint page](https://clawhub.ai/itspremkumar/skills/skill-lint) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON command-line lint results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local filesystem checks and Python standard-library scripts; CI verification should be run only in an isolated environment when targets are untrusted.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
