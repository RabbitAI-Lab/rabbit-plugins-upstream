## Description: <br>
Resolve hostnames to IP addresses using `dig` from bind-utils. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to have an agent propose DNS lookup commands for A, AAAA, ANY, and reverse lookups with `dig`. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DNS lookups for sensitive internal hostnames can expose those names to the configured resolver and network path. <br>
Mitigation: Avoid querying sensitive internal hostnames unless the resolver, network path, and disclosure implications are approved for that environment. <br>
Risk: The skill depends on the external `dig` command and may fail or produce no useful command path when bind-utils is unavailable. <br>
Mitigation: Install bind-utils from trusted system repositories before relying on the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xejrax/skills/dns-lookup) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the `dig` binary from bind-utils.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
