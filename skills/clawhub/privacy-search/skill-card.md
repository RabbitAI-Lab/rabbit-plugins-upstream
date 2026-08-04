## Description: <br>
Privacy Search helps agents run multi-engine web searches with privacy modes, local SearXNG support, caching, diagnostics, and ranked result output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to perform parallel web searches across configured engines, inspect privacy posture, manage local SearXNG, and return ranked or JSON search results for downstream workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to the configured search engines, so those services may receive query text and network metadata. <br>
Mitigation: Use strict mode, prefer local SearXNG, and configure a proxy or VPN when IP privacy matters. <br>
Risk: Search cache and history are stored locally by default and can leave traces on shared or sensitive machines. <br>
Mitigation: Disable caching, turn logging off for sensitive use, and clear existing cache and history when needed. <br>
Risk: The pip-based SearXNG setup path may install unpinned packages. <br>
Mitigation: Prefer the Docker SearXNG path or review package sources before using the pip setup flow. <br>
Risk: Automatic update checks may send update metadata from the machine. <br>
Mitigation: Disable update checks when outbound update metadata is not acceptable. <br>


## Reference(s): <br>
- [Privacy Search skill page](https://clawhub.ai/fyniujin/skills/privacy-search) <br>
- [Quick start guide](references/QUICK_START.md) <br>
- [Engine reference](references/engines.md) <br>
- [Chinese engine and fallback reference](references/engines_zh.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text or JSON results with Markdown documentation and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results may be cached locally and can include privacy reports, engine diagnostics, and ranked result metadata.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
