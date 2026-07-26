## Description: <br>
Manage AI agent personas for OpenClaw by installing, switching, restoring, creating, validating, publishing, and syncing Soul persona packages through the ClawSouls CLI and registry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomleelive](https://clawhub.ai/user/tomleelive) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and agent operators use this skill to manage AI agent persona packages in OpenClaw-compatible workspaces. It supports browsing, installing, switching, restoring, creating, validating, publishing, and syncing personas when the user explicitly asks for those actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persona switching can replace local agent identity files in the workspace. <br>
Mitigation: Confirm before switching personas and keep the built-in backup and restore workflow enabled. <br>
Risk: Publishing uploads selected soul directories to a public registry. <br>
Mitigation: Confirm before publishing, list the files to be uploaded, and avoid publishing sensitive prompts, memories, or client data. <br>
Risk: Memory sync can push encrypted agent memory to a configured remote. <br>
Mitigation: Run sync or swarm only on explicit user request and verify the remote and encryption setup before use. <br>
Risk: CLI behavior may vary if the latest package is resolved dynamically. <br>
Mitigation: Pin and review the ClawSouls CLI version when reproducible installs are required. <br>


## Reference(s): <br>
- [Clawsouls Skill on ClaWHub](https://clawhub.ai/tomleelive/skills/clawsouls) <br>
- [ClawSouls Registry](https://clawsouls.ai) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [ClawSouls CLI npm Package](https://www.npmjs.com/package/clawsouls) <br>
- [Soul Spec MCP](https://github.com/clawsouls/soul-spec-mcp) <br>
- [Soul-Driven Interaction Design](https://doi.org/10.5281/zenodo.18772585) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline CLI commands and generated persona or configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or run ClawSouls CLI actions that modify local persona files, contact the registry, publish selected soul directories, or sync encrypted memory only after explicit user confirmation.] <br>

## Skill Version(s): <br>
0.6.4 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
