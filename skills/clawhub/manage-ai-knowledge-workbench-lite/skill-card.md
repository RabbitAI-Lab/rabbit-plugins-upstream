## Description: <br>
Autonomously build and refresh on demand a metadata-only local Markdown or Obsidian knowledge index with an offline HTML dashboard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexfengrui](https://clawhub.ai/user/alexfengrui) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
Developers and agent users use this skill to build a local, metadata-only knowledge workbench from an authorized Markdown folder or Obsidian vault, including derived Markdown indexes, an offline HTML dashboard, status checks, on-demand refresh, and safe uninstall. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads authorized Markdown files to extract metadata and structure. <br>
Mitigation: Install it only for directories the user is willing to have scanned for metadata, and keep note bodies out of model transport and dashboard output. <br>
Risk: The skill writes derived dashboard and index files inside the selected workspace. <br>
Mitigation: Limit operation to a user-authorized workspace and distinguish derived folders from original source notes. <br>
Risk: The build performs a temporary loopback verification step. <br>
Mitigation: Use it as a local build verification step and stop it after verification rather than treating it as a persistent service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexfengrui/skills/manage-ai-knowledge-workbench-lite) <br>
- [Runtime contract](references/RUNTIME_CONTRACT.md) <br>
- [Privacy boundary](references/PRIVACY.md) <br>
- [Autonomy gates](references/AUTONOMY_GATES.md) <br>
- [OpenClaw Getting Started](https://docs.openclaw.ai/start/getting-started) <br>
- [Python downloads](https://www.python.org/downloads/) <br>
- [Obsidian downloads](https://obsidian.md/download) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, Configuration, Files] <br>
**Output Format:** [Markdown guidance plus JSON command results and generated local Markdown/HTML files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces derived outputs inside the selected workspace and reports structured status codes.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
