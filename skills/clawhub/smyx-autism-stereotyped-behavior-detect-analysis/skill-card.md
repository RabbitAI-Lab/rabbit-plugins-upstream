## Description: <br>
Analyzes fixed-camera child behavior videos to detect stereotyped behaviors such as spinning, hand flapping, and body rocking, then returns structured behavior statistics and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External therapists, rehabilitation centers, special education programs, and caregivers use this skill to submit child behavior videos or video URLs to a cloud analysis service for visual behavior statistics, history lookup, and report generation. Results are intended to support objective monitoring and professional review, not diagnosis or treatment decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes highly sensitive children's behavior videos or video URLs through a configured cloud service. <br>
Mitigation: Obtain explicit guardian consent, submit only necessary footage, verify the configured service endpoint and retention policy, and avoid using identifying content when a lower-risk representation is sufficient. <br>
Risk: The skill can create or reuse a local identity and store service tokens locally. <br>
Mitigation: Run it only in a controlled workspace, restrict access to local data files, and rotate or remove local identity and token records when the skill is no longer needed. <br>
Risk: Cloud-stored history reports may expose sensitive child behavior records if accessed by unauthorized users. <br>
Mitigation: Limit history-report access to authorized users, confirm cloud access controls before deployment, and avoid sharing generated report links outside the care or review workflow. <br>
Risk: Behavior detection outputs may be mistaken for clinical diagnosis, assessment scores, or treatment recommendations. <br>
Mitigation: Use outputs only as descriptive monitoring support and require review by qualified clinicians or rehabilitation professionals for diagnosis, assessment, or intervention decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-autism-stereotyped-behavior-detect-analysis) <br>
- [Autism Stereotyped Behavior Detection API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON or Markdown report text with structured behavior metrics and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save output to a file when --output is supplied; history queries return cloud-stored report lists.] <br>

## Skill Version(s): <br>
1.0.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
