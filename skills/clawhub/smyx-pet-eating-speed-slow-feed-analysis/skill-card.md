## Description: <br>
Analyzes pet food-bowl videos or video URLs to estimate eating start and end times, eating speed, and non-diagnostic slow-feeding intervention guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze pet feeding videos, estimate feeding duration and speed, and generate slow-feeding recommendations, structured reports, or report links. The skill is intended for pet behavior and health-management support, not disease diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet feeding videos or URLs are processed by external LifeEmergence services. <br>
Mitigation: Use non-sensitive videos, confirm permission to submit the media, and avoid uploading household footage that should not leave the user's environment. <br>
Risk: The skill may silently create or reuse an internal identity and store authentication tokens in a workspace SQLite database. <br>
Mitigation: Review or clear workspace data files and stored credentials when identity reuse across runs is not desired. <br>
Risk: Cloud history lookup can return reports associated with the internally resolved identity. <br>
Mitigation: Run history queries only for authorized users and review report links before sharing results. <br>


## Reference(s): <br>
- [Pet Eating Speed API Documentation](artifact/references/api_doc.md) <br>
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-eating-speed-slow-feed-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON-style structured analysis report with command-line invocation examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include eating timestamps, eating-speed estimates, risk labels, intervention suggestions, historical report summaries, and report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
