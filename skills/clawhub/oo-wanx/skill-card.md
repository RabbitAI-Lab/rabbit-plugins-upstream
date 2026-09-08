## Description:

Wanx lets agents inspect live Wanx connector schemas and run image or video generation actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate or edit images with Wan Image 2.7 and submit or retrieve Wan 3.0 video generation tasks through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run an unverified remote installer script when the oo CLI is missing.

Mitigation: Review the installer URL before execution and prefer an official signed or checksum-verifiable installation method.

Risk: The skill can use an OOMOL-connected Wanx account and associated credits.

Mitigation: Only approve authentication, account connection, or paid generation steps when that account usage is intended.

Risk: The submit_video_generation action changes service state by creating an asynchronous generation job.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Wanx ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wanx)
- [Wanx homepage](https://tongyi.aliyun.com/wanxiang/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands, validated JSON payload guidance, connector result references, and setup guidance for authentication or Wanx account connection failures.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
