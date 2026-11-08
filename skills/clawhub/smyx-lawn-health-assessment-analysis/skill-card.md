## Description:

Assesses lawn health from overhead images or video by estimating yellowing, weed and bare-soil coverage, then producing a composite health score and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Homeowners, groundskeepers, and golf-course or municipal green-space managers can use overhead lawn images or video to estimate yellowing, weed coverage, bare soil, and overall turf condition. The results can inform irrigation, fertilization, weeding, or reseeding decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags account and credential handling and remote media processing as broader than the lawn assessment purpose.

Mitigation: Review account and credential permissions and remote media handling before use; submit only media appropriate for the service.

Risk: The security review notes that analysis may run when a no-analysis option is selected.

Mitigation: Check the requested operation and confirm the expected behavior before running the skill.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-lawn-health-assessment-analysis)

## Skill Output:

**Output Type(s):** [text, JSON, Markdown, guidance]

**Output Format:** [Structured JSON analysis results, text summaries, and Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
