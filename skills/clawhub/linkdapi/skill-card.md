## Description: <br>
Work with the LinkdAPI Python SDK to access LinkedIn profile, company, job, and search data through short-lived Python scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[foontinz](https://clawhub.ai/user/foontinz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to write and run temporary Python scripts for LinkedIn profile lookup, company enrichment, job search, people search, and related LinkdAPI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated scripts may expose or mishandle the LinkdAPI API key if credentials are embedded directly in code. <br>
Mitigation: Keep the API key in an environment variable and review scripts before running them in sensitive workspaces. <br>
Risk: The skill installs and uses the third-party linkdapi Python package at runtime. <br>
Mitigation: Install only when LinkdAPI and its Python package are trusted for the environment. <br>
Risk: Profile and contact-info endpoints can return personal data. <br>
Mitigation: Use returned data only for legitimate, authorized purposes and minimize retention or sharing. <br>


## Reference(s): <br>
- [LinkdAPI documentation](https://linkdapi.com/docs) <br>
- [LinkdAPI signup](https://linkdapi.com/signup?ref=K_CZJSWF) <br>
- [ClawHub skill page](https://clawhub.ai/foontinz/skills/linkdapi) <br>


## Skill Output: <br>
**Output Type(s):** [code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkdAPI API key, typically supplied through the LINKDAPI_API_KEY environment variable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
