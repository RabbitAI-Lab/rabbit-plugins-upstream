## Description: <br>
Secure database credential management using MGC Blackbox for MySQL, PostgreSQL, SQLite, MariaDB, and related database workflows while avoiding direct credential exposure to AI models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zkeviny](https://clawhub.ai/user/zkeviny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use this skill to design database workflows that store credentials in MGC Blackbox, reference them by identifier, and retrieve them through trusted local execution paths instead of placing passwords in prompts, logs, or skill files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calling mgc_get for real credential records can place secret material into the agent context. <br>
Mitigation: Use trusted local scripts to retrieve credentials and return only non-sensitive results; call mgc_get for real credential records only with explicit user approval. <br>
Risk: Sealed-script examples using action="run" represent code execution. <br>
Mitigation: Require explicit user approval and trusted script provenance before running sealed scripts; inspect or scan scripts where possible before execution. <br>
Risk: The release under-discloses sensitive credential retrieval and script execution paths. <br>
Mitigation: Review the security guidance before enabling the skill and define deployment-specific boundaries for MGC access and database operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/mgc-database-security) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown documentation with tool-call examples, configuration snippets, and conceptual code patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; examples reference MGC MCP tools and local script patterns rather than providing executable code in the artifact.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
