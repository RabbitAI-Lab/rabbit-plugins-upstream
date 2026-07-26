## Description: <br>
Generates high-fidelity text-to-vector assets with 4MP-tier quality for production-grade SVG-style assets and detailed illustrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to call the dLazy hosted Recraft V4 Pro Vector CLI, submit prompts, and receive generated vector or image output URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends prompts and selected local files to dLazy-hosted services. <br>
Mitigation: Review prompts and files for sensitive data before execution and use the service only when that data transfer is acceptable. <br>
Risk: Authentication requires a dLazy API key that may be stored in local CLI configuration. <br>
Mitigation: Use DLAZY_API_KEY per invocation when local persistence is undesirable, and rotate or revoke keys from dLazy when needed. <br>
Risk: Installing the pinned npm CLI adds third-party executable code to the environment. <br>
Mitigation: Review the pinned @dlazy/cli package or source before installing, and consider npx @dlazy/cli@1.2.3 to avoid a persistent global install. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON output containing generated asset URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a dLazy API key; generated outputs are returned as files.dlazy.com URLs, with optional async task status.] <br>

## Skill Version(s): <br>
1.3.5 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
