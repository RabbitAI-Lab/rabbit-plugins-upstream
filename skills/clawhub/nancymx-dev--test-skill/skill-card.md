## Description: <br>
Exercises a portable OpenClaw skill bundle for validating skill discovery, supported text files, frontmatter, and bundled-resource loading without external services or credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nancymx-dev](https://clawhub.ai/user/nancymx-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and test automation use this skill to validate that a portable OpenClaw skill fixture is discoverable, packaged correctly, and able to load bundled resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundle includes a shell verifier that runs local file checks. <br>
Mitigation: Review scripts/verify.sh before execution and run it only in environments where bundled verification scripts are acceptable. <br>


## Reference(s): <br>
- [Fixture contract](references/fixture-contract.md) <br>
- [ClawHub skill page](https://clawhub.ai/nancymx-dev/skills/test-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with an inline shell command and plain-text verifier output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires POSIX sh on macOS or Linux; no network, credential, package-install, or external-service dependency.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
