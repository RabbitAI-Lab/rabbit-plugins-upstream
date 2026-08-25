## Description:

Syncs daily health and fitness data from Garmin Connect into markdown files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weirdei](https://clawhub.ai/user/weirdei)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to sync Garmin Connect health and fitness metrics into local daily markdown files that an agent can read when answering personal health or training questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived Garmin tokens are stored locally and can grant access to the user's Garmin account if exposed.

Mitigation: Install only on a trusted machine/account and restrict permissions on ~/.garminconnect.

Risk: Daily markdown outputs contain sensitive personal health and fitness data.

Mitigation: Keep the health output directory private and avoid syncing it to shared backups, repositories, or collaborative folders.

Risk: Other Garmin tools using the same token cache may be able to reuse the session.

Mitigation: Review related Garmin tooling before installation and account for shared token-cache behavior.

## Reference(s):

- [uv documentation](https://docs.astral.sh/uv/)
- [python-garminconnect](https://github.com/cyberjunky/python-garminconnect)
- [garmin-nutrition related skill](https://github.com/weirdei/garmin-nutrition)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown files with command-line setup and sync instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes one local health markdown file per synced day; sections appear only when Garmin has data for them.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
