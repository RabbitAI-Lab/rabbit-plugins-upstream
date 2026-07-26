## Description: <br>
ThinkWiki helps agents create, maintain, query, and visualize a local Markdown knowledge base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wzdavid](https://clawhub.ai/user/wzdavid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and knowledge workers use ThinkWiki to manage a local Markdown wiki, import source material, answer questions from existing pages, and generate viewer, graph, inbox, and governance artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional LLM or embedding integrations can send relevant wiki content to configured providers. <br>
Mitigation: Enable those API keys only when the provider and data-sharing posture are acceptable for the wiki contents. <br>
Risk: Entity merge operations may consolidate pages or aliases incorrectly if merge plans are not reviewed. <br>
Mitigation: Review entity merge plans before applying them and use dry-run or preview outputs for ambiguous groups. <br>
Risk: Runtime files and dependencies are installed from the referenced ThinkWiki source. <br>
Mitigation: Verify the source repository, imported commit, and dependency provenance before installation. <br>


## Reference(s): <br>
- [ClawHub ThinkWiki Skill](https://clawhub.ai/wzdavid/skills/thinkwiki) <br>
- [Server-resolved Source Repository](https://github.com/wzdavid/ThinkWiki) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command blocks and generated Markdown or HTML file artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local wiki root and optional LLM or embedding environment variables for remote AI features.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
