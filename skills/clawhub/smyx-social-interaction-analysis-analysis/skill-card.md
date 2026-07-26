## Description: <br>
Analyzes multi-pet images or videos to identify social interactions, classify behaviors such as sniffing, chasing, biting, fleeing, hiding, and play, and produce a structured behavior report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, boarding centers, daycare operators, and behavior clinics use this skill to analyze multi-pet media for interaction patterns, potential conflict, and social-behavior reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet or home-camera media and generated report history may be processed by lifeemergence.com cloud services. <br>
Mitigation: Use only with media the user is authorized to share, avoid sensitive scenes, and confirm organizational approval for cloud processing before installation. <br>
Risk: The skill can silently create or reuse a local identity, authenticate remotely, store returned tokens locally, and fetch report history tied to that identity. <br>
Mitigation: Review local identity and token storage before deployment, restrict runtime access to trusted environments, and clear stored credentials when the skill is no longer needed. <br>
Risk: Behavior classifications such as play, aggression, stress, or conflict are observational and can be uncertain from visual media alone. <br>
Mitigation: Treat outputs as behavior observations rather than medical or training advice, and route serious conflict or welfare concerns to a qualified professional. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-social-interaction-analysis-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Pet social interaction API documentation](artifact/references/api_doc.md) <br>
- [Common analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown text with structured JSON report content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save output to a file when requested; history reports are fetched from the cloud service.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
