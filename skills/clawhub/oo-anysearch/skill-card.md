## Description: <br>
AnySearch connects an agent to OOMOL's AnySearch connector for search, batch search, sub-domain discovery, and HTML page extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run AnySearch searches and page extraction through an OOMOL-connected AnySearch account without handling raw credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can use the connected AnySearch account for search and extraction actions. <br>
Mitigation: Only connect an AnySearch account whose search and extraction access is appropriate to delegate to the agent. <br>
Risk: First-time setup may require installing the oo CLI before the connector can run. <br>
Mitigation: Review the oo CLI installation step and install guide before running first-time setup commands. <br>


## Reference(s): <br>
- [ClawHub AnySearch Skill Page](https://clawhub.ai/oomol/skills/oo-anysearch) <br>
- [AnySearch Homepage](https://anysearch.com/home) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON returned through oo CLI command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search responses include data and meta.executionId when run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
