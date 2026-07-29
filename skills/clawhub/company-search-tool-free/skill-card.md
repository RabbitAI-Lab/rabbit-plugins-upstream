## Description: <br>
A free company lookup skill that helps agents query company basic information, legal representatives, shareholders, key personnel, outside investments, and registration changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and business analysts use this skill to look up company records for lightweight background checks, partner review, and investment context. It is intended for single-company queries rather than due-diligence reports, batch lookup, monitoring, or advanced risk screening. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan flags this skill as suspicious because it combines broad activation, generic command execution, external callbacks, and company or person-linked data lookup. <br>
Mitigation: Install only when those behaviors are intended, review commands before execution, use trusted callback URLs only, and prefer a version with tighter tool allowlists and schema validation. <br>
Risk: Company and person-linked query results may contain sensitive business data. <br>
Mitigation: Confirm the exact company or person before lookup and handle returned data according to applicable privacy, confidentiality, and business-use requirements. <br>


## Reference(s): <br>
- [Detailed reference](references/detail.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell and Python examples, plus JSON or text query results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include company and person-linked business data; some workflows accept optional callback URLs.] <br>

## Skill Version(s): <br>
1.0.2 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
