## Description: <br>
Bootstrap a fresh VPS into an operational OpenClaw deployment with backup, restore, security baseline, and post-recovery verification support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bustes01](https://clawhub.ai/user/bustes01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to bootstrap, migrate, or recover an OpenClaw VPS, including installation, service setup, backup restoration, and readiness verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bootstrap and recovery actions can change SSH, firewall, service, and system package state in ways that may lock users out or disrupt an existing server. <br>
Mitigation: Install only on a fresh, disposable, or fully backed-up VPS after reading the scripts and confirming the intended SSH and firewall changes. <br>
Risk: Restoring from an untrusted backup tarball can overwrite workspace files, credentials, cron data, GPG keys, password-store data, and OAuth configuration. <br>
Mitigation: Do not run restore.sh with an untrusted or unverified backup tarball; verify backup provenance and contents before restoring credentials or configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bustes01/skills/vps-bootstrap) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash commands, shell scripts, configuration notes, and verification guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational guidance for VPS setup, restore, and verification; execution requires user review and appropriate system privileges.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata; artifact _meta.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
