## Description: <br>
Assesses frog skin moisture from clear images or videos by analyzing glossiness, wrinkles, white film, species humidity context, and image quality to produce structured alerts and care recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External keepers, amphibian farms, animal hospitals, and developers integrating vivarium cameras use this skill to analyze frog skin media for moisture status, dehydration risk alerts, and historical report lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends frog images, videos, URLs, identity values, and report-history requests to configured lifeemergence.com services. <br>
Mitigation: Review before installing, prefer non-sensitive media, and confirm cloud retention, account deletion, and token revocation practices before use. <br>
Risk: The skill persists service tokens in the workspace data directory. <br>
Mitigation: Use only in trusted workspaces, protect workspace storage, and revoke or rotate tokens if the workspace is shared or compromised. <br>
Risk: The security verdict is suspicious because the skill automatically handles identity, uploads media or URLs, queries cloud history, and lacks sufficient user control or disclosure. <br>
Mitigation: Require user review of cloud-backed behavior and disclosures before deployment, and avoid using sensitive animal hospital or farm media unless approved. <br>


## Reference(s): <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-frog-skin-moisture-assessment-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown and JSON-backed structured reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and historical report tables; input media can be local files or URLs.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter says 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
