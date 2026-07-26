## Description: <br>
Analyzes indoor pet camera video from local files or URLs to detect sustained mouth contact with hazardous non-food items such as electric wires, plastic bags, socks, tissues, and toy fragments, then returns warning-oriented safety results without diagnosing disease. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze indoor pet monitoring video for possible pica behavior and receive structured safety warnings, risk levels, intervention suggestions, and report links. It also supports querying historical reports associated with the skill-managed identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Indoor camera media or video URLs are sent to the publisher's cloud service for analysis. <br>
Mitigation: Use only with appropriate authorization, avoid submitting sensitive footage when possible, and confirm cloud data-handling expectations before deployment. <br>
Risk: The skill may silently create or reuse a persistent local identity and query historical reports linked to that identity. <br>
Mitigation: Run it in controlled workspaces, restrict access to local identity and token storage, and review report access against the deployment's privacy policy. <br>
Risk: The security evidence flags the release as suspicious because it sends media and report data to external APIs while managing persistent identities and tokens. <br>
Mitigation: Review before installing, validate the publisher and endpoints, and deploy only where these data flows are acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](artifact/references/api_doc.md) <br>
- [Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis or report-list output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include warning signals, risk levels, intervention suggestions, historical report tables, and report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter and changelog list 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
