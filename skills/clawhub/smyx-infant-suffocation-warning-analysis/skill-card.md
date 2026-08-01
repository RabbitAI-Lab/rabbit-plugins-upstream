## Description: <br>
Identifies prone sleeping positions, head covering, and occlusion of the mouth/nose by bedding or clothing; provides real-time high-risk alerts to safeguard infant sleep safety. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, monitoring integrators, and agents use this skill to analyze infant sleep videos or video URLs for prone sleeping, head covering, and mouth or nose occlusion risk. It returns structured findings, safety guidance, report links, and optional history listings for prior cloud reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Infant sleep videos or video URLs are sent to a configured cloud service for analysis. <br>
Mitigation: Use only with explicit consent for cloud processing and confirm the service endpoint, retention policy, and access controls before deployment. <br>
Risk: The skill can silently create or reuse a local identity and link reports to it. <br>
Mitigation: Require an explicit account or consent flow and document how report identity association works. <br>
Risk: Account tokens and identity data may be persisted locally. <br>
Mitigation: Provide a way to disable or clear local token and history persistence, and restrict local file access to trusted users. <br>
Risk: History and report access are available without clear user control. <br>
Mitigation: Gate history queries behind user intent, authorization checks, and clear controls for viewing or deleting past reports. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-infant-suffocation-warning-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [JSON or Markdown reports with risk findings, safety suggestions, report links, and command-line status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local video files or video URLs, sensitivity levels 1-5, basic/standard/json detail modes, optional file output, and history listing.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
