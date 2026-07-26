## Description: <br>
Integrates TokenLab chat, image, audio, video, and other API families into apps or scripts with runnable examples, model discovery, public contract checks, and agent-first recovery paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hedging8563](https://clawhub.ai/user/hedging8563) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to add TokenLab API calls to applications or scripts with runnable examples, setup commands, model discovery, and route-selection guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated examples may use a TokenLab API key and make paid network API calls. <br>
Mitigation: Review the selected endpoint, model, required environment variables, and expected costs before running generated commands. <br>
Risk: Incorrect model, route, or request-shape assumptions can produce failed requests or unsupported parameters. <br>
Mitigation: Use TokenLab model discovery, recommended-for shortlists, and model contract checks before hardcoding non-chat request details. <br>
Risk: The skill depends on a third-party TokenLab service. <br>
Mitigation: Confirm that the user trusts the TokenLab service before installing the skill or running generated integration examples. <br>


## Reference(s): <br>
- [Usage Notes](references/usage-notes.md) <br>
- [TokenLab API overview](https://api.tokenlab.sh/llms.txt) <br>
- [TokenLab model discovery](https://api.tokenlab.sh/v1/models) <br>
- [TokenLab model contract endpoint](https://api.tokenlab.sh/v1/models/:model) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with runnable code and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes model discovery notes, routing guidance, assumptions, caveats, or next actions when needed.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
