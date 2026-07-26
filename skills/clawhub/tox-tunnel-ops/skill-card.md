## Description: <br>
Tox Tunnel Ops helps agents plan, configure, verify, and diagnose encrypted ToxTunnel TCP tunnels for remote SSH, desktop, database, web service, homelab, proxy, metrics, and failover use cases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentx-icu](https://clawhub.ai/user/agentx-icu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and homelab administrators use this skill to produce ToxTunnel client/server YAML, scoped access-control rules, verification commands, and troubleshooting guidance for encrypted remote TCP access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote network exposure and persistent services can create high-impact access paths. <br>
Mitigation: Review generated rules so they allow only exact friends, hosts, and ports, and avoid enabling persistent services until the configuration is reviewed. <br>
Risk: Installer shortcuts or unpinned packages can increase supply-chain risk. <br>
Mitigation: Prefer manually downloaded, version-pinned release packages with checksums over one-line installers. <br>
Risk: Diagnostic cleanup commands can remove important identity data if the target path is wrong. <br>
Mitigation: Do not run rm -rf diagnostics without verifying and backing up the exact target path. <br>


## Reference(s): <br>
- [ToxTunnel project homepage](https://github.com/agentx-icu/tox-tcp-tunnel) <br>
- [ClawHub skill page](https://clawhub.ai/agentx-icu/skills/tox-tunnel-ops) <br>
- [Diagnose Reference](references/diagnose.md) <br>
- [Execute Reference](references/execute.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with YAML and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include client/server configs, rules.yaml snippets, diagnostic checklists, and verification commands; requires the toxtunnel binary.] <br>

## Skill Version(s): <br>
0.4.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
