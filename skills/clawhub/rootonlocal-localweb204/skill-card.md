## Description: <br>
Control and query LifeSmart Smart Station IoT devices registered in the RootONLocal app. Queries local device/zone info via http://127.0.0.1:18080, then calls the LifeSmart LocalWeb API directly to get or set device state (lights, switches, blinds, AC, custom IR remotes) and read measurements (air quality, temperature, power/energy meters, solar). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kcobstkin](https://clawhub.ai/user/kcobstkin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and automation developers use this skill to let an agent resolve natural-language smart-home requests into RootONLocal local info API lookups and LifeSmart LocalWeb device queries or controls. It is intended for same-device OpenClaw-style deployments where the RootONLocal app exposes device, zone, credential, and station metadata on loopback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles reusable LocalWeb username and password values returned by the local RootONLocal info API. <br>
Mitigation: Treat these credentials as sensitive secrets, keep them in memory only, and install the skill only on trusted devices and LANs. <br>
Risk: The local info API has no authentication and returns credentials in plaintext on loopback. <br>
Mitigation: Keep the RootONLocal server bound to 127.0.0.1 and do not expose, proxy, or forward the local API to other hosts. <br>
Risk: HTTP mode or disabled TLS verification can weaken protection for LocalWeb calls on the LAN. <br>
Mitigation: Prefer HTTPS, avoid HTTP mode, and avoid clients that disable TLS verification except for explicitly trusted private-LAN self-signed certificate cases. <br>
Risk: Commands can change physical smart-home state, including blinds, HVAC, plugs, and IR remotes. <br>
Mitigation: Require explicit user confirmation before state-changing commands and reject unsupported or ambiguous device actions. <br>


## Reference(s): <br>
- [RootONLocal_Monorepo homepage](https://github.com/Kcobstkin/RootONLocal_Monorepo) <br>
- [RootONLocal IoT Skill](artifact/SKILL.md) <br>
- [RootONLocal IoT Info API Spec](artifact/api-spec.md) <br>
- [LifeSmart Local Web API Spec](artifact/localweb-spec.md) <br>
- [Device Types & Channel Map](artifact/device-types.md) <br>
- [Natural Language to API Examples](artifact/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON and HTTP request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces same-device local API lookup guidance, LifeSmart LocalWeb request bodies, and recommended JSON success or error responses.] <br>

## Skill Version(s): <br>
2.0.4 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
