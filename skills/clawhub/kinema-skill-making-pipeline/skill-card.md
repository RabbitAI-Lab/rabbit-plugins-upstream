## Description: <br>
KinemaClaw cross-platform skill development and publishing specification for Codex and Claude plugin development, version management, marketplace indexing, and publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeshunee](https://clawhub.ai/user/leeshunee) <br>

### License/Terms of Use: <br>
GNU General Public License v3.0 <br>


## Use Case: <br>
Developers and engineers use this skill to create, modify, version, validate, and publish cross-platform skills for Codex, Claude Code, GitHub Releases, and ClawHub. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing guidance can affect repositories, releases, marketplace entries, and ClawHub skill versions if executed against the wrong target. <br>
Mitigation: Before publishing, inspect the package directory and verify the destination repository, marketplace entry, ClawHub slug, and release version. <br>
Risk: A release package can accidentally include secrets, private files, cache directories, or build artifacts. <br>
Mitigation: Remove secrets and private files before publication, and use the documented temporary package flow that excludes runtime caches and platform wrapper metadata. <br>
Risk: Cache update or cleanup commands can delete local plugin cache directories. <br>
Mitigation: Review any cache deletion or force-update command before allowing it to run, and apply it only to the intended skill cache path. <br>
Risk: The ClawHub API fallback reads the local ClawHub token from user configuration. <br>
Mitigation: Use the fallback only when the normal publish command fails, keep the token local, and avoid printing, copying, or storing credential values in release notes or logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leeshunee/skills/kinema-skill-making-pipeline) <br>
- [ONBOARDING.md](references/ONBOARDING.md) <br>
- [release-process.md](references/release-process.md) <br>
- [marketplace-publishing.md](references/marketplace-publishing.md) <br>
- [clawhub-api-fallback.md](references/clawhub-api-fallback.md) <br>
- [Claude Code Plugins Reference](https://code.claude.com/docs/en/plugins-reference) <br>
- [ClawHub Documentation](https://docs.openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, code snippets, checklists, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance is procedural and should be reviewed before running publish, cache update, or credential-sensitive commands.] <br>

## Skill Version(s): <br>
1.11.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
