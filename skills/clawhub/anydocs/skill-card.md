## Description: <br>
Generic Documentation Indexing & Search. Index any documentation site (SPA/static) and search it instantly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pektech](https://clawhub.ai/user/pektech) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to configure documentation profiles, index documentation sites, and retrieve ranked search results or fetched page content from local indexes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make outbound requests to configured or supplied documentation URLs. <br>
Mitigation: Use trusted documentation profiles and review configured base and sitemap URLs before indexing. <br>
Risk: Scraped documentation text and search indexes are cached locally. <br>
Mitigation: Avoid indexing confidential or authenticated documentation unless local caching is approved, and clear ~/.anydocs/cache when retention is no longer needed. <br>
Risk: Optional browser rendering can use a configurable gateway and token. <br>
Mitigation: Use browser rendering only with trusted local or HTTPS gateways, protect gateway tokens, and avoid passing tokens through shell history. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pektech/skills/anydocs) <br>
- [README](artifact/README.md) <br>
- [Quick Start](artifact/examples/QUICKSTART.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, plain text, CLI output, JSON configuration, and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include ranked documentation titles, URLs, relevance scores, tags, and snippets when an index is available.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and artifact manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
