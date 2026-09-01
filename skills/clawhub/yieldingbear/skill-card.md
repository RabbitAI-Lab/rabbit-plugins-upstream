## Description:

Yielding Bear wires OpenClaw, Hermes, or shell workflows to a Yielding Bear API key with smart model routing, model catalog checks, and doctor/smoke-test commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yieldingbear](https://clawhub.ai/user/yieldingbear)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure Yielding Bear credentials and model defaults for OpenClaw, Hermes, or shell-based workflows, then verify connectivity with catalog, doctor, and smoke-test commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install path includes a curl-to-bash option and downloads SDK files from yieldingbear.com without checksum verification.

Mitigation: Review the installer before execution and prefer running the bundled local script installed by ClawHub.

Risk: The installer stores the Yielding Bear API key on the local filesystem.

Mitigation: Use a dedicated customer API key, keep generated secret files private, and rotate the key if the host or files are exposed.

## Reference(s):

- [Yielding Bear site](https://yieldingbear.com)
- [Yielding Bear docs](https://yieldingbear.com/docs)
- [How it works](https://yieldingbear.com/how-it-works)
- [Pricing](https://yieldingbear.com/pricing)
- [Developer dashboard](https://yieldingbear.com/dashboard?tab=developer)
- [ClawHub skill page](https://clawhub.ai/yieldingbear/skills/yieldingbear)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local setup guidance and helper command output for Yielding Bear API connectivity.]

## Skill Version(s):

2.1.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
