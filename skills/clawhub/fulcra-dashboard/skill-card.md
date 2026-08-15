## Description:

Builds a highly customizable, interactive HTML dashboard using Alpine.js, modern Vanilla CSS, and a Python backend to display private data from the user's Fulcra data store locally. Includes workflows to export a specific, previewable directory for public sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fulcra](https://clawhub.ai/user/fulcra)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Fulcra users use this skill to scaffold and customize a local HTML dashboard for approved Fulcra data, then optionally export only the curated public directory for sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private Fulcra records may be fetched and rendered in the dashboard.

Mitigation: Require explicit user consent before data ingestion and include only approved final data files in the dashboard public directory.

Risk: Publishing the wrong directory could expose intermediate files or private datasets.

Mitigation: Preview locally, inspect the public/ directory, list the exact files to be published, and publish only after final user confirmation.

Risk: The browser dashboard can load third-party CDN scripts for visualization.

Mitigation: Disclose CDN usage before scaffolding and proceed only when the user approves using external scripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fulcra/skills/fulcra-dashboard)
- [Fulcra publisher profile](https://clawhub.ai/user/fulcra)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated web app files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a local dashboard directory with a public/ subdirectory for approved data and static assets.]

## Skill Version(s):

0.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
