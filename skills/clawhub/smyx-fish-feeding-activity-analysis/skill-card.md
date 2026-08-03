## Description: <br>
Analyzes fish feeding videos from smart feeder or aquarium cameras to estimate gathering behavior, feeding intensity, remaining feed, and a 0-100 feeding activity score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, aquarium operators, aquaculture teams, and smart feeder integrators can use this skill to submit post-feeding media for fish feeding activity reports, appetite-decline alerts, and history lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may submit media URLs or uploaded media to a cloud-backed analyzer. <br>
Mitigation: Use it only with aquarium, farm, or facility videos that are approved for external processing. <br>
Risk: The skill silently creates or reuses a backend identity and stores authentication tokens locally for report access. <br>
Mitigation: Review workspace data handling and token storage policies before deployment, especially in shared or regulated environments. <br>
Risk: Feeding scores and alerts can be misleading when video quality, timing, water clarity, or species baseline is unsuitable. <br>
Mitigation: Require clear post-feeding footage, species-specific baselines, and human review before acting on abnormal feeding alerts. <br>
Risk: Fish health recommendations could be mistaken for diagnosis or treatment advice. <br>
Mitigation: Keep outputs limited to visual activity assessment and non-drug recommendations, and refer serious or repeated abnormalities to qualified fish health professionals. <br>


## Reference(s): <br>
- [Fish feeding activity API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON reports with feeding activity scores, key metrics, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write the report to a user-specified output file and can list cloud-backed historical reports.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
