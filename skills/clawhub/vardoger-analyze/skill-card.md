## Description: <br>
Analyzes OpenClaw conversation history with the vardoger CLI to generate tailored assistant instructions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dstrupl](https://clawhub.ai/user/dstrupl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and assistant users use this skill to inspect prior OpenClaw conversations, summarize behavioral patterns, and generate global personalization guidance for future assistant sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads prior conversation history, which may include secrets or sensitive personal data. <br>
Mitigation: Run it only when the user intentionally wants conversation-history analysis, avoid histories containing sensitive data, and review the generated personalization before relying on it. <br>
Risk: The skill can write derived preferences into global assistant rules outside the current workspace. <br>
Mitigation: Approve filesystem access only when that global update is intended, then inspect the written personalization file. <br>
Risk: The workflow depends on the external vardoger CLI. <br>
Mitigation: Verify the CLI source and installation path before granting it filesystem access outside the workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dstrupl/skills/vardoger-analyze) <br>
- [vardoger project](https://github.com/dstrupl/vardoger) <br>
- [pipx installation](https://pipx.pypa.io/stable/installation/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated personalization text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the vardoger CLI and may write approved personalization guidance to global assistant rules.] <br>

## Skill Version(s): <br>
0.3.2 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
