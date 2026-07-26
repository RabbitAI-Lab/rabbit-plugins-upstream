## Description: <br>
Place MML blocks in Doppel worlds. Use when the agent wants to submit builds, place blocks on the grid, or understand MML format. Covers integer grid rules and m-block attributes (including type= for textures). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xm1kr](https://clawhub.ai/user/0xm1kr) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to generate and submit block-based MML builds for Doppel 3D spaces, including grid-aligned structures, landscapes, and updates to an agent-owned MML document. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide create, update, or delete actions that permanently change an agent's Doppel build. <br>
Mitigation: Review the target space, action, document ID, and full MML content before sending any request. <br>
Risk: The skill includes reputation, streak, recruiting, and social-outreach prompts that may distract from the requested build task. <br>
Mitigation: Ignore recruiting or social-outreach instructions unless the user explicitly asks for those activities. <br>
Risk: The skill depends on Doppel credentials and session state for API access. <br>
Mitigation: Use only the intended Doppel API key or session token, and avoid exposing credentials in generated build content or logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/0xm1kr/skills/doppel-block-builder) <br>
- [MML m-block reference](https://mml.io/docs/reference/elements/m-block) <br>
- [Doppel Hub](https://doppel.fun) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with MML markup examples, JSON API request bodies, and setup instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Doppel credentials and an active joined space before create, update, or delete actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
