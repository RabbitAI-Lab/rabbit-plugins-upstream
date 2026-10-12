## Description:

Helps agents manage Planly teams, social channels, media, and scheduled posts through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People managing social media use this skill to inspect Planly teams, channels, schedules, and media, and to import media or create scheduled posts with their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running a remote installer script directly in a shell.

Mitigation: Install the OOMOL CLI only from trusted documentation after inspecting or verifying the installer.

Risk: Creating scheduled posts or deleting media can change or remove Planly content.

Mitigation: Review exact action payloads and targets with the user before approving writes or deletions.

## Reference(s):

- [Planly skill on ClawHub](https://clawhub.ai/oomol/skills/oo-planly)
- [Planly](https://planly.com)
- [OOMOL CLI documentation](https://cli.oomol.com/install-guide.md)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text with JSON action results where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report Planly listings and publication status; write actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
