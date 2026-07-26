## Description: <br>
Configure AI personality using the AURA protocol (HEXACO-based). Use when user wants to customize agent personality, reduce sycophancy, adjust communication style, or mentions AURA/personality configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phiro56](https://clawhub.ai/user/phiro56) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents use AURA to ask for personality preferences, map them to HEXACO-style trait values, and create or update a local AURA.yaml profile. Users can then show, reset, or load that profile to guide response style, directness, autonomy, and anti-sycophancy boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may create or modify AURA.yaml with personal communication preferences. <br>
Mitigation: Review AURA.yaml before committing, sharing, or relying on it, and avoid storing sensitive personal details in the profile. <br>
Risk: Reset behavior may delete the local AURA.yaml profile and remove customized settings. <br>
Mitigation: Confirm reset intent and keep a backup of any profile that should be preserved. <br>
Risk: A personality profile can materially change an agent's tone, directness, and autonomy. <br>
Mitigation: Review generated trait values and boundaries before applying them to ongoing work. <br>


## Reference(s): <br>
- [AURA Protocol Specification](https://github.com/phiro56/AURA) <br>
- [ClawHub AURA Skill Page](https://clawhub.ai/phiro56/skills/aura) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown instructions and YAML configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create, show, or remove a local AURA.yaml profile.] <br>

## Skill Version(s): <br>
0.1.0-beta.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
