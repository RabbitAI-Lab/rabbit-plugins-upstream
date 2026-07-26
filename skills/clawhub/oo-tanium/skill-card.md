## Description: <br>
Tanium (tanium.com). Use this skill for ANY Tanium request - searching and reading data. Whenever a task involves Tanium, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Tanium through an OOMOL-connected account, inspect live connector schemas, and execute Tanium Gateway GraphQL operations through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes a broad raw GraphQL action against a high-impact endpoint management system. <br>
Mitigation: Review each GraphQL document before execution, especially mutation-like operations, and require explicit user confirmation for changes to Tanium assets, endpoints, or configuration. <br>
Risk: The skill describes untagged actions as read-oriented, but the available GraphQL action can express operations whose effects depend on the submitted document. <br>
Mitigation: Fetch the live action schema, inspect the operation text and variables, and treat any state-changing or ambiguous operation as requiring confirmation before running it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tanium) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Tanium homepage](https://www.tanium.com) <br>
- [OOMOL Tanium connection](https://console.oomol.com/app-connections?provider=tanium) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON command payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands should fetch the live connector schema before execution and preserve the execution id from JSON responses.] <br>

## Skill Version(s): <br>
1.0.1 (source: server metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
