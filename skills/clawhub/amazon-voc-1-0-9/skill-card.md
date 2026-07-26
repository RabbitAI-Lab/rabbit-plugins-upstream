## Description: <br>
Collects and analyzes Amazon buyer reviews to generate VOC reports covering pain points, purchase drivers, personas, usage scenarios, competitor comparisons, trends, and Listing optimization suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[funewa](https://clawhub.ai/user/funewa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to collect Amazon review data through ARI and produce buyer voice reports after confirming any paid collection or analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An untrusted ARI_BASE_URL or ARI_WEB_URL override could send the ARI key and review-analysis data to an unintended server. <br>
Mitigation: Use the skill only in a trusted shell or agent environment, leave those variables unset unless intentionally using a trusted ARI development server, and revoke the ARI key if unexpected overrides may have been present. <br>
Risk: Paid collection or analysis can spend ARI credits, and interrupted paid commands may already have been charged. <br>
Mitigation: Run paid workflows first without --confirm to show pricing, add --confirm only after explicit user approval, and check existing reports before retrying interrupted paid commands. <br>
Risk: The skill stores or reads a local ARI API key for authenticated requests. <br>
Mitigation: Do not include the key in reports, screenshots, or command examples; recreate or revoke the key if it may have been exposed. <br>


## Reference(s): <br>
- [ARI CLI and API Reference](references/reference.md) <br>
- [ARI Amazon Review Assistant User Guide](使用说明.md) <br>
- [ClawHub Skill Release](https://clawhub.ai/funewa/skills/amazon-voc-1-0-9) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and guidance with inline shell commands; CLI responses may be JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid collection or analysis commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact _meta.json reports package version 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
