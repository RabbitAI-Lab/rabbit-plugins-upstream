## Description: <br>
Solve CAPTCHAs with 2Captcha from the command line during browser automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adinvadim](https://clawhub.ai/user/adinvadim) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and automation engineers use this skill to configure and invoke a Python command-line helper for solving supported CAPTCHA challenges through the 2Captcha service during authorized browser automation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CAPTCHA content, page URLs, sitekeys, challenge data, and related metadata are sent to 2Captcha and its human solvers. <br>
Mitigation: Use the skill only for authorized workflows, avoid sensitive or internal pages unless approved, and confirm that sending this data to 2Captcha is acceptable for the use case. <br>
Risk: The 2Captcha API key may be stored in an environment variable or local config file. <br>
Mitigation: Protect the API key, limit local file access, avoid committing credentials, and rotate the key if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/adinvadim/skills/2captcha) <br>
- [2Captcha CLI source and feedback](https://github.com/adinvadim/2captcha-cli) <br>
- [2Captcha service](https://2captcha.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration snippets, and browser automation code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The referenced CLI can emit human-readable text, quiet token output, or JSON responses depending on command flags.] <br>

## Skill Version(s): <br>
2.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
