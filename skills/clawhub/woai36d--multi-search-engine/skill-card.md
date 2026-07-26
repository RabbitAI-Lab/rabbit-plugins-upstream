## Description: <br>
Multi Search Engine helps agents query and aggregate results from 16 Chinese and global search engines without API keys, with support for advanced operators, time filters, site search, privacy-focused engines, and WolframAlpha knowledge queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to run multi-source web searches across Chinese and global search providers, apply advanced search operators, and summarize the collected results into a search report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms may be sent to multiple third-party search providers, potentially across regions. <br>
Mitigation: Do not use secrets, confidential project names, regulated data, or sensitive personal searches; constrain the selected engine when privacy matters. <br>
Risk: The artifact privacy notice says there is no external data transmission even though search requests transmit query text to third-party engines. <br>
Mitigation: Treat external query transmission as expected behavior and disclose it clearly before deployment or use. <br>
Risk: Automated search requests may trigger provider rate limits or terms-of-service issues if used aggressively. <br>
Mitigation: Use controlled batching, delays between requests, and comply with each search provider's terms and crawling policies. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/woai36d/skills/multi-search-engine) <br>
- [Domestic Search Guide](artifact/references/advanced-search.md) <br>
- [International Search Guide](artifact/references/international-search.md) <br>
- [Version History](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown search report with web_fetch call examples and summarized search results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No API keys are required; query text may be sent to multiple third-party search providers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and target metadata; artifact files contain conflicting local versions) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
