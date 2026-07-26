## Description: <br>
Play Pokemon Red autonomously via PyBoy emulator: the OpenClaw agent starts the emulator server, sees screenshots, reads game state from RAM, and makes decisions through a local HTTP API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drbarq](https://clawhub.ai/user/drbarq) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External agents and developers use this skill to run a local PyBoy Pokemon Red emulator session, inspect screenshots and RAM state, and choose navigation, battle, quest, and save actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation asks the agent to download and run unpinned external code outside the reviewed bundle. <br>
Mitigation: Review or pin the external Pokemon-OpenClaw repository and Python dependencies before use, and run the skill in a virtual environment or container. <br>
Risk: The workflow depends on a local emulator server and a Pokemon Red ROM. <br>
Mitigation: Use only a legally obtained ROM, keep the emulator server bound to localhost, and stop the background server after gameplay. <br>


## Reference(s): <br>
- [Pokemon Red game instructions](references/game_instructions.md) <br>
- [Pokemon-OpenClaw repository referenced by setup instructions](https://github.com/drbarq/Pokemon-OpenClaw.git) <br>
- [ClawHub skill page](https://clawhub.ai/drbarq/skills/pokemon-red) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, API calls, JSON actions] <br>
**Output Format:** [Markdown instructions with bash and curl examples plus JSON action objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.10+, PyBoy dependencies, a legally obtained Pokemon Red ROM, and a local emulator server.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
