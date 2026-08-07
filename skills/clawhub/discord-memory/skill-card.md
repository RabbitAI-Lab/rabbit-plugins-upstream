## Description: <br>
Helps agents remember, search, and recall Discord conversation context using BlueColumn persistent memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to give Discord-based agents continuity by storing summaries, recording quick notes, and recalling prior channel context through BlueColumn memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Discord-derived summaries may be stored in an external persistent memory service without clear consent, scope, deletion, or sensitive-data limits. <br>
Mitigation: Use only where users and moderators have approved storage, restrict which channels are summarized, redact credentials and personal or confidential data, and define retention and deletion controls before use. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends selected Discord-derived text to an external persistent memory service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
