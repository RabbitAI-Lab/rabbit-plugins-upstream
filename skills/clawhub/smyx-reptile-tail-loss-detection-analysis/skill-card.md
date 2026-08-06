## Description: <br>
Detects possible tail-loss events in gecko or lizard images or videos by comparing tail length against historical or body-length baselines and flagging wounds, scabs, or abnormal shortening. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External reptile keepers, breeders, and smart-vivarium operators use this skill to analyze gecko or lizard tail media for possible autotomy events, image-quality issues, and history reports. The skill is intended to support monitoring workflows and does not replace professional veterinary review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says the skill uploads reptile enclosure images or videos and related account metadata to configured LifeEmergence services. <br>
Mitigation: Use only with media the user is comfortable sending to those services, and avoid sensitive household footage unless the publisher provides clear consent, retention, and deletion controls. <br>
Risk: The security review says the skill automatically creates or reuses identity and stores tokens in a local workspace database. <br>
Mitigation: Review the local workspace data location and remove stored identity or token data when the skill is no longer needed. <br>
Risk: The security review says the skill relies on cloud history retrieval for report lists. <br>
Mitigation: Treat history output as dependent on the configured cloud service and verify important records before making operational decisions. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, json, shell commands] <br>
**Output Format:** [Markdown or JSON structured analysis report with optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tail-length estimates, shortening ratio, wound or scab indicators, alert level, recommended actions, disclaimers, and cloud history results.] <br>

## Skill Version(s): <br>
1.0.7 (source: ClawHub release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
