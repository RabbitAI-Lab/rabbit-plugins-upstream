## Description: <br>
Jits Builder helps an agent generate single-file vanilla JavaScript mini-apps from voice or text requests and expose them through local serving plus Cloudflare tunnel URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dannyshmueli](https://clawhub.ai/user/dannyshmueli) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and end users use this skill to request small, single-page utilities such as timers, calculators, formatters, and converters, then receive generated app code and a temporary public URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated mini-apps can be exposed on public Cloudflare tunnel URLs. <br>
Mitigation: Use the skill only for non-sensitive mini-apps, avoid secrets or private business data, review generated code before sharing, and stop tunnels when finished. <br>
Risk: The helper relies on weak scoping and control for app names, ports, tunnel lifecycle, and cloudflared execution. <br>
Mitigation: Prefer a hardened deployment that validates names and ports, verifies cloudflared from an official source outside /tmp, asks before public deployment, and expires or cleans up running apps automatically. <br>
Risk: Generated app code may be incorrect, misleading, or unsuitable for the user's context. <br>
Mitigation: Review and test generated HTML, CSS, and JavaScript before use, especially before sharing the public URL. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dannyshmueli/skills/jits-builder) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>
- [JITS helper script](artifact/jits.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with HTML, CSS, JavaScript, shell command usage, and public URL text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces self-contained single-page app artifacts and app-management commands; generated apps may be reachable through public Cloudflare tunnel URLs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
