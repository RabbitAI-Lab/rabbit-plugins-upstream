## Description: <br>
Audit AI agent skills for security vulnerabilities, including OWASP Agentic Skills Top 10 checks, pre-run safety reviews, CI/CD gating, and audit reports in text, JSON, SARIF, or HTML. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[markeljan](https://clawhub.ai/user/markeljan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and platform teams use Agentsec to audit installed AI agent skills, check OWASP Agentic Skills Top 10 coverage, gate CI/CD workflows, and generate security reports for stakeholders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Default scans may read broader local skill or project folders than a user expects. <br>
Mitigation: Review the folders to be scanned before running Agentsec and pass an explicit path when only one project or skill directory should be checked. <br>
Risk: Generated reports may include local file paths, skill metadata, or snippets from private local skill files. <br>
Mitigation: Treat generated reports as sensitive review artifacts and avoid sharing them outside the intended audience without redaction. <br>


## Reference(s): <br>
- [Agentsec Homepage](https://agentsec.sh) <br>
- [Agent Skills Specification](https://agentskills.io/specification) <br>
- [Skills Ecosystem](https://skills.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and report formats including text, JSON, SARIF, and HTML] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate or reference local audit report files when an output path is supplied.] <br>

## Skill Version(s): <br>
0.4.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
