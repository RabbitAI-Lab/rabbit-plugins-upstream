## Description: <br>
Analyzes cat litter box image or video inputs through LifeEmergence/Smyx cloud APIs to produce structured observations about feces morphology, urine clump size, and health-risk alerts without disease diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit cat litter box videos or URLs for waste characteristic analysis, smart litter box monitoring, and multi-cat household health trend review. It returns observations and risk prompts rather than veterinary diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Litter-box videos or video URLs are sent to LifeEmergence/Smyx cloud services for analysis. <br>
Mitigation: Install only when users accept that cloud transfer; avoid submitting sensitive media and confirm service terms before production use. <br>
Risk: The skill can silently create or reuse an internal identity and use it for report retrieval. <br>
Mitigation: Require explicit user or workspace approval for identity creation and history lookup before enabling the skill. <br>
Risk: Tokens may be stored in a workspace SQLite database for later API calls. <br>
Mitigation: Limit workspace access, rotate credentials if exposed, and prefer an updated release with explicit token storage and deletion controls. <br>


## Reference(s): <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-litter-box-waste-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis reports with optional saved text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured observations, risk prompts, suggestions, report links, and historical report lists from cloud APIs.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
