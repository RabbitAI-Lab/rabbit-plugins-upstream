## Description: <br>
Search and read UK Energy Performance Certificate data through OOMOL's energy_performance_certificates connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve full certificate details by certificate number and search domestic, non-domestic, or display Energy Performance Certificates through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries may include property-related identifiers or filters sent to the OOMOL connector. <br>
Mitigation: Use the skill only for intended certificate lookups and searches, and confirm sensitive query details with the user before execution. <br>
Risk: First-time setup may require installing or authenticating the oo CLI. <br>
Mitigation: Verify the oo CLI install source and run setup or authentication only after a command fails for that reason. <br>


## Reference(s): <br>
- [Energy Performance Certificates homepage](https://get-energy-performance-data.communities.gov.uk) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only certificate lookup and search actions; connector responses include data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
