## Description: <br>
Access Granola meeting transcripts and notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scald](https://clawhub.ai/user/scald) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Granola users and developers use this skill to sync meeting transcripts, notes, and summaries from Granola into a local folder for listing and searching. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The sync uses the user's signed-in Granola desktop session to download meeting history to local files. <br>
Mitigation: Install only if that access is acceptable, store the output folder in a protected location, and avoid shared or broadly synced folders. <br>
Risk: An automated cron sync can keep refreshing local copies of sensitive meeting data in the background. <br>
Mitigation: Enable the cron job only when ongoing sync is wanted, and disable it when local meeting copies are no longer needed. <br>


## Reference(s): <br>
- [Granola website](https://granola.ai) <br>
- [ClawHub skill page](https://clawhub.ai/scald/skills/granola) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON, Files] <br>
**Output Format:** [Markdown instructions with bash and JavaScript command examples; synced meetings are saved as Markdown and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, the requests Python package, macOS Granola desktop authentication, and a writable local output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
