## Description: <br>
Deploy anything an agent builds to a live URL via the DataEcho platform at https://dataecho.ai: a single file, a static site, or a server-side app with a Dockerfile, with private cloud Drives for agent memory and handoff. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohocp](https://clawhub.ai/user/mohocp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use DataEcho to publish generated files, static sites, and containerized apps to live URLs, then update or claim those deployments. They can also use DataEcho Drives for private, versioned file storage and cross-session handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload files, folders, or app source to a third-party hosting and storage provider. <br>
Mitigation: Confirm the exact path being published and avoid uploading credentials, private documents, proprietary code, or regulated data unless the user has approval. <br>
Risk: The security summary flags unpinned remote install scripts. <br>
Mitigation: Inspect or manually download install scripts before running them instead of piping remote code directly to a shell. <br>
Risk: Credential files, claim files, and Drive share tokens can grant access to deployments or stored files. <br>
Mitigation: Treat ~/.artifact credentials, claim data, and DataEcho Drive share tokens as sensitive secrets and avoid printing or sharing them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mohocp/skills/dataecho) <br>
- [Server-Resolved GitHub Import](https://github.com/mohocp/dataecho/tree/main/skills/dataecho) <br>
- [DataEcho Homepage](https://dataecho.ai) <br>
- [DataEcho Agent Context](https://dataecho.ai/llms-full.txt) <br>
- [DataEcho OpenAPI](https://dataecho.ai/openapi.json) <br>
- [DataEcho Documentation](https://dataecho.ai/docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, code snippets, REST API guidance, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce commands that publish local files, folders, or containerized apps to DataEcho and may write credentials or claim files under ~/.artifact when the user chooses authenticated or claimable workflows.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata); artifact frontmatter reports 1.2.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
