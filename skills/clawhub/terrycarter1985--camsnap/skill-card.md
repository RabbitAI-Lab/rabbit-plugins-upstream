## Description:

Camera snapshot and monitoring skill for OpenClaw - capture, compare, and manage camera snapshots with automated detection and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use CamSnap to ask an agent for camera snapshot commands, camera configuration guidance, frame comparison workflows, and watch-mode alert setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled camsnap command is primarily release automation rather than the camera capture implementation described by the skill.

Mitigation: Review the command behavior before installation and do not rely on the bundled command for camera capture unless a trusted capture implementation is verified separately.

Risk: Release scripts, Git hooks, or cron usage can modify skill files and publish the package automatically.

Mitigation: Run release automation only when publication is intended, prefer dry-run review first, and avoid installing the Git hook or cron job unless automatic publication is explicitly desired.

Risk: Unpinned global npm or Cargo installation may pull packages whose provenance has not been verified.

Mitigation: Verify package provenance and use trusted, pinned installation sources before installing globally.

Risk: Publishing the skill directory could expose secrets or private files if they are present in the package path.

Mitigation: Inspect the skill directory before running any publish command and keep credentials or private files outside the package.

## Reference(s):

- [CamSnap ClawHub listing](https://clawhub.ai/terrycarter1985/skills/camsnap)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, YAML configuration examples, and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing guidance for using the camsnap CLI and release-related helper scripts]

## Skill Version(s):

0.1.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
