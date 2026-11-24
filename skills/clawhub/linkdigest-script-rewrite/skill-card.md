## Description:

Analyzes a Douyin, Xiaohongshu, or TikTok video transcript and structure, then drafts an original spoken-video script for the user's topic using that structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators use this skill to extract a reference video's transcript and storytelling beats, then draft a new script for their own topic, product, or persona. They provide the video link, their subject, and a target duration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the reference video link to LinkDigest and uses LINKDIGEST_API_KEY for the request, so the URL and credential cross a network boundary.

Mitigation: Only submit links you intend to process through LinkDigest, and provide the API key through the environment as documented.

Risk: The security review is partial and the declared tool scope is missing, so the available review may not cover all relevant behavior.

Mitigation: Review the script and its external-service access before enabling it, and resolve the missing local references when available.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/linkdigest-script-rewrite)
- [LinkDigest documentation](https://linkdigest.dev/zh/docs?ref=skill-linkdigest-script-rewrite)
- [LinkDigest API key setup](https://linkdigest.dev/signin?ref=skill-linkdigest-script-rewrite&next=/app/keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown with title options, timed script beats, production cues, and a reference-to-new-script beat mapping]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user-provided topic and target duration; separates reference-video analysis from newly drafted wording.]

## Skill Version(s):

1.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
