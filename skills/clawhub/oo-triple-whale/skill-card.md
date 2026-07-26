## Description: <br>
This skill lets an agent handle explicit Triple Whale requests by searching and reading data through the OOMOL Triple Whale connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and commerce operators use this skill to let an agent retrieve Triple Whale metrics, customer journey attribution data, API key metadata, and custom Data-Out SQL results through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording could cause the agent to use the Triple Whale connector for requests that only loosely mention Triple Whale. <br>
Mitigation: Use the skill when the user's Triple Whale intent is explicit, and ask for clarification before accessing connector-backed account data. <br>
Risk: Connector access can expose store metrics, attribution exports, SQL query results, or API key metadata from connected Triple Whale accounts. <br>
Mitigation: Review connector permissions and credentials before use so the agent only accesses intended Triple Whale accounts and data. <br>


## Reference(s): <br>
- [Triple Whale homepage](https://www.triplewhale.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-triple-whale) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent responses may include connector command output summaries and setup guidance for authentication, connection, or billing errors.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
