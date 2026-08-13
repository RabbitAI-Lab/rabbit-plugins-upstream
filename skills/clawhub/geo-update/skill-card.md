## Description:

Update the installed SEO + GEO skills and the seogeo CLI to the latest release. Reports the installed version, the latest published version, what changed, and reinstalls the skill set across every detected agent tool. Use when the user says "update geo", "update skills", "upgrade seogeo", "aggiorna", or asks whether a newer version exists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to check whether the SEO + GEO toolkit is current, upgrade the seogeo CLI, and reinstall bundled skills across detected agent tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default update path can overwrite bundled SEO + GEO skill files across every detected agent tool.

Mitigation: Run a dry run or choose a single explicit target before applying updates, and preserve any locally edited bundled skill under a new name.

Risk: The skill uses remote shell installer commands to update the seogeo CLI.

Mitigation: Review the installer source and rely on the documented checksum verification behavior before allowing installation.

Risk: Vague requests such as updating skills could trigger broad changes beyond the user's intended target.

Mitigation: Confirm that the user wants the SEO + GEO toolkit updated before running commands that modify installed agent skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/geo-update)
- [Latest release API endpoint referenced by skill](https://api.github.com/repos/asale-ai/seo-geo-skill/releases/latest)
- [Unix installer referenced by skill](https://raw.githubusercontent.com/asale-ai/seo-geo-skill/main/install.sh)
- [Windows installer referenced by skill](https://raw.githubusercontent.com/asale-ai/seo-geo-skill/main/install.ps1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON command output summaries from seogeo checks or dry runs.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
