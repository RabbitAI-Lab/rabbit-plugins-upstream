## Description:

A demonstration skill for content ingestion workflows that checks a workspace folder for text/markdown assets, generates a simple inventory report, and prints a summary.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content pipeline maintainers use this demonstration skill to test ClawHub ingestion or CI/CD publishing flows by inventorying markdown and text files in a workspace folder.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated inventory may expose private file names from the selected target directory.

Mitigation: Set TARGET_DIR only to folders whose markdown and text file names are acceptable to show in the agent output.

Risk: The artifact describes a lightweight demonstration workflow rather than a production ingestion system.

Mitigation: Add appropriate logging, error handling, and metadata extraction before using it in production content pipelines.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/terrycarter1985/skills/demo-content-ingest)
- [Publisher profile](https://clawhub.ai/user/terrycarter1985)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks and plain-text inventory output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists top-level markdown and text files from the selected target directory; no persistence, credentials, network access, or destructive actions are reported in security evidence.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
