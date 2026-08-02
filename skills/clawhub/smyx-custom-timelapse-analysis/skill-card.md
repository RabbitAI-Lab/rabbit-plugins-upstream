## Description: <br>
Generates condensed album highlights based on specified keywords or targets, extracting specific target segments from long videos and compiling them into a summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to condense long videos into highlights matching supplied people, pets, scenes, events, or keywords, and to list prior cloud reports for the resolved identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Videos, URLs, identifiers, and analysis metadata may be sent to configured lifeemergence.com services. <br>
Mitigation: Use only media approved for external processing, review the configured service endpoint before execution, and avoid sending sensitive personal footage unless the data handling is acceptable. <br>
Risk: The skill can automatically create or reuse a local/cloud account identity and store authentication tokens locally. <br>
Mitigation: Run the skill in an isolated workspace, protect or remove the local SQLite data after use, and avoid shared machines for sensitive workflows. <br>
Risk: History queries can retrieve prior cloud reports associated with the resolved identity. <br>
Mitigation: Confirm the active identity and user authorization before listing or exporting historical reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-custom-timelapse-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown or JSON analysis report, with optional report links and optional file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [History queries can return Markdown tables of cloud reports; --output can write report content to a local file.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
