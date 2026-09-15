## Description:

Turn a real win into a set of designed, on-brand image assets for social media, email, and a profile, in every size those channels need, built around a verified screenshot as proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT

## Use Case:

External users, creators, founders, and developers use this skill to turn a captured milestone, ranking, launch, award, chart result, or similar public proof point into posting-ready visual assets and captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe configuration fields may execute raw HTML or JavaScript during rendering.

Mitigation: Use only celebration JSON that you control, avoid headline_html and banner_headline_html, and review configs before rendering.

Risk: Output path, name, or slug values may write files outside the intended output folder.

Mitigation: Use simple filenames and render into a controlled local directory.

Risk: Sensitive screenshots or hostile HTML can expose embedded proof data through the browser-based renderer.

Mitigation: Crop screenshots locally, remove personal or sensitive information, and inspect rendered images before sharing.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/OthmanAdi/celebrate)
- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/celebrate)
- [Publisher profile](https://clawhub.ai/user/othmanadi)
- [Copy guidance](references/copy.md)
- [Design guidance](references/design.md)
- [Format guidance](references/formats.md)
- [Proof handling guidance](references/proof.md)
- [Rendering guidance](references/rendering.md)
- [Verification guidance](references/verify.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON configuration, generated image files, and caption text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3.8+, Pillow, and Chrome, Chromium, or Edge for local rendering.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
