## Description: <br>
Analyzes pet activity media to detect over-excitement behaviors, score excitement level, and return structured calming guidance with report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, boarding centers, daycare operators, and training schools use this skill to analyze pet activity media for over-excitement behaviors and receive structured calming recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet or household videos and remote video URLs may be sent to external services for analysis. <br>
Mitigation: Use only media appropriate for cloud processing, and avoid videos that include people, children, private interiors, or sensitive routines unless the service's privacy and retention practices are acceptable. <br>
Risk: The skill can create or reuse a local identity and cache tokens for report history. <br>
Mitigation: Review local workspace data handling before installing, and clear cached identity or token data when using shared environments. <br>
Risk: Calming guidance may be mistaken for veterinary or medical advice. <br>
Mitigation: Treat outputs as behavior-safety guidance only, and consult a veterinarian or qualified behavior trainer for persistent, severe, or injury-related behavior concerns. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-excitement-calming-guide-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown and JSON text, with optional local output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include remote report links and historical report lists; media inputs can be local files or URLs.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter declares 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
