## Description: <br>
Estimates an indoor plant transpiration rate index from thermal or RGB leaf imagery with optional environmental data, then returns a structured plant stress and root water-uptake assessment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, plant-care operators, greenhouse teams, and smart-planter workflows use this skill to analyze leaf imagery and produce transpiration-rate, root water-uptake, stress, and care-guidance outputs for indoor plants. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-backed analysis sends media, URLs, identity data, and report-history requests to lifeemergence.com services. <br>
Mitigation: Use only with data appropriate for third-party cloud processing, and avoid private files or URLs unless the publisher clarifies consent, retention, and authentication handling. <br>
Risk: The security evidence says the skill automatically creates or reuses backend identities and stores token-capable local SQLite state. <br>
Mitigation: Review local storage and identity behavior before deployment, restrict execution to trusted environments, and clear local state when account linkage should not persist. <br>
Risk: The authoritative security verdict is suspicious because user-facing disclosure around cloud processing, identity reuse, and local token storage is weak. <br>
Mitigation: Require deployment review and user disclosure before enabling the skill in workflows that handle sensitive images, URLs, or account-linked history. <br>


## Reference(s): <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON text, with optional file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured analysis results, report links, history-query output, and command examples for local script execution.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; SKILL.md frontmatter lists 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
