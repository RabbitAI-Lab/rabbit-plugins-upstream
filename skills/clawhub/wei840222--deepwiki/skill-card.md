## Description: <br>
Retrieve source-backed understanding of public GitHub projects: repository structure, package boundaries, architecture, data flow, and codebase-specific behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wei840222](https://clawhub.ai/user/wei840222) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill for onboarding, subsystem exploration, implementation research, and repository-grounded Q&A on public GitHub repositories when general library documentation is insufficient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public DeepWiki or public MCP calls can expose private or unverified repository names, URLs, source, or metadata. <br>
Mitigation: Run the repository visibility preflight first and proceed with public DeepWiki only when GitHub returns a canonical public owner/repo; use an approved Devin/private MCP path for private repositories. <br>
Risk: Generated DeepWiki documentation can be sparse, stale, or incomplete for consequential implementation or security decisions. <br>
Mitigation: Use read_wiki_structure before focused questions and verify high-risk claims against repository source before editing code or making recommendations. <br>
Risk: Full wiki retrieval and repeated failures can create unnecessary large outputs, load, or duplicate exposure. <br>
Mitigation: Use read_wiki_contents only when broad extraction is explicitly needed, apply bounded candidate failover, retry rate limits at most once, and stop immediately on authentication failures. <br>


## Reference(s): <br>
- [DeepWiki via mcporter](references/mcporter-workflow.md) <br>
- [DeepWiki MCP API Fallback](references/api-fallback.md) <br>
- [DeepWiki](https://deepwiki.com/) <br>
- [Devin DeepWiki Docs](https://docs.devin.ai/work-with-devin/deepwiki) <br>
- [DeepWiki MCP Docs](https://docs.devin.ai/work-with-devin/deepwiki-mcp) <br>
- [DeepWiki Skill on ClawHub](https://clawhub.ai/wei840222/skills/deepwiki) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and source references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include DeepWiki links, source-file references, structured diagnostics, and bounded fallback guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
