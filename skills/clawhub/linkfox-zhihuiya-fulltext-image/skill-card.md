## Description: <br>
Retrieves full-text patent images, drawings, diagrams, and related metadata from Zhihuiya by patent ID or publication number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patent analysts, IP researchers, and agents use this skill to retrieve and review full-text patent drawings and figure metadata for a known patent publication number or patent ID. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LinkFox API calls consume credits for patent-image lookups. <br>
Mitigation: Confirm cost expectations before repeated queries, use pagination deliberately, and avoid automatic retries or exploratory parameter changes. <br>
Risk: Full API responses are saved locally by default and may retain patent response data and session metadata. <br>
Mitigation: Use the skill only in workspaces where local response storage is acceptable, and review or remove saved response files before sharing a project. <br>
Risk: Authentication or quota handling may prompt installation of a remote onboarding skill. <br>
Mitigation: Review the remote onboarding source and obtain explicit user approval before downloading or installing it. <br>
Risk: Feedback may be reported to LinkFox automatically based on the user interaction. <br>
Mitigation: Avoid including sensitive user content in feedback and review this behavior before use in restricted environments. <br>


## Reference(s): <br>
- [Zhihuiya Fulltext Image API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-fulltext-image) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown summaries and tables, JSON API responses, and saved local response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires either patentId or patentNumber; each request returns at most 100 images and may consume LinkFox credits.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
