## Description: <br>
Generate random quotes from The Office (US), with offline quotes plus optional API mode for SVG cards, character avatars, and episode metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gumadeiras](https://clawhub.ai/user/gumadeiras) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to fetch Office-themed quotes for lightweight content, icebreakers, or generated quote cards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API mode contacts a third-party service and may expose request metadata outside the local environment. <br>
Mitigation: Prefer offline mode for routine or sensitive use; enable API mode only when third-party network calls are acceptable. <br>
Risk: Image conversion renders API-provided SVG content and creates local image files. <br>
Mitigation: Run image conversion in a sandboxed environment and avoid automated or sensitive workflows unless the SVG rendering path is hardened. <br>
Risk: The security scan classified the release as suspicious because documentation understates risky API and image-rendering behavior. <br>
Mitigation: Install only when the npm publisher is trusted and review the behavior before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gumadeiras/skills/office-quotes) <br>
- [npm package @gumadeiras/office-quotes](https://www.npmjs.com/package/@gumadeiras/office-quotes) <br>
- [Office API](https://officeapi.akashrajpurohit.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, image files, shell commands] <br>
**Output Format:** [Plain text or JSON; API mode may return SVG, PNG, JPG, or WebP image file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline mode is local by default; API mode contacts a third-party service and may create temporary local image files.] <br>

## Skill Version(s): <br>
1.2.4 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
