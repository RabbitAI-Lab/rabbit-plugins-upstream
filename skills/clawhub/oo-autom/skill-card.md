## Description: <br>
Autom (autom.dev). Use this skill for ANY Autom request - searching and reading data. Whenever a task involves Autom, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to run read-only Autom lookup and usage actions through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The get_usage action can return Autom usage, quota, rate limit, account, and API key metadata. <br>
Mitigation: Run it only for the intended OOMOL-connected Autom account and avoid sharing outputs that contain account or API key metadata. <br>
Risk: Installing the oo CLI or starting OOMOL login connects local agent activity to an OOMOL account. <br>
Mitigation: Use installer, login, and Autom connection steps only when the user intentionally wants to set up OOMOL and Autom access. <br>


## Reference(s): <br>
- [Autom homepage](https://www.autom.dev) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-autom) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the live Autom connector schema before sending action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
