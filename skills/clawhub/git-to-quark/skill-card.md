## Description:

GitToQuark helps an agent save public GitHub repository source archives or release assets to Quark Cloud Drive with geolocation-aware proxy routing for users in China.

This skill is ready for commercial/non-commercial use.

## Publisher:

[violet27chen](https://clawhub.ai/user/violet27chen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to provide a public GitHub repository URL or owner/repo identifier and have an agent download the default-branch source archive or latest release asset, then upload it to Quark Cloud Drive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary rates the release suspicious because installation and runtime behavior rely on missing wrapper scripts while requesting persistent Quark Cloud Drive authorization and automatic external calls.

Mitigation: Review the package before installing, confirm wrapper scripts and CLI provenance, and authorize Quark Cloud Drive only in an environment where persistent credentials are acceptable.

Risk: The skill may perform geolocation checks and proxy-routed GitHub downloads before saving files to cloud storage.

Mitigation: Inform users about external network calls, verify the selected download URLs and proxy behavior, and review upload destinations before running the workflow.

## Reference(s):

- [Quark Cloud Drive CLI](https://github.com/quark-clouddrive/quarkclouddrive_offical)
- [GitToQuark ClawHub skill page](https://clawhub.ai/violet27chen/skills/git-to-quark)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks and stepwise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger external HTTP requests, Quark Cloud Drive CLI authorization, file downloads, uploads, and temporary file cleanup.]

## Skill Version(s):

0.0.1 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
