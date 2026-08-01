## Description: <br>
AI-powered orchid growth-status detection from HD images, including roots visible through transparent pots, that measures new-shoot count, flower-spike length, root color and condition, overall vitality, and care guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External orchid hobbyists, greenhouse operators, horticulture studios, and agent users use this skill to analyze orchid images or videos for shoots, flower spikes, root condition, growth vitality, history reports, and care guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Orchid images, videos, or supplied media URLs are sent to lifeemergence.com analysis services. <br>
Mitigation: Use only with media intended for that third-party service, avoid sensitive or private content, and review endpoint configuration before deployment. <br>
Risk: The skill can create or reuse a local user identity, store tokens, and associate report history with cloud services. <br>
Mitigation: Run in a workspace where persistent local identity storage is expected, review data/smyx-api-key.txt and the workspace data directory, and avoid shared workspaces unless that behavior is approved. <br>
Risk: Cloud report history and exported report links may expose analysis records beyond the local agent session. <br>
Mitigation: Confirm users understand that history lookups come from the cloud service and restrict use to approved accounts or environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-orchid-growth-status-detection-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report text with structured JSON-like analysis content, command examples, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include orchid growth assessments, root and spike status, history report listings, and cloud report export links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
