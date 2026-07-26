## Description: <br>
Book Painter helps users find and book local painter services through the Lokuli protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can use this skill to collect booking details and request local painter services through Lokuli. It is intended for booking assistance, not high-assurance decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is loosely documented and may send user-provided booking details to an unspecified external service. <br>
Mitigation: Review what booking data will be shared, confirm the service endpoint and privacy expectations, and avoid sending sensitive details until the endpoint is known. <br>
Risk: The skill declares execution access and has broad, inconsistent instructions outside the core painter-booking task. <br>
Mitigation: Limit use to painter booking, review proposed commands before execution, and prefer a version with narrower activation conditions and unrelated LLM claims removed. <br>


## Reference(s): <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with JSON-shaped service results and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May assemble API request details and parse external service responses for user-readable booking output.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
