## Description: <br>
Exercise a portable OpenClaw skill bundle in tests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nancymx-dev](https://clawhub.ai/user/nancymx-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and release reviewers use this skill to validate portable OpenClaw skill discovery, supported text files, frontmatter, and bundled-resource loading without external services or credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes an executable shell script. <br>
Mitigation: Review the bundled verifier before execution; evidence indicates it only checks expected files and prints a fixed success message. <br>


## Reference(s): <br>
- [Fixture contract](references/fixture-contract.md) <br>
- [ClawHub skill page](https://clawhub.ai/nancymx-dev/skills/test-skill-5) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and plain text verifier output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local fixture-validation guidance and a fixed success message when the bundled verifier passes.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
