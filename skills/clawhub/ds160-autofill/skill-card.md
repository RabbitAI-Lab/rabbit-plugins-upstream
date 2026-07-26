## Description: <br>
Automates filling and resuming U.S. DS-160 nonimmigrant visa applications using CSV data, browser automation, LLM assistance for captchas or missing elements, and Chinese-to-English translation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clulessboy](https://clawhub.ai/user/clulessboy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to assist with supervised DS-160 form completion from a CSV template, resume interrupted sessions, and identify missing or complex fields for review. It is suited to careful use because it processes highly sensitive visa details and security-answer data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes highly sensitive visa, identity, and security-answer information. <br>
Mitigation: Use fake data for testing, keep the workspace private, and delete or protect ds160-user-info.csv and ds160-session.json after use. <br>
Risk: Personal fields, screenshots, or captcha images may be sent to external AI tools during assistance flows. <br>
Mitigation: Use external AI assistance only after explicit user acceptance of that disclosure. <br>
Risk: Automated filling or generated security answers could introduce incorrect application data. <br>
Mitigation: Review every page before continuing, do not rely on generated security answers, and keep final submission under direct user control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clulessboy/skills/ds160-autofill) <br>
- [CEAC DS-160 application site](https://ceac.state.gov/genniv/) <br>
- [DS-160 element mappings](references/ds160-elements.yaml) <br>
- [DS-160 user data CSV template](references/ds160-user-info.csv) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, Code, Configuration, Files] <br>
**Output Format:** [Markdown guidance with JavaScript snippets, browser automation steps, CSV/YAML file usage, and JSON session state] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires supervised browser interaction and may create ds160/ds160-user-info.csv and ds160/ds160-session.json in the workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
