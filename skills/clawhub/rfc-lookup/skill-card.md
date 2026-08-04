## Description: <br>
Look up IETF RFCs, inspect relevant sections, verify current status, and flag superseded specifications before citation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shbernal](https://clawhub.ai/user/shbernal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, standards reviewers, and agents use this skill to find the right IETF RFC, check whether it is current, read targeted sections, and quote normative language with verifiable section citations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches RFC data from RFC Editor and may cache RFC text locally. <br>
Mitigation: Use it only where outbound RFC Editor access and local cache writes are acceptable, and review the configured mirror directory before use. <br>
Risk: Full-text mode can download a roughly 512 MB RFC corpus into the configured mirror directory. <br>
Mitigation: Run the sync command only after explicit user approval and after confirming disk space and the intended mirror path. <br>
Risk: Citing an obsolete RFC can produce incorrect standards guidance. <br>
Mitigation: Run the metadata check before citation, follow replacement RFCs when an obsolescence banner appears, and cite the specific section used. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shbernal/skills/rfc-lookup) <br>
- [Release changelog](https://github.com/shbernal/rfc-ai-tooling/releases/tag/v0.2.3) <br>
- [RFC Editor index](https://www.rfc-editor.org/rfc-index.txt) <br>
- [RFC Editor text corpus](https://www.rfc-editor.org/rfc/) <br>
- [mcp-server-ietf parsing reference](https://github.com/tizee/mcp-server-ietf) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include RFC headers, obsolescence and update banners, search result totals, section line ranges, and section-scoped RFC excerpts.] <br>

## Skill Version(s): <br>
0.2.3 (source: release evidence and script __version__) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
