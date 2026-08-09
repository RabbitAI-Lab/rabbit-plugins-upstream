## Description: <br>
Predicts expected yield of economic crops such as tomato, corn and potato by combining growth stage, nutrition status, environmental data and historical yield references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agricultural operations teams use this skill to analyze crop plant or field images, videos, or URLs and receive yield estimates, confidence signals, influencing factors, and report links for harvest planning, market matching, supply-chain planning, and agricultural insurance review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crop images, videos, URLs, environmental details, and historical-yield context may be processed by the Life Emergence remote service. <br>
Mitigation: Use only media and context suitable for third-party processing, and review provider data handling before submitting private farm, insurance, or business-sensitive material. <br>
Risk: The skill can create or reuse an internal identity, register it remotely, and store authentication tokens in the workspace data directory. <br>
Mitigation: Run it only in trusted workspaces, restrict access to the workspace data directory, and remove stored identity or token data when it is no longer needed. <br>
Risk: Yield estimates are advisory and may be inaccurate because single images or short videos capture only partial field conditions. <br>
Mitigation: Treat outputs as planning support and verify final yield, insurance, or business decisions with field measurements and applicable business rules. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crop-yield-prediction-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Crop yield prediction API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown report text with structured JSON content and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return crop-yield ranges, confidence, influencing factors, historical report lists, and report export links.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; SKILL.md frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
