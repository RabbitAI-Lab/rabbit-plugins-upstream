## Description:

Extracts transcripts, on-screen text, captions, key points, and engagement details from Instagram reels and posts through LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing public Instagram content can use this skill to retrieve spoken and on-screen text, captions, and key points for research, note-taking, or content analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted Instagram links are processed by the external LinkDigest service, and the scanner does not verify its data handling or declared tool scope.

Mitigation: Review LinkDigest's privacy information and provide links and an API key only if its data handling is acceptable.

Risk: Paid reads and optional analysis features consume API credits; the scanner cannot verify billing guarantees.

Mitigation: Review current pricing and use the script's --max-credits option when limiting spend.

Risk: Remote extraction accuracy is not verified by the scanner.

Mitigation: Check transcripts and extracted text against the original post before relying on them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/jackchew7143/skills/instagram-to-text)
- [LinkDigest platform information](https://linkdigest.dev/platforms?ref=skill-instagram-to-text)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)
- [LinkDigest remote MCP endpoint](https://linkdigest.dev/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON, with transcript and on-screen text timestamps when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Photo carousels are limited to the first slide; optional translations, breakdowns, and question answering can consume additional credits.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
