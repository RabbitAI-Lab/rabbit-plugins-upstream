## Description:

Helps users and observers review Canvas LMS courses, assignments, grades, announcements, conversations, planner items, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Canvas users and observer account holders use the skill to check course activity, including grades, assignments, submissions, upcoming work, and course communications. It can also download course files to a configured local folder.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration accesses sensitive Canvas records and authentication credentials.

Mitigation: Review browser bridge permissions, choose an appropriate authentication mode, and protect credentials and session caches.

Risk: Course files are downloaded to the local filesystem.

Mitigation: Choose a dedicated download folder and review files before sharing them.

Risk: The supplied instructions do not establish the integrity of downloaded runtime and extension releases.

Mitigation: Pin the npm package version and verify extension release checksums or build the extension from source.

## Reference(s):

- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Canvas record summaries and downloaded course files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downloaded files are saved within CANVAS_OUTPUT_DIR (default: ~/Downloads).]

## Skill Version(s):

2.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
