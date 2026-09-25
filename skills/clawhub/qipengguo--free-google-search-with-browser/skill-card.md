## Description:

Search Google using scrapling and return structured results with a title, link, and snippet for each result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qipengguo](https://clawhub.ai/user/qipengguo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill when an agent needs to run a live Google search and consume structured result records. It is best suited to environments that permit visible browser automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to Google through a visible browser session.

Mitigation: Avoid sensitive queries unless that exposure is acceptable, and run the skill only in an isolated browsing environment.

Risk: Setup can download browser and dependency artifacts.

Mitigation: Install in an isolated environment and pin dependency versions before production use.

Risk: The skill creates a local scrapling_storage.db file that may retain browsing state.

Mitigation: Use a dedicated working directory and review or delete the storage file between runs when privacy matters.

Risk: The script requires a GUI because it launches a non-headless browser.

Mitigation: Run it on a desktop-capable host or configure a virtual display such as xvfb for server environments.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result records from the script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search result snippets are truncated to 300 characters by the script.]

## Skill Version(s):

0.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
