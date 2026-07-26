## Description: <br>
Generates basic SBOM data for npm and pip projects and helps check packages and dependencies against OSV and related vulnerability data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security-minded maintainers use this skill to inspect npm or pip dependencies, generate a lightweight SBOM, and identify known vulnerability matches before dependency updates or routine project security checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dependency names and versions from private projects may be sent to external OSV, npm, or PyPI services during lookups. <br>
Mitigation: Review before use in private repositories and run only when sharing dependency metadata with those services is acceptable. <br>
Risk: The skill can propose or run shell commands for package inspection, audit, and SBOM generation. <br>
Mitigation: Review commands before execution, run in a controlled workspace, and install required tools such as jq, npm, or pip-audit deliberately. <br>
Risk: The artifact's trigger text incorrectly mentions database and SQL tasks, which could cause off-purpose activation. <br>
Mitigation: Correct the trigger text and restrict routine use to SBOM and dependency vulnerability tasks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bom-vuln-intel-tool-free) <br>
- [OSV API](https://api.osv.dev) <br>
- [npm registry](https://registry.npmjs.org) <br>
- [PyPI](https://pypi.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and JSON snippets; generated SBOM and vulnerability results may be returned as text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires agent command execution; external lookups may contact OSV, npm registry, and PyPI.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
