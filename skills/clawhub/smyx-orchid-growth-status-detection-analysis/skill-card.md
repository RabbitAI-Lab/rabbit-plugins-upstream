## Description: <br>
Analyzes orchid images or videos to estimate new-shoot count, flower-spike growth, root color and condition, overall vitality, and care-oriented observations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Orchid hobbyists, greenhouse operators, and horticulture studios use this skill to review orchid media for visible growth status, including shoots, flower spikes, and roots visible through transparent pots. It can also return or list structured cloud-backed analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted orchid media and URLs are processed by the publisher's cloud service. <br>
Mitigation: Use non-sensitive media unless the publisher clarifies retention, access, and handling of private or signed URLs. <br>
Risk: The skill can create or reuse a persistent local identity and store auth tokens in a workspace SQLite database. <br>
Mitigation: Avoid shared workspaces, keep per-user workspace separation, and remove local tokens or databases after use when required by policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-orchid-growth-status-detection-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown summaries and JSON-backed structured analysis reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and historical report listings returned by the provider's cloud service.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
