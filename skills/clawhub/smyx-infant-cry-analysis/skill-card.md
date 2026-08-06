## Description: <br>
Detects baby cries via audio AI in real time, analyzes likely causes, and identifies needs such as hunger, tiredness, pain, discomfort, or irritability to assist new parents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit baby cry audio or video for cloud analysis, receive a structured report, and retrieve account-linked historical reports. The analysis is for parenting support and should not replace medical evaluation when a baby has persistent distress. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Baby cry recordings, videos, or URLs may include a baby, family members, or the home and are processed by LifeEmergence cloud endpoints. <br>
Mitigation: Use only recordings approved for cloud processing, disclose that media leaves the local environment, and avoid uploading clips with unnecessary household or family content. <br>
Risk: The skill retrieves account-linked history and creates or reuses local identity records with token storage. <br>
Mitigation: Run the skill with an isolated account when possible, restrict access to the local data directory, and clear stored identity and token data when no longer needed. <br>
Risk: History retrieval can expose prior report metadata and report links for the current identity. <br>
Mitigation: Confirm user intent before listing historical reports and avoid sharing report links outside the intended user context. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-cry-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands] <br>
**Output Format:** [Markdown text containing structured JSON analysis results, status messages, report links, or a Markdown-formatted history listing.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save the returned report text to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter says 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
