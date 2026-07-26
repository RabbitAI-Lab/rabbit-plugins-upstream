## Description: <br>
Extracts media from social media and other supported URLs using yt-dlp, with explicit controls for public uploads and browser-cookie use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to inspect or download media from user-provided URLs. It returns titles, metadata, local file paths, or public temporary links when upload is explicitly confirmed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Downloaded files over 50 MB or forced uploads can be sent to public third-party temporary hosts. <br>
Mitigation: Require explicit --confirm-upload before public upload, use --no-upload when local-only handling is preferred, and share returned links only when public access is intended. <br>
Risk: Browser-cookie access can expose active session tokens for logged-in platforms. <br>
Mitigation: Use browser cookies only as a last resort with explicit consent, prefer narrower authentication methods when available, and avoid paid, private, confidential, or regulated content. <br>
Risk: Media downloading can create privacy, copyright, or policy exposure when used on sensitive or restricted content. <br>
Mitigation: Confirm the content is non-sensitive and appropriate to download before extraction, and do not use the skill for private, paid, confidential, copyrighted, or regulated content unless consequences are understood. <br>


## Reference(s): <br>
- [Clip Media on ClawHub](https://clawhub.ai/jlacroix82/skills/clip-media) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; script output may be plain text, JSON metadata, local file paths, or public temporary URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May download media to local storage; public uploads require --confirm-upload and return links accessible to anyone with the URL.] <br>

## Skill Version(s): <br>
0.3.5 (source: server release and clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
