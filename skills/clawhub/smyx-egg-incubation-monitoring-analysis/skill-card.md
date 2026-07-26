## Description: <br>
Analyzes turtle or snake egg images or videos to identify shell, vascular, embryo, and quality signals and produce incubation monitoring reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External reptile breeders, farm operators, and hobbyist keepers use this skill to review turtle or snake egg media, monitor fertilization and development signals, and retrieve incubation progress reports. The skill can support smart incubator or breeding-management workflows where users still make final husbandry decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Egg photos, videos, URLs, and history queries are sent to cloud services for analysis and report lookup. <br>
Mitigation: Use only media intended for this service, avoid unrelated sensitive content, and confirm users understand that analysis and history retrieval rely on external services. <br>
Risk: The skill creates or reuses a local identity and stores account tokens locally. <br>
Mitigation: Review local token storage and account handling before deployment, and prefer a release that clearly documents identity creation, token retention, and user consent. <br>
Risk: Incorrect incubation classifications could affect husbandry decisions. <br>
Mitigation: Treat visual classifications as decision support and require users to combine reports with species guidance, temperature and humidity logs, and professional reptile breeding judgment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-egg-incubation-monitoring-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON-like structured report text with optional report links and Markdown tables for history queries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include incubation stage classifications, alert levels, recommended actions, disclaimers, and report export links.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
