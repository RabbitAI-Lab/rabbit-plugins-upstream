## Description: <br>
Install, bootstrap, validate, and optionally connect StablePay MCP on Codex, Claude Code, or Cursor. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bubblevan](https://clawhub.ai/user/bubblevan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to install or validate the StablePay CLI, complete wallet onboarding, optionally configure StablePay MCP, and report setup status or pause points. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to install npm packages, modify MCP configuration, run wallet onboarding, set payment limits, or publish an npm package. <br>
Mitigation: Use it only for an explicitly requested setup step and require confirmation before global installs, wallet or payment-limit changes, MCP config writes, or npm publish commands. <br>
Risk: Onboarding includes browser-based X verification and account-related steps that should not be bypassed or treated as complete automatically. <br>
Mitigation: Pause at external verification, preserve the resume command when provided, and wait for the user to complete the browser step before continuing. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown] <br>
**Output Format:** [Markdown with inline bash commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes compact setup status, validation results, MCP configuration state, and any remaining external-verification step.] <br>

## Skill Version(s): <br>
1.4.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
