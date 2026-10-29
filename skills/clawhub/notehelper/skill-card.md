## Description:

Save an article or link to the user's NoteHelper (笔记同步助手) cloud notebook, or search articles already saved there, via https://claw.notebooksyncer.com. Use ONLY when the user explicitly asks to save/clip something to NoteHelper (e.g. "存到笔记同步助手", "剪藏到笔记库", "save this to NoteHelper"), to search their NoteHelper notebook ("在笔记同步助手里搜 X"), or to set up their NoteHelper key. Do NOT use for general web search, summarizing or debugging a link, browser bookmarks, other note apps, or a bare URL without a save request — in that case ask first. Explicit commands - /notehelper save | link | search | config.

This skill is ready for commercial/non-commercial use.

## Publisher:

[notesynchelper](https://clawhub.ai/user/notesynchelper)

### License/Terms of Use:

MIT-0

## Use Case:

People using NoteHelper can save user-approved articles or links to their cloud notebook, search saved articles, and get instructions for configuring the service key. The skill is limited to explicit NoteHelper requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-approved content and links are sent to NoteHelper’s cloud service, and link processing can spend credits.

Mitigation: Show the destination, content to be sent, and applicable cost before submission, and proceed only after confirmation.

Risk: The API key can access the notebook and spend credits if exposed.

Mitigation: Keep the key private and use the documented secret-reference configuration where available.

## Reference(s):

- [NoteHelper developer integration guide](https://www.bijitongbu.site/tutorials/developer-integration/)
- [NoteHelper points and pricing](https://www.bijitongbu.site/tutorials/points-explained/)
- [NoteHelper ClawHub release](https://clawhub.ai/notesynchelper/skills/notehelper)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls]

**Output Format:** [User-facing text and structured API request/response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save user-approved content or links, search the cloud notebook, or provide setup instructions; link processing may consume credits.]

## Skill Version(s):

1.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
