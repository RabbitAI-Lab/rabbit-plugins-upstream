## Description: <br>
Analyzes aquarium camera media to estimate fish respiratory rate from gill-cover motion and produce structured hypoxia alerts, monitoring results, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and aquarium operators use this skill to analyze fixed-camera aquarium videos or URLs for gill-cover movement, respiratory-rate BPM, abnormal breathing states, and hypoxia-oriented care suggestions. It is intended for home aquariums, public aquariums, ornamental fish farms, and laboratory monitoring workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends aquarium media or video URLs to the configured lifeemergence.com cloud service and can query cloud-hosted history. <br>
Mitigation: Use only media appropriate for cloud processing, avoid sensitive footage, and ask the publisher for retention, deletion, and access-control details before deployment. <br>
Risk: Reports are linked to an automatically resolved local identity, and service tokens may be stored in the local workspace database. <br>
Mitigation: Review local workspace storage before installation, restrict workspace access, and confirm token revocation and deletion procedures with the publisher. <br>
Risk: Fish respiratory alerts and recommendations could be mistaken for veterinary diagnosis or automatic device-control authority. <br>
Mitigation: Treat outputs as visual monitoring guidance only, require user confirmation for aquarium equipment changes, and consult qualified aquarium or veterinary professionals for serious conditions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-respiratory-rate-monitor-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-oriented structured analysis reports with optional shell command usage examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include BPM estimates, signal stability, alert level, recommended actions, report links, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
