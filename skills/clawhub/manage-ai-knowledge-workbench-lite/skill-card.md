## Description: <br>
AI Knowledge Workbench Lite lets an agent build and refresh a metadata-only Markdown or Obsidian knowledge index with an offline HTML dashboard for one authorized local workspace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexfengrui](https://clawhub.ai/user/alexfengrui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Knowledge workers, developers, and other external users can use this skill to turn an authorized local Markdown folder or Obsidian Vault into a derived metadata index and offline dashboard without modifying source notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent scans metadata from the selected local Markdown or Obsidian workspace. <br>
Mitigation: Install and run the skill only for folders the user has explicitly authorized for metadata scanning. <br>
Risk: The skill creates derived .ai-workbench, AI-Knowledge, and AI-Dashboard directories inside the chosen workspace. <br>
Mitigation: Treat those directories as generated outputs and continue editing the original source notes rather than the derived index. <br>
Risk: Dashboard verification briefly binds a loopback listener. <br>
Mitigation: Use the listener only for local verification and do not present the Lite release as a persistent web service. <br>
Risk: Users may expect automatic background watching from the phrase "automatic update". <br>
Mitigation: Describe updates as foreground, user-requested refreshes; the Lite release does not run continuously in the background. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexfengrui/skills/manage-ai-knowledge-workbench-lite) <br>
- [Privacy boundary](references/PRIVACY.md) <br>
- [Runtime contract](references/RUNTIME_CONTRACT.md) <br>
- [Autonomy gates](references/AUTONOMY_GATES.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Agent guidance with JSON command results and generated Markdown and HTML files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Metadata-only derived outputs are written inside the authorized workspace.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter, README, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
