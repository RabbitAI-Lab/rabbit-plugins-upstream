## Description: <br>
Privacy Search helps an agent run multi-engine search workflows with privacy modes, local SearXNG management, result deduplication, diagnostics, and optional JSON output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to perform privacy-oriented command-line searches, select search engines, manage a local SearXNG instance, inspect privacy settings, and diagnose network, configuration, or engine failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Strict privacy mode can automatically send searches to lower-privacy engines. <br>
Mitigation: Prefer explicitly selecting trusted engines such as local SearXNG, and ask the publisher to make lower-privacy fallback opt-in. <br>
Risk: Search queries may be sensitive and can disclose metadata to selected search engines or update services. <br>
Mitigation: Review before installing, use local SearXNG for sensitive searches, and disable update checks when metadata disclosure matters. <br>
Risk: The pip and Docker latest SearXNG setup paths may introduce supply-chain risk. <br>
Mitigation: Avoid latest-tag install paths unless reviewed, and pin or verify dependencies and container images before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fyniujin/skills/privacy-search) <br>
- [Quick Start Guide](references/QUICK_START.md) <br>
- [Search Engine Adapter Documentation](references/engines.md) <br>
- [Domestic Search Engine Guide](references/engines_zh.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text or JSON search results, Markdown guidance, shell commands, and configuration recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Searches may contact external engines unless local SearXNG or explicitly trusted engines are selected.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
