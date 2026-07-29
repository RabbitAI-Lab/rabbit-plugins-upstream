## Description: <br>
One-click market viability assessment for Amazon sellers that analyzes market size, competition intensity, brand landscape, pricing structure, and consumer pain points to deliver a GO/CAUTION/AVOID recommendation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and commerce analysts use this skill to evaluate a named product niche or category, compare sub-markets, and decide whether market entry is GO, CAUTION, or AVOID. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled ZooData CLI can access more ZooData endpoints than the market-entry workflow normally uses, which can broaden API activity and credit spend. <br>
Mitigation: Use the market-entry workflow or documented granular commands only, avoid unrelated subcommands, and monitor ZooData credit consumption. <br>
Risk: Composite market-entry scans and review fallback processing can consume multiple API credits. <br>
Mitigation: Estimate credit cost before broad scans, confirm with the user for multi-call workflows, and use granular commands under a credit cap. <br>
Risk: Credentials can be read from local configuration and temporary review work directories may remain after fallback processing. <br>
Mitigation: Prefer ZOODATA_API_KEY over local credential files and clean /tmp review work directories after review fallback processing. <br>


## Reference(s): <br>
- [API Field Reference](references/reference.md) <br>
- [ZooData-Skills repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-market-entry-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report with structured tables, confidence labels, data provenance, API usage, and inline shell commands when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and may consume ZooData API credits for multi-call market scans.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
