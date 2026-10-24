## Description:

Identifies and lists duplicate files in a chosen local directory to help users find unnecessary duplicate data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albionaiinc-del](https://clawhub.ai/user/albionaiinc-del)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and power users can use Dup Finder from the command line to identify duplicate files in a selected local directory before deciding what to remove.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool reads file contents inside the directory provided by the user while computing duplicate hashes.

Mitigation: Run it only on directories you are comfortable having scanned, especially when files may contain sensitive data.

Risk: Printed duplicate paths may reveal local file names or directory structure.

Mitigation: Use it in an environment where exposing those paths in terminal output or logs is acceptable.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text command-line output listing duplicate file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads files inside the requested directory to compute hashes and prints duplicate path groups; it does not remove files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
