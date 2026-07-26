## Description: <br>
Use when an agent needs to call the FlowUs API through the FlowUs CLI, authenticate FlowUs, upload a file, create or update a page, query a database, search content, edit Markdown page content, or any task involving the `flowus` command. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flowus](https://clawhub.ai/user/flowus) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect FlowUs CLI help, verify authentication, and perform authorized FlowUs API, content, database, search, Markdown, and file workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use configured FlowUs credentials and act through the user's FlowUs account. <br>
Mitigation: Install only for intended FlowUs account use, verify authentication with the CLI before API calls, and avoid exposing bearer tokens in commands, logs, files, or chat. <br>
Risk: Authorized write actions can modify pages, blocks, databases, Markdown content, and uploaded files in a remote workspace. <br>
Mitigation: Review the exact target and expected impact before writes, read current content when feasible, and use available idempotency or version controls. <br>
Risk: Installing or updating the external FlowUs CLI runs downloaded software. <br>
Mitigation: Require explicit user approval, use the official FlowUs CDN URL, verify source, version, and integrity data when available, and prefer manual installation if integrity data is unavailable. <br>


## Reference(s): <br>
- [FlowUs CLI skill on ClawHub](https://clawhub.ai/flowus/skills/flowus-skills) <br>
- [FlowUs CLI installer](https://cdn2.flowus.cn/flowus-cli/install) <br>
- [FlowUs CLI Windows installer](https://cdn2.flowus.cn/flowus-cli/install.ps1) <br>
- [FlowUs API base URL](https://api.flowus.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prefers `--json` command output and local request-body files for stable, reviewable FlowUs operations.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
