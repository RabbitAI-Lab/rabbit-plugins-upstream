## Description: <br>
Installs, upgrades, and uses Dokku to create apps, deploy, run one-off/background tasks, and clean up containers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akhil-naidu](https://clawhub.ai/user/akhil-naidu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to administer Dokku hosts, including installation, upgrades, app deployment, process management, domains, certificates, plugins, logs, storage, network settings, and cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Root-level host administration commands can change the Dokku host or installed packages. <br>
Mitigation: Review sudo, install, upgrade, and package-management commands before execution and run them only on the intended Dokku host. <br>
Risk: Destructive cleanup and app deletion commands can remove apps, images, containers, volumes, or build cache. <br>
Mitigation: Confirm the target app or Docker scope before using --force, apps:destroy, docker prune, or dokku-nuke guidance. <br>
Risk: Plugin installation, SSH key import, config export, and network binding guidance can expand access or expose services. <br>
Mitigation: Use verified plugin sources, inspect SSH keys and exported configuration, and confirm network exposure before applying bind or domain changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/akhil-naidu/skills/dokku) <br>
- [Dokku installation documentation](https://dokku.com/docs/getting-started/installation) <br>
- [Dokku upgrading documentation](https://dokku.com/docs/getting-started/upgrading) <br>
- [Dokku releases](https://github.com/dokku/dokku/releases) <br>
- [Docker prune documentation](https://docs.docker.com/engine/reference/commandline/system_prune/) <br>
- [Dokku postgres plugin](https://github.com/dokku/dokku-postgres.git) <br>
- [Dokku letsencrypt plugin](https://github.com/dokku/dokku-letsencrypt.git) <br>
- [Dokku nuke plugin](https://github.com/dokku-community/dokku-nuke) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Markdown] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides command reference guidance for Dokku host administration; commands may require local or SSH access to a Dokku host.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release metadata; artifact CHANGELOG lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
