## Description: <br>
Build and run Gemini 2.5 Computer Use browser-control agents with Playwright. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[am-will](https://clawhub.ai/user/am-will) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to create a Gemini Computer Use agent loop that observes browser screenshots, receives model actions, executes supported actions in Playwright, and returns updated screenshots and URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser screenshots, page URLs, and task text may be sent to Gemini during automation. <br>
Mitigation: Avoid banking, health, internal company, admin, and other sensitive authenticated pages unless explicit consent, redaction, or site restrictions are added. <br>
Risk: Model-selected browser actions can interact with live pages in ways the user did not intend. <br>
Mitigation: Run in a sandboxed browser profile or container, require confirmation for safety decisions, and use action exclusions for risky operations. <br>


## Reference(s): <br>
- [Gemini Computer Use Notes](references/google-computer-use.md) <br>
- [ClawHub skill page](https://clawhub.ai/am-will/skills/gemini-computer-use) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and Python code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GEMINI_API_KEY and Playwright; supports turn limits, viewport settings, browser selection, and action exclusions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
