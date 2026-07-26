## Description: <br>
Extracts important family-related information from recent phone notifications, groups it by family member, and marks items by importance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vivalavida-say-hi](https://clawhub.ai/user/vivalavida-say-hi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ClawHub users use this skill to summarize family messages from notification data by spouse, parents, children, teachers, and other family contacts. It highlights action-needed items, informational notices, sources, deadlines, and person-specific summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill analyzes sensitive family notification contents, including private communications from spouses, parents, teachers, and schools. <br>
Mitigation: Install and invoke it only when that notification data should be analyzed in the current session, and avoid using it on unrelated or shared notification archives. <br>
Risk: Broad trigger phrases such as "important information" or "today's notice" may not clearly express consent to analyze private family messages. <br>
Mitigation: Use explicit family-summary requests and, when possible, specify the person or date range to limit the data reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vivalavida-say-hi/skills/yoooclaw-family-digest-en) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown family digest grouped by person with action markers, sources, and deadlines.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces session text only; no files are written by the skill.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
