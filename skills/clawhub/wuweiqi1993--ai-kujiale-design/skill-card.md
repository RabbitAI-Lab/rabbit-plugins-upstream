## Description:

AI-assisted interior design skill that guides a staged conversation through floor-plan confirmation, style selection, layout confirmation, and rendered design output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wuweiqi1993](https://clawhub.ai/user/wuweiqi1993)

### License/Terms of Use:

MIT-0

## Use Case:

External users and design agents use this skill to create Kujiale interior design outputs by selecting or uploading a floor plan, choosing style preferences, triggering layout generation, and collecting rendered images, panorama links, design highlights, and a design-detail link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a Kujiale access token.

Mitigation: Use a scoped or short-lived token when possible, keep .kjlconfig.json out of source control, and rotate the token after testing.

Risk: The skill uploads local images to Kujiale services.

Mitigation: Confirm the exact image file before upload and avoid uploading sensitive floor plans unless the account and service terms are appropriate.

Risk: The skill can trigger layout and rendering actions that may consume account quota or credits.

Mitigation: Do not proceed with layout or rendering until the user understands and confirms any quota, credit, or account effects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wuweiqi1993/skills/ai-kujiale-design)
- [Kujiale skill token page](https://www.kujiale.com/skills)
- [Skill workflow](artifact/SKILL.md)
- [Floor-plan search API](artifact/docs/planSearch.md)
- [Floor-plan information API](artifact/docs/floorplanInfo.md)
- [Design creation API](artifact/docs/createDesign.md)
- [Image upload API](artifact/docs/upload.md)
- [Bitmap import API](artifact/docs/planUrlCreate.md)
- [Layout API](artifact/docs/layout.md)
- [Layout result API](artifact/docs/layoutResult.md)
- [Render result API](artifact/docs/renderResult.md)
- [Version check API](artifact/docs/versionCheck.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, guidance]

**Output Format:** [Markdown with rendered-image links, panorama links, design highlights, and inline shell commands during execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Kujiale access token and can trigger layout or rendering actions that affect account quota or credits.]

## Skill Version(s):

0.0.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
