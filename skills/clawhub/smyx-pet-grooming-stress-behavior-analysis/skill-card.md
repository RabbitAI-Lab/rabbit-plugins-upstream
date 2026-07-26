## Description: <br>
Analyzes pet grooming session videos or video URLs through server-side APIs to identify stress behaviors such as struggling, panting, and tail tucking, then returns stress grading and structured observations for grooming, veterinary, and pet-care contexts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External groomers, veterinary clinic staff, pet-care providers, and developers use this skill to submit grooming videos or URLs for stress-behavior analysis and to retrieve structured reports or historical report lists. The output is intended as behavior-observation support, not medical diagnosis or behavior-correction advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded grooming videos or supplied URLs are sent to the LifeEmergence/Open API service for analysis. <br>
Mitigation: Use the skill only when sharing that footage or URL with the service is acceptable; avoid sensitive customer footage or internal URLs unless retention, deletion, and authentication terms are clear. <br>
Risk: The skill can silently create or reuse a local identity and store service tokens in workspace data for remote history access. <br>
Mitigation: Run it in a controlled workspace, review local token storage expectations before deployment, and clear workspace data when identity persistence is not desired. <br>
Risk: Stress scoring could be mistaken for veterinary diagnosis or behavior-correction guidance. <br>
Mitigation: Present results as observational support for grooming decisions and escalate health concerns to qualified veterinary staff. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown and structured JSON-like text with report links; historical reports may be returned as Markdown tables or structured lists.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a report export link and can optionally save the returned analysis text to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence, released 2026-07-12) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
