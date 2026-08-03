## Description: <br>
Analyzes fixed-camera aquarium video to detect fish flashing or scraping behavior, count abnormal friction events, and produce ectoparasite-risk warnings with observation-focused recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External aquarium keepers, public-aquarium staff, aquaculture operators, and developers use this skill to analyze fish-tank or pond video for abnormal rubbing behavior and generate structured early-warning reports. The skill supports review workflows for possible ectoparasite risk, but it does not diagnose a specific parasite or prescribe treatment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aquarium videos or URLs are processed by the lifeemergence.com service. <br>
Mitigation: Use only with videos the user is authorized to submit, and avoid sensitive or private footage unless cloud processing is acceptable. <br>
Risk: The skill silently creates or reuses an identity and may store auth tokens or report-history data locally. <br>
Mitigation: Review the local data directory for smyx-api-key.txt and smyx-common-claw.db, and avoid shared workspaces unless identity and report-history access are acceptable. <br>
Risk: Fish flashing and scraping can be caused by species baseline behavior, breeding, water changes, stress, or unreliable video quality. <br>
Mitigation: Require adequate video quality and species context, treat outputs as behavior-based warnings, and route diagnosis or treatment decisions to qualified aquatic veterinary review. <br>


## Reference(s): <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown tables or JSON analysis reports with alert levels, friction-event metrics, recommended observation actions, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should remain limited to behavior-based risk warnings and observation guidance; they should not include parasite diagnosis, medication names, dosages, or automated aquarium-device control.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
