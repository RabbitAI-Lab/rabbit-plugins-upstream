## Description: <br>
LIFX (lifx.com) helps agents handle LIFX requests for reading, creating, and updating data through the LIFX connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate LIFX lights and scenes through an OOMOL-connected account, including listing lights and scenes, activating scenes, setting light state, toggling power, turning effects off, and validating color strings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Some state-changing light actions may not be labeled as write actions. <br>
Mitigation: Treat toggle_power and turn_effects_off as write actions and confirm the selector, payload, and expected lighting effect before running them. <br>
Risk: Commands operate through the user's OOMOL-connected LIFX account and can affect physical lights. <br>
Mitigation: Inspect the live connector schema before building each payload and only run actions for the intended account, selector, and scene. <br>


## Reference(s): <br>
- [ClawHub LIFX Skill](https://clawhub.ai/oomol/skills/oo-lifx) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [LIFX Homepage](https://www.lifx.com) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the oo CLI to inspect connector schemas and run LIFX connector actions with JSON responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
