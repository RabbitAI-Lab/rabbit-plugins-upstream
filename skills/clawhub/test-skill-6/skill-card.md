## Description: <br>
Exercise a portable OpenClaw skill bundle in tests. Use when validating skill discovery, supported text files, frontmatter, or bundled-resource loading without external services or credentials. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[nancymx-dev](https://clawhub.ai/user/nancymx-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and release testers use this skill to validate OpenClaw skill discovery, packaging, supported text files, frontmatter, and bundled-resource loading without external services or credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes a shell verifier that users may run locally. <br>
Mitigation: Review the bundled script before execution; the security evidence indicates it only checks for expected files and prints a fixed success message. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nancymx-dev/skills/test-skill-6) <br>
- [Publisher profile](https://clawhub.ai/user/nancymx-dev) <br>
- [Fixture contract](references/fixture-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and plain text verifier output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local validation guidance and a fixed success message when bundled files are present.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
