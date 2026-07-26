## Description: <br>
Analyzes fixed-camera child behavior videos to report repetitive stereotyped behaviors such as spinning, hand flapping, and body rocking; it does not provide autism diagnosis, scale scoring, or rehabilitation prescriptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Therapists, caregivers, special-education teams, and developers use this skill to submit child behavior videos or URLs to a cloud analysis service and receive objective behavior-event counts, durations, trend summaries, and report links for professional review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Child behavior videos, report queries, and account-linked identifiers may be sent to the configured cloud service. <br>
Mitigation: Use only where guardian consent, data-retention expectations, and access controls are already established before uploading footage. <br>
Risk: The skill may create a local shared SQLite database and store service tokens in the workspace data directory. <br>
Mitigation: Run it in a controlled workspace, restrict access to local data, and remove or protect generated identity and token files after use. <br>
Risk: Computer-vision results may misclassify ordinary movements or be degraded by occlusion, multiple children, poor framing, low frame rate, or unstable lighting. <br>
Mitigation: Treat outputs as descriptive behavior statistics for review by qualified therapists or caregivers, not as diagnosis, scale scoring, or treatment prescription. <br>


## Reference(s): <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON or Markdown analysis reports from the API] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write report output files when --output is supplied; historical report listings are rendered as Markdown tables.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter says 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
