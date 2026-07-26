## Description: <br>
Analyzes infant diaper or stool images or URLs to classify stool color, flag clay-pale or bloody appearances, and return visual screening guidance without making a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and care workflows can use this skill to submit infant diaper or stool images for visual color screening and receive a structured report with color class, risk level, confidence, recommended action, and report links. It is for visual screening support only and does not replace pediatric or surgical medical evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Infant-related images or URLs may be sent to external cloud services. <br>
Mitigation: Use the skill only when external processing is acceptable and guardian consent has been obtained for the media being processed. <br>
Risk: The skill may create or reuse a persistent local identity and store authentication tokens in a workspace SQLite database. <br>
Mitigation: Review local identity and token storage before deployment, restrict workspace access, and clear stored credentials when they are no longer needed. <br>
Risk: The skill can retrieve cloud history automatically with limited user-facing control. <br>
Mitigation: Disclose the history retrieval behavior to users and verify that account or identity boundaries are appropriate before enabling history queries. <br>
Risk: Image quality, lighting, filters, or color cast can lead to misleading visual screening results. <br>
Mitigation: Require clear images in natural white or cool white light, avoid filters, and direct users to seek medical evaluation for clay-pale, bloody, or otherwise concerning results. <br>


## Reference(s): <br>
- [Infant stool color API reference](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON screening report with color class, risk level, confidence, recommended action, alert text, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the report to a local output file when requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: server-resolved release metadata; SKILL.md frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
