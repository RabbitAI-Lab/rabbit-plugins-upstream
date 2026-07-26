## Description: <br>
Exercise a portable OpenClaw skill bundle when validating skill discovery, supported text files, frontmatter, or bundled-resource loading without external services or credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nancymx-dev](https://clawhub.ai/user/nancymx-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill as a portable fixture for local and automated validation of OpenClaw skill discovery, packaging, bundled resource loading, and verifier behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes a shell verifier that should be run only against the intended fixture directory. <br>
Mitigation: Review scripts/verify.sh before use and run it from the fixture directory or pass the intended directory explicitly. <br>


## Reference(s): <br>
- [Fixture contract](references/fixture-contract.md) <br>
- [ClawHub release page](https://clawhub.ai/nancymx-dev/skills/test-skill-3) <br>
- [Publisher profile](https://clawhub.ai/user/nancymx-dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell command examples and plain-text verifier output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled verifier prints a stable success message from assets/expected-output.txt when required fixture files are present.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
