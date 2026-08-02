## Description: <br>
Analyzes pet food-bowl videos or video URLs through server-side APIs to estimate eating duration and speed, report fast-eating risk, and provide slow-feed intervention guidance without diagnosing disease. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, pet-care operators, and developers use this skill to analyze pet feeding-area videos for eating start and end times, speed estimates, fast-eating risk, and slow-feed intervention guidance for smart feeders or pet health management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet or home videos may be uploaded or submitted by URL to a cloud analysis service. <br>
Mitigation: Install and run the skill only when users and workspace owners accept cloud processing of the video content. <br>
Risk: The skill can create or reuse a backend identity and persist identity-linked tokens locally. <br>
Mitigation: Use it only in workspaces where account linkage and local token storage are acceptable, and review or clear local stored credentials as needed. <br>
Risk: History-report keywords can trigger cloud history queries tied to the resolved backend identity. <br>
Mitigation: Use the history feature only where querying identity-linked cloud report history is expected and authorized. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-eating-speed-slow-feed-analysis) <br>
- [Pet Eating Speed API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown text with structured JSON content and optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include cloud report links and slow-feed intervention guidance; the --output option can write the result to a local file.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
