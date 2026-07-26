## Description: <br>
Advanced AI-powered search skill using SearXNG as the universal search backend. Multi-engine dork generation, 90+ search engines, intelligent search strategies, intent parsing, result analysis, and adaptive query refinement. No API keys required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[elmaslouhymouaad](https://clawhub.ai/user/elmaslouhymouaad) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to run SearXNG-backed web, OSINT, SEO, security research, academic, code, file, news, image, video, and social searches from natural language or explicit dork queries. It returns scored, deduplicated search results and suggested refinements for downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can generate and run searches for exposed secrets, admin panels, personal data, and other sensitive OSINT targets. <br>
Mitigation: Use it only for authorized research, restrict searches to approved domains or entities, and review generated dork queries before execution. <br>
Risk: Search queries may be sent through third-party engines configured behind the selected SearXNG instance. <br>
Mitigation: Use a trusted self-hosted SearXNG instance and avoid submitting confidential targets, personal identifiers, or sensitive internal terms. <br>
Risk: Piracy-oriented engines or search categories can surface inappropriate or unauthorized file sources. <br>
Mitigation: Disable or avoid those engines and limit file-hunting workflows to legitimate, authorized research tasks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/elmaslouhymouaad/search-intelligence-skill) <br>
- [Publisher profile](https://clawhub.ai/user/elmaslouhymouaad) <br>
- [README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured Python objects with scored search results, snippets, URLs, metadata, suggestions, errors, and timing information.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.9+, httpx, and a reachable SearXNG instance with JSON output enabled.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
