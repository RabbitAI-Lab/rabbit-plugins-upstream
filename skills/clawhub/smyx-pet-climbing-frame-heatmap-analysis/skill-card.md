## Description: <br>
Analyzes cat climbing frame or cat tree videos from local files or URLs to summarize dwell time by region, jump or transition counts, activity density, and a 2D activity heatmap without providing disease diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet care teams, developers, and external users can use this skill to process cat tree area videos and generate structured activity observations for enrichment and behavior monitoring. The skill is for activity distribution and exercise trend review, not veterinary diagnosis or treatment guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos or video URLs are sent to a configured cloud service for analysis. <br>
Mitigation: Use non-sensitive videos, confirm the cloud endpoint is acceptable for the deployment, and avoid submitting media that includes private locations, people, or unrelated personal data. <br>
Risk: The skill can silently create or reuse an identity, attach tokens to requests, and persist account state in the workspace data directory. <br>
Mitigation: Run in a separate workspace when possible, review persisted identity files after use, and remove data/smyx-api-key.txt or the local smyx-common-claw.db when persistent account state is not desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-climbing-frame-heatmap-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report text with JSON-style structured analysis fields and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query historical cloud reports and may write an optional output file when requested.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
