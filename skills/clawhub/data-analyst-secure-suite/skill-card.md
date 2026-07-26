## Description: <br>
A secure data analysis workflow suite based on MGC Blackbox, providing credential protection, zero-exposure script application, script sealing collaboration, and knowledge management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zkeviny](https://clawhub.ai/user/zkeviny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Data analysts, teams, and organizations use this skill to manage local credential storage, user-owned script application, secure collaboration, and reusable analysis knowledge through MGC Blackbox workflows. Developers can also use its system prompt template to configure a data-analysis agent that asks for explicit authorization before sensitive operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credential-handling examples and zero-exposure claims may not fully align with the behavior a deployment provides. <br>
Mitigation: Review the skill before installation, especially for production credentials or business-sensitive knowledge, and verify MGC credential flow, token protection, token expiration, and revocation behavior. <br>
Risk: MGC scripts are trusted local code that may receive raw secrets. <br>
Mitigation: Require explicit approval for every secret or script use, avoid broad or unreviewed scripts, and run only reviewed user-owned scripts that comply with organizational policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/data-analyst-secure-suite) <br>
- [MGC Blackbox repository](https://github.com/zkeviny/MGC-Blackbox) <br>
- [README](artifact/README.md) <br>
- [Data Analyst Agent system prompt template](artifact/agent_system_prompt.md) <br>
- [Credential management workflow](artifact/prompts/credential_management.md) <br>
- [Script management workflow](artifact/prompts/script_management.md) <br>
- [Knowledge management workflow](artifact/prompts/knowledge_management.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user authorization for sensitive credential, script, or knowledge operations.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
