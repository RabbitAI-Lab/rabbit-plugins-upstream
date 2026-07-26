## Description: <br>
This skill lets agents operate NetSuite through an OOMOL-connected account by reading records, running SuiteQL queries, and creating or updating records through the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business operators use this skill to inspect, create, and update NetSuite records through an OOMOL-connected account. It supports record lookup, record listing, SuiteQL queries, and state-changing record operations with confirmation for writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create or update NetSuite records. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running create or update actions. <br>
Risk: Read actions, including record listing and SuiteQL queries, can expose sensitive business data. <br>
Mitigation: Run read actions only for the user's stated purpose and avoid broad queries when narrower record access is sufficient. <br>
Risk: The skill depends on an OOMOL-connected NetSuite account and the oo CLI. <br>
Mitigation: Install and connect the CLI only when the user intends to let the agent access that NetSuite account. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-netsuite) <br>
- [NetSuite Homepage](https://www.netsuite.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL NetSuite Connection](https://console.oomol.com/app-connections?provider=netsuite) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill retrieves live connector schemas before constructing action payloads and returns connector results as JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
