## Description: <br>
GNO helps agents index, search, retrieve, and answer questions over local documents, notes, files, and knowledge bases using keyword, vector, and hybrid search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nicoataiza](https://clawhub.ai/user/nicoataiza) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, knowledge workers, and agent users use this skill to search local folders, build searchable knowledge bases, retrieve document content, run local Q&A with citations, and configure GNO's MCP integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Indexing broad local folders can expose private documents or secrets through search results, snippets, MCP tools, or generated answers. <br>
Mitigation: Index only folders the user intentionally wants searchable, exclude sensitive paths, and avoid broad home-directory collections. <br>
Risk: Serving a web UI for private indexed documents can expose local content if it is bound beyond localhost. <br>
Mitigation: Bind the GNO web UI to localhost unless the user has intentionally configured network access and access controls. <br>
Risk: MCP write tools and destructive maintenance commands can make persistent changes to files, indexes, or agent configuration. <br>
Mitigation: Do not enable MCP write tools, use --force, or run reset, cleanup, or skill-install commands unless the user explicitly requests those persistent changes. <br>
Risk: The skill depends on a local gno CLI whose source and installation are outside the card evidence. <br>
Mitigation: Install and run the gno CLI only from a trusted source and verify the intended local configuration before indexing documents. <br>


## Reference(s): <br>
- [GNO CLI Reference](cli-reference.md) <br>
- [GNO Usage Examples](examples.md) <br>
- [GNO MCP Installation](mcp-reference.md) <br>
- [GNO MCP Documentation](https://www.gno.sh/docs/MCP) <br>
- [ClawHub Skill Page](https://clawhub.ai/nicoataiza/skills/gno-bak-2026-01-28t18-01-20-10-30) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON snippets, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose GNO CLI commands, MCP configuration, local indexing workflows, search queries, and document retrieval steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
