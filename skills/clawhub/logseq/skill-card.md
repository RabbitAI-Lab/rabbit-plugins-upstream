## Description: <br>
Provide commands for creating pages, inserting blocks, querying the graph database, managing tasks, retrieving content, and automating workflows through a local Logseq instance with the Plugin API enabled. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juanirm](https://clawhub.ai/user/juanirm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to automate a locally running Logseq graph through the Plugin API, including page creation, block edits, task management, database queries, Git operations, and asset workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Logseq API bridge can expose broad access to local notes and graph operations. <br>
Mitigation: Keep the bridge localhost-only, require an auth token, allowlist only needed methods, confirm deletes and bulk changes, restrict Git commands, and keep backups or version control enabled. <br>


## Reference(s): <br>
- [Logseq Skill Page](https://clawhub.ai/juanirm/skills/logseq) <br>
- [Logseq Plugin API Documentation](https://logseq.github.io/plugins/) <br>
- [Logseq Plugin Samples](https://github.com/logseq/logseq-plugin-samples) <br>
- [API Reference](references/api-reference.md) <br>
- [Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JavaScript, TypeScript, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are guidance and code examples for local Logseq automation; bridge setup and API execution remain user-controlled.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
