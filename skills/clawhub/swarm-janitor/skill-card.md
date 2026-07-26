## Description: <br>
Enterprise-grade OpenClaw skill for cleaning up orphaned subagent processes, archiving transcripts to SuperMemory, and freeing disk space without losing work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvcidpsyche](https://clawhub.ai/user/lvcidpsyche) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to inspect OpenClaw session directories, preview cleanup actions, archive transcripts, and remove orphaned subagent sessions under configurable retention policies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release instructs users to run cleanup code that is missing from the artifact and would delete or archive private agent session data. <br>
Mitigation: Obtain and review the implementation from a trusted source before execution; start with dry-run only, keep independent backups, and avoid --force or --no-archive unless data-loss risk is accepted. <br>
Risk: Transcript archival can expose private session data to external storage when SuperMemory, S3, or another remote destination is enabled. <br>
Mitigation: Enable external archival only after confirming exactly what session data will be stored and after validating credential scope, retention settings, and destination access controls. <br>
Risk: Cron-based cleanup can repeat destructive actions unattended. <br>
Mitigation: Run manual dry-runs first, verify the session path and retention thresholds, and enable automation only after reviewing logs and expected deletion counts. <br>


## Reference(s): <br>
- [Swarm Janitor ClawHub page](https://clawhub.ai/lvcidpsyche/skills/swarm-janitor) <br>
- [Configuration reference](references/config.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and YAML configuration references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3; the submitted artifact references scripts/swarm_janitor.py, but that implementation is not included.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
