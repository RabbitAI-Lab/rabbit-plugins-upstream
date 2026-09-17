## Description:

Operate Imgix through an OOMOL-connected account using the oo CLI to inspect action schemas, retrieve and list sources, update sources, and purge cached asset URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Imgix sources and cache purges through an OOMOL-connected account while checking live action schemas before sending requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Review the installer path first and prefer a verified release or package manager with publisher integrity checks before running installation commands.

Risk: Imgix update and purge actions can change service state or invalidate cached assets.

Mitigation: Confirm the exact action target, payload, and expected effect with the user before approving write or destructive operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-imgix)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Imgix](https://www.imgix.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include validated JSON request payloads and confirmation prompts for write or destructive Imgix actions.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
