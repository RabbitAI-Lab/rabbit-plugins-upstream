## Description: <br>
Bidirectional sync with reMarkable tablets via rmapi for fetching handwritten notes or sketches, processing them with AI, and pushing documents or enhanced images back to the tablet. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolmanns](https://clawhub.ai/user/coolmanns) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to move sketches, notes, documents, and generated images between a reMarkable tablet and an agent workflow for conversion, interpretation, enhancement, and upload back to the tablet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Synced notes, journals, sketches, and the rmapi token can contain sensitive personal or work-confidential information. <br>
Mitigation: Treat the rmapi token and synced tablet content as sensitive; use a dedicated sync folder or tags and avoid sending private or regulated notes to downstream AI tools unless intended. <br>
Risk: The workflow depends on rmapi and Python conversion packages that are installed outside the skill artifact. <br>
Mitigation: Install only trusted rmapi and package releases, prefer pinned versions or checksum verification where possible, and review bulk upload and download targets before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolmanns/skills/remarkable-sync) <br>
- [Publisher profile](https://clawhub.ai/user/coolmanns) <br>
- [rmapi releases](https://github.com/ddvk/rmapi/releases) <br>
- [reMarkable desktop connection](https://my.remarkable.com/connect/desktop) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline shell and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes command examples for rmapi, conversion workflows, authentication setup, and troubleshooting.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
