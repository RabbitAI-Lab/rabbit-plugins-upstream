## Description: <br>
Read and write messages on a Vestaboard using the Vestaboard Cloud API (cloud.vestaboard.com) and optional legacy RW endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seidprojects](https://clawhub.ai/user/seidprojects) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and Vestaboard owners use this skill to preview, read, and update board messages from an agent. It supports plain text, short status messages, simple pixel-art layouts, and current board state retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change a real Vestaboard message. <br>
Mitigation: Install it only for agents that should read or update the board, and preview sensitive messages before writing. <br>
Risk: Vestaboard API credentials could be exposed if entered into prompts, logs, or committed files. <br>
Mitigation: Provide credentials only through runtime environment variables such as VESTABOARD_TOKEN or VESTABOARD_RW_KEY. <br>
Risk: A custom API base could direct requests away from the trusted Vestaboard service. <br>
Mitigation: Leave VESTABOARD_API_BASE pointed at a trusted Vestaboard endpoint unless the deployment explicitly requires another endpoint. <br>
Risk: Arbitrary layout JSON can write unexpected content to the board. <br>
Mitigation: Use write-layout only with known 6x22 layout JSON files that have been reviewed before execution. <br>


## Reference(s): <br>
- [Vestaboard Character Codes](references/character-codes.md) <br>
- [Vestaboard Formatting Notes](references/formatting.md) <br>
- [Vestaboard Cloud API](https://cloud.vestaboard.com/) <br>
- [Vestaboard Character Codes Documentation](https://docs.vestaboard.com/docs/characterCodes/) <br>
- [ClawHub Vestaboard Skill](https://clawhub.ai/seidprojects/skills/vestaboard) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-compatible Vestaboard layouts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Formats text for a 6x22 Vestaboard layout, truncates overflow, and can read or write board state through authenticated API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
