## Description: <br>
Analyzes pet image or video inputs for cats, dogs, and birds through a remote health analysis service and returns a structured Pet Safety Guardian health report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit pet media or media URLs for health screening, feature-based issue detection, care suggestions, report links, and historical report retrieval. Results are health references and should not replace a veterinarian's diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet media is sent to lifeemergence.com services for analysis. <br>
Mitigation: Use only with media the user is permitted to share with that service, and avoid submitting sensitive or unnecessary background content. <br>
Risk: The skill silently creates or reuses a local identity and stores service tokens in a workspace SQLite database. <br>
Mitigation: Install only in workspaces where local identity and token storage are acceptable; avoid shared workspaces unless user identity, token files, and database access are isolated. <br>
Risk: Historical report retrieval may expose reports associated with the reused local identity. <br>
Mitigation: Before enabling history queries, confirm that the workspace identity maps to the intended user and that report access boundaries are clear. <br>
Risk: Pet health analysis output may be incomplete or misleading if treated as a medical diagnosis. <br>
Mitigation: Present results as health reference material and direct users to professional veterinary care for diagnosis or urgent concerns. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-formatted analysis reports, report links, historical report tables, and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write analysis output to a user-selected file path when the --output option is used.] <br>

## Skill Version(s): <br>
999.999.1002 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
