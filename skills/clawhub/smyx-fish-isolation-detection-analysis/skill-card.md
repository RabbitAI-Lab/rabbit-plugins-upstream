## Description: <br>
Analyzes aquarium media to detect fish schooling patterns, persistent isolation from the school centroid, unreliable tracking conditions, and suggested observation or escalation actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Aquarium keepers, aquaculture teams, and developers can use this skill to analyze fixed-camera fish footage or URLs for prolonged isolation behavior, schooling quality, alert severity, and non-diagnostic recommended follow-up actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aquarium media or video URLs may be processed by the Life Emergence cloud service. <br>
Mitigation: Use only media the user is comfortable sending to that service, and restrict network access or avoid private camera footage where policy requires local processing. <br>
Risk: The skill may create or reuse a persistent account-linked identity and store tokens for history queries. <br>
Mitigation: Review token storage and account-linking behavior before deployment, and clear or isolate workspace data for shared or sensitive environments. <br>
Risk: Behavior alerts could be mistaken for veterinary diagnosis or treatment guidance. <br>
Mitigation: Present results as behavioral signals only, avoid medication names or dosing, and direct users to a qualified aquarium veterinarian or aquaculture specialist for diagnosis and treatment. <br>
Risk: Poor ReID tracking, occlusion, unclear water, or incomplete tank coverage can make isolation signals unreliable. <br>
Mitigation: Require clear fixed-camera footage, whole-tank coverage, and a stable tracking rate; return an unreliable-signal result instead of an alert when tracking quality is insufficient. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-isolation-detection-analysis) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with report links and optional history-list output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include isolation classifications, alert levels, tracked-fish metrics, recommended actions, and report export links.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
