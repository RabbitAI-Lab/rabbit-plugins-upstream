## Description: <br>
Predicts flowering dates for ornamental and cut-flower plants from bud images or videos, optional temperature and light data, and a pre-trained phenology model, producing a structured report for planning pollination, harvesting, or visitor timing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Growers, greenhouse operators, botanical garden teams, and agricultural developers use this skill to estimate full-bloom timing from flower-bud media and optional environmental context. The output supports production scheduling, harvest planning, pollination timing, and flower tourism planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review marks the release as suspicious because it sends media or URLs to a remote service. <br>
Mitigation: Review the publisher, service endpoint, and data-handling expectations before installing or using the skill with sensitive media. <br>
Risk: The security review notes that the skill silently creates or reuses a local identity and can store authentication tokens in a workspace SQLite database. <br>
Mitigation: Run the skill in a controlled workspace, inspect local storage policies, and avoid using shared or persistent workspaces unless token storage is acceptable. <br>
Risk: The security review notes mismatched pet-health and generic-analysis artifacts in the package. <br>
Mitigation: Confirm the backend behavior, report access, and publisher expectations before relying on the flower analysis output. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-flowering-date-prediction-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON or text analysis results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return structured reports, history report tables, report links, and optional saved output files.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
