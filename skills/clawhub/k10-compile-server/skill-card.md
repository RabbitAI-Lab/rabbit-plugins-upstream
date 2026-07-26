## Description: <br>
Compiles UNIHIKER K10 PlatformIO projects via a K10 Compile Server, then helps download firmware or flash a K10 through Web Serial, server-side USB, or local esptool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rockets-cn](https://clawhub.ai/user/rockets-cn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and educators use this skill to compile UNIHIKER K10 PlatformIO projects on a trusted LAN compile server, then download or flash the resulting firmware without installing the full PlatformIO toolchain locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Projects are uploaded to a compile server, and compiled firmware may be downloaded or flashed to hardware. <br>
Mitigation: Use only a compile server and network path that the user controls or strongly trusts, avoid placing secrets in uploaded projects, and review firmware before flashing where practical. <br>
Risk: The helper workflows use certificate checks that tolerate self-signed or untrusted HTTPS certificates. <br>
Mitigation: Prefer a real trusted certificate, VPN, or tunnel, and avoid public or unknown servers. <br>
Risk: The server setup documentation describes an unauthenticated compile server that should not be exposed publicly. <br>
Mitigation: Keep the server on a trusted LAN or private access path, or place it behind authentication, rate limiting, and HTTPS with a trusted certificate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rockets-cn/skills/k10-compile-server) <br>
- [K10 Compile Server repository](https://github.com/rockets-cn/unihiker-k10-compile-server) <br>
- [K10 Compile Server API Reference](artifact/references/server-api.md) <br>
- [Server Setup Guide](artifact/references/server-setup.md) <br>
- [Troubleshooting](artifact/references/troubleshooting.md) <br>
- [DFRobot UniHiker PlatformIO platform](https://github.com/DFRobot/platform-unihiker.git) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash, PowerShell, curl, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to upload projects to a trusted compile server, download firmware files, open a Web Serial flash page, or run flashing commands.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
