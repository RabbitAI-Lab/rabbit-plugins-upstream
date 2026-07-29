## Description: <br>
DNS查询免费版 helps agents run dig-based DNS lookups for common record types, reverse DNS checks, and resolver comparisons, then summarize the results for operators and developers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and support engineers use this skill to investigate DNS resolution issues, validate DNS changes, inspect mail and name-server records, and compare resolver responses with dig commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DNS queries can disclose internal hostnames or investigation targets to public DNS resolvers. <br>
Mitigation: Use approved internal resolvers for sensitive names and query public resolvers only when that disclosure is acceptable. <br>
Risk: The free edition's JSON and structured-output claims may not match actual command behavior. <br>
Mitigation: Treat structured-output examples as illustrative and verify dig output before automating downstream decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dns-lookup-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and DNS result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires dig and network access to the selected DNS resolver; free edition behavior should be verified before relying on structured-output examples.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
