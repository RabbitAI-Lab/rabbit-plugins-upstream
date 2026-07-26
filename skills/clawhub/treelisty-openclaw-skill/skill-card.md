## Description: <br>
TreeListy helps agents decompose complex projects and nested information into hierarchical plans using specialized patterns, then export the trees as JSON, Markdown, Mermaid, CSV, checklist, or HTML. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[prairie2cloud](https://clawhub.ai/user/prairie2cloud) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and agents use TreeListy to turn complex goals, outlines, and planning inputs into structured trees for project planning, analysis, documentation, and visual diagrams. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated or exported trees may contain sensitive project, family, email, filesystem, knowledge-base, or speech-analysis content. <br>
Mitigation: Keep tree files local by default, review exports before sharing, and avoid including sensitive information unless the destination is trusted. <br>
Risk: The optional push command can send a tree to a WebSocket bridge host. <br>
Mitigation: Use push only with your own trusted local TreeListy bridge, and avoid untrusted hosts unless you intentionally want to transmit the tree there. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/prairie2cloud/skills/treelisty-openclaw-skill) <br>
- [TreeListy Pattern Reference](references/PATTERNS.md) <br>
- [TreeListy Web App](https://treelisty.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated tree outputs in JSON, Markdown, Mermaid, CSV, checklist, or HTML] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local Node.js CLI processing; optional WebSocket push to a trusted TreeListy bridge.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, skill metadata, and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
